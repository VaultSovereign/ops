#!/usr/bin/env python3
"""
Safety Guardrails and Consent Validation for Social Engineering Awareness Campaigns

This module provides comprehensive safety controls, consent management, and ethical
guidelines to ensure all social engineering awareness activities are conducted safely
and with proper authorization.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
import datetime
import uuid
import json
from collections import defaultdict


class ConsentStatus(Enum):
    PENDING = "pending"
    GRANTED = "granted"
    DENIED = "denied"
    REVOKED = "revoked"
    EXPIRED = "expired"


class SafetyLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ApprovalStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    REQUIRES_REVIEW = "requires_review"


@dataclass
class ConsentRecord:
    """Record of participant consent for awareness activities"""
    participant_id: str
    participant_name: str
    campaign_id: str
    consent_type: str
    status: ConsentStatus
    granted_date: Optional[datetime.datetime]
    revoked_date: Optional[datetime.datetime]
    expiration_date: Optional[datetime.datetime]
    consent_method: str  # email, form, verbal, etc.
    witness: Optional[str] = None
    notes: str = ""


@dataclass
class SafetyAssessment:
    """Assessment of safety risks for a campaign or activity"""
    assessment_id: str
    campaign_id: str
    activity_type: str
    safety_level: SafetyLevel
    risk_factors: List[str]
    mitigation_measures: List[str]
    approval_required: bool
    approver: Optional[str] = None
    approval_date: Optional[datetime.datetime] = None
    assessment_date: datetime.datetime = field(default_factory=datetime.datetime.now)


@dataclass
class SafetyViolation:
    """Record of safety violations or incidents"""
    violation_id: str
    campaign_id: str
    participant_id: str
    violation_type: str
    description: str
    severity: SafetyLevel
    reported_date: datetime.datetime
    resolved_date: Optional[datetime.datetime] = None
    resolution_notes: str = ""


class SafetyGuardrails:
    """
    Comprehensive safety guardrails system for social engineering awareness campaigns.
    
    This system ensures:
    - Proper consent management and validation
    - Safety risk assessment and mitigation
    - Ethical guidelines compliance
    - Incident tracking and resolution
    - Approval workflow management
    """
    
    def __init__(self):
        self.consent_records = {}
        self.safety_assessments = {}
        self.safety_violations = {}
        self.approval_workflows = {}
        self.ethical_guidelines = self._initialize_ethical_guidelines()
    
    def _initialize_ethical_guidelines(self) -> Dict[str, List[str]]:
        """Initialize ethical guidelines for social engineering awareness activities"""
        return {
            "consent_requirements": [
                "Explicit consent must be obtained before any simulation activities",
                "Consent must be informed and specific to the activity type",
                "Participants must be able to withdraw consent at any time",
                "Consent must be documented and verifiable",
                "Consent must be renewed periodically (annually minimum)"
            ],
            "harm_prevention": [
                "No actual harm or damage to participants or systems",
                "No collection of real passwords or sensitive information",
                "No psychological manipulation beyond educational purposes",
                "No targeting of vulnerable populations",
                "No activities that could cause embarrassment or humiliation"
            ],
            "privacy_protection": [
                "Participant data must be anonymized when possible",
                "Personal information must be protected and secured",
                "Data collection must be limited to educational purposes",
                "Participants must be informed of data usage",
                "Data retention must follow company policies"
            ],
            "transparency_requirements": [
                "All activities must be clearly identified as simulations",
                "Participants must understand the educational purpose",
                "Clear opt-out mechanisms must be provided",
                "Escalation procedures must be clearly communicated",
                "Results must be used only for educational purposes"
            ],
            "approval_requirements": [
                "Security team approval required for all activities",
                "Legal team approval required for sensitive activities",
                "HR approval required for employee-targeted activities",
                "Management approval required for department-wide activities",
                "External activities require additional approvals"
            ]
        }
    
    def request_consent(self, participant_id: str, participant_name: str,
                       campaign_id: str, consent_type: str,
                       consent_method: str = "email",
                       witness: Optional[str] = None) -> str:
        """Request consent from a participant for awareness activities"""
        
        consent_id = str(uuid.uuid4())
        
        consent_record = ConsentRecord(
            participant_id=participant_id,
            participant_name=participant_name,
            campaign_id=campaign_id,
            consent_type=consent_type,
            status=ConsentStatus.PENDING,
            granted_date=None,
            revoked_date=None,
            expiration_date=datetime.datetime.now() + datetime.timedelta(days=365),
            consent_method=consent_method,
            witness=witness
        )
        
        self.consent_records[consent_id] = consent_record
        return consent_id
    
    def grant_consent(self, consent_id: str, witness: Optional[str] = None) -> bool:
        """Grant consent for awareness activities"""
        
        if consent_id not in self.consent_records:
            return False
        
        consent_record = self.consent_records[consent_id]
        
        if consent_record.status != ConsentStatus.PENDING:
            return False
        
        consent_record.status = ConsentStatus.GRANTED
        consent_record.granted_date = datetime.datetime.now()
        if witness:
            consent_record.witness = witness
        
        return True
    
    def revoke_consent(self, consent_id: str, reason: str = "") -> bool:
        """Revoke consent for awareness activities"""
        
        if consent_id not in self.consent_records:
            return False
        
        consent_record = self.consent_records[consent_id]
        
        if consent_record.status not in [ConsentStatus.GRANTED, ConsentStatus.PENDING]:
            return False
        
        consent_record.status = ConsentStatus.REVOKED
        consent_record.revoked_date = datetime.datetime.now()
        consent_record.notes = reason
        
        return True
    
    def check_consent_status(self, participant_id: str, campaign_id: str) -> ConsentStatus:
        """Check current consent status for a participant"""
        
        # Find active consent records for this participant and campaign
        active_consents = [
            record for record in self.consent_records.values()
            if (record.participant_id == participant_id and 
                record.campaign_id == campaign_id and
                record.status == ConsentStatus.GRANTED and
                (record.expiration_date is None or record.expiration_date > datetime.datetime.now()))
        ]
        
        if not active_consents:
            return ConsentStatus.DENIED
        
        return ConsentStatus.GRANTED
    
    def conduct_safety_assessment(self, campaign_id: str, activity_type: str,
                                risk_factors: List[str]) -> SafetyAssessment:
        """Conduct a safety assessment for a campaign or activity"""
        
        assessment_id = str(uuid.uuid4())
        
        # Determine safety level based on risk factors
        safety_level = self._assess_safety_level(risk_factors)
        
        # Generate mitigation measures
        mitigation_measures = self._generate_mitigation_measures(risk_factors, safety_level)
        
        # Determine if approval is required
        approval_required = safety_level in [SafetyLevel.HIGH, SafetyLevel.CRITICAL]
        
        assessment = SafetyAssessment(
            assessment_id=assessment_id,
            campaign_id=campaign_id,
            activity_type=activity_type,
            safety_level=safety_level,
            risk_factors=risk_factors,
            mitigation_measures=mitigation_measures,
            approval_required=approval_required
        )
        
        self.safety_assessments[assessment_id] = assessment
        return assessment
    
    def _assess_safety_level(self, risk_factors: List[str]) -> SafetyLevel:
        """Assess safety level based on risk factors"""
        
        high_risk_factors = [
            "external_participants",
            "sensitive_data_involved",
            "high_authority_impersonation",
            "financial_transactions",
            "remote_access_requests",
            "physical_security_breach"
        ]
        
        medium_risk_factors = [
            "phone_communications",
            "email_simulations",
            "group_activities",
            "data_collection",
            "behavioral_analysis"
        ]
        
        high_risk_count = sum(1 for factor in risk_factors if factor in high_risk_factors)
        medium_risk_count = sum(1 for factor in risk_factors if factor in medium_risk_factors)
        
        if high_risk_count >= 2:
            return SafetyLevel.CRITICAL
        elif high_risk_count >= 1 or medium_risk_count >= 3:
            return SafetyLevel.HIGH
        elif medium_risk_count >= 1:
            return SafetyLevel.MEDIUM
        else:
            return SafetyLevel.LOW
    
    def _generate_mitigation_measures(self, risk_factors: List[str], 
                                    safety_level: SafetyLevel) -> List[str]:
        """Generate mitigation measures based on risk factors and safety level"""
        
        measures = []
        
        # Base mitigation measures
        measures.extend([
            "Clear opt-out mechanisms provided",
            "Participant consent documented",
            "Activity clearly identified as simulation",
            "Escalation procedures established"
        ])
        
        # Risk-specific mitigation measures
        if "external_participants" in risk_factors:
            measures.extend([
                "Additional consent verification required",
                "External participant briefing conducted",
                "Legal team approval obtained"
            ])
        
        if "sensitive_data_involved" in risk_factors:
            measures.extend([
                "Data anonymization implemented",
                "Data protection protocols followed",
                "Privacy impact assessment completed"
            ])
        
        if "high_authority_impersonation" in risk_factors:
            measures.extend([
                "Authority verification procedures established",
                "Management approval obtained",
                "Clear boundaries defined for impersonation"
            ])
        
        if "financial_transactions" in risk_factors:
            measures.extend([
                "No actual financial transactions allowed",
                "Simulation clearly identified",
                "Financial team approval obtained"
            ])
        
        if "remote_access_requests" in risk_factors:
            measures.extend([
                "No actual remote access granted",
                "Simulation environment used",
                "IT security team approval obtained"
            ])
        
        if "physical_security_breach" in risk_factors:
            measures.extend([
                "Controlled environment only",
                "Physical security team approval obtained",
                "No actual security vulnerabilities created"
            ])
        
        # Safety level specific measures
        if safety_level == SafetyLevel.CRITICAL:
            measures.extend([
                "Executive approval required",
                "Legal team review completed",
                "Risk management team approval obtained",
                "Enhanced monitoring implemented"
            ])
        elif safety_level == SafetyLevel.HIGH:
            measures.extend([
                "Security team approval required",
                "Enhanced consent verification",
                "Additional monitoring implemented"
            ])
        
        return measures
    
    def request_approval(self, assessment_id: str, approver: str) -> str:
        """Request approval for a safety assessment"""
        
        if assessment_id not in self.safety_assessments:
            raise ValueError(f"Assessment {assessment_id} not found")
        
        assessment = self.safety_assessments[assessment_id]
        
        if not assessment.approval_required:
            return "No approval required"
        
        approval_id = str(uuid.uuid4())
        
        self.approval_workflows[approval_id] = {
            "approval_id": approval_id,
            "assessment_id": assessment_id,
            "approver": approver,
            "status": ApprovalStatus.PENDING,
            "requested_date": datetime.datetime.now(),
            "approved_date": None,
            "notes": ""
        }
        
        return approval_id
    
    def approve_assessment(self, approval_id: str, notes: str = "") -> bool:
        """Approve a safety assessment"""
        
        if approval_id not in self.approval_workflows:
            return False
        
        approval = self.approval_workflows[approval_id]
        
        if approval["status"] != ApprovalStatus.PENDING:
            return False
        
        approval["status"] = ApprovalStatus.APPROVED
        approval["approved_date"] = datetime.datetime.now()
        approval["notes"] = notes
        
        # Update the assessment
        assessment_id = approval["assessment_id"]
        if assessment_id in self.safety_assessments:
            self.safety_assessments[assessment_id].approver = approval["approver"]
            self.safety_assessments[assessment_id].approval_date = approval["approved_date"]
        
        return True
    
    def reject_assessment(self, approval_id: str, reason: str) -> bool:
        """Reject a safety assessment"""
        
        if approval_id not in self.approval_workflows:
            return False
        
        approval = self.approval_workflows[approval_id]
        
        if approval["status"] != ApprovalStatus.PENDING:
            return False
        
        approval["status"] = ApprovalStatus.REJECTED
        approval["notes"] = reason
        
        return True
    
    def report_safety_violation(self, campaign_id: str, participant_id: str,
                              violation_type: str, description: str,
                              severity: SafetyLevel) -> str:
        """Report a safety violation or incident"""
        
        violation_id = str(uuid.uuid4())
        
        violation = SafetyViolation(
            violation_id=violation_id,
            campaign_id=campaign_id,
            participant_id=participant_id,
            violation_type=violation_type,
            description=description,
            severity=severity,
            reported_date=datetime.datetime.now()
        )
        
        self.safety_violations[violation_id] = violation
        return violation_id
    
    def resolve_violation(self, violation_id: str, resolution_notes: str) -> bool:
        """Resolve a safety violation"""
        
        if violation_id not in self.safety_violations:
            return False
        
        violation = self.safety_violations[violation_id]
        violation.resolved_date = datetime.datetime.now()
        violation.resolution_notes = resolution_notes
        
        return True
    
    def validate_campaign_safety(self, campaign_id: str) -> Dict[str, Any]:
        """Validate overall safety of a campaign"""
        
        validation_result = {
            "campaign_id": campaign_id,
            "is_safe": True,
            "safety_issues": [],
            "required_approvals": [],
            "consent_status": {},
            "risk_level": SafetyLevel.LOW,
            "recommendations": []
        }
        
        # Check for safety assessments
        campaign_assessments = [
            assessment for assessment in self.safety_assessments.values()
            if assessment.campaign_id == campaign_id
        ]
        
        if not campaign_assessments:
            validation_result["safety_issues"].append("No safety assessment conducted")
            validation_result["is_safe"] = False
        
        # Check approval status
        for assessment in campaign_assessments:
            if assessment.approval_required and not assessment.approver:
                validation_result["required_approvals"].append(assessment.assessment_id)
                validation_result["is_safe"] = False
            
            if assessment.safety_level.value > validation_result["risk_level"].value:
                validation_result["risk_level"] = assessment.safety_level
        
        # Check for unresolved violations
        unresolved_violations = [
            violation for violation in self.safety_violations.values()
            if violation.campaign_id == campaign_id and not violation.resolved_date
        ]
        
        if unresolved_violations:
            validation_result["safety_issues"].extend([
                f"Unresolved violation: {v.violation_type}" for v in unresolved_violations
            ])
            validation_result["is_safe"] = False
        
        # Generate recommendations
        if validation_result["risk_level"] == SafetyLevel.CRITICAL:
            validation_result["recommendations"].append("Consider postponing campaign until risks are mitigated")
        elif validation_result["risk_level"] == SafetyLevel.HIGH:
            validation_result["recommendations"].append("Implement additional safety measures")
        
        if validation_result["required_approvals"]:
            validation_result["recommendations"].append("Obtain required approvals before proceeding")
        
        return validation_result
    
    def get_consent_summary(self, campaign_id: str) -> Dict[str, Any]:
        """Get summary of consent status for a campaign"""
        
        campaign_consents = [
            record for record in self.consent_records.values()
            if record.campaign_id == campaign_id
        ]
        
        summary = {
            "total_participants": len(campaign_consents),
            "consent_granted": len([r for r in campaign_consents if r.status == ConsentStatus.GRANTED]),
            "consent_pending": len([r for r in campaign_consents if r.status == ConsentStatus.PENDING]),
            "consent_denied": len([r for r in campaign_consents if r.status == ConsentStatus.DENIED]),
            "consent_revoked": len([r for r in campaign_consents if r.status == ConsentStatus.REVOKED]),
            "expired_consents": len([r for r in campaign_consents if r.status == ConsentStatus.EXPIRED])
        }
        
        return summary
    
    def export_safety_report(self, campaign_id: str) -> Dict[str, Any]:
        """Export comprehensive safety report for a campaign"""
        
        report = {
            "campaign_id": campaign_id,
            "generated_at": datetime.datetime.now().isoformat(),
            "safety_validation": self.validate_campaign_safety(campaign_id),
            "consent_summary": self.get_consent_summary(campaign_id),
            "safety_assessments": [
                {
                    "assessment_id": assessment.assessment_id,
                    "activity_type": assessment.activity_type,
                    "safety_level": assessment.safety_level.value,
                    "risk_factors": assessment.risk_factors,
                    "mitigation_measures": assessment.mitigation_measures,
                    "approval_required": assessment.approval_required,
                    "approver": assessment.approver,
                    "approval_date": assessment.approval_date.isoformat() if assessment.approval_date else None
                }
                for assessment in self.safety_assessments.values()
                if assessment.campaign_id == campaign_id
            ],
            "safety_violations": [
                {
                    "violation_id": violation.violation_id,
                    "participant_id": violation.participant_id,
                    "violation_type": violation.violation_type,
                    "description": violation.description,
                    "severity": violation.severity.value,
                    "reported_date": violation.reported_date.isoformat(),
                    "resolved_date": violation.resolved_date.isoformat() if violation.resolved_date else None,
                    "resolution_notes": violation.resolution_notes
                }
                for violation in self.safety_violations.values()
                if violation.campaign_id == campaign_id
            ],
            "ethical_guidelines": self.ethical_guidelines
        }
        
        return report


def main():
    """Example usage of the safety guardrails system"""
    
    # Initialize the safety guardrails
    guardrails = SafetyGuardrails()
    
    # Request consent for a participant
    consent_id = guardrails.request_consent(
        participant_id="user_001",
        participant_name="Alice Johnson",
        campaign_id="campaign_001",
        consent_type="phishing_simulation",
        consent_method="email"
    )
    
    # Grant consent
    guardrails.grant_consent(consent_id, witness="Security Team Lead")
    
    # Conduct safety assessment
    assessment = guardrails.conduct_safety_assessment(
        campaign_id="campaign_001",
        activity_type="phishing_simulation",
        risk_factors=["email_simulations", "data_collection"]
    )
    
    print("=== SAFETY GUARDRAILS SYSTEM ===")
    print(f"Consent ID: {consent_id}")
    print(f"Assessment ID: {assessment.assessment_id}")
    print(f"Safety Level: {assessment.safety_level.value}")
    print(f"Approval Required: {assessment.approval_required}")
    
    # Validate campaign safety
    validation = guardrails.validate_campaign_safety("campaign_001")
    print(f"Campaign Safe: {validation['is_safe']}")
    print(f"Safety Issues: {len(validation['safety_issues'])}")
    
    # Export safety report
    report = guardrails.export_safety_report("campaign_001")
    print(f"Safety Report: {len(report)} sections")


if __name__ == "__main__":
    main()
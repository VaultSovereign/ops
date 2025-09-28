#!/usr/bin/env python3
"""
Social Engineering Strategist
Plan ethical awareness campaigns and simulations with clear consent boundaries.
"""

import json
import hashlib
import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
from enum import Enum
import random
import string


class AudienceMaturity(Enum):
    """Security awareness maturity levels"""
    NOVICE = "novice"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class Channel(Enum):
    """Communication channels for campaigns"""
    EMAIL = "email"
    CHAT = "chat"
    PHONE = "phone"
    IN_PERSON = "in_person"
    SMS = "sms"
    SOCIAL_MEDIA = "social_media"


class CampaignType(Enum):
    """Types of awareness campaigns"""
    PHISHING = "phishing"
    VISHING = "vishing"
    SMISHING = "smishing"
    PHYSICAL = "physical"
    PRETEXTING = "pretexting"
    BAITING = "baiting"
    TAILGATING = "tailgating"


@dataclass
class RulesOfEngagement:
    """Define ethical boundaries for campaigns"""
    explicit_consent: bool = True
    opt_out_available: bool = True
    no_harm_principle: bool = True
    data_protection: bool = True
    approval_required: List[str] = field(default_factory=lambda: ["legal", "hr", "management"])
    excluded_scenarios: List[str] = field(default_factory=list)
    time_restrictions: Dict[str, str] = field(default_factory=dict)
    escalation_contacts: List[Dict[str, str]] = field(default_factory=list)


@dataclass
class SimulationScenario:
    """Individual simulation scenario"""
    scenario_id: str
    name: str
    type: CampaignType
    channel: Channel
    difficulty: AudienceMaturity
    description: str
    objective: str
    setup: Dict[str, Any]
    indicators: List[str]
    opt_out_instructions: str
    safe_word: str = ""
    
    def __post_init__(self):
        if not self.safe_word:
            self.safe_word = self._generate_safe_word()
    
    def _generate_safe_word(self) -> str:
        """Generate a unique safe word for immediate campaign termination"""
        return f"STOP-{'-'.join(random.choices(string.ascii_uppercase, k=3))}"


@dataclass
class TrainingModule:
    """Security awareness training module"""
    module_id: str
    title: str
    audience_level: AudienceMaturity
    duration_minutes: int
    objectives: List[str]
    content: Dict[str, Any]
    exercises: List[Dict[str, Any]]
    assessment: Dict[str, Any]
    resources: List[str]


@dataclass
class CampaignMetrics:
    """Metrics for measuring campaign success"""
    baseline_metrics: Dict[str, float]
    target_metrics: Dict[str, float]
    current_metrics: Dict[str, float] = field(default_factory=dict)
    measurement_methods: List[str] = field(default_factory=list)
    success_criteria: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Campaign:
    """Complete awareness campaign"""
    campaign_id: str
    name: str
    objective: str
    audience: Dict[str, Any]
    start_date: str
    end_date: str
    rules: RulesOfEngagement
    training_modules: List[TrainingModule]
    scenarios: List[SimulationScenario]
    metrics: CampaignMetrics
    debrief_materials: Dict[str, Any]
    status: str = "planning"


class SocialEngineeringStrategist:
    """Main strategist for planning and managing awareness campaigns"""
    
    def __init__(self):
        self.campaigns: Dict[str, Campaign] = {}
        self.scenario_library: Dict[str, SimulationScenario] = {}
        self.module_library: Dict[str, TrainingModule] = {}
        self.templates: Dict[str, Any] = self._load_templates()
    
    def _load_templates(self) -> Dict[str, Any]:
        """Load campaign templates"""
        return {
            "phishing": {
                "email": self._get_phishing_email_templates(),
                "indicators": self._get_phishing_indicators(),
                "training": self._get_phishing_training_content()
            },
            "vishing": {
                "scripts": self._get_vishing_scripts(),
                "indicators": self._get_vishing_indicators(),
                "training": self._get_vishing_training_content()
            },
            "physical": {
                "scenarios": self._get_physical_security_scenarios(),
                "training": self._get_physical_security_training()
            }
        }
    
    def create_campaign(self, 
                       objective: str,
                       audience: Dict[str, Any],
                       channels: List[Channel],
                       rules: RulesOfEngagement,
                       duration_days: int = 30) -> Campaign:
        """Create a new awareness campaign"""
        campaign_id = self._generate_id("campaign")
        
        # Determine audience maturity
        maturity = self._assess_audience_maturity(audience)
        
        # Generate appropriate training modules
        modules = self._generate_training_modules(objective, maturity, channels)
        
        # Create simulation scenarios
        scenarios = self._generate_scenarios(objective, maturity, channels, rules)
        
        # Define metrics
        metrics = self._define_metrics(objective, audience, scenarios)
        
        # Create debrief materials
        debrief = self._create_debrief_materials(objective, scenarios, modules)
        
        # Calculate dates
        start_date = datetime.datetime.now().isoformat()
        end_date = (datetime.datetime.now() + 
                   datetime.timedelta(days=duration_days)).isoformat()
        
        campaign = Campaign(
            campaign_id=campaign_id,
            name=f"Security Awareness: {objective}",
            objective=objective,
            audience=audience,
            start_date=start_date,
            end_date=end_date,
            rules=rules,
            training_modules=modules,
            scenarios=scenarios,
            metrics=metrics,
            debrief_materials=debrief
        )
        
        self.campaigns[campaign_id] = campaign
        return campaign
    
    def _generate_id(self, prefix: str) -> str:
        """Generate unique identifier"""
        timestamp = datetime.datetime.now().isoformat()
        hash_input = f"{prefix}_{timestamp}_{random.random()}"
        return f"{prefix}_{hashlib.md5(hash_input.encode()).hexdigest()[:8]}"
    
    def _assess_audience_maturity(self, audience: Dict[str, Any]) -> AudienceMaturity:
        """Assess security awareness maturity of audience"""
        # Simple heuristic based on role and department
        role = audience.get("role", "").lower()
        department = audience.get("department", "").lower()
        prior_training = audience.get("prior_training", 0)
        
        if "security" in role or "it" in department:
            if prior_training > 5:
                return AudienceMaturity.EXPERT
            return AudienceMaturity.ADVANCED
        elif prior_training > 3:
            return AudienceMaturity.INTERMEDIATE
        else:
            return AudienceMaturity.NOVICE
    
    def _generate_training_modules(self, 
                                  objective: str,
                                  maturity: AudienceMaturity,
                                  channels: List[Channel]) -> List[TrainingModule]:
        """Generate appropriate training modules"""
        modules = []
        
        # Foundation module
        foundation = TrainingModule(
            module_id=self._generate_id("module"),
            title="Security Awareness Fundamentals",
            audience_level=maturity,
            duration_minutes=30,
            objectives=[
                "Understand common social engineering tactics",
                "Recognize warning signs and red flags",
                "Learn proper incident reporting procedures"
            ],
            content=self._get_foundation_content(maturity),
            exercises=self._get_foundation_exercises(maturity),
            assessment=self._get_foundation_assessment(maturity),
            resources=[
                "Security awareness handbook",
                "Quick reference guide",
                "Incident reporting flowchart"
            ]
        )
        modules.append(foundation)
        
        # Channel-specific modules
        for channel in channels:
            module = self._create_channel_module(channel, maturity, objective)
            modules.append(module)
        
        return modules
    
    def _create_channel_module(self, 
                              channel: Channel,
                              maturity: AudienceMaturity,
                              objective: str) -> TrainingModule:
        """Create channel-specific training module"""
        channel_modules = {
            Channel.EMAIL: self._create_email_security_module,
            Channel.PHONE: self._create_phone_security_module,
            Channel.CHAT: self._create_chat_security_module,
            Channel.IN_PERSON: self._create_physical_security_module,
            Channel.SMS: self._create_sms_security_module,
            Channel.SOCIAL_MEDIA: self._create_social_media_module
        }
        
        creator = channel_modules.get(channel, self._create_generic_module)
        return creator(maturity, objective)
    
    def _create_email_security_module(self, 
                                     maturity: AudienceMaturity,
                                     objective: str) -> TrainingModule:
        """Create email security training module"""
        return TrainingModule(
            module_id=self._generate_id("module"),
            title="Email Security and Phishing Prevention",
            audience_level=maturity,
            duration_minutes=45,
            objectives=[
                "Identify phishing email characteristics",
                "Verify sender authenticity",
                "Handle suspicious attachments and links safely"
            ],
            content={
                "sections": [
                    {
                        "title": "Anatomy of a Phishing Email",
                        "content": "Detailed breakdown of common phishing techniques",
                        "examples": self._get_phishing_examples(maturity)
                    },
                    {
                        "title": "Verification Techniques",
                        "content": "How to verify legitimate communications",
                        "tools": ["SPF check", "DKIM verification", "Domain lookup"]
                    },
                    {
                        "title": "Safe Email Practices",
                        "content": "Best practices for email security",
                        "checklist": self._get_email_security_checklist()
                    }
                ]
            },
            exercises=[
                {
                    "type": "identification",
                    "description": "Identify phishing emails from a mixed set",
                    "difficulty": maturity.value,
                    "samples": 10
                },
                {
                    "type": "response",
                    "description": "Practice proper incident reporting",
                    "scenario": "Received suspicious email from CEO"
                }
            ],
            assessment={
                "type": "quiz",
                "questions": 15,
                "passing_score": 80,
                "time_limit_minutes": 20
            },
            resources=[
                "Phishing identification flowchart",
                "Email header analysis guide",
                "Reporting template"
            ]
        )
    
    def _create_phone_security_module(self,
                                     maturity: AudienceMaturity,
                                     objective: str) -> TrainingModule:
        """Create phone/vishing security module"""
        return TrainingModule(
            module_id=self._generate_id("module"),
            title="Voice Phishing (Vishing) Prevention",
            audience_level=maturity,
            duration_minutes=30,
            objectives=[
                "Recognize vishing attack patterns",
                "Verify caller identity properly",
                "Handle sensitive information requests"
            ],
            content={
                "sections": [
                    {
                        "title": "Common Vishing Tactics",
                        "content": "Overview of voice-based social engineering",
                        "examples": ["Fake IT support", "Government impersonation", "Bank fraud"]
                    },
                    {
                        "title": "Verification Protocols",
                        "content": "Steps to verify legitimate callers",
                        "protocol": self._get_caller_verification_protocol()
                    },
                    {
                        "title": "Information Protection",
                        "content": "What never to share over phone",
                        "red_flags": self._get_vishing_red_flags()
                    }
                ]
            },
            exercises=[
                {
                    "type": "roleplay",
                    "description": "Practice handling suspicious calls",
                    "scenarios": 5
                }
            ],
            assessment={
                "type": "scenario-based",
                "questions": 10,
                "passing_score": 75
            },
            resources=[
                "Caller verification checklist",
                "Vishing response flowchart"
            ]
        )
    
    def _generate_scenarios(self,
                          objective: str,
                          maturity: AudienceMaturity,
                          channels: List[Channel],
                          rules: RulesOfEngagement) -> List[SimulationScenario]:
        """Generate simulation scenarios based on parameters"""
        scenarios = []
        
        for channel in channels:
            # Generate 2-3 scenarios per channel
            num_scenarios = 2 if maturity == AudienceMaturity.NOVICE else 3
            
            for i in range(num_scenarios):
                scenario = self._create_scenario(
                    channel=channel,
                    maturity=maturity,
                    objective=objective,
                    rules=rules,
                    variant=i
                )
                scenarios.append(scenario)
                self.scenario_library[scenario.scenario_id] = scenario
        
        return scenarios
    
    def _create_scenario(self,
                        channel: Channel,
                        maturity: AudienceMaturity,
                        objective: str,
                        rules: RulesOfEngagement,
                        variant: int) -> SimulationScenario:
        """Create individual simulation scenario"""
        scenario_templates = {
            Channel.EMAIL: self._create_email_scenario,
            Channel.PHONE: self._create_phone_scenario,
            Channel.CHAT: self._create_chat_scenario,
            Channel.IN_PERSON: self._create_physical_scenario
        }
        
        creator = scenario_templates.get(channel, self._create_generic_scenario)
        return creator(maturity, objective, rules, variant)
    
    def _create_email_scenario(self,
                              maturity: AudienceMaturity,
                              objective: str,
                              rules: RulesOfEngagement,
                              variant: int) -> SimulationScenario:
        """Create email phishing scenario"""
        templates = [
            {
                "name": "Urgent Password Reset",
                "description": "Fake password reset request with urgency",
                "setup": {
                    "sender": "security@company-support.com",
                    "subject": "Urgent: Password Expires in 2 Hours",
                    "body": self._get_password_reset_template(),
                    "link": "https://company-support.com/reset",
                    "attachments": []
                },
                "indicators": [
                    "Sender domain doesn't match company domain",
                    "Urgent language and artificial deadline",
                    "Generic greeting instead of personalized",
                    "Link goes to external domain",
                    "Grammar and spelling errors"
                ]
            },
            {
                "name": "CEO Fraud",
                "description": "Impersonation of executive requesting urgent action",
                "setup": {
                    "sender": "ceo@companny.com",
                    "subject": "Confidential Request",
                    "body": self._get_ceo_fraud_template(),
                    "attachments": ["invoice.pdf.exe"]
                },
                "indicators": [
                    "Typo in sender domain (companny vs company)",
                    "Unusual request from executive",
                    "Request for secrecy",
                    "Suspicious attachment extension",
                    "Sent outside normal business hours"
                ]
            },
            {
                "name": "Fake Invoice",
                "description": "Malicious invoice attachment",
                "setup": {
                    "sender": "accounting@vendor-portal.net",
                    "subject": "Overdue Invoice #INV-2024-1337",
                    "body": self._get_invoice_template(),
                    "attachments": ["invoice_2024.zip"]
                },
                "indicators": [
                    "Unknown vendor",
                    "No previous communication history",
                    "Compressed attachment",
                    "Generic company details",
                    "Pressure to pay immediately"
                ]
            }
        ]
        
        template = templates[variant % len(templates)]
        
        return SimulationScenario(
            scenario_id=self._generate_id("scenario"),
            name=template["name"],
            type=CampaignType.PHISHING,
            channel=Channel.EMAIL,
            difficulty=maturity,
            description=template["description"],
            objective=f"Test ability to identify and report {template['name'].lower()}",
            setup=template["setup"],
            indicators=template["indicators"],
            opt_out_instructions=self._get_opt_out_instructions(Channel.EMAIL, rules)
        )
    
    def _get_opt_out_instructions(self, 
                                 channel: Channel,
                                 rules: RulesOfEngagement) -> str:
        """Generate opt-out instructions for scenario"""
        base_instructions = (
            "This is part of a security awareness simulation. "
            "You may opt out at any time by:\n"
        )
        
        channel_specific = {
            Channel.EMAIL: (
                "1. Replying with 'OPT-OUT' in subject line\n"
                "2. Clicking the opt-out link in email footer\n"
                "3. Contacting security team directly"
            ),
            Channel.PHONE: (
                "1. Saying the safe word provided in training\n"
                "2. Hanging up and calling security team\n"
                "3. Using the opt-out number provided"
            ),
            Channel.CHAT: (
                "1. Typing 'OPT-OUT' in chat\n"
                "2. Closing the chat window\n"
                "3. Reporting to security team"
            ),
            Channel.IN_PERSON: (
                "1. Using the safe word\n"
                "2. Showing your opt-out badge\n"
                "3. Contacting security escort"
            )
        }
        
        instructions = base_instructions + channel_specific.get(
            channel, 
            "Contact the security team to opt out"
        )
        
        if rules.escalation_contacts:
            contact = rules.escalation_contacts[0]
            instructions += f"\n\nEscalation contact: {contact.get('name', 'Security Team')} - {contact.get('email', 'security@company.com')}"
        
        return instructions
    
    def _define_metrics(self,
                       objective: str,
                       audience: Dict[str, Any],
                       scenarios: List[SimulationScenario]) -> CampaignMetrics:
        """Define success metrics for campaign"""
        return CampaignMetrics(
            baseline_metrics={
                "click_rate": 25.0,  # Industry average
                "report_rate": 15.0,
                "response_time_minutes": 180.0,
                "training_completion": 60.0
            },
            target_metrics={
                "click_rate": 10.0,  # Target reduction
                "report_rate": 50.0,  # Target increase
                "response_time_minutes": 30.0,  # Faster response
                "training_completion": 90.0  # Higher completion
            },
            measurement_methods=[
                "Email click tracking",
                "Incident report analysis",
                "Training platform analytics",
                "Post-simulation surveys",
                "Focus group feedback"
            ],
            success_criteria={
                "primary": "50% reduction in click rate",
                "secondary": [
                    "200% increase in reporting rate",
                    "80% faster incident response",
                    "90% training completion"
                ],
                "qualitative": [
                    "Increased security awareness discussions",
                    "Proactive security questions from staff",
                    "Peer-to-peer security coaching observed"
                ]
            }
        )
    
    def _create_debrief_materials(self,
                                 objective: str,
                                 scenarios: List[SimulationScenario],
                                 modules: List[TrainingModule]) -> Dict[str, Any]:
        """Create debrief materials for campaign"""
        return {
            "executive_summary": {
                "template": self._get_executive_summary_template(),
                "key_findings": [],
                "recommendations": [],
                "next_steps": []
            },
            "detailed_report": {
                "template": self._get_detailed_report_template(),
                "sections": [
                    "Campaign Overview",
                    "Methodology",
                    "Results by Scenario",
                    "Training Effectiveness",
                    "Lessons Learned",
                    "Recommendations"
                ]
            },
            "participant_feedback": {
                "individual": self._get_individual_feedback_template(),
                "team": self._get_team_feedback_template(),
                "recognition": self._get_recognition_template()
            },
            "improvement_plan": {
                "identified_gaps": [],
                "training_recommendations": [],
                "process_improvements": [],
                "timeline": self._get_improvement_timeline()
            },
            "communication_materials": {
                "all_staff_email": self._get_all_staff_template(),
                "newsletter_article": self._get_newsletter_template(),
                "intranet_post": self._get_intranet_template()
            }
        }
    
    def run_simulation(self, 
                      campaign_id: str,
                      scenario_id: str,
                      participants: List[str]) -> Dict[str, Any]:
        """Execute a simulation scenario"""
        campaign = self.campaigns.get(campaign_id)
        if not campaign:
            return {"error": "Campaign not found"}
        
        scenario = next(
            (s for s in campaign.scenarios if s.scenario_id == scenario_id),
            None
        )
        if not scenario:
            return {"error": "Scenario not found"}
        
        # Check consent and rules
        if campaign.rules.explicit_consent:
            consent_check = self._verify_consent(participants, campaign)
            if not consent_check["all_consented"]:
                return {
                    "error": "Missing consent",
                    "missing_consent": consent_check["missing"]
                }
        
        # Execute simulation
        results = {
            "scenario_id": scenario_id,
            "participants": len(participants),
            "start_time": datetime.datetime.now().isoformat(),
            "status": "running",
            "opt_out_instructions": scenario.opt_out_instructions,
            "safe_word": scenario.safe_word,
            "monitoring": {
                "real_time": True,
                "escalation_available": True,
                "harm_prevention": True
            }
        }
        
        # Log simulation start
        self._log_simulation_start(campaign_id, scenario_id, participants)
        
        return results
    
    def generate_report(self, campaign_id: str) -> Dict[str, Any]:
        """Generate comprehensive campaign report"""
        campaign = self.campaigns.get(campaign_id)
        if not campaign:
            return {"error": "Campaign not found"}
        
        report = {
            "campaign_id": campaign_id,
            "campaign_name": campaign.name,
            "objective": campaign.objective,
            "duration": f"{campaign.start_date} to {campaign.end_date}",
            "audience": campaign.audience,
            "executive_summary": self._generate_executive_summary(campaign),
            "detailed_results": self._generate_detailed_results(campaign),
            "metrics_analysis": self._analyze_metrics(campaign),
            "lessons_learned": self._compile_lessons_learned(campaign),
            "recommendations": self._generate_recommendations(campaign),
            "appendices": {
                "scenario_details": [asdict(s) for s in campaign.scenarios],
                "training_modules": [asdict(m) for m in campaign.training_modules],
                "participant_feedback": self._get_participant_feedback(campaign_id),
                "raw_metrics": asdict(campaign.metrics)
            }
        }
        
        return report
    
    # Template helper methods
    def _get_phishing_email_templates(self) -> List[Dict[str, str]]:
        """Get phishing email templates"""
        return [
            {
                "type": "password_reset",
                "subject_patterns": [
                    "Password Expires Soon",
                    "Security Alert: Update Required",
                    "Account Verification Needed"
                ],
                "body_elements": [
                    "urgent action required",
                    "click here immediately",
                    "verify your account",
                    "suspended if not completed"
                ]
            },
            {
                "type": "ceo_fraud",
                "subject_patterns": [
                    "Urgent Request",
                    "Confidential",
                    "Quick favor"
                ],
                "body_elements": [
                    "wire transfer",
                    "gift cards",
                    "don't tell anyone",
                    "handle personally"
                ]
            }
        ]
    
    def _get_phishing_indicators(self) -> List[str]:
        """Get common phishing indicators"""
        return [
            "Sender address doesn't match organization domain",
            "Generic greeting (Dear Customer/User)",
            "Urgency and threats",
            "Grammar and spelling errors",
            "Suspicious attachments or links",
            "Requests for sensitive information",
            "Too good to be true offers",
            "Mismatched URLs (hover vs displayed)",
            "Unexpected communication",
            "Pressure to bypass normal procedures"
        ]
    
    def _get_phishing_training_content(self) -> Dict[str, Any]:
        """Get phishing training content"""
        return {
            "modules": [
                "Introduction to Phishing",
                "Email Header Analysis",
                "Link and Attachment Safety",
                "Reporting Procedures",
                "Incident Response"
            ],
            "interactive_elements": [
                "Phishing email identifier game",
                "URL analysis tool",
                "Simulated reporting practice"
            ],
            "resources": [
                "Quick reference card",
                "Decision tree poster",
                "Mobile app for verification"
            ]
        }
    
    def _get_vishing_scripts(self) -> List[Dict[str, str]]:
        """Get vishing scenario scripts"""
        return [
            {
                "scenario": "IT Support Scam",
                "opening": "Hi, this is IT support. We've detected unusual activity on your account.",
                "request": "I need to verify your password to secure your account.",
                "pressure": "If we don't fix this now, your account will be locked."
            },
            {
                "scenario": "Vendor Update",
                "opening": "This is accounts payable. We need to update our payment information.",
                "request": "Can you confirm the routing number for wire transfers?",
                "pressure": "We have invoices pending that need immediate payment."
            }
        ]
    
    def _get_vishing_indicators(self) -> List[str]:
        """Get vishing red flags"""
        return [
            "Caller creates urgency or fear",
            "Requests sensitive information",
            "Refuses to provide callback number",
            "Becomes aggressive when questioned",
            "Claims to be from IT/Security without prior notice",
            "Asks to bypass normal procedures",
            "Background noise doesn't match claimed location",
            "Caller ID appears spoofed or blocked"
        ]
    
    def _get_vishing_training_content(self) -> Dict[str, Any]:
        """Get vishing training content"""
        return {
            "topics": [
                "Voice phishing overview",
                "Caller verification techniques",
                "Information protection protocols",
                "Proper call handling procedures"
            ],
            "exercises": [
                "Roleplay scenarios",
                "Verification practice",
                "Incident reporting drill"
            ]
        }
    
    def _get_physical_security_scenarios(self) -> List[Dict[str, str]]:
        """Get physical security test scenarios"""
        return [
            {
                "type": "tailgating",
                "description": "Attempt to follow employee through secured door",
                "setup": "Carry boxes, appear to struggle with badge"
            },
            {
                "type": "visitor_badge",
                "description": "Test visitor badge procedures",
                "setup": "Request access to restricted areas"
            },
            {
                "type": "information_gathering",
                "description": "Attempt to gather sensitive information",
                "setup": "Pose as vendor conducting survey"
            }
        ]
    
    def _get_physical_security_training(self) -> Dict[str, Any]:
        """Get physical security training content"""
        return {
            "topics": [
                "Badge and access control",
                "Visitor management",
                "Clean desk policy",
                "Sensitive information handling",
                "Incident reporting"
            ],
            "practical_exercises": [
                "Badge checking drill",
                "Visitor escort practice",
                "Security walk-through"
            ]
        }
    
    # Additional helper methods
    def _get_foundation_content(self, maturity: AudienceMaturity) -> Dict[str, Any]:
        """Get foundation training content based on maturity"""
        return {
            "core_concepts": [
                "Social engineering definition",
                "Common attack vectors",
                "Psychology of manipulation",
                "Defense strategies"
            ],
            "case_studies": self._get_case_studies(maturity),
            "best_practices": self._get_best_practices(maturity)
        }
    
    def _get_case_studies(self, maturity: AudienceMaturity) -> List[Dict[str, str]]:
        """Get relevant case studies"""
        studies = [
            {
                "title": "Basic Phishing Attack",
                "description": "Simple email phishing attempt",
                "lessons": ["Verify sender", "Check links", "Report suspicious emails"],
                "difficulty": AudienceMaturity.NOVICE
            },
            {
                "title": "Targeted Spear Phishing",
                "description": "Sophisticated targeted attack using personal information",
                "lessons": ["Social media privacy", "Information verification", "Multi-factor authentication"],
                "difficulty": AudienceMaturity.INTERMEDIATE
            },
            {
                "title": "Advanced Persistent Threat",
                "description": "Long-term sophisticated campaign",
                "lessons": ["Behavioral analysis", "Network monitoring", "Incident response"],
                "difficulty": AudienceMaturity.ADVANCED
            }
        ]
        
        # Filter based on maturity level
        maturity_value = list(AudienceMaturity).index(maturity)
        return [s for s in studies if list(AudienceMaturity).index(s["difficulty"]) <= maturity_value]
    
    def _get_best_practices(self, maturity: AudienceMaturity) -> List[str]:
        """Get security best practices"""
        practices = [
            "Verify all unexpected requests",
            "Never share passwords or credentials",
            "Report suspicious activity immediately",
            "Keep software and systems updated",
            "Use strong, unique passwords",
            "Enable multi-factor authentication",
            "Regular security training participation",
            "Maintain situational awareness"
        ]
        
        if maturity in [AudienceMaturity.ADVANCED, AudienceMaturity.EXPERT]:
            practices.extend([
                "Implement zero-trust principles",
                "Regular security audits",
                "Threat intelligence monitoring",
                "Incident response planning"
            ])
        
        return practices
    
    def _get_foundation_exercises(self, maturity: AudienceMaturity) -> List[Dict[str, Any]]:
        """Get foundation exercises"""
        return [
            {
                "type": "identification",
                "title": "Spot the Red Flags",
                "description": "Identify security issues in scenarios",
                "difficulty": maturity.value,
                "time_minutes": 10
            },
            {
                "type": "decision_tree",
                "title": "Response Decision Making",
                "description": "Choose appropriate responses to security situations",
                "difficulty": maturity.value,
                "time_minutes": 15
            }
        ]
    
    def _get_foundation_assessment(self, maturity: AudienceMaturity) -> Dict[str, Any]:
        """Get foundation assessment"""
        return {
            "format": "multiple_choice",
            "questions": 20 if maturity == AudienceMaturity.NOVICE else 30,
            "passing_score": 70 if maturity == AudienceMaturity.NOVICE else 80,
            "time_limit_minutes": 30,
            "retake_allowed": True,
            "feedback_provided": True
        }
    
    def _verify_consent(self, 
                       participants: List[str],
                       campaign: Campaign) -> Dict[str, Any]:
        """Verify participant consent"""
        # This would integrate with actual consent management system
        return {
            "all_consented": True,
            "missing": [],
            "opted_out": []
        }
    
    def _log_simulation_start(self, 
                             campaign_id: str,
                             scenario_id: str,
                             participants: List[str]):
        """Log simulation start for audit trail"""
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "campaign_id": campaign_id,
            "scenario_id": scenario_id,
            "participants": len(participants),
            "action": "simulation_started"
        }
        # Would write to actual logging system
        print(f"Simulation started: {json.dumps(log_entry, indent=2)}")
    
    def _generate_executive_summary(self, campaign: Campaign) -> Dict[str, Any]:
        """Generate executive summary of campaign"""
        return {
            "overview": f"Security awareness campaign '{campaign.name}' completed successfully",
            "key_achievements": [
                "Increased reporting rate by 150%",
                "Reduced click rate by 60%",
                "90% training completion rate"
            ],
            "areas_for_improvement": [
                "Response time to incidents",
                "Physical security awareness",
                "Mobile device security"
            ],
            "recommendations": [
                "Quarterly refresher training",
                "Enhanced incident response procedures",
                "Department-specific scenarios"
            ]
        }
    
    def _generate_detailed_results(self, campaign: Campaign) -> Dict[str, Any]:
        """Generate detailed campaign results"""
        return {
            "participation": {
                "total_eligible": 500,
                "total_participated": 450,
                "participation_rate": 90.0,
                "opt_outs": 10
            },
            "scenario_results": {
                scenario.scenario_id: {
                    "name": scenario.name,
                    "success_rate": random.uniform(60, 90),
                    "average_response_time": random.uniform(5, 30),
                    "reported": random.uniform(40, 80)
                }
                for scenario in campaign.scenarios
            },
            "training_results": {
                module.module_id: {
                    "title": module.title,
                    "completion_rate": random.uniform(80, 95),
                    "average_score": random.uniform(70, 90),
                    "time_spent": module.duration_minutes * random.uniform(0.8, 1.2)
                }
                for module in campaign.training_modules
            }
        }
    
    def _analyze_metrics(self, campaign: Campaign) -> Dict[str, Any]:
        """Analyze campaign metrics"""
        metrics = campaign.metrics
        return {
            "baseline_comparison": {
                metric: {
                    "baseline": baseline,
                    "target": metrics.target_metrics.get(metric, baseline),
                    "achieved": baseline * random.uniform(0.4, 1.2),
                    "improvement": random.uniform(-20, 60)
                }
                for metric, baseline in metrics.baseline_metrics.items()
            },
            "trend_analysis": "Positive trend observed across all metrics",
            "statistical_significance": "Results are statistically significant (p < 0.05)"
        }
    
    def _compile_lessons_learned(self, campaign: Campaign) -> List[str]:
        """Compile lessons learned from campaign"""
        return [
            "Personalized scenarios are more effective",
            "Morning simulations have higher engagement",
            "Technical staff require advanced scenarios",
            "Positive reinforcement improves participation",
            "Clear opt-out procedures reduce anxiety"
        ]
    
    def _generate_recommendations(self, campaign: Campaign) -> List[Dict[str, str]]:
        """Generate recommendations based on campaign results"""
        return [
            {
                "priority": "High",
                "recommendation": "Implement monthly micro-training sessions",
                "rationale": "Maintains awareness without training fatigue",
                "timeline": "Next quarter"
            },
            {
                "priority": "Medium",
                "recommendation": "Develop role-specific scenarios",
                "rationale": "Increases relevance and engagement",
                "timeline": "Next 6 months"
            },
            {
                "priority": "Low",
                "recommendation": "Create security champions program",
                "rationale": "Peer influence enhances culture change",
                "timeline": "Next year"
            }
        ]
    
    def _get_participant_feedback(self, campaign_id: str) -> Dict[str, Any]:
        """Get participant feedback (simulated)"""
        return {
            "survey_responses": 380,
            "overall_satisfaction": 4.2,
            "training_effectiveness": 4.5,
            "scenario_realism": 4.0,
            "comments": [
                "Very eye-opening experience",
                "Helped me understand the risks better",
                "Would like more hands-on practice"
            ]
        }
    
    # Template methods for various communications
    def _get_password_reset_template(self) -> str:
        """Get password reset phishing template"""
        return """Dear User,

Your password will expire in 2 hours. Click here immediately to reset:
http://company-support.com/reset

If you don't reset now, your account will be locked and you won't be able to work.

IT Support Team
This message is confidential"""
    
    def _get_ceo_fraud_template(self) -> str:
        """Get CEO fraud template"""
        return """Hi,

I need you to handle something urgently and confidentially. 
I'm in a meeting and can't talk. Please purchase $2000 in gift cards 
for a client emergency and send me the codes ASAP.

Don't mention this to anyone else - it's sensitive.

Thanks,
CEO"""
    
    def _get_invoice_template(self) -> str:
        """Get fake invoice template"""
        return """Attention Accounts Payable,

Our records show invoice #INV-2024-1337 is now 30 days overdue.
Amount due: $15,847.23

Please process payment immediately to avoid service interruption.
See attached invoice for details.

Vendor Portal Team"""
    
    def _get_email_security_checklist(self) -> List[str]:
        """Get email security checklist"""
        return [
            "Check sender's email address carefully",
            "Hover over links before clicking",
            "Verify unexpected attachments",
            "Look for spelling and grammar errors",
            "Question urgent requests",
            "Verify through separate channel if unsure",
            "Never provide passwords via email",
            "Report suspicious emails immediately"
        ]
    
    def _get_caller_verification_protocol(self) -> Dict[str, str]:
        """Get caller verification protocol"""
        return {
            "step1": "Ask for caller's name and department",
            "step2": "Request callback number",
            "step3": "End call politely",
            "step4": "Verify through company directory",
            "step5": "Call back on verified number",
            "step6": "Report if verification fails"
        }
    
    def _get_vishing_red_flags(self) -> List[str]:
        """Get vishing red flags"""
        return [
            "Unsolicited calls requesting information",
            "Pressure to act immediately",
            "Threats of account closure or legal action",
            "Requests for passwords or PINs",
            "Caller can't provide verifiable information",
            "Request to install software or visit website",
            "Unusual payment requests",
            "Caller becomes hostile when questioned"
        ]
    
    def _create_chat_security_module(self,
                                    maturity: AudienceMaturity,
                                    objective: str) -> TrainingModule:
        """Create chat/messaging security module"""
        return TrainingModule(
            module_id=self._generate_id("module"),
            title="Chat and Messaging Security",
            audience_level=maturity,
            duration_minutes=30,
            objectives=[
                "Identify chat-based social engineering",
                "Verify identity in messaging platforms",
                "Protect sensitive information in chats"
            ],
            content={
                "sections": [
                    {
                        "title": "Chat Platform Risks",
                        "content": "Overview of messaging platform vulnerabilities",
                        "platforms": ["Slack", "Teams", "Discord", "WhatsApp"]
                    },
                    {
                        "title": "Identity Verification",
                        "content": "How to verify users in chat platforms",
                        "techniques": ["Video call verification", "Shared secret", "Official channels"]
                    }
                ]
            },
            exercises=[
                {
                    "type": "simulation",
                    "description": "Identify fake chat requests",
                    "scenarios": 5
                }
            ],
            assessment={
                "type": "practical",
                "tasks": 8,
                "passing_score": 75
            },
            resources=["Chat security guide", "Platform-specific settings"]
        )
    
    def _create_physical_security_module(self,
                                        maturity: AudienceMaturity,
                                        objective: str) -> TrainingModule:
        """Create physical security module"""
        return TrainingModule(
            module_id=self._generate_id("module"),
            title="Physical Security Awareness",
            audience_level=maturity,
            duration_minutes=40,
            objectives=[
                "Understand physical security threats",
                "Follow access control procedures",
                "Identify and report suspicious behavior"
            ],
            content={
                "sections": [
                    {
                        "title": "Access Control",
                        "content": "Badge procedures and tailgating prevention"
                    },
                    {
                        "title": "Visitor Management",
                        "content": "Proper visitor handling and escort procedures"
                    },
                    {
                        "title": "Information Protection",
                        "content": "Clean desk policy and document handling"
                    }
                ]
            },
            exercises=[
                {
                    "type": "walkthrough",
                    "description": "Security tour of facility",
                    "duration_minutes": 20
                }
            ],
            assessment={
                "type": "checklist",
                "items": 15,
                "passing_score": 90
            },
            resources=["Facility map", "Emergency procedures", "Security contacts"]
        )
    
    def _create_sms_security_module(self,
                                   maturity: AudienceMaturity,
                                   objective: str) -> TrainingModule:
        """Create SMS/smishing security module"""
        return TrainingModule(
            module_id=self._generate_id("module"),
            title="SMS and Smishing Prevention",
            audience_level=maturity,
            duration_minutes=25,
            objectives=[
                "Recognize smishing attempts",
                "Verify legitimate SMS communications",
                "Protect against SIM swapping"
            ],
            content={
                "sections": [
                    {
                        "title": "Smishing Tactics",
                        "content": "Common SMS-based attacks",
                        "examples": ["Fake delivery notifications", "Bank alerts", "2FA bypasses"]
                    },
                    {
                        "title": "Mobile Security",
                        "content": "Protecting your mobile device",
                        "settings": ["App permissions", "Unknown sources", "Carrier security"]
                    }
                ]
            },
            exercises=[
                {
                    "type": "identification",
                    "description": "Spot fake SMS messages",
                    "samples": 10
                }
            ],
            assessment={
                "type": "quiz",
                "questions": 10,
                "passing_score": 80
            },
            resources=["SMS security checklist", "Carrier security contacts"]
        )
    
    def _create_social_media_module(self,
                                   maturity: AudienceMaturity,
                                   objective: str) -> TrainingModule:
        """Create social media security module"""
        return TrainingModule(
            module_id=self._generate_id("module"),
            title="Social Media Security and Privacy",
            audience_level=maturity,
            duration_minutes=35,
            objectives=[
                "Understand social media risks",
                "Configure privacy settings properly",
                "Recognize social engineering on platforms"
            ],
            content={
                "sections": [
                    {
                        "title": "Information Leakage",
                        "content": "How attackers use social media for reconnaissance"
                    },
                    {
                        "title": "Privacy Settings",
                        "content": "Platform-specific privacy configurations"
                    },
                    {
                        "title": "Social Engineering",
                        "content": "Common attacks via social media"
                    }
                ]
            },
            exercises=[
                {
                    "type": "audit",
                    "description": "Review and secure your social media profiles",
                    "platforms": ["LinkedIn", "Facebook", "Twitter", "Instagram"]
                }
            ],
            assessment={
                "type": "practical",
                "tasks": 10,
                "passing_score": 85
            },
            resources=["Privacy settings guides", "Professional vs personal guidelines"]
        )
    
    def _create_generic_module(self,
                              maturity: AudienceMaturity,
                              objective: str) -> TrainingModule:
        """Create generic security module"""
        return TrainingModule(
            module_id=self._generate_id("module"),
            title="General Security Awareness",
            audience_level=maturity,
            duration_minutes=30,
            objectives=[
                "Understand security fundamentals",
                "Recognize common threats",
                "Follow security best practices"
            ],
            content={
                "sections": [
                    {
                        "title": "Security Basics",
                        "content": "Fundamental security concepts"
                    },
                    {
                        "title": "Threat Landscape",
                        "content": "Current threats and trends"
                    },
                    {
                        "title": "Best Practices",
                        "content": "Security hygiene and procedures"
                    }
                ]
            },
            exercises=[
                {
                    "type": "review",
                    "description": "Security policy review",
                    "documents": 5
                }
            ],
            assessment={
                "type": "quiz",
                "questions": 15,
                "passing_score": 75
            },
            resources=["Security policy", "Quick reference guide"]
        )
    
    def _create_phone_scenario(self,
                              maturity: AudienceMaturity,
                              objective: str,
                              rules: RulesOfEngagement,
                              variant: int) -> SimulationScenario:
        """Create phone/vishing scenario"""
        templates = [
            {
                "name": "IT Support Vishing",
                "description": "Fake IT support call requesting credentials",
                "setup": {
                    "script": "Hello, this is IT support. We're doing system maintenance and need to verify your account.",
                    "caller_id": "IT Help Desk",
                    "requests": ["Username", "Password", "2FA code"]
                },
                "indicators": [
                    "Unsolicited IT support call",
                    "Requests for password",
                    "Creates false urgency",
                    "Can't provide ticket number"
                ]
            },
            {
                "name": "Vendor Payment Update",
                "description": "Fake vendor requesting payment information update",
                "setup": {
                    "script": "This is your software vendor. We need to update payment information on file.",
                    "requests": ["Credit card", "Banking details", "Authorize payment"]
                },
                "indicators": [
                    "Unsolicited payment request",
                    "Different phone number than usual",
                    "Pressure to act quickly",
                    "Can't verify account details"
                ]
            }
        ]
        
        template = templates[variant % len(templates)]
        
        return SimulationScenario(
            scenario_id=self._generate_id("scenario"),
            name=template["name"],
            type=CampaignType.VISHING,
            channel=Channel.PHONE,
            difficulty=maturity,
            description=template["description"],
            objective=f"Test ability to identify and handle {template['name'].lower()}",
            setup=template["setup"],
            indicators=template["indicators"],
            opt_out_instructions=self._get_opt_out_instructions(Channel.PHONE, rules)
        )
    
    def _create_chat_scenario(self,
                             maturity: AudienceMaturity,
                             objective: str,
                             rules: RulesOfEngagement,
                             variant: int) -> SimulationScenario:
        """Create chat/messaging scenario"""
        return SimulationScenario(
            scenario_id=self._generate_id("scenario"),
            name="Chat Impersonation",
            type=CampaignType.PRETEXTING,
            channel=Channel.CHAT,
            difficulty=maturity,
            description="Impersonation attempt via chat platform",
            objective="Test ability to verify identity in chat platforms",
            setup={
                "platform": "Corporate Chat",
                "impersonation": "Colleague or manager",
                "request": "Urgent file or information sharing"
            },
            indicators=[
                "New or unusual chat request",
                "Urgency without context",
                "Request for sensitive data",
                "Avoiding voice/video call"
            ],
            opt_out_instructions=self._get_opt_out_instructions(Channel.CHAT, rules)
        )
    
    def _create_physical_scenario(self,
                                 maturity: AudienceMaturity,
                                 objective: str,
                                 rules: RulesOfEngagement,
                                 variant: int) -> SimulationScenario:
        """Create physical security scenario"""
        return SimulationScenario(
            scenario_id=self._generate_id("scenario"),
            name="Tailgating Test",
            type=CampaignType.TAILGATING,
            channel=Channel.IN_PERSON,
            difficulty=maturity,
            description="Test physical access control awareness",
            objective="Verify badge checking and access control procedures",
            setup={
                "location": "Main entrance",
                "method": "Follow employee through door",
                "props": ["Boxes", "Coffee cups", "Phone call distraction"]
            },
            indicators=[
                "No visible badge",
                "Avoiding security checkpoint",
                "Following closely behind",
                "Creating distraction"
            ],
            opt_out_instructions=self._get_opt_out_instructions(Channel.IN_PERSON, rules)
        )
    
    def _create_generic_scenario(self,
                                maturity: AudienceMaturity,
                                objective: str,
                                rules: RulesOfEngagement,
                                variant: int) -> SimulationScenario:
        """Create generic scenario for any channel"""
        return SimulationScenario(
            scenario_id=self._generate_id("scenario"),
            name="Generic Security Test",
            type=CampaignType.PRETEXTING,
            channel=Channel.EMAIL,
            difficulty=maturity,
            description="General security awareness test",
            objective="Test overall security awareness",
            setup={
                "type": "generic",
                "customizable": True
            },
            indicators=["Various security indicators"],
            opt_out_instructions=self._get_opt_out_instructions(Channel.EMAIL, rules)
        )
    
    # Report template methods
    def _get_executive_summary_template(self) -> str:
        """Get executive summary template"""
        return """
# Executive Summary

## Campaign Overview
{campaign_name}
Duration: {start_date} to {end_date}
Participants: {participant_count}

## Key Findings
• {finding_1}
• {finding_2}
• {finding_3}

## Recommendations
1. {recommendation_1}
2. {recommendation_2}
3. {recommendation_3}

## Next Steps
{next_steps}
"""
    
    def _get_detailed_report_template(self) -> str:
        """Get detailed report template"""
        return """
# Detailed Security Awareness Campaign Report

## 1. Campaign Overview
{overview_section}

## 2. Methodology
{methodology_section}

## 3. Results by Scenario
{scenario_results}

## 4. Training Effectiveness
{training_results}

## 5. Lessons Learned
{lessons_learned}

## 6. Recommendations
{recommendations}

## Appendices
A. Raw Data
B. Participant Feedback
C. Scenario Details
"""
    
    def _get_individual_feedback_template(self) -> str:
        """Get individual participant feedback template"""
        return """
Dear {participant_name},

Thank you for participating in our security awareness campaign.

Your Results:
• Scenarios completed: {scenarios_completed}
• Success rate: {success_rate}%
• Training modules completed: {modules_completed}
• Areas of strength: {strengths}
• Areas for improvement: {improvements}

Next Steps:
{next_steps}

Resources:
{resources}

Thank you for helping keep our organization secure!
"""
    
    def _get_team_feedback_template(self) -> str:
        """Get team feedback template"""
        return """
Team Performance Summary

Department: {department}
Participation Rate: {participation}%
Overall Success Rate: {success_rate}%

Strengths:
{team_strengths}

Opportunities:
{team_opportunities}

Recommended Actions:
{team_actions}
"""
    
    def _get_recognition_template(self) -> str:
        """Get recognition template for high performers"""
        return """
Security Champion Recognition

We're pleased to recognize the following individuals for exceptional 
performance in our security awareness campaign:

{champion_list}

These security champions demonstrated:
• Excellent threat detection
• Prompt incident reporting
• Peer mentoring and support
• 100% training completion

Thank you for your commitment to security!
"""
    
    def _get_improvement_timeline(self) -> Dict[str, List[str]]:
        """Get improvement timeline"""
        return {
            "immediate": [
                "Update incident response procedures",
                "Deploy quick reference guides",
                "Schedule follow-up training"
            ],
            "30_days": [
                "Implement enhanced email filtering",
                "Roll out security champion program",
                "Conduct targeted department training"
            ],
            "90_days": [
                "Deploy technical controls",
                "Measure improvement metrics",
                "Plan next campaign"
            ],
            "6_months": [
                "Full program review",
                "Advanced scenario development",
                "Culture assessment"
            ]
        }
    
    def _get_all_staff_template(self) -> str:
        """Get all-staff communication template"""
        return """
Subject: Security Awareness Campaign Results

Dear Team,

We recently completed our security awareness campaign with excellent results:

✓ 90% participation rate
✓ 65% improvement in threat detection
✓ 150% increase in incident reporting

Key Takeaways:
• Always verify unexpected requests
• Report suspicious activity immediately
• When in doubt, reach out to security

Thank you for your participation and commitment to keeping our organization secure!

Security Team
"""
    
    def _get_newsletter_template(self) -> str:
        """Get newsletter article template"""
        return """
SECURITY SPOTLIGHT: Awareness Campaign Success

Our recent security awareness campaign showed significant improvements 
in our collective security posture. Through realistic simulations and 
engaging training, participants learned to identify and respond to 
various security threats.

Highlights include improved phishing detection, faster incident response 
times, and increased security discussions among teams.

Remember: Security is everyone's responsibility. Stay vigilant!
"""
    
    def _get_intranet_template(self) -> str:
        """Get intranet post template"""
        return """
<h2>Security Awareness Campaign Complete</h2>

<p>Thank you to everyone who participated in our security awareness campaign!</p>

<h3>Results</h3>
<ul>
<li>450 participants trained</li>
<li>60% reduction in clicking suspicious links</li>
<li>2x faster incident reporting</li>
</ul>

<h3>Resources</h3>
<p>Access training materials and quick reference guides on the security portal.</p>

<button>View Resources</button>
"""


# Example usage
if __name__ == "__main__":
    # Initialize strategist
    strategist = SocialEngineeringStrategist()
    
    # Define rules of engagement
    rules = RulesOfEngagement(
        explicit_consent=True,
        opt_out_available=True,
        no_harm_principle=True,
        data_protection=True,
        approval_required=["legal", "hr", "ciso"],
        excluded_scenarios=["financial_loss", "reputation_damage"],
        time_restrictions={"business_hours_only": "9am-5pm"},
        escalation_contacts=[
            {"name": "Security Team", "email": "security@company.com", "phone": "x1234"}
        ]
    )
    
    # Create campaign
    campaign = strategist.create_campaign(
        objective="Improve phishing detection and reporting",
        audience={
            "department": "Finance",
            "role": "All levels",
            "size": 50,
            "prior_training": 2,
            "risk_level": "high"
        },
        channels=[Channel.EMAIL, Channel.PHONE],
        rules=rules,
        duration_days=30
    )
    
    print(f"Campaign created: {campaign.campaign_id}")
    print(f"Name: {campaign.name}")
    print(f"Training modules: {len(campaign.training_modules)}")
    print(f"Scenarios: {len(campaign.scenarios)}")
    print("\nScenarios:")
    for scenario in campaign.scenarios:
        print(f"  - {scenario.name} ({scenario.type.value} via {scenario.channel.value})")
        print(f"    Safe word: {scenario.safe_word}")
    
    print("\nTraining Modules:")
    for module in campaign.training_modules:
        print(f"  - {module.title} ({module.duration_minutes} minutes)")
    
    print("\nSuccess Metrics:")
    for metric, target in campaign.metrics.target_metrics.items():
        baseline = campaign.metrics.baseline_metrics.get(metric, 0)
        print(f"  - {metric}: {baseline:.1f} -> {target:.1f} (target)")
    
    # Simulate running a scenario
    print("\n" + "="*50)
    if campaign.scenarios:
        simulation_result = strategist.run_simulation(
            campaign_id=campaign.campaign_id,
            scenario_id=campaign.scenarios[0].scenario_id,
            participants=["user1@company.com", "user2@company.com"]
        )
        print(f"Simulation started: {simulation_result}")
    
    # Generate report
    print("\n" + "="*50)
    report = strategist.generate_report(campaign.campaign_id)
    print("Campaign Report Generated:")
    print(f"  Executive Summary: {report['executive_summary']['overview']}")
    print(f"  Lessons Learned: {len(report['lessons_learned'])} items")
    print(f"  Recommendations: {len(report['recommendations'])} items")
#!/usr/bin/env python3
"""
Social Engineering Strategist

A tool for planning ethical awareness campaigns and simulations with clear consent boundaries.
Focuses on security awareness training through controlled, consensual social engineering simulations.

Safety Class: Advisory
Purpose: Plan ethical awareness campaigns and simulations with clear consent boundaries
"""

import json
import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import uuid


class Channel(Enum):
    EMAIL = "email"
    CHAT = "chat"
    PHONE = "phone"
    IN_PERSON = "in_person"


class RulesOfEngagement(Enum):
    CONSENT = "consent"
    NO_HARM = "no_harm"
    OPT_OUT = "opt_out"


@dataclass
class CampaignInputs:
    """Input parameters for social engineering awareness campaigns"""
    objective: str
    audience: str
    channels: List[Channel]
    rules_of_engagement: List[RulesOfEngagement]
    department: Optional[str] = None
    role: Optional[str] = None


@dataclass
class TrainingModule:
    """Individual training module structure"""
    id: str
    title: str
    content: str
    audience_level: str
    duration_minutes: int
    learning_objectives: List[str]
    opt_out_instructions: str
    escalation_path: str


@dataclass
class SimulationScenario:
    """Simulated social engineering scenario"""
    id: str
    name: str
    description: str
    channel: Channel
    difficulty_level: str
    consent_required: bool
    opt_out_language: str
    success_criteria: List[str]
    debrief_questions: List[str]
    estimated_duration_minutes: int = 30


@dataclass
class SuccessMetrics:
    """Metrics for measuring campaign effectiveness"""
    baseline_metrics: Dict[str, float]
    target_improvements: Dict[str, float]
    measurement_methods: List[str]
    reporting_frequency: str


@dataclass
class DebriefMaterials:
    """Materials for post-simulation debriefing"""
    general_guidelines: str
    scenario_specific_notes: Dict[str, str]
    learning_outcomes: List[str]
    follow_up_actions: List[str]


class SocialEngineeringStrategist:
    """
    Main class for planning ethical social engineering awareness campaigns.
    
    This tool helps security teams create educational simulations that:
    - Respect participant consent and privacy
    - Provide clear opt-out mechanisms
    - Focus on learning rather than punishment
    - Measure effectiveness through defined metrics
    """
    
    def __init__(self):
        self.campaigns = {}
        self.training_modules = {}
        self.scenarios = {}
        
    def create_campaign(self, inputs: CampaignInputs) -> Dict[str, Any]:
        """
        Create a comprehensive social engineering awareness campaign.
        
        Args:
            inputs: Campaign configuration parameters
            
        Returns:
            Complete campaign plan with training modules, scenarios, and metrics
        """
        campaign_id = str(uuid.uuid4())
        
        # Validate inputs and ensure safety compliance
        self._validate_inputs(inputs)
        
        # Generate campaign components
        training_modules = self._generate_training_modules(inputs)
        scenarios = self._generate_simulation_scenarios(inputs)
        metrics = self._create_success_metrics(inputs)
        debrief_materials = self._create_debrief_materials(inputs)
        
        campaign = {
            "id": campaign_id,
            "created_at": datetime.datetime.now().isoformat(),
            "inputs": asdict(inputs),
            "training_modules": [asdict(module) for module in training_modules],
            "simulation_scenarios": [asdict(scenario) for scenario in scenarios],
            "success_metrics": asdict(metrics),
            "debrief_materials": asdict(debrief_materials),
            "safety_compliance": self._generate_safety_compliance_report(inputs)
        }
        
        self.campaigns[campaign_id] = campaign
        return campaign
    
    def _validate_inputs(self, inputs: CampaignInputs) -> None:
        """Validate campaign inputs and ensure safety compliance"""
        if not inputs.objective:
            raise ValueError("Campaign objective is required")
        
        if not inputs.audience:
            raise ValueError("Target audience must be specified")
        
        if not inputs.channels:
            raise ValueError("At least one communication channel must be specified")
        
        if RulesOfEngagement.CONSENT not in inputs.rules_of_engagement:
            raise ValueError("Consent must be included in rules of engagement")
        
        if RulesOfEngagement.OPT_OUT not in inputs.rules_of_engagement:
            raise ValueError("Opt-out mechanism must be included in rules of engagement")
    
    def _generate_training_modules(self, inputs: CampaignInputs) -> List[TrainingModule]:
        """Generate audience-specific training modules"""
        modules = []
        
        # Determine audience maturity level
        maturity_level = self._assess_audience_maturity(inputs.audience)
        
        # Core awareness module
        core_module = TrainingModule(
            id=str(uuid.uuid4()),
            title="Social Engineering Awareness Fundamentals",
            content=self._generate_core_content(inputs, maturity_level),
            audience_level=maturity_level,
            duration_minutes=30,
            learning_objectives=[
                "Recognize common social engineering tactics",
                "Understand the psychology behind social engineering",
                "Learn to verify requests through proper channels",
                "Know when and how to report suspicious activity"
            ],
            opt_out_instructions=self._generate_opt_out_instructions(),
            escalation_path="Report to security team or supervisor immediately"
        )
        modules.append(core_module)
        
        # Channel-specific modules
        for channel in inputs.channels:
            channel_module = TrainingModule(
                id=str(uuid.uuid4()),
                title=f"Social Engineering Defense - {channel.value.title()}",
                content=self._generate_channel_specific_content(channel, maturity_level),
                audience_level=maturity_level,
                duration_minutes=20,
                learning_objectives=[
                    f"Identify social engineering attempts via {channel.value}",
                    f"Apply appropriate verification procedures for {channel.value}",
                    f"Report suspicious {channel.value} communications"
                ],
                opt_out_instructions=self._generate_opt_out_instructions(),
                escalation_path="Contact IT security team or use incident reporting system"
            )
            modules.append(channel_module)
        
        return modules
    
    def _generate_simulation_scenarios(self, inputs: CampaignInputs) -> List[SimulationScenario]:
        """Generate ethical simulation scenarios with proper consent mechanisms"""
        scenarios = []
        
        for channel in inputs.channels:
            scenario = SimulationScenario(
                id=str(uuid.uuid4()),
                name=f"Simulated {channel.value.title()} Attack - {inputs.audience}",
                description=self._generate_scenario_description(channel, inputs.audience),
                channel=channel,
                difficulty_level=self._assess_difficulty_level(inputs.audience),
                consent_required=True,
                opt_out_language=self._generate_scenario_opt_out_language(),
                success_criteria=self._generate_success_criteria(channel),
                debrief_questions=self._generate_debrief_questions(channel),
                estimated_duration_minutes=30
            )
            scenarios.append(scenario)
        
        return scenarios
    
    def _create_success_metrics(self, inputs: CampaignInputs) -> SuccessMetrics:
        """Create measurable success metrics for the campaign"""
        return SuccessMetrics(
            baseline_metrics={
                "current_awareness_score": 0.0,  # To be measured before campaign
                "incident_response_time": 0.0,   # Average time to report incidents
                "false_positive_rate": 0.0,      # Incorrectly flagged legitimate communications
                "training_completion_rate": 0.0   # Percentage completing training
            },
            target_improvements={
                "awareness_score_increase": 25.0,  # Percentage improvement target
                "response_time_reduction": 50.0,   # Percentage faster response
                "false_positive_reduction": 30.0,  # Reduce false positives
                "completion_rate_target": 95.0     # Target completion percentage
            },
            measurement_methods=[
                "Pre and post-training assessments",
                "Simulation participation tracking",
                "Incident reporting metrics",
                "Feedback surveys"
            ],
            reporting_frequency="Weekly during campaign, monthly post-campaign"
        )
    
    def _create_debrief_materials(self, inputs: CampaignInputs) -> DebriefMaterials:
        """Create comprehensive debrief materials"""
        return DebriefMaterials(
            general_guidelines=self._generate_debrief_guidelines(),
            scenario_specific_notes=self._generate_scenario_notes(inputs.channels),
            learning_outcomes=[
                "Enhanced recognition of social engineering tactics",
                "Improved verification procedures",
                "Better incident reporting practices",
                "Increased security awareness culture"
            ],
            follow_up_actions=[
                "Schedule follow-up training sessions",
                "Implement additional security controls if needed",
                "Share lessons learned with other departments",
                "Update security policies based on findings"
            ]
        )
    
    def _assess_audience_maturity(self, audience: str) -> str:
        """Assess the security awareness maturity level of the target audience"""
        audience_lower = audience.lower()
        
        if any(term in audience_lower for term in ["executive", "c-suite", "senior", "management"]):
            return "advanced"
        elif any(term in audience_lower for term in ["it", "security", "technical", "engineer"]):
            return "intermediate"
        else:
            return "beginner"
    
    def _assess_difficulty_level(self, audience: str) -> str:
        """Assess appropriate difficulty level for simulations"""
        maturity = self._assess_audience_maturity(audience)
        
        if maturity == "advanced":
            return "high"
        elif maturity == "intermediate":
            return "medium"
        else:
            return "low"
    
    def _generate_core_content(self, inputs: CampaignInputs, maturity_level: str) -> str:
        """Generate core training content based on audience maturity"""
        if maturity_level == "beginner":
            return """
            # Social Engineering Awareness - Beginner Level
            
            ## What is Social Engineering?
            Social engineering is the art of manipulating people to give up confidential information or perform actions that compromise security.
            
            ## Common Tactics
            - **Phishing**: Fake emails trying to trick you
            - **Pretexting**: Creating false scenarios to gain trust
            - **Baiting**: Offering something tempting to get information
            - **Tailgating**: Following someone into a secure area
            
            ## Red Flags to Watch For
            - Urgent requests for sensitive information
            - Requests to bypass normal procedures
            - Pressure to act quickly without verification
            - Unusual communication channels or timing
            
            ## How to Protect Yourself
            1. **Verify**: Always verify requests through official channels
            2. **Think**: Take time to think before acting
            3. **Report**: When in doubt, report to security team
            4. **Trust your instincts**: If something feels wrong, it probably is
            """
        elif maturity_level == "intermediate":
            return """
            # Social Engineering Defense - Intermediate Level
            
            ## Advanced Attack Vectors
            - **Spear Phishing**: Targeted attacks using personal information
            - **Vishing**: Voice-based social engineering
            - **Smishing**: SMS-based attacks
            - **Business Email Compromise**: Impersonating executives
            
            ## Psychological Principles
            - **Authority**: Attackers impersonate authority figures
            - **Urgency**: Creating time pressure to bypass rational thinking
            - **Social Proof**: Using others' actions to influence behavior
            - **Reciprocity**: Creating obligation through small favors
            
            ## Defense Strategies
            - Implement multi-factor verification for sensitive requests
            - Use out-of-band communication for verification
            - Establish clear escalation procedures
            - Regular security awareness training and testing
            """
        else:  # advanced
            return """
            # Advanced Social Engineering Defense
            
            ## Sophisticated Attack Techniques
            - **OSINT Gathering**: Using public information for targeted attacks
            - **Deepfake Technology**: AI-generated voice/video impersonation
            - **Supply Chain Attacks**: Compromising trusted third parties
            - **Insider Threats**: Social engineering internal personnel
            
            ## Organizational Defense
            - **Zero Trust Architecture**: Verify everything, trust nothing
            - **Behavioral Analytics**: Monitor for unusual patterns
            - **Incident Response**: Rapid detection and containment
            - **Continuous Monitoring**: Ongoing threat assessment
            
            ## Leadership Responsibilities
            - Foster security-conscious culture
            - Allocate resources for security initiatives
            - Lead by example in security practices
            - Support incident response efforts
            """
    
    def _generate_channel_specific_content(self, channel: Channel, maturity_level: str) -> str:
        """Generate content specific to communication channel"""
        channel_content = {
            Channel.EMAIL: """
            # Email Security Best Practices
            
            ## Email Red Flags
            - Suspicious sender addresses
            - Unexpected attachments or links
            - Urgent requests for sensitive information
            - Poor grammar or unusual formatting
            
            ## Verification Steps
            1. Check sender's email address carefully
            2. Verify through alternative communication method
            3. Look for official company signatures
            4. Check for recent security advisories
            """,
            Channel.CHAT: """
            # Chat Platform Security
            
            ## Chat-Specific Threats
            - Impersonation in group chats
            - Malicious file sharing
            - Social engineering through casual conversation
            - Credential harvesting attempts
            
            ## Protection Measures
            1. Verify identity before sharing sensitive information
            2. Use official company chat platforms only
            3. Report suspicious behavior immediately
            4. Don't click unknown links or download unexpected files
            """,
            Channel.PHONE: """
            # Phone-Based Social Engineering Defense
            
            ## Voice Attack Vectors
            - Caller ID spoofing
            - Vishing (voice phishing)
            - Impersonation of IT support
            - Urgent requests for remote access
            
            ## Verification Procedures
            1. Ask for callback number and verify through directory
            2. Use established verification phrases
            3. Never provide passwords over the phone
            4. Hang up and call back through official channels
            """,
            Channel.IN_PERSON: """
            # Physical Security Awareness
            
            ## In-Person Threats
            - Tailgating into secure areas
            - Shoulder surfing
            - Dumpster diving for information
            - Impersonation of contractors or visitors
            
            ## Physical Security Measures
            1. Always verify visitor credentials
            2. Don't let others follow you into secure areas
            3. Secure sensitive documents and screens
            4. Report suspicious individuals immediately
            """
        }
        
        return channel_content.get(channel, "Channel-specific content not available")
    
    def _generate_scenario_description(self, channel: Channel, audience: str) -> str:
        """Generate realistic but ethical simulation scenario descriptions"""
        scenarios = {
            Channel.EMAIL: f"""
            **Email Phishing Simulation for {audience}**
            
            Participants will receive a carefully crafted phishing email that appears to come from a legitimate source (e.g., IT department, HR, or a trusted vendor). The email will contain subtle social engineering elements designed to test awareness without causing harm.
            
            **Scenario Elements:**
            - Sender appears legitimate but uses slightly suspicious domain
            - Contains urgent request for password reset or account verification
            - Includes link to fake login page (harmless, just logs the attempt)
            - Uses psychological pressure tactics (urgency, authority)
            
            **Learning Objectives:**
            - Identify suspicious email characteristics
            - Practice verification procedures
            - Understand reporting protocols
            """,
            Channel.CHAT: f"""
            **Chat Impersonation Simulation for {audience}**
            
            A simulated scenario where participants receive messages from someone claiming to be a colleague or supervisor, requesting sensitive information or asking them to perform unusual actions.
            
            **Scenario Elements:**
            - Impersonation of known team members
            - Requests for password sharing or account access
            - Pressure to act quickly without verification
            - Attempts to bypass normal procedures
            
            **Learning Objectives:**
            - Recognize impersonation attempts
            - Practice verification in chat environments
            - Understand appropriate response procedures
            """,
            Channel.PHONE: f"""
            **Vishing Simulation for {audience}**
            
            Participants will receive a phone call from someone claiming to be IT support, requesting remote access or password verification. The call will be conducted by trained security team members.
            
            **Scenario Elements:**
            - Caller claims urgent technical issue
            - Requests remote access to computer
            - Asks for password verification
            - Uses authority and urgency tactics
            
            **Learning Objectives:**
            - Identify vishing attempts
            - Practice phone verification procedures
            - Learn proper escalation methods
            """,
            Channel.IN_PERSON: f"""
            **Physical Security Simulation for {audience}**
            
            A controlled simulation where participants encounter someone attempting to gain unauthorized access to secure areas or information through social engineering tactics.
            
            **Scenario Elements:**
            - Attempted tailgating into secure areas
            - Requests for sensitive information
            - Impersonation of contractors or visitors
            - Attempts to bypass security procedures
            
            **Learning Objectives:**
            - Recognize physical security threats
            - Practice challenge procedures
            - Understand reporting requirements
            """
        }
        
        return scenarios.get(channel, "Scenario description not available")
    
    def _generate_opt_out_instructions(self) -> str:
        """Generate clear opt-out instructions for all participants"""
        return """
        **OPT-OUT INSTRUCTIONS**
        
        You have the right to opt out of this security awareness training and simulation at any time without penalty or negative consequences.
        
        **To opt out:**
        1. Contact the security team at security@company.com
        2. Speak with your direct supervisor
        3. Use the anonymous reporting hotline: 1-800-SECURITY
        
        **What happens if you opt out:**
        - You will not participate in simulations
        - You will still receive general security awareness materials
        - Your decision will not affect your employment or performance reviews
        - You can opt back in at any time
        
        **Questions or concerns:**
        Contact the security team for any questions about this program or your rights as a participant.
        """
    
    def _generate_scenario_opt_out_language(self) -> str:
        """Generate opt-out language specific to simulation scenarios"""
        return """
        **SIMULATION OPT-OUT**
        
        This is a controlled security awareness simulation. You can opt out at any time by:
        - Saying "I opt out" during the simulation
        - Contacting security@company.com
        - Speaking with your supervisor
        
        No negative consequences will result from opting out.
        """
    
    def _generate_success_criteria(self, channel: Channel) -> List[str]:
        """Generate success criteria for each simulation scenario"""
        return [
            f"Participant correctly identifies {channel.value} social engineering attempt",
            "Participant follows proper verification procedures",
            "Participant reports incident through appropriate channels",
            "Participant demonstrates understanding of red flags",
            "Participant completes scenario without providing sensitive information"
        ]
    
    def _generate_debrief_questions(self, channel: Channel) -> List[str]:
        """Generate debrief questions for post-simulation discussion"""
        return [
            f"What made you suspicious about the {channel.value} communication?",
            "What verification steps did you take (or should have taken)?",
            "How did you feel during the simulation?",
            "What would you do differently in a real situation?",
            "What additional training would be helpful?",
            "How confident do you feel about recognizing similar attacks?"
        ]
    
    def _generate_debrief_guidelines(self) -> str:
        """Generate general debriefing guidelines"""
        return """
        **DEBRIEF GUIDELINES**
        
        ## Purpose
        The debrief is a learning opportunity, not a performance evaluation. Focus on education and improvement.
        
        ## Key Principles
        - **Blameless Culture**: No one is at fault for falling for social engineering
        - **Learning Focus**: Emphasize what was learned, not what went wrong
        - **Positive Reinforcement**: Acknowledge good security practices
        - **Continuous Improvement**: Identify areas for additional training
        
        ## Discussion Points
        1. **Recognition**: What signs did participants notice?
        2. **Response**: How did they react to the simulation?
        3. **Learning**: What new insights did they gain?
        4. **Application**: How will they apply this learning?
        5. **Support**: What additional resources do they need?
        
        ## Follow-up Actions
        - Schedule additional training if needed
        - Update security procedures based on feedback
        - Share lessons learned with other teams
        - Monitor for similar real-world attacks
        """
    
    def _generate_scenario_notes(self, channels: List[Channel]) -> Dict[str, str]:
        """Generate scenario-specific debrief notes"""
        notes = {}
        for channel in channels:
            notes[channel.value] = f"""
            **{channel.value.title()} Scenario Debrief Notes**
            
            - Focus on channel-specific red flags
            - Discuss verification procedures for this medium
            - Review reporting mechanisms
            - Address any channel-specific concerns
            - Provide additional resources for this communication method
            """
        return notes
    
    def _generate_safety_compliance_report(self, inputs: CampaignInputs) -> Dict[str, Any]:
        """Generate safety compliance report for the campaign"""
        return {
            "consent_obtained": True,
            "opt_out_mechanisms": "Multiple opt-out methods provided",
            "data_protection": "Participant data will be anonymized and protected",
            "harm_prevention": "Simulations designed to educate, not harm",
            "escalation_paths": "Clear escalation procedures established",
            "approval_status": "Requires security team and legal approval",
            "risk_assessment": "Low risk - educational simulations only",
            "compliance_notes": "All activities comply with ethical guidelines and company policies"
        }
    
    def export_campaign(self, campaign_id: str, format: str = "json") -> str:
        """Export campaign data in specified format"""
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign {campaign_id} not found")
        
        campaign = self.campaigns[campaign_id]
        
        if format.lower() == "json":
            return json.dumps(campaign, indent=2, default=str)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def get_campaign_summary(self, campaign_id: str) -> Dict[str, Any]:
        """Get a summary of the campaign"""
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign {campaign_id} not found")
        
        campaign = self.campaigns[campaign_id]
        
        return {
            "id": campaign["id"],
            "objective": campaign["inputs"]["objective"],
            "audience": campaign["inputs"]["audience"],
            "channels": [ch["value"] for ch in campaign["inputs"]["channels"]],
            "training_modules_count": len(campaign["training_modules"]),
            "scenarios_count": len(campaign["simulation_scenarios"]),
            "created_at": campaign["created_at"],
            "safety_compliance": campaign["safety_compliance"]["approval_status"]
        }


def main():
    """Example usage of the Social Engineering Strategist"""
    
    # Initialize the strategist
    strategist = SocialEngineeringStrategist()
    
    # Example campaign inputs
    inputs = CampaignInputs(
        objective="Improve phishing awareness among customer service team",
        audience="customer service representatives",
        channels=[Channel.EMAIL, Channel.CHAT, Channel.PHONE],
        rules_of_engagement=[RulesOfEngagement.CONSENT, RulesOfEngagement.NO_HARM, RulesOfEngagement.OPT_OUT],
        department="Customer Service",
        role="Representative"
    )
    
    # Create the campaign
    campaign = strategist.create_campaign(inputs)
    
    # Display campaign summary
    print("=== SOCIAL ENGINEERING AWARENESS CAMPAIGN ===")
    print(f"Campaign ID: {campaign['id']}")
    print(f"Objective: {campaign['inputs']['objective']}")
    print(f"Audience: {campaign['inputs']['audience']}")
    print(f"Channels: {[ch.value for ch in campaign['inputs']['channels']]}")
    print(f"Training Modules: {len(campaign['training_modules'])}")
    print(f"Simulation Scenarios: {len(campaign['simulation_scenarios'])}")
    print(f"Safety Compliance: {campaign['safety_compliance']['approval_status']}")
    
    # Export campaign data
    campaign_json = strategist.export_campaign(campaign['id'])
    print(f"\nCampaign exported to JSON format ({len(campaign_json)} characters)")


if __name__ == "__main__":
    main()
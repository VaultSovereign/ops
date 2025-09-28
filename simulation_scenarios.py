#!/usr/bin/env python3
"""
Simulation Scenarios for Social Engineering Awareness Training

This module contains pre-built simulation scenarios for different types of social engineering attacks.
Each scenario includes proper consent mechanisms, opt-out language, and educational objectives.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import uuid
import datetime


class ScenarioType(Enum):
    PHISHING = "phishing"
    VISHING = "vishing"
    SMISHING = "smishing"
    PHYSICAL = "physical"
    PRETEXTING = "pretexting"
    BAITING = "baiting"


class DifficultyLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class SimulationScenario:
    """Complete simulation scenario structure"""
    id: str
    name: str
    scenario_type: ScenarioType
    difficulty_level: DifficultyLevel
    description: str
    learning_objectives: List[str]
    setup_instructions: str
    execution_script: str
    opt_out_language: str
    success_criteria: List[str]
    debrief_questions: List[str]
    safety_considerations: List[str]
    estimated_duration_minutes: int
    required_consent: bool
    data_collection_scope: str


class SimulationScenarioLibrary:
    """Library of pre-built simulation scenarios"""
    
    @staticmethod
    def get_phishing_email_scenario(difficulty: DifficultyLevel = DifficultyLevel.MEDIUM) -> SimulationScenario:
        """Create a phishing email simulation scenario"""
        return SimulationScenario(
            id=str(uuid.uuid4()),
            name="Corporate Phishing Email Simulation",
            scenario_type=ScenarioType.PHISHING,
            difficulty_level=difficulty,
            description="""
            Participants will receive a carefully crafted phishing email that appears to come from the IT department.
            The email will contain subtle social engineering elements designed to test awareness without causing harm.
            """,
            learning_objectives=[
                "Identify suspicious email characteristics",
                "Recognize social engineering tactics in email communications",
                "Practice verification procedures for suspicious emails",
                "Understand proper reporting protocols for phishing attempts"
            ],
            setup_instructions="""
            1. Create a test email account that appears to be from IT department
            2. Craft email with subtle red flags (slight domain misspelling, urgency tactics)
            3. Include a harmless link that logs click attempts
            4. Ensure all participants have provided consent
            5. Set up monitoring to track responses
            6. Prepare debrief materials
            """,
            execution_script="""
            **Email Content:**
            Subject: URGENT: Password Reset Required - Action Needed Within 24 Hours
            
            Dear Employee,
            
            Our security system has detected unusual activity on your account. To prevent unauthorized access, 
            you must reset your password immediately.
            
            Click here to reset your password: [LINK]
            
            This is urgent - your account will be locked if you don't act within 24 hours.
            
            Best regards,
            IT Security Team
            security@company.com
            
            **Red Flags in this email:**
            - Urgent language and time pressure
            - Generic greeting
            - Suspicious link (hover to reveal)
            - Sender address may be slightly off
            """,
            opt_out_language="""
            **SIMULATION NOTICE**
            This is a controlled security awareness simulation. You can opt out at any time by:
            - Replying to this email with "OPT OUT"
            - Contacting security@company.com
            - Speaking with your supervisor
            
            No negative consequences will result from opting out or falling for this simulation.
            """,
            success_criteria=[
                "Participant identifies at least 2 red flags in the email",
                "Participant does not click the suspicious link",
                "Participant reports the email to security team",
                "Participant demonstrates understanding of verification procedures"
            ],
            debrief_questions=[
                "What made you suspicious about this email?",
                "What verification steps did you take (or should have taken)?",
                "How did the urgent language make you feel?",
                "What would you do differently in a real situation?",
                "How confident do you feel about recognizing similar attacks?"
            ],
            safety_considerations=[
                "Ensure all links are harmless and only log click attempts",
                "Do not collect any actual passwords or sensitive information",
                "Provide clear opt-out mechanism",
                "Anonymize all collected data",
                "Follow up with participants who fell for the simulation"
            ],
            estimated_duration_minutes=30,
            required_consent=True,
            data_collection_scope="Click tracking, response time, reporting behavior"
        )
    
    @staticmethod
    def get_vishing_call_scenario(difficulty: DifficultyLevel = DifficultyLevel.MEDIUM) -> SimulationScenario:
        """Create a vishing (voice phishing) simulation scenario"""
        return SimulationScenario(
            id=str(uuid.uuid4()),
            name="IT Support Vishing Simulation",
            scenario_type=ScenarioType.VISHING,
            difficulty_level=difficulty,
            description="""
            Participants will receive a phone call from someone claiming to be IT support.
            The caller will use social engineering tactics to try to gain access or information.
            """,
            learning_objectives=[
                "Recognize common vishing attack patterns",
                "Identify psychological manipulation tactics in phone calls",
                "Apply proper verification procedures for phone communications",
                "Understand escalation procedures for suspicious calls"
            ],
            setup_instructions="""
            1. Train security team members on vishing simulation techniques
            2. Prepare caller scripts with appropriate social engineering elements
            3. Set up call logging and monitoring systems
            4. Ensure all participants have provided explicit consent
            5. Prepare debrief materials and follow-up procedures
            6. Coordinate with HR and legal teams for approval
            """,
            execution_script="""
            **Caller Script:**
            "Hi, this is Mike from IT support. We're seeing some unusual activity on your computer 
            and need to check it remotely. Can you help me with that?"
            
            **If participant asks for verification:**
            "Sure, you can call me back at [number] or check with your supervisor. But this is urgent 
            - we're seeing malware activity that could spread to other computers."
            
            **If participant agrees:**
            "Great, I'll send you a link to download our remote access tool. It's safe, 
            we use it all the time. Just click the link and enter your password when prompted."
            
            **Red flags in this call:**
            - Unsolicited call from "IT support"
            - Claims of urgent security issues
            - Requests for remote access
            - Pressure to act quickly
            - Requests for password over phone
            """,
            opt_out_language="""
            **SIMULATION NOTICE**
            This is a controlled security awareness simulation. You can opt out at any time by:
            - Saying "I opt out" during the call
            - Hanging up and contacting security@company.com
            - Speaking with your supervisor
            
            No negative consequences will result from opting out or falling for this simulation.
            """,
            success_criteria=[
                "Participant asks for verification of caller identity",
                "Participant does not provide password or remote access",
                "Participant reports the call to security team",
                "Participant demonstrates understanding of verification procedures"
            ],
            debrief_questions=[
                "What made you suspicious about this call?",
                "What verification steps did you take (or should have taken)?",
                "How did the urgent language make you feel?",
                "What would you do differently in a real situation?",
                "How confident do you feel about handling similar calls?"
            ],
            safety_considerations=[
                "Ensure caller is clearly identified as part of simulation",
                "Do not actually request or collect passwords",
                "Provide clear opt-out mechanism during call",
                "Follow up with all participants regardless of outcome",
                "Document lessons learned for future training"
            ],
            estimated_duration_minutes=20,
            required_consent=True,
            data_collection_scope="Call duration, verification attempts, reporting behavior"
        )
    
    @staticmethod
    def get_physical_tailgating_scenario(difficulty: DifficultyLevel = DifficultyLevel.LOW) -> SimulationScenario:
        """Create a physical security tailgating simulation scenario"""
        return SimulationScenario(
            id=str(uuid.uuid4()),
            name="Physical Security Tailgating Simulation",
            scenario_type=ScenarioType.PHYSICAL,
            difficulty_level=difficulty,
            description="""
            Participants will encounter someone attempting to tailgate (follow them through a secure door)
            into a restricted area. This tests their physical security awareness and challenge procedures.
            """,
            learning_objectives=[
                "Recognize physical security threats and social engineering attempts",
                "Apply proper challenge procedures for unknown individuals",
                "Understand the importance of physical security in overall security posture",
                "Practice reporting procedures for physical security incidents"
            ],
            setup_instructions="""
            1. Coordinate with facilities and security teams
            2. Identify appropriate areas for simulation (not high-security zones)
            3. Train actors on appropriate social engineering techniques
            4. Ensure all participants are aware this is a simulation
            5. Set up observation points for monitoring
            6. Prepare debrief materials and follow-up procedures
            """,
            execution_script="""
            **Actor Script:**
            "Oh, I forgot my badge! Can you let me in? I'm just going to grab something from my desk."
            
            **If participant challenges:**
            "I work in accounting, I'm just running late today. I promise I'm not going to cause any trouble."
            
            **If participant asks for ID:**
            "I don't have my wallet with me, but I can show you my employee directory listing when we get inside."
            
            **If participant offers to help:**
            "That's okay, I really just need to get in quickly. I'm already late for a meeting."
            
            **Red flags in this interaction:**
            - No visible security badge
            - Attempting to bypass security procedures
            - Pressure to act quickly
            - Vague explanations for presence
            - Attempting to avoid verification
            """,
            opt_out_language="""
            **SIMULATION NOTICE**
            This is a controlled security awareness simulation. You can opt out at any time by:
            - Saying "I opt out" to the actor
            - Contacting security@company.com
            - Speaking with your supervisor
            
            No negative consequences will result from opting out or falling for this simulation.
            """,
            success_criteria=[
                "Participant challenges the individual appropriately",
                "Participant does not allow unauthorized access",
                "Participant reports the incident to security",
                "Participant demonstrates understanding of challenge procedures"
            ],
            debrief_questions=[
                "What made you suspicious about this person?",
                "How did you challenge their request?",
                "What would you do differently in a real situation?",
                "How confident do you feel about handling similar situations?"
            ],
            safety_considerations=[
                "Ensure simulation is conducted in safe, controlled environment",
                "Provide clear identification that this is a simulation",
                "Do not create actual security vulnerabilities",
                "Follow up with all participants regardless of outcome",
                "Coordinate with physical security team"
            ],
            estimated_duration_minutes=15,
            required_consent=True,
            data_collection_scope="Challenge behavior, reporting actions, response time"
        )
    
    @staticmethod
    def get_pretexting_scenario(difficulty: DifficultyLevel = DifficultyLevel.HIGH) -> SimulationScenario:
        """Create a pretexting simulation scenario"""
        return SimulationScenario(
            id=str(uuid.uuid4()),
            name="Executive Pretexting Simulation",
            scenario_type=ScenarioType.PRETEXTING,
            difficulty_level=difficulty,
            description="""
            Participants will receive a communication from someone claiming to be a senior executive
            requesting urgent assistance with a sensitive matter. This tests their ability to verify
            authority and resist pressure from perceived authority figures.
            """,
            learning_objectives=[
                "Recognize pretexting and authority-based social engineering",
                "Apply verification procedures for high-authority requests",
                "Understand the importance of following established procedures",
                "Practice escalation procedures for unusual requests"
            ],
            setup_instructions="""
            1. Coordinate with executive team for approval
            2. Create realistic pretexting scenario using known executive information
            3. Train actors on appropriate authority-based social engineering
            4. Ensure all participants understand this is a simulation
            5. Set up monitoring and logging systems
            6. Prepare comprehensive debrief materials
            """,
            execution_script="""
            **Email/Message Content:**
            Subject: URGENT - Confidential Request - CEO
            
            Hi [Name],
            
            I'm in a board meeting and need your help with something confidential. 
            I can't discuss this over email, but I need you to purchase $500 in gift cards 
            for client appreciation. Can you handle this and send me the codes?
            
            I'll reimburse you immediately after the meeting. This is time-sensitive.
            
            Thanks,
            [CEO Name]
            
            **Red flags in this communication:**
            - Urgent request from high authority
            - Unusual request (gift cards)
            - Pressure to act quickly
            - Request to bypass normal procedures
            - Vague explanation of need
            """,
            opt_out_language="""
            **SIMULATION NOTICE**
            This is a controlled security awareness simulation. You can opt out at any time by:
            - Replying with "OPT OUT"
            - Contacting security@company.com
            - Speaking with your supervisor
            
            No negative consequences will result from opting out or falling for this simulation.
            """,
            success_criteria=[
                "Participant verifies the request through official channels",
                "Participant does not make unauthorized purchases",
                "Participant reports the suspicious communication",
                "Participant demonstrates understanding of authority verification"
            ],
            debrief_questions=[
                "What made you suspicious about this request?",
                "How would you verify a request from a senior executive?",
                "What procedures should you follow for unusual requests?",
                "How confident do you feel about handling similar situations?"
            ],
            safety_considerations=[
                "Ensure no actual financial transactions occur",
                "Provide clear identification that this is a simulation",
                "Coordinate with executive team for approval",
                "Follow up with all participants regardless of outcome",
                "Document lessons learned for policy updates"
            ],
            estimated_duration_minutes=45,
            required_consent=True,
            data_collection_scope="Verification attempts, reporting behavior, response time"
        )
    
    @staticmethod
    def get_baiting_scenario(difficulty: DifficultyLevel = DifficultyLevel.MEDIUM) -> SimulationScenario:
        """Create a baiting simulation scenario"""
        return SimulationScenario(
            id=str(uuid.uuid4()),
            name="USB Baiting Simulation",
            scenario_type=ScenarioType.BAITING,
            difficulty_level=difficulty,
            description="""
            Participants will encounter USB drives labeled with tempting names left in common areas.
            This tests their awareness of baiting attacks and their response to found devices.
            """,
            learning_objectives=[
                "Recognize baiting attacks and their potential dangers",
                "Understand proper procedures for handling found devices",
                "Apply security best practices for unknown devices",
                "Practice reporting procedures for security incidents"
            ],
            setup_instructions="""
            1. Create harmless USB drives with tempting labels
            2. Place drives in common areas (break room, parking lot, etc.)
            3. Set up monitoring to track device handling
            4. Ensure all participants are aware this is a simulation
            5. Coordinate with IT security team
            6. Prepare debrief materials and follow-up procedures
            """,
            execution_script="""
            **USB Drive Setup:**
            - Label: "Q4 Bonuses - Confidential"
            - Location: Break room table, near coffee machine
            - Contents: Harmless text file with simulation notice
            - Monitoring: Track who picks up and attempts to use device
            
            **Expected Participant Behavior:**
            - Should not pick up unknown USB drives
            - Should report found devices to security
            - Should not plug unknown devices into computers
            - Should follow established security procedures
            
            **Red flags in this scenario:**
            - Unknown USB drive in common area
            - Tempting label designed to create curiosity
            - No clear owner or purpose
            - Potential security risk if plugged into computer
            """,
            opt_out_language="""
            **SIMULATION NOTICE**
            This is a controlled security awareness simulation. You can opt out at any time by:
            - Contacting security@company.com
            - Speaking with your supervisor
            
            No negative consequences will result from opting out or falling for this simulation.
            """,
            success_criteria=[
                "Participant does not pick up the USB drive",
                "Participant reports the found device to security",
                "Participant does not plug unknown devices into computers",
                "Participant demonstrates understanding of baiting attacks"
            ],
            debrief_questions=[
                "What would you do if you found a USB drive labeled 'Q4 Bonuses'?",
                "Why might unknown USB drives be dangerous?",
                "What procedures should you follow for found devices?",
                "How confident do you feel about recognizing baiting attacks?"
            ],
            safety_considerations=[
                "Ensure USB drives are completely harmless",
                "Provide clear identification that this is a simulation",
                "Do not create actual security vulnerabilities",
                "Follow up with all participants regardless of outcome",
                "Coordinate with IT security team for approval"
            ],
            estimated_duration_minutes=20,
            required_consent=True,
            data_collection_scope="Device handling behavior, reporting actions, response time"
        )
    
    @classmethod
    def get_all_scenarios(cls) -> Dict[str, SimulationScenario]:
        """Get all available simulation scenarios"""
        return {
            "phishing_email": cls.get_phishing_email_scenario(),
            "vishing_call": cls.get_vishing_call_scenario(),
            "physical_tailgating": cls.get_physical_tailgating_scenario(),
            "pretexting": cls.get_pretexting_scenario(),
            "baiting": cls.get_baiting_scenario()
        }
    
    @classmethod
    def get_scenarios_by_difficulty(cls, difficulty: DifficultyLevel) -> List[SimulationScenario]:
        """Get scenarios appropriate for specific difficulty level"""
        all_scenarios = cls.get_all_scenarios()
        appropriate_scenarios = []
        
        for scenario in all_scenarios.values():
            if scenario.difficulty_level == difficulty:
                appropriate_scenarios.append(scenario)
        
        return appropriate_scenarios
    
    @classmethod
    def get_scenarios_by_type(cls, scenario_type: ScenarioType) -> List[SimulationScenario]:
        """Get scenarios of specific type"""
        all_scenarios = cls.get_all_scenarios()
        appropriate_scenarios = []
        
        for scenario in all_scenarios.values():
            if scenario.scenario_type == scenario_type:
                appropriate_scenarios.append(scenario)
        
        return appropriate_scenarios


def main():
    """Example usage of simulation scenario library"""
    library = SimulationScenarioLibrary()
    
    print("Available Simulation Scenarios:")
    print("=" * 50)
    
    all_scenarios = library.get_all_scenarios()
    for name, scenario in all_scenarios.items():
        print(f"\n{scenario.name}")
        print(f"Type: {scenario.scenario_type.value}")
        print(f"Difficulty: {scenario.difficulty_level.value}")
        print(f"Duration: {scenario.estimated_duration_minutes} minutes")
        print(f"Learning Objectives: {len(scenario.learning_objectives)} objectives")
        print(f"Safety Considerations: {len(scenario.safety_considerations)} items")
    
    print("\n" + "=" * 50)
    print("High Difficulty Scenarios:")
    high_difficulty = library.get_scenarios_by_difficulty(DifficultyLevel.HIGH)
    for scenario in high_difficulty:
        print(f"- {scenario.name}")


if __name__ == "__main__":
    main()
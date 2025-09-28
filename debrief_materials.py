#!/usr/bin/env python3
"""
Debrief Materials Generator for Social Engineering Awareness Campaigns

This module provides comprehensive debrief materials and guidance for post-simulation
discussions, ensuring effective learning and continuous improvement.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import datetime
import uuid
from collections import defaultdict


class DebriefType(Enum):
    INDIVIDUAL = "individual"
    GROUP = "group"
    TEAM = "team"
    DEPARTMENT = "department"
    ORGANIZATION = "organization"


class LearningLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


@dataclass
class DebriefSession:
    """Structure for a debrief session"""
    id: str
    session_type: DebriefType
    learning_level: LearningLevel
    participants: List[str]
    scenario_id: str
    session_date: datetime.datetime
    duration_minutes: int
    facilitator: str
    objectives: List[str]
    discussion_points: List[str]
    key_learnings: List[str]
    action_items: List[str]
    follow_up_required: bool
    notes: str = ""


@dataclass
class DebriefTemplate:
    """Template for debrief materials"""
    name: str
    description: str
    debrief_type: DebriefType
    learning_level: LearningLevel
    duration_minutes: int
    agenda: List[str]
    discussion_questions: List[str]
    learning_outcomes: List[str]
    action_items: List[str]
    materials_needed: List[str]
    facilitation_notes: str


class DebriefMaterialsGenerator:
    """
    Generator for comprehensive debrief materials and session planning.
    
    This class provides:
    - Pre-built debrief templates for different scenarios
    - Session planning and facilitation guidance
    - Learning outcome tracking and assessment
    - Follow-up action planning
    """
    
    def __init__(self):
        self.debrief_templates = self._initialize_debrief_templates()
        self.sessions = {}
    
    def _initialize_debrief_templates(self) -> Dict[str, DebriefTemplate]:
        """Initialize standard debrief templates"""
        return {
            "phishing_debrief": DebriefTemplate(
                name="Phishing Simulation Debrief",
                description="Debrief template for phishing email simulation scenarios",
                debrief_type=DebriefType.GROUP,
                learning_level=LearningLevel.BEGINNER,
                duration_minutes=30,
                agenda=[
                    "Welcome and session overview (5 minutes)",
                    "Scenario recap and participant experiences (10 minutes)",
                    "Key learning points discussion (10 minutes)",
                    "Action items and next steps (5 minutes)"
                ],
                discussion_questions=[
                    "What made you suspicious about the email?",
                    "What verification steps did you take (or should have taken)?",
                    "How did the urgent language make you feel?",
                    "What would you do differently in a real situation?",
                    "How confident do you feel about recognizing similar attacks?",
                    "What additional training would be helpful?"
                ],
                learning_outcomes=[
                    "Enhanced recognition of phishing email characteristics",
                    "Improved verification procedures for suspicious emails",
                    "Better understanding of social engineering tactics",
                    "Increased confidence in reporting suspicious activity"
                ],
                action_items=[
                    "Review company email security policies",
                    "Practice verification procedures with colleagues",
                    "Report any suspicious emails to security team",
                    "Share learnings with team members"
                ],
                materials_needed=[
                    "Projector or screen for displaying examples",
                    "Printed copies of the simulation email",
                    "Company security policies and procedures",
                    "Contact information for security team"
                ],
                facilitation_notes="""
                **Facilitation Guidelines:**
                - Create a safe, non-judgmental environment
                - Focus on learning, not performance evaluation
                - Encourage participation from all attendees
                - Use specific examples from the simulation
                - Address any concerns or questions openly
                - Ensure all participants understand next steps
                """
            ),
            
            "vishing_debrief": DebriefTemplate(
                name="Vishing Simulation Debrief",
                description="Debrief template for voice phishing simulation scenarios",
                debrief_type=DebriefType.GROUP,
                learning_level=LearningLevel.INTERMEDIATE,
                duration_minutes=35,
                agenda=[
                    "Welcome and session overview (5 minutes)",
                    "Call scenario recap and participant experiences (10 minutes)",
                    "Verification procedures discussion (10 minutes)",
                    "Psychological tactics analysis (5 minutes)",
                    "Action items and next steps (5 minutes)"
                ],
                discussion_questions=[
                    "What made you suspicious about the call?",
                    "What verification steps did you take (or should have taken)?",
                    "How did the caller's authority and urgency tactics affect you?",
                    "What would you do differently in a real situation?",
                    "How confident do you feel about handling similar calls?",
                    "What additional training would be helpful?"
                ],
                learning_outcomes=[
                    "Enhanced recognition of vishing attack patterns",
                    "Improved verification procedures for phone calls",
                    "Better understanding of psychological manipulation tactics",
                    "Increased confidence in challenging suspicious callers"
                ],
                action_items=[
                    "Review company phone verification procedures",
                    "Practice verification phrases with colleagues",
                    "Report any suspicious calls to security team",
                    "Share learnings with team members"
                ],
                materials_needed=[
                    "Audio recording of the simulation call (if available)",
                    "Company verification procedures document",
                    "Contact information for security team",
                    "Examples of legitimate vs. suspicious calls"
                ],
                facilitation_notes="""
                **Facilitation Guidelines:**
                - Play back key moments from the call if available
                - Discuss the psychological tactics used by the caller
                - Practice verification procedures with participants
                - Address any concerns about challenging authority figures
                - Ensure all participants understand escalation procedures
                """
            ),
            
            "physical_security_debrief": DebriefTemplate(
                name="Physical Security Debrief",
                description="Debrief template for physical security simulation scenarios",
                debrief_type=DebriefType.TEAM,
                learning_level=LearningLevel.BEGINNER,
                duration_minutes=25,
                agenda=[
                    "Welcome and session overview (5 minutes)",
                    "Scenario recap and participant experiences (10 minutes)",
                    "Challenge procedures discussion (5 minutes)",
                    "Action items and next steps (5 minutes)"
                ],
                discussion_questions=[
                    "What made you suspicious about the person?",
                    "How did you challenge their request?",
                    "What would you do differently in a real situation?",
                    "How confident do you feel about handling similar situations?",
                    "What additional training would be helpful?"
                ],
                learning_outcomes=[
                    "Enhanced recognition of physical security threats",
                    "Improved challenge procedures for unknown individuals",
                    "Better understanding of social engineering in physical spaces",
                    "Increased confidence in maintaining physical security"
                ],
                action_items=[
                    "Review company physical security policies",
                    "Practice challenge procedures with team members",
                    "Report any suspicious individuals to security",
                    "Share learnings with other teams"
                ],
                materials_needed=[
                    "Company physical security policies",
                    "Challenge procedure guidelines",
                    "Contact information for security team",
                    "Examples of legitimate vs. suspicious behavior"
                ],
                facilitation_notes="""
                **Facilitation Guidelines:**
                - Discuss the importance of physical security
                - Practice challenge procedures with participants
                - Address any concerns about confronting people
                - Ensure all participants understand reporting procedures
                - Emphasize the importance of following established protocols
                """
            ),
            
            "advanced_threat_debrief": DebriefTemplate(
                name="Advanced Threat Debrief",
                description="Debrief template for advanced social engineering scenarios",
                debrief_type=DebriefType.DEPARTMENT,
                learning_level=LearningLevel.ADVANCED,
                duration_minutes=45,
                agenda=[
                    "Welcome and session overview (5 minutes)",
                    "Scenario recap and participant experiences (15 minutes)",
                    "Advanced tactics analysis (10 minutes)",
                    "Defense strategies discussion (10 minutes)",
                    "Action items and next steps (5 minutes)"
                ],
                discussion_questions=[
                    "What made this attack particularly sophisticated?",
                    "What verification steps did you take (or should have taken)?",
                    "How did the attacker use information about you or the organization?",
                    "What additional verification methods could have been used?",
                    "How confident do you feel about handling similar attacks?",
                    "What additional training would be helpful?"
                ],
                learning_outcomes=[
                    "Enhanced recognition of advanced social engineering techniques",
                    "Improved verification procedures for high-value requests",
                    "Better understanding of OSINT and reconnaissance tactics",
                    "Increased confidence in defending against sophisticated attacks"
                ],
                action_items=[
                    "Review and update verification procedures",
                    "Implement additional security controls if needed",
                    "Share lessons learned with other departments",
                    "Update security policies based on findings"
                ],
                materials_needed=[
                    "Advanced threat intelligence reports",
                    "Updated security procedures document",
                    "Contact information for security team",
                    "Examples of sophisticated attack techniques"
                ],
                facilitation_notes="""
                **Facilitation Guidelines:**
                - Discuss the sophistication of the attack techniques
                - Analyze the information gathering methods used
                - Review advanced verification procedures
                - Address any concerns about defending against sophisticated attacks
                - Ensure all participants understand the importance of continuous learning
                """
            ),
            
            "refresher_debrief": DebriefTemplate(
                name="Security Awareness Refresher Debrief",
                description="Debrief template for refresher training sessions",
                debrief_type=DebriefType.GROUP,
                learning_level=LearningLevel.BEGINNER,
                duration_minutes=20,
                agenda=[
                    "Welcome and session overview (5 minutes)",
                    "Key concepts review (10 minutes)",
                    "Action items and next steps (5 minutes)"
                ],
                discussion_questions=[
                    "What are the most important security awareness concepts?",
                    "How confident do you feel about recognizing social engineering attacks?",
                    "What additional training would be helpful?",
                    "How can you help maintain a security-conscious culture?"
                ],
                learning_outcomes=[
                    "Reinforced understanding of security awareness concepts",
                    "Improved confidence in recognizing threats",
                    "Better understanding of personal security responsibilities",
                    "Increased commitment to security best practices"
                ],
                action_items=[
                    "Review company security policies",
                    "Practice security procedures regularly",
                    "Report any suspicious activity immediately",
                    "Help colleagues stay security-conscious"
                ],
                materials_needed=[
                    "Company security policies summary",
                    "Quick reference security guide",
                    "Contact information for security team",
                    "Security awareness resources"
                ],
                facilitation_notes="""
                **Facilitation Guidelines:**
                - Keep the session positive and encouraging
                - Focus on reinforcing key concepts
                - Address any questions or concerns
                - Ensure all participants understand their responsibilities
                - Encourage ongoing security awareness
                """
            )
        }
    
    def create_debrief_session(self, scenario_id: str, participants: List[str],
                             debrief_type: DebriefType, learning_level: LearningLevel,
                             facilitator: str, custom_objectives: Optional[List[str]] = None) -> DebriefSession:
        """Create a new debrief session"""
        
        # Select appropriate template
        template = self._select_template(debrief_type, learning_level)
        
        # Create session
        session = DebriefSession(
            id=str(uuid.uuid4()),
            session_type=debrief_type,
            learning_level=learning_level,
            participants=participants,
            scenario_id=scenario_id,
            session_date=datetime.datetime.now(),
            duration_minutes=template.duration_minutes,
            facilitator=facilitator,
            objectives=custom_objectives or template.learning_outcomes,
            discussion_points=template.discussion_questions,
            key_learnings=[],
            action_items=template.action_items,
            follow_up_required=True,
            notes=""
        )
        
        self.sessions[session.id] = session
        return session
    
    def _select_template(self, debrief_type: DebriefType, learning_level: LearningLevel) -> DebriefTemplate:
        """Select appropriate debrief template based on type and level"""
        
        # Simple template selection logic - can be enhanced
        if learning_level == LearningLevel.BEGINNER:
            if debrief_type == DebriefType.GROUP:
                return self.debrief_templates["phishing_debrief"]
            else:
                return self.debrief_templates["refresher_debrief"]
        elif learning_level == LearningLevel.INTERMEDIATE:
            return self.debrief_templates["vishing_debrief"]
        else:  # ADVANCED
            return self.debrief_templates["advanced_threat_debrief"]
    
    def generate_debrief_materials(self, session_id: str) -> Dict[str, Any]:
        """Generate comprehensive debrief materials for a session"""
        
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.sessions[session_id]
        template = self._select_template(session.session_type, session.learning_level)
        
        materials = {
            "session_info": {
                "id": session.id,
                "type": session.session_type.value,
                "learning_level": session.learning_level.value,
                "participants": session.participants,
                "facilitator": session.facilitator,
                "duration_minutes": session.duration_minutes,
                "date": session.session_date.isoformat()
            },
            "agenda": template.agenda,
            "discussion_questions": template.discussion_questions,
            "learning_outcomes": session.objectives,
            "action_items": session.action_items,
            "materials_needed": template.materials_needed,
            "facilitation_guidelines": template.facilitation_notes,
            "session_notes": session.notes
        }
        
        return materials
    
    def update_session_notes(self, session_id: str, notes: str) -> None:
        """Update session notes"""
        
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        self.sessions[session_id].notes = notes
    
    def add_key_learning(self, session_id: str, learning: str) -> None:
        """Add a key learning to a session"""
        
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        self.sessions[session_id].key_learnings.append(learning)
    
    def add_action_item(self, session_id: str, action_item: str) -> None:
        """Add an action item to a session"""
        
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        self.sessions[session_id].action_items.append(action_item)
    
    def complete_session(self, session_id: str, key_learnings: List[str],
                        action_items: List[str], notes: str = "") -> None:
        """Complete a debrief session with final notes"""
        
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.sessions[session_id]
        session.key_learnings.extend(key_learnings)
        session.action_items.extend(action_items)
        session.notes = notes
        session.follow_up_required = False
    
    def generate_follow_up_plan(self, session_id: str) -> Dict[str, Any]:
        """Generate a follow-up plan for a completed session"""
        
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.sessions[session_id]
        
        follow_up_plan = {
            "session_id": session_id,
            "follow_up_required": session.follow_up_required,
            "action_items": session.action_items,
            "key_learnings": session.key_learnings,
            "next_steps": self._generate_next_steps(session),
            "success_metrics": self._generate_success_metrics(session),
            "timeline": self._generate_timeline(session)
        }
        
        return follow_up_plan
    
    def _generate_next_steps(self, session: DebriefSession) -> List[str]:
        """Generate next steps based on session outcomes"""
        next_steps = []
        
        # Add action items as next steps
        next_steps.extend(session.action_items)
        
        # Add follow-up training if needed
        if session.learning_level == LearningLevel.BEGINNER:
            next_steps.append("Schedule follow-up training session in 3 months")
        
        # Add team sharing if group session
        if session.session_type in [DebriefType.GROUP, DebriefType.TEAM]:
            next_steps.append("Share key learnings with other team members")
        
        # Add policy review if advanced session
        if session.learning_level == LearningLevel.ADVANCED:
            next_steps.append("Review and update security policies based on findings")
        
        return next_steps
    
    def _generate_success_metrics(self, session: DebriefSession) -> List[str]:
        """Generate success metrics for the session"""
        metrics = []
        
        # Participation metrics
        metrics.append(f"Session participation: {len(session.participants)} participants")
        
        # Learning metrics
        metrics.append(f"Key learnings identified: {len(session.key_learnings)}")
        metrics.append(f"Action items created: {len(session.action_items)}")
        
        # Follow-up metrics
        if session.follow_up_required:
            metrics.append("Follow-up required: Yes")
        else:
            metrics.append("Follow-up required: No")
        
        return metrics
    
    def _generate_timeline(self, session: DebriefSession) -> Dict[str, str]:
        """Generate timeline for follow-up actions"""
        timeline = {}
        
        # Immediate actions (within 1 week)
        timeline["immediate"] = [
            "Complete action items from session",
            "Share key learnings with team",
            "Report any security concerns to security team"
        ]
        
        # Short-term actions (within 1 month)
        timeline["short_term"] = [
            "Implement improved security procedures",
            "Schedule additional training if needed",
            "Monitor for similar security threats"
        ]
        
        # Long-term actions (within 3 months)
        timeline["long_term"] = [
            "Conduct follow-up security awareness assessment",
            "Review and update security policies",
            "Plan next security awareness campaign"
        ]
        
        return timeline
    
    def get_session_summary(self, session_id: str) -> Dict[str, Any]:
        """Get a summary of a debrief session"""
        
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.sessions[session_id]
        
        return {
            "id": session.id,
            "type": session.session_type.value,
            "learning_level": session.learning_level.value,
            "participants_count": len(session.participants),
            "duration_minutes": session.duration_minutes,
            "facilitator": session.facilitator,
            "key_learnings_count": len(session.key_learnings),
            "action_items_count": len(session.action_items),
            "follow_up_required": session.follow_up_required,
            "date": session.session_date.isoformat()
        }
    
    def export_session_data(self, session_id: str) -> Dict[str, Any]:
        """Export complete session data"""
        
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} not found")
        
        session = self.sessions[session_id]
        
        return {
            "session_info": {
                "id": session.id,
                "type": session.session_type.value,
                "learning_level": session.learning_level.value,
                "participants": session.participants,
                "scenario_id": session.scenario_id,
                "date": session.session_date.isoformat(),
                "duration_minutes": session.duration_minutes,
                "facilitator": session.facilitator
            },
            "objectives": session.objectives,
            "discussion_points": session.discussion_points,
            "key_learnings": session.key_learnings,
            "action_items": session.action_items,
            "follow_up_required": session.follow_up_required,
            "notes": session.notes
        }


def main():
    """Example usage of the debrief materials generator"""
    
    # Initialize the generator
    generator = DebriefMaterialsGenerator()
    
    # Create a debrief session
    session = generator.create_debrief_session(
        scenario_id="phishing_sim_001",
        participants=["Alice", "Bob", "Charlie", "Diana"],
        debrief_type=DebriefType.GROUP,
        learning_level=LearningLevel.BEGINNER,
        facilitator="Security Team Lead"
    )
    
    # Generate debrief materials
    materials = generator.generate_debrief_materials(session.id)
    
    print("=== DEBRIEF MATERIALS GENERATOR ===")
    print(f"Session ID: {session.id}")
    print(f"Participants: {len(session.participants)}")
    print(f"Duration: {session.duration_minutes} minutes")
    print(f"Discussion Questions: {len(materials['discussion_questions'])}")
    print(f"Action Items: {len(materials['action_items'])}")
    
    # Complete the session
    generator.complete_session(
        session_id=session.id,
        key_learnings=[
            "Participants improved their ability to identify phishing emails",
            "Verification procedures were reinforced",
            "Confidence in reporting suspicious activity increased"
        ],
        action_items=[
            "Review company email security policies",
            "Practice verification procedures with colleagues",
            "Report any suspicious emails to security team"
        ],
        notes="Session went well, all participants engaged and learned key concepts"
    )
    
    # Generate follow-up plan
    follow_up = generator.generate_follow_up_plan(session.id)
    print(f"\nFollow-up Plan: {len(follow_up['action_items'])} action items")


if __name__ == "__main__":
    main()
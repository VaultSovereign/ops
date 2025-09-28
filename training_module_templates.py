#!/usr/bin/env python3
"""
Training Module Templates for Social Engineering Awareness

This module contains pre-built templates for different types of security awareness training modules.
Each template is designed to be audience-appropriate and includes proper opt-out mechanisms.
"""

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum


class ModuleType(Enum):
    INTERACTIVE = "interactive"
    PRESENTATION = "presentation"
    SIMULATION = "simulation"
    ASSESSMENT = "assessment"
    REFRESHER = "refresher"


@dataclass
class ModuleTemplate:
    """Template structure for training modules"""
    name: str
    module_type: ModuleType
    audience_levels: List[str]
    duration_minutes: int
    content_template: str
    learning_objectives: List[str]
    interactive_elements: List[str]
    assessment_questions: List[str]


class TrainingModuleTemplates:
    """Collection of training module templates for different scenarios"""
    
    @staticmethod
    def get_phishing_awareness_template() -> ModuleTemplate:
        """Template for phishing awareness training"""
        return ModuleTemplate(
            name="Phishing Awareness Fundamentals",
            module_type=ModuleType.INTERACTIVE,
            audience_levels=["beginner", "intermediate"],
            duration_minutes=25,
            content_template="""
            # Phishing Awareness Training
            
            ## Learning Objectives
            {learning_objectives}
            
            ## What is Phishing?
            Phishing is a cyber attack that uses disguised email as a weapon. The goal is to trick the email recipient into believing that the message is something they want or need — a request from their bank, for instance, or a note from someone in their company — and to click a link or download an attachment.
            
            ## Common Phishing Techniques
            1. **Urgent Requests**: "Your account will be closed if you don't act now"
            2. **Authority Impersonation**: Emails from "IT Support" or "HR Department"
            3. **Fake Links**: Hover over links to see the real destination
            4. **Suspicious Attachments**: Unexpected files, especially .exe or .zip files
            5. **Poor Grammar**: Many phishing emails contain spelling and grammar errors
            
            ## Red Flags to Watch For
            - Unexpected emails asking for personal information
            - Urgent requests to verify account information
            - Emails with suspicious sender addresses
            - Requests to click on links or download attachments
            - Poor spelling and grammar
            - Generic greetings like "Dear Customer"
            
            ## How to Protect Yourself
            1. **Verify the Sender**: Check the email address carefully
            2. **Don't Click Links**: Type URLs directly or use bookmarks
            3. **Verify Requests**: Contact the sender through official channels
            4. **Report Suspicious Emails**: Forward to security team
            5. **Keep Software Updated**: Ensure email clients and browsers are current
            
            ## Interactive Exercise
            {interactive_elements}
            
            ## Assessment
            {assessment_questions}
            
            ## Opt-Out Information
            {opt_out_instructions}
            """,
            learning_objectives=[
                "Identify common phishing email characteristics",
                "Recognize social engineering tactics in emails",
                "Apply verification procedures for suspicious emails",
                "Report phishing attempts through proper channels"
            ],
            interactive_elements=[
                "Email analysis exercise with real examples",
                "Hover-over link demonstration",
                "Sender verification practice",
                "Reporting procedure walkthrough"
            ],
            assessment_questions=[
                "What is the most reliable way to verify a suspicious email?",
                "True or False: Legitimate companies never ask for passwords via email",
                "What should you do if you receive a suspicious email?",
                "How can you tell if a link in an email is safe to click?"
            ]
        )
    
    @staticmethod
    def get_vishing_awareness_template() -> ModuleTemplate:
        """Template for voice phishing (vishing) awareness training"""
        return ModuleTemplate(
            name="Voice Phishing (Vishing) Defense",
            module_type=ModuleType.PRESENTATION,
            audience_levels=["beginner", "intermediate", "advanced"],
            duration_minutes=20,
            content_template="""
            # Voice Phishing (Vishing) Awareness
            
            ## Learning Objectives
            {learning_objectives}
            
            ## What is Vishing?
            Vishing (voice phishing) is a form of social engineering that uses voice communication to trick victims into revealing sensitive information. Attackers often use phone calls, voicemails, or even voice messages to manipulate targets.
            
            ## Common Vishing Scenarios
            1. **IT Support Impersonation**: "This is IT support, we need to fix your computer"
            2. **Bank Security Alerts**: "Your account has been compromised, please verify your identity"
            3. **Government Agency Calls**: "This is the IRS, you owe back taxes"
            4. **Tech Support Scams**: "We detected a virus on your computer"
            5. **Urgent Business Requests**: "I'm your boss, I need you to buy gift cards immediately"
            
            ## Psychological Tactics Used
            - **Authority**: Impersonating trusted figures (IT, management, government)
            - **Urgency**: Creating time pressure to bypass rational thinking
            - **Fear**: Using threats of account closure or legal action
            - **Helpfulness**: Offering to "help" with a technical problem
            - **Familiarity**: Using information gathered from social media or data breaches
            
            ## Red Flags in Phone Calls
            - Unexpected calls asking for sensitive information
            - Callers who won't provide callback numbers
            - Requests to download software or provide remote access
            - Pressure to act immediately without verification
            - Callers who become aggressive when questioned
            - Requests for payment via gift cards or wire transfers
            
            ## Defense Strategies
            1. **Verify Identity**: Ask for callback number and verify through official channels
            2. **Use Established Procedures**: Follow company verification protocols
            3. **Never Share Passwords**: Legitimate IT never asks for passwords
            4. **Hang Up and Call Back**: Use official numbers from company directory
            5. **Trust Your Instincts**: If something feels wrong, it probably is
            6. **Report Suspicious Calls**: Document and report to security team
            
            ## Interactive Exercise
            {interactive_elements}
            
            ## Assessment
            {assessment_questions}
            
            ## Opt-Out Information
            {opt_out_instructions}
            """,
            learning_objectives=[
                "Recognize common vishing attack patterns",
                "Identify psychological manipulation tactics",
                "Apply proper verification procedures for phone calls",
                "Report suspicious calls through appropriate channels"
            ],
            interactive_elements=[
                "Role-playing exercise with simulated vishing calls",
                "Verification procedure demonstration",
                "Caller ID spoofing explanation",
                "Reporting process walkthrough"
            ],
            assessment_questions=[
                "What should you do if someone claiming to be IT support calls asking for your password?",
                "True or False: Legitimate companies sometimes ask for passwords over the phone",
                "How can you verify the identity of someone calling from your bank?",
                "What information should you never share over the phone?"
            ]
        )
    
    @staticmethod
    def get_physical_security_template() -> ModuleTemplate:
        """Template for physical security awareness training"""
        return ModuleTemplate(
            name="Physical Security and Social Engineering",
            module_type=ModuleType.SIMULATION,
            audience_levels=["beginner", "intermediate"],
            duration_minutes=30,
            content_template="""
            # Physical Security Awareness
            
            ## Learning Objectives
            {learning_objectives}
            
            ## Physical Security Threats
            Physical security involves protecting people, property, and information from physical threats. Social engineers often exploit physical security weaknesses to gain unauthorized access.
            
            ## Common Physical Security Attacks
            1. **Tailgating**: Following someone through a secure door
            2. **Piggybacking**: Carrying items to appear legitimate
            3. **Dumpster Diving**: Searching trash for sensitive information
            4. **Shoulder Surfing**: Watching someone enter passwords or PINs
            5. **Impersonation**: Pretending to be an employee, contractor, or visitor
            6. **Social Engineering**: Manipulating people to bypass security measures
            
            ## Attack Scenarios
            - **Contractor Impersonation**: "I'm here to fix the printer, can you let me in?"
            - **Delivery Person**: "I have a package for John Smith, can you help me find him?"
            - **Lost Employee**: "I forgot my badge, can you let me in just this once?"
            - **Emergency Situation**: "There's a fire drill, everyone needs to evacuate now"
            - **Authority Figure**: "I'm from corporate, I need to inspect the server room"
            
            ## Physical Security Best Practices
            1. **Badge Awareness**: Always wear and display your security badge
            2. **Challenge Unknown People**: Ask for identification and purpose
            3. **Secure Workstations**: Lock screens when away from desk
            4. **Clean Desk Policy**: Secure sensitive documents and information
            5. **Visitor Management**: Escort visitors and verify their purpose
            6. **Report Suspicious Activity**: Immediately report unauthorized individuals
            
            ## Challenge Procedures
            - **Approach Politely**: "Excuse me, can I help you?"
            - **Ask for Identification**: "May I see your badge/ID?"
            - **Verify Purpose**: "What brings you to this area?"
            - **Escort if Necessary**: "Let me help you find who you're looking for"
            - **Report Concerns**: Contact security if something seems wrong
            
            ## Interactive Exercise
            {interactive_elements}
            
            ## Assessment
            {assessment_questions}
            
            ## Opt-Out Information
            {opt_out_instructions}
            """,
            learning_objectives=[
                "Recognize physical security threats and social engineering attempts",
                "Apply proper challenge procedures for unknown individuals",
                "Implement physical security best practices in daily work",
                "Report suspicious physical security incidents"
            ],
            interactive_elements=[
                "Simulated tailgating scenarios",
                "Challenge procedure role-playing",
                "Badge checking exercise",
                "Visitor management simulation"
            ],
            assessment_questions=[
                "What should you do if someone tries to follow you through a secure door?",
                "True or False: It's okay to let someone in if they look like they belong",
                "How should you handle a visitor who can't find their escort?",
                "What information should you never leave visible on your desk?"
            ]
        )
    
    @staticmethod
    def get_advanced_threat_template() -> ModuleTemplate:
        """Template for advanced threat awareness training"""
        return ModuleTemplate(
            name="Advanced Social Engineering Threats",
            module_type=ModuleType.INTERACTIVE,
            audience_levels=["intermediate", "advanced"],
            duration_minutes=45,
            content_template="""
            # Advanced Social Engineering Threats
            
            ## Learning Objectives
            {learning_objectives}
            
            ## Sophisticated Attack Vectors
            Modern social engineering attacks have become increasingly sophisticated, using advanced techniques and technology to bypass traditional security measures.
            
            ## Advanced Attack Techniques
            1. **OSINT (Open Source Intelligence)**: Gathering information from public sources
            2. **Deepfake Technology**: AI-generated voice and video impersonation
            3. **Supply Chain Attacks**: Compromising trusted third parties
            4. **Insider Threats**: Social engineering internal personnel
            5. **Multi-Vector Attacks**: Combining multiple attack methods
            6. **AI-Powered Phishing**: Machine learning to create convincing messages
            
            ## OSINT and Reconnaissance
            Attackers gather information from:
            - Social media profiles and posts
            - Company websites and press releases
            - Professional networking sites (LinkedIn)
            - Public databases and records
            - Employee directories and org charts
            - Public Wi-Fi networks and locations
            
            ## Deepfake and AI Threats
            - **Voice Cloning**: Replicating voices for phone calls
            - **Video Deepfakes**: Creating fake video calls
            - **AI-Generated Text**: Creating convincing phishing emails
            - **Synthetic Identities**: Creating fake online personas
            - **Behavioral Mimicking**: AI that learns communication patterns
            
            ## Supply Chain Vulnerabilities
            - **Vendor Compromise**: Attackers target trusted suppliers
            - **Software Supply Chain**: Malicious code in legitimate software
            - **Third-Party Access**: Compromised vendor accounts
            - **Shared Infrastructure**: Attacks through shared services
            - **Trust Exploitation**: Using established relationships
            
            ## Defense Strategies
            1. **Zero Trust Architecture**: Verify everything, trust nothing
            2. **Behavioral Analytics**: Monitor for unusual patterns
            3. **Multi-Factor Authentication**: Multiple verification methods
            4. **Incident Response**: Rapid detection and containment
            5. **Continuous Monitoring**: Ongoing threat assessment
            6. **Employee Training**: Regular awareness and testing
            
            ## Advanced Verification Methods
            - **Out-of-Band Communication**: Verify through different channels
            - **Code Words**: Pre-established verification phrases
            - **Visual Confirmation**: Video calls to verify identity
            - **Behavioral Analysis**: Recognizing unusual communication patterns
            - **Technical Verification**: Checking digital signatures and certificates
            
            ## Interactive Exercise
            {interactive_elements}
            
            ## Assessment
            {assessment_questions}
            
            ## Opt-Out Information
            {opt_out_instructions}
            """,
            learning_objectives=[
                "Understand advanced social engineering techniques and technologies",
                "Recognize OSINT gathering and reconnaissance activities",
                "Apply advanced verification methods for sensitive requests",
                "Implement defense strategies against sophisticated attacks"
            ],
            interactive_elements=[
                "OSINT investigation exercise",
                "Deepfake detection demonstration",
                "Advanced verification scenario practice",
                "Behavioral analysis training"
            ],
            assessment_questions=[
                "What is OSINT and how can attackers use it against your organization?",
                "How can you verify the authenticity of a video call from a colleague?",
                "What additional verification steps should you take for high-value requests?",
                "How can behavioral analytics help detect social engineering attempts?"
            ]
        )
    
    @staticmethod
    def get_refresher_template() -> ModuleTemplate:
        """Template for refresher training modules"""
        return ModuleTemplate(
            name="Security Awareness Refresher",
            module_type=ModuleType.ASSESSMENT,
            audience_levels=["beginner", "intermediate", "advanced"],
            duration_minutes=15,
            content_template="""
            # Security Awareness Refresher
            
            ## Learning Objectives
            {learning_objectives}
            
            ## Quick Review
            This refresher module covers the essential security awareness concepts you need to protect yourself and the organization from social engineering attacks.
            
            ## Key Concepts Recap
            1. **Social Engineering**: Manipulating people to give up confidential information
            2. **Common Tactics**: Phishing, vishing, pretexting, baiting, tailgating
            3. **Red Flags**: Urgent requests, authority pressure, unusual channels
            4. **Defense**: Verify, think, report, trust your instincts
            5. **Reporting**: Always report suspicious activity immediately
            
            ## Quick Assessment
            {assessment_questions}
            
            ## Best Practices Checklist
            - [ ] I verify all requests for sensitive information
            - [ ] I use official channels to confirm suspicious communications
            - [ ] I report suspicious activity to the security team
            - [ ] I keep my work area secure and clean
            - [ ] I challenge unknown individuals in secure areas
            - [ ] I keep my security awareness training current
            - [ ] I help colleagues stay security-conscious
            
            ## Resources
            - Security team contact: security@company.com
            - Incident reporting: incident@company.com
            - Security hotline: 1-800-SECURITY
            - Training portal: security.company.com/training
            
            ## Opt-Out Information
            {opt_out_instructions}
            """,
            learning_objectives=[
                "Review essential security awareness concepts",
                "Assess current knowledge and identify gaps",
                "Reinforce best practices for daily security",
                "Ensure readiness to respond to security threats"
            ],
            interactive_elements=[
                "Quick knowledge check quiz",
                "Best practices self-assessment",
                "Resource identification exercise",
                "Scenario-based quick decisions"
            ],
            assessment_questions=[
                "What is the first thing you should do when you receive a suspicious email?",
                "True or False: It's okay to share your password with IT support if they call",
                "How should you handle someone trying to follow you through a secure door?",
                "What information should you never share over the phone or email?"
            ]
        )
    
    @classmethod
    def get_all_templates(cls) -> Dict[str, ModuleTemplate]:
        """Get all available training module templates"""
        return {
            "phishing_awareness": cls.get_phishing_awareness_template(),
            "vishing_awareness": cls.get_vishing_awareness_template(),
            "physical_security": cls.get_physical_security_template(),
            "advanced_threats": cls.get_advanced_threat_template(),
            "refresher": cls.get_refresher_template()
        }
    
    @classmethod
    def get_template_by_audience(cls, audience_level: str) -> List[ModuleTemplate]:
        """Get templates appropriate for specific audience level"""
        all_templates = cls.get_all_templates()
        appropriate_templates = []
        
        for template in all_templates.values():
            if audience_level in template.audience_levels:
                appropriate_templates.append(template)
        
        return appropriate_templates


def main():
    """Example usage of training module templates"""
    templates = TrainingModuleTemplates()
    
    print("Available Training Module Templates:")
    print("=" * 50)
    
    all_templates = templates.get_all_templates()
    for name, template in all_templates.items():
        print(f"\n{template.name}")
        print(f"Type: {template.module_type.value}")
        print(f"Audience Levels: {', '.join(template.audience_levels)}")
        print(f"Duration: {template.duration_minutes} minutes")
        print(f"Learning Objectives: {len(template.learning_objectives)} objectives")
    
    print("\n" + "=" * 50)
    print("Templates for Beginner Audience:")
    beginner_templates = templates.get_template_by_audience("beginner")
    for template in beginner_templates:
        print(f"- {template.name}")


if __name__ == "__main__":
    main()
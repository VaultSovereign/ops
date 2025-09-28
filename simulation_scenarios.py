#!/usr/bin/env python3
"""
Simulation Scenario Templates for Social Engineering Testing
Provides ready-to-use scenarios with clear consent and safety mechanisms
"""

import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum


class ScenarioComplexity(Enum):
    """Complexity levels for scenarios"""
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class TargetGroup(Enum):
    """Target groups for scenarios"""
    GENERAL_STAFF = "general_staff"
    FINANCE = "finance"
    HR = "hr"
    IT = "it"
    EXECUTIVES = "executives"
    CUSTOMER_SERVICE = "customer_service"
    SALES = "sales"


@dataclass
class ConsentMechanism:
    """Consent and safety mechanisms for scenarios"""
    pre_campaign_notification: bool = True
    opt_in_required: bool = False
    opt_out_available: bool = True
    opt_out_methods: List[str] = field(default_factory=lambda: [
        "Email reply with OPT-OUT",
        "Click opt-out link",
        "Call security team",
        "Use safe word"
    ])
    safe_word: str = ""
    notification_text: str = ""
    consent_form_template: str = ""
    excluded_individuals: List[str] = field(default_factory=list)
    excluded_departments: List[str] = field(default_factory=list)
    time_restrictions: Dict[str, str] = field(default_factory=dict)
    
    def __post_init__(self):
        if not self.safe_word:
            self.safe_word = self._generate_safe_word()
        if not self.notification_text:
            self.notification_text = self._generate_notification()
        if not self.consent_form_template:
            self.consent_form_template = self._generate_consent_form()
    
    def _generate_safe_word(self) -> str:
        """Generate a safe word for immediate termination"""
        import random
        import string
        words = ["STOP", "PAUSE", "END", "HALT"]
        code = ''.join(random.choices(string.digits, k=4))
        return f"{random.choice(words)}-{code}"
    
    def _generate_notification(self) -> str:
        """Generate pre-campaign notification text"""
        return """
Dear Team,

As part of our ongoing security awareness program, we will be conducting 
security simulations over the next 30 days. These simulations are designed 
to help us identify areas for improvement and provide targeted training.

Important Information:
- This is a learning exercise, not a test
- No disciplinary action will result from participation
- You may opt out at any time
- Results will be anonymized

If you wish to opt out or have concerns, please contact the security team.

Thank you for your participation in keeping our organization secure.

Security Team
"""
    
    def _generate_consent_form(self) -> str:
        """Generate consent form template"""
        return """
SECURITY AWARENESS SIMULATION CONSENT FORM

I understand that:
1. Security simulations will be conducted for training purposes
2. These may include simulated phishing emails, phone calls, or physical tests
3. My responses will be used to improve security training
4. I can opt out at any time without consequence
5. Data will be handled confidentially

[ ] I consent to participate in security awareness simulations
[ ] I wish to opt out of all simulations
[ ] I wish to opt out of specific types: ________________

Signature: _________________
Date: _________________
"""


@dataclass
class ScenarioTemplate:
    """Template for a simulation scenario"""
    template_id: str
    name: str
    description: str
    complexity: ScenarioComplexity
    target_groups: List[TargetGroup]
    attack_vector: str
    scenario_data: Dict[str, Any]
    indicators: List[str]
    learning_points: List[str]
    success_criteria: Dict[str, Any]
    consent: ConsentMechanism
    debrief_content: str = ""
    
    def __post_init__(self):
        if not self.debrief_content:
            self.debrief_content = self._generate_debrief()
    
    def _generate_debrief(self) -> str:
        """Generate debrief content for the scenario"""
        return f"""
Scenario Debrief: {self.name}

What Happened:
{self.description}

Red Flags to Notice:
{chr(10).join(f'• {indicator}' for indicator in self.indicators)}

Key Learning Points:
{chr(10).join(f'• {point}' for point in self.learning_points)}

What to Do Next Time:
• Verify the sender/caller through official channels
• Report suspicious activity to security
• When in doubt, don't click/share/provide information
• Use the security team as a resource

Remember: It's better to be cautious and verify than to fall victim to an attack.
"""


class SimulationScenarioLibrary:
    """Library of simulation scenario templates"""
    
    def __init__(self):
        self.scenarios: Dict[str, ScenarioTemplate] = {}
        self._initialize_scenarios()
    
    def _initialize_scenarios(self):
        """Initialize all scenario templates"""
        self._add_phishing_scenarios()
        self._add_vishing_scenarios()
        self._add_smishing_scenarios()
        self._add_physical_scenarios()
        self._add_pretexting_scenarios()
        self._add_baiting_scenarios()
        self._add_business_email_compromise()
    
    def _add_phishing_scenarios(self):
        """Add phishing email scenarios"""
        
        # Basic password reset phishing
        self.scenarios["phish_password_basic"] = ScenarioTemplate(
            template_id="phish_password_basic",
            name="Basic Password Reset Phishing",
            description="Simple password reset scam with obvious indicators",
            complexity=ScenarioComplexity.BASIC,
            target_groups=[TargetGroup.GENERAL_STAFF],
            attack_vector="email",
            scenario_data={
                "sender": {
                    "display_name": "IT Support",
                    "email": "support@companny-help.com",  # Typo intentional
                    "reply_to": "noreply@suspicious-domain.com"
                },
                "subject_lines": [
                    "Urgent: Password Expires Today",
                    "Action Required: Update Your Password Now",
                    "Security Alert: Reset Password Immediately"
                ],
                "body": """
Dear User,

Your password will expire in 2 hours! Click below to reset:

[RESET PASSWORD NOW]
http://company-support.fake/reset?user={email}

If you don't reset immediately, you will lose access to all systems.

IT Support Team
This email is confidential and urgent
                """,
                "attachments": [],
                "links": ["http://company-support.fake/reset"],
                "urgency_level": "high",
                "personalization": "none"
            },
            indicators=[
                "Sender domain has typo (companny vs company)",
                "Generic greeting (Dear User)",
                "Extreme urgency (2 hours)",
                "External link domain",
                "Grammar issues",
                "Threatening language"
            ],
            learning_points=[
                "IT never sends password reset links via email",
                "Check sender domain carefully",
                "Be suspicious of urgent threats",
                "Verify through official channels"
            ],
            success_criteria={
                "report_without_clicking": "excellent",
                "report_after_clicking": "good",
                "no_action": "needs_improvement",
                "provided_credentials": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True
            )
        )
        
        # Advanced spear phishing
        self.scenarios["phish_spear_advanced"] = ScenarioTemplate(
            template_id="phish_spear_advanced",
            name="Advanced Spear Phishing Attack",
            description="Sophisticated targeted attack using public information",
            complexity=ScenarioComplexity.ADVANCED,
            target_groups=[TargetGroup.EXECUTIVES, TargetGroup.FINANCE],
            attack_vector="email",
            scenario_data={
                "sender": {
                    "display_name": "{target_manager_name}",
                    "email": "{manager_firstname}.{manager_lastname}@gmaiI.com",  # Capital I
                    "spoofed": True
                },
                "subject_lines": [
                    "Re: {recent_project} - Quick question",
                    "Following up on our {recent_meeting} discussion",
                    "{target_firstname}, need your input on {current_initiative}"
                ],
                "body": """
Hi {target_firstname},

Hope you're having a good {day_of_week}. Following up on our discussion 
about {recent_project}, I need you to review the updated proposal.

I've shared it via SecureShare since it contains sensitive pricing:
{malicious_link}

Can you review and approve by EOD? The board meeting is tomorrow and 
I want to make sure we're aligned.

Also, I'll be in {mentioned_location} next week for the conference. 
Let me know if you want to grab coffee.

Thanks,
{manager_firstname}

Sent from my iPhone
                """,
                "personalization_data": {
                    "uses_linkedin": True,
                    "uses_company_intel": True,
                    "references_real_events": True,
                    "mimics_writing_style": True
                },
                "attachments": [],
                "links": ["https://secure-share.net/{random}"],
                "sophistication": {
                    "domain_lookalike": True,
                    "ssl_certificate": True,
                    "branded_landing_page": True,
                    "credential_harvester": True
                }
            },
            indicators=[
                "Email domain is lookalike (gmaiI with capital I)",
                "Unusual file sharing service",
                "Pressure for quick action",
                "Personal email for business matter",
                "Link doesn't match company systems",
                "Sent from iPhone (unusual for formal request)"
            ],
            learning_points=[
                "Attackers research targets on social media",
                "Verify sender through known contact methods",
                "Question unusual communication channels",
                "Be extra cautious with sensitive requests",
                "Check email headers for spoofing"
            ],
            success_criteria={
                "detected_spoofing": "excellent",
                "verified_sender": "excellent",
                "reported": "good",
                "clicked_but_stopped": "fair",
                "entered_credentials": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True,
                notification_text="Advanced simulation using public information only"
            )
        )
        
        # CEO fraud / BEC
        self.scenarios["phish_ceo_fraud"] = ScenarioTemplate(
            template_id="phish_ceo_fraud",
            name="CEO Fraud / Business Email Compromise",
            description="Impersonation of executive requesting urgent wire transfer",
            complexity=ScenarioComplexity.INTERMEDIATE,
            target_groups=[TargetGroup.FINANCE, TargetGroup.HR],
            attack_vector="email",
            scenario_data={
                "sender": {
                    "display_name": "{ceo_name}",
                    "email": "{ceo_name_variation}@protonmail.com",
                    "urgency": "extreme"
                },
                "subject_lines": [
                    "Urgent - Confidential Request",
                    "Need your help - Private",
                    "Quick favor - Don't discuss"
                ],
                "body": """
{target_name},

I need you to handle something urgently and confidentially.

I'm in a meeting with the board about an acquisition and can't talk. 
We need to wire $50,000 to secure the deal before close of business.

Please initiate a wire transfer to:
Bank: First National Bank
Account: 1234567890
Routing: 987654321
Reference: Project Phoenix

Do not discuss this with anyone else as it's highly sensitive. 
The announcement will be made Monday.

Reply to confirm once complete.

{ceo_name}
Sent from mobile
                """,
                "red_flags": {
                    "unusual_request": True,
                    "bypasses_process": True,
                    "secrecy_demanded": True,
                    "external_email": True,
                    "pressure_tactics": True
                }
            },
            indicators=[
                "Personal email address (not corporate)",
                "Unusual payment request",
                "Demands secrecy",
                "Bypasses normal approval process",
                "Can't be reached by phone",
                "Grammar slightly off",
                "Urgent timeline"
            ],
            learning_points=[
                "Always verify wire transfer requests",
                "Follow established approval processes",
                "Be suspicious of secrecy demands",
                "Call to verify using known number",
                "CEO fraud costs millions annually"
            ],
            success_criteria={
                "immediately_reported": "excellent",
                "attempted_verification": "good",
                "questioned_request": "fair",
                "initiated_transfer": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True,
                excluded_departments=["Treasury"]  # May be too sensitive
            )
        )
    
    def _add_vishing_scenarios(self):
        """Add voice phishing scenarios"""
        
        self.scenarios["vish_it_support"] = ScenarioTemplate(
            template_id="vish_it_support",
            name="IT Support Vishing Attack",
            description="Fake IT support call requesting credentials",
            complexity=ScenarioComplexity.INTERMEDIATE,
            target_groups=[TargetGroup.GENERAL_STAFF],
            attack_vector="phone",
            scenario_data={
                "caller_id": "IT Help Desk",
                "script": {
                    "opening": """
Hello, this is {fake_name} from IT Support. I'm calling about the 
security update we're rolling out today. Have you received our email 
about it?
                    """,
                    "build_rapport": """
I know these updates are annoying, but with all the ransomware attacks 
lately, we need to make sure everyone's protected. This will just take 
a minute.
                    """,
                    "the_ask": """
I need to verify your account before pushing the update. Can you confirm 
your username? Great, and I'll need your password to complete the 
verification. I know we usually don't ask for this, but it's required 
for this critical update.
                    """,
                    "pressure": """
If we don't complete this now, your account will be locked for security 
reasons and you won't be able to work. Your manager will be notified 
of the delay.
                    """,
                    "if_questioned": """
I understand your concern. You can call the help desk back at 
555-0100 (fake number) to verify. But we need to do this in the next 
10 minutes or the update window closes.
                    """
                },
                "techniques": [
                    "Name dropping (mentions real employees)",
                    "Technical jargon to confuse",
                    "False urgency",
                    "Threat of consequences",
                    "Provides callback number (fake)"
                ],
                "requested_info": [
                    "Username",
                    "Password",
                    "MFA code",
                    "Security questions"
                ]
            },
            indicators=[
                "Unsolicited call about security",
                "Requests password over phone",
                "Creates urgency and fear",
                "Won't provide ticket number",
                "Callback number not recognized",
                "Pressure when questioned"
            ],
            learning_points=[
                "IT never asks for passwords",
                "Verify callers independently",
                "Don't trust caller ID",
                "Use official contact methods",
                "Report suspicious calls"
            ],
            success_criteria={
                "refused_and_reported": "excellent",
                "refused_info": "good",
                "asked_to_verify": "good",
                "provided_username_only": "fair",
                "provided_password": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True,
                safe_word="SECURITY-STOP"
            )
        )
        
        self.scenarios["vish_vendor_update"] = ScenarioTemplate(
            template_id="vish_vendor_update",
            name="Vendor Payment Update Vishing",
            description="Fake vendor calling to update payment information",
            complexity=ScenarioComplexity.ADVANCED,
            target_groups=[TargetGroup.FINANCE],
            attack_vector="phone",
            scenario_data={
                "caller_id": "Blocked",
                "script": {
                    "opening": """
Hi, this is {name} from {real_vendor} accounts receivable. I'm calling 
about an urgent issue with your account that's affecting your service.
                    """,
                    "problem": """
We've had a banking change due to a merger, and our old account is being 
closed Friday. We need to update our payment information in your system 
or your service will be interrupted Monday.
                    """,
                    "legitimacy": """
I have your account number here: {partial_real_account}... is that correct? 
Good. Your last payment was {approximate_amount} last month. We really 
appreciate your business and want to avoid any disruption.
                    """,
                    "the_ask": """
Can you update our banking information? The new routing number is 
123456789 and account is 987654321. Also, we have an outstanding 
invoice for {amount} that needs to be paid to the new account.
                    """
                },
                "social_engineering": {
                    "uses_real_vendor": True,
                    "has_partial_info": True,
                    "name_drops": True,
                    "creates_urgency": True,
                    "fear_of_disruption": True
                }
            },
            indicators=[
                "Unsolicited payment change request",
                "Urgency around banking change",
                "Blocked caller ID",
                "Can't provide written documentation",
                "Different contact than usual",
                "Pressure to act quickly"
            ],
            learning_points=[
                "Always verify payment changes in writing",
                "Use established vendor contacts",
                "Follow payment change procedures",
                "Document all change requests",
                "Verify through multiple channels"
            ],
            success_criteria={
                "followed_procedure": "excellent",
                "requested_verification": "good",
                "suspicious_but_no_action": "fair",
                "updated_payment_info": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True,
                excluded_departments=["Accounts Payable"]  # If too sensitive
            )
        )
    
    def _add_smishing_scenarios(self):
        """Add SMS phishing scenarios"""
        
        self.scenarios["smish_package"] = ScenarioTemplate(
            template_id="smish_package",
            name="Package Delivery Smishing",
            description="Fake delivery notification with malicious link",
            complexity=ScenarioComplexity.BASIC,
            target_groups=[TargetGroup.GENERAL_STAFF],
            attack_vector="sms",
            scenario_data={
                "sender": "USPS-DELIVERY",
                "messages": [
                    """
USPS: Your package is held at our facility. Delivery fee of $2.99 
required. Pay now: http://usps-delivery.tk/pay?id=8374
                    """,
                    """
FedEx: We attempted delivery but you weren't home. Reschedule: 
https://fedex-redelivery.link/track?pkg=2947
                    """,
                    """
Your Amazon package couldn't be delivered. Update address: 
http://amz.delivery-update.com/fix
                    """
                ],
                "techniques": [
                    "Spoofed sender name",
                    "URL shortener or lookalike",
                    "Small fee to seem legitimate",
                    "Creates urgency"
                ]
            },
            indicators=[
                "Unexpected delivery notification",
                "Suspicious URL",
                "Request for payment via text",
                "Generic message",
                "Grammar/spelling errors",
                "Unusual domain"
            ],
            learning_points=[
                "Delivery companies don't request payment via SMS",
                "Don't click links in unexpected texts",
                "Verify through official apps/websites",
                "Check tracking numbers independently"
            ],
            success_criteria={
                "deleted_and_reported": "excellent",
                "ignored": "good",
                "clicked_but_stopped": "fair",
                "provided_payment": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True,
                opt_out_methods=["Reply STOP", "Contact security"]
            )
        )
        
        self.scenarios["smish_2fa"] = ScenarioTemplate(
            template_id="smish_2fa",
            name="Two-Factor Authentication Bypass",
            description="Attempt to steal 2FA codes via SMS",
            complexity=ScenarioComplexity.ADVANCED,
            target_groups=[TargetGroup.GENERAL_STAFF],
            attack_vector="sms",
            scenario_data={
                "sender": "SHORT-CODE",
                "message": """
Security Alert: Someone tried to access your account from Russia. 
If this wasn't you, reply with the 6-digit code we just sent you 
to secure your account.
                """,
                "timing": "Triggered after legitimate 2FA request",
                "techniques": [
                    "Fear-based messaging",
                    "Geographic threat",
                    "Requests legitimate code",
                    "Times with real login attempt"
                ]
            },
            indicators=[
                "Asks you to share 2FA code",
                "Creates panic/fear",
                "Requests reply via SMS",
                "Not from official number",
                "Different format than usual"
            ],
            learning_points=[
                "Never share 2FA codes with anyone",
                "2FA codes are only entered on websites",
                "Companies never ask for codes via SMS",
                "Verify through official channels"
            ],
            success_criteria={
                "recognized_attack": "excellent",
                "didn't_share_code": "good",
                "reported": "good",
                "shared_code": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True,
                time_restrictions={"business_hours": "9am-5pm"}
            )
        )
    
    def _add_physical_scenarios(self):
        """Add physical security test scenarios"""
        
        self.scenarios["physical_tailgating"] = ScenarioTemplate(
            template_id="physical_tailgating",
            name="Tailgating Assessment",
            description="Test employee response to tailgating attempts",
            complexity=ScenarioComplexity.BASIC,
            target_groups=[TargetGroup.GENERAL_STAFF],
            attack_vector="physical",
            scenario_data={
                "locations": [
                    "Main entrance",
                    "Side doors",
                    "Parking garage entrance",
                    "Secure floors"
                ],
                "techniques": [
                    {
                        "name": "Hands Full",
                        "description": "Carry boxes/coffee, struggle with badge",
                        "props": ["Boxes", "Coffee tray"]
                    },
                    {
                        "name": "Phone Distraction",
                        "description": "On important call, gesture to be let in",
                        "props": ["Phone", "Briefcase"]
                    },
                    {
                        "name": "Familiar Face",
                        "description": "Act like regular employee, chat casually",
                        "props": ["Company swag", "Coffee mug"]
                    }
                ],
                "tester_appearance": {
                    "professional_dress": True,
                    "company_branded_items": False,
                    "visible_badge": False,
                    "confidence_level": "high"
                },
                "escalation_protocol": {
                    "if_confronted": "Thank them and leave",
                    "if_questioned": "Admit to security test",
                    "emergency_contact": "Security team on standby"
                }
            },
            indicators=[
                "No visible badge",
                "Avoids badge reader",
                "Follows closely behind",
                "Unfamiliar face",
                "Asks to be let in",
                "Creates distraction"
            ],
            learning_points=[
                "Everyone needs to badge in",
                "Politely ask people to use their badge",
                "Don't hold doors for strangers",
                "Report suspicious behavior",
                "Security is everyone's responsibility"
            ],
            success_criteria={
                "denied_access": "excellent",
                "questioned_and_reported": "excellent",
                "questioned_only": "good",
                "allowed_entry": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=False,  # Building-wide test
                notification_text="Physical security assessments this month",
                excluded_individuals=["Visitors", "Contractors without badges"]
            )
        )
        
        self.scenarios["physical_sensitive_info"] = ScenarioTemplate(
            template_id="physical_sensitive_info",
            name="Clean Desk and Information Protection Test",
            description="Assessment of sensitive information protection",
            complexity=ScenarioComplexity.INTERMEDIATE,
            target_groups=[TargetGroup.GENERAL_STAFF],
            attack_vector="physical",
            scenario_data={
                "test_methods": [
                    {
                        "name": "After Hours Walk-Through",
                        "description": "Check for exposed sensitive information",
                        "items_checked": [
                            "Passwords on sticky notes",
                            "Unlocked computers",
                            "Sensitive documents on desks",
                            "Whiteboards with confidential info",
                            "Unlocked drawers/cabinets"
                        ]
                    },
                    {
                        "name": "Visitor Test",
                        "description": "Authorized visitor notes visible information",
                        "scope": "Public areas and conference rooms only"
                    }
                ],
                "documentation": {
                    "photos": False,  # Privacy concern
                    "checklist": True,
                    "anonymized": True
                },
                "positive_reinforcement": {
                    "recognize_good": True,
                    "rewards": ["Security champion badge", "Team recognition"]
                }
            },
            indicators=[
                "Passwords visible",
                "Screens unlocked",
                "Documents exposed",
                "Cabinets unlocked",
                "Sensitive info on whiteboards"
            ],
            learning_points=[
                "Lock screens when away (Win+L)",
                "Store documents securely",
                "Clear whiteboards after meetings",
                "Don't write passwords down",
                "Follow clean desk policy"
            ],
            success_criteria={
                "fully_secured": "excellent",
                "mostly_secured": "good",
                "some_issues": "needs_improvement",
                "major_exposure": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True,
                time_restrictions={"after_hours": "After 6pm only"}
            )
        )
    
    def _add_pretexting_scenarios(self):
        """Add pretexting scenarios"""
        
        self.scenarios["pretext_new_employee"] = ScenarioTemplate(
            template_id="pretext_new_employee",
            name="New Employee Information Gathering",
            description="Pretexting as new employee to gather information",
            complexity=ScenarioComplexity.INTERMEDIATE,
            target_groups=[TargetGroup.HR, TargetGroup.IT],
            attack_vector="multi-channel",
            scenario_data={
                "persona": {
                    "name": "Alex Johnson",
                    "story": "Starting next Monday in Marketing",
                    "manager": "Someone on vacation",
                    "background": "Just relocated from another office"
                },
                "channels": [
                    {
                        "channel": "phone",
                        "script": "Hi, I'm starting Monday and trying to get prepared..."
                    },
                    {
                        "channel": "email",
                        "message": "HR gave me your contact for IT setup..."
                    },
                    {
                        "channel": "in-person",
                        "approach": "Show up for 'orientation' early"
                    }
                ],
                "information_sought": [
                    "System access procedures",
                    "Network credentials",
                    "Employee directory",
                    "Org chart",
                    "Physical access codes"
                ],
                "red_flags": [
                    "No official paperwork",
                    "Manager unreachable",
                    "Not in HR system",
                    "Unusual requests",
                    "Pressing for immediate access"
                ]
            },
            indicators=[
                "Can't verify employment",
                "Manager unavailable",
                "No official onboarding",
                "Requests unusual access",
                "Lacks basic company knowledge"
            ],
            learning_points=[
                "Always verify new employees with HR",
                "Follow official onboarding process",
                "Don't grant access without authorization",
                "Verify manager approval",
                "Report suspicious requests"
            ],
            success_criteria={
                "verified_and_denied": "excellent",
                "requested_verification": "good",
                "suspicious_but_no_action": "fair",
                "provided_information": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True
            )
        )
    
    def _add_baiting_scenarios(self):
        """Add baiting scenarios"""
        
        self.scenarios["bait_usb_drop"] = ScenarioTemplate(
            template_id="bait_usb_drop",
            name="USB Baiting Campaign",
            description="Test response to found USB devices",
            complexity=ScenarioComplexity.BASIC,
            target_groups=[TargetGroup.GENERAL_STAFF],
            attack_vector="physical",
            scenario_data={
                "device_types": [
                    {
                        "type": "USB drive",
                        "label": "Salary Review 2024",
                        "appearance": "Professional"
                    },
                    {
                        "type": "USB drive",
                        "label": "Confidential - Board Meeting",
                        "appearance": "Executive style"
                    }
                ],
                "drop_locations": [
                    "Parking lot",
                    "Lobby",
                    "Cafeteria",
                    "Conference rooms",
                    "Restrooms"
                ],
                "device_behavior": {
                    "actual_function": "Phones home when inserted",
                    "no_malware": True,
                    "tracks": ["Device ID", "Time inserted", "Computer name"],
                    "safe_mode": True
                },
                "safety_measures": {
                    "clearly_marked": "Property of [Company] Security Team",
                    "contact_info": "If found: security@company.com",
                    "harmless": True
                }
            },
            indicators=[
                "Unknown USB device",
                "Found in unusual location",
                "Suspicious label",
                "Too good to be true",
                "No clear owner"
            ],
            learning_points=[
                "Never insert unknown USB devices",
                "Turn in found devices to security",
                "USB devices can contain malware",
                "Curiosity can be dangerous",
                "Report to security team"
            ],
            success_criteria={
                "turned_in_to_security": "excellent",
                "reported_without_inserting": "excellent",
                "left_alone": "good",
                "inserted_device": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=False,  # Passive test
                notification_text="Security will be conducting USB awareness tests"
            )
        )
    
    def _add_business_email_compromise(self):
        """Add business email compromise scenarios"""
        
        self.scenarios["bec_invoice_fraud"] = ScenarioTemplate(
            template_id="bec_invoice_fraud",
            name="Invoice Fraud Simulation",
            description="Fake invoice with payment redirection",
            complexity=ScenarioComplexity.ADVANCED,
            target_groups=[TargetGroup.FINANCE],
            attack_vector="email",
            scenario_data={
                "attack_chain": [
                    {
                        "step": 1,
                        "action": "Compromise or spoof vendor email",
                        "detail": "research@real-vendor.com → research@rea1-vendor.com"
                    },
                    {
                        "step": 2,
                        "action": "Monitor communications",
                        "detail": "Learn about pending invoices"
                    },
                    {
                        "step": 3,
                        "action": "Send fake invoice",
                        "detail": "Match format but change payment details"
                    }
                ],
                "email_details": {
                    "sender": "accounts@{vendor-lookalike}.com",
                    "subject": "Invoice #{real_invoice_number} - Payment Reminder",
                    "attachment": "Invoice_{number}_FINAL.pdf",
                    "body": """
Dear Valued Customer,

Please find attached invoice #{invoice_number} for {amount}.

IMPORTANT: We've recently updated our banking information due to a 
change in our payment processor. Please update your records and 
remit payment to:

Bank: International Business Bank
Account: 9876543210
Routing: 123456789
SWIFT: IBBKUS33

The previous account is no longer active. We apologize for any 
inconvenience.

Payment is due within 30 days. Thank you for your business.

Best regards,
Accounts Receivable
{vendor_name}
                    """
                },
                "invoice_modifications": {
                    "matches_real_format": True,
                    "correct_items": True,
                    "only_change": "Payment details",
                    "professional_appearance": True
                }
            },
            indicators=[
                "Payment details changed",
                "Different email domain",
                "No prior notification of change",
                "Unusual bank/location",
                "Pressure to update records",
                "Slight differences in format"
            ],
            learning_points=[
                "Verify all payment changes directly",
                "Use established vendor contacts",
                "Follow payment change procedures",
                "Compare with previous invoices",
                "Question any banking changes"
            ],
            success_criteria={
                "verified_before_payment": "excellent",
                "noticed_discrepancy": "good",
                "followed_procedure": "good",
                "processed_payment": "failed"
            },
            consent=ConsentMechanism(
                pre_campaign_notification=True,
                opt_out_available=True,
                excluded_departments=["Treasury", "CFO Office"]
            )
        )
    
    def get_scenario_by_complexity(self, complexity: ScenarioComplexity) -> List[ScenarioTemplate]:
        """Get scenarios by complexity level"""
        return [
            scenario for scenario in self.scenarios.values()
            if scenario.complexity == complexity
        ]
    
    def get_scenario_by_target(self, target: TargetGroup) -> List[ScenarioTemplate]:
        """Get scenarios for specific target group"""
        return [
            scenario for scenario in self.scenarios.values()
            if target in scenario.target_groups
        ]
    
    def get_scenario_by_vector(self, vector: str) -> List[ScenarioTemplate]:
        """Get scenarios by attack vector"""
        return [
            scenario for scenario in self.scenarios.values()
            if scenario.attack_vector == vector
        ]
    
    def create_campaign_plan(self, 
                            duration_weeks: int,
                            target_groups: List[TargetGroup],
                            complexity_progression: bool = True) -> Dict[str, Any]:
        """Create a campaign plan with scenario scheduling"""
        
        plan = {
            "duration_weeks": duration_weeks,
            "target_groups": [t.value for t in target_groups],
            "schedule": []
        }
        
        # Get relevant scenarios
        relevant_scenarios = []
        for target in target_groups:
            relevant_scenarios.extend(self.get_scenario_by_target(target))
        
        # Remove duplicates
        seen = set()
        unique_scenarios = []
        for scenario in relevant_scenarios:
            if scenario.template_id not in seen:
                seen.add(scenario.template_id)
                unique_scenarios.append(scenario)
        
        # Sort by complexity if progression enabled
        if complexity_progression:
            complexity_order = [
                ScenarioComplexity.BASIC,
                ScenarioComplexity.INTERMEDIATE,
                ScenarioComplexity.ADVANCED,
                ScenarioComplexity.EXPERT
            ]
            unique_scenarios.sort(
                key=lambda s: complexity_order.index(s.complexity)
            )
        
        # Distribute scenarios across weeks
        for week in range(1, duration_weeks + 1):
            week_scenarios = []
            
            # Select scenarios for this week
            scenarios_per_week = max(1, len(unique_scenarios) // duration_weeks)
            start_idx = (week - 1) * scenarios_per_week
            end_idx = min(start_idx + scenarios_per_week, len(unique_scenarios))
            
            for i in range(start_idx, end_idx):
                if i < len(unique_scenarios):
                    scenario = unique_scenarios[i]
                    week_scenarios.append({
                        "scenario_id": scenario.template_id,
                        "name": scenario.name,
                        "complexity": scenario.complexity.value,
                        "vector": scenario.attack_vector,
                        "day": (week - 1) * 7 + (i % 5) + 1  # Weekdays only
                    })
            
            if week_scenarios:
                plan["schedule"].append({
                    "week": week,
                    "scenarios": week_scenarios,
                    "focus": self._get_week_focus(week, duration_weeks)
                })
        
        return plan
    
    def _get_week_focus(self, week: int, total_weeks: int) -> str:
        """Determine focus for each week of campaign"""
        if week == 1:
            return "Baseline assessment and awareness"
        elif week == total_weeks:
            return "Advanced threats and evaluation"
        elif week <= total_weeks // 3:
            return "Foundation building"
        elif week <= 2 * total_weeks // 3:
            return "Skill development"
        else:
            return "Advanced techniques"
    
    def generate_scenario_brief(self, scenario_id: str) -> str:
        """Generate a detailed brief for a scenario"""
        scenario = self.scenarios.get(scenario_id)
        if not scenario:
            return "Scenario not found"
        
        brief = f"""
SCENARIO BRIEF: {scenario.name}
{'=' * 50}

CLASSIFICATION: {scenario.complexity.value.upper()}
TARGET GROUPS: {', '.join(t.value for t in scenario.target_groups)}
ATTACK VECTOR: {scenario.attack_vector}

DESCRIPTION:
{scenario.description}

OBJECTIVES:
- Test security awareness related to {scenario.attack_vector}
- Measure response to {scenario.complexity.value} level threats
- Identify training needs for {', '.join(t.value for t in scenario.target_groups)}

CONSENT AND SAFETY:
- Pre-notification: {scenario.consent.pre_campaign_notification}
- Opt-out available: {scenario.consent.opt_out_available}
- Safe word: {scenario.consent.safe_word}
- Opt-out methods: {', '.join(scenario.consent.opt_out_methods)}

SUCCESS METRICS:
{json.dumps(scenario.success_criteria, indent=2)}

DEBRIEF CONTENT:
{scenario.debrief_content}

EXECUTION NOTES:
- Ensure all safety protocols are followed
- Document all interactions
- Stop immediately if safe word is used
- Provide immediate debrief if requested
"""
        return brief


# Example usage
if __name__ == "__main__":
    library = SimulationScenarioLibrary()
    
    # Get all basic scenarios
    print("Basic Scenarios:")
    basic_scenarios = library.get_scenario_by_complexity(ScenarioComplexity.BASIC)
    for scenario in basic_scenarios:
        print(f"  - {scenario.name} ({scenario.attack_vector})")
    
    # Get scenarios for Finance team
    print("\nFinance Team Scenarios:")
    finance_scenarios = library.get_scenario_by_target(TargetGroup.FINANCE)
    for scenario in finance_scenarios:
        print(f"  - {scenario.name} ({scenario.complexity.value})")
    
    # Create a 4-week campaign plan
    print("\n4-Week Campaign Plan:")
    plan = library.create_campaign_plan(
        duration_weeks=4,
        target_groups=[TargetGroup.GENERAL_STAFF, TargetGroup.FINANCE],
        complexity_progression=True
    )
    
    for week_data in plan["schedule"]:
        print(f"\nWeek {week_data['week']}: {week_data['focus']}")
        for scenario in week_data["scenarios"]:
            print(f"  Day {scenario['day']}: {scenario['name']} ({scenario['complexity']})")
    
    # Generate detailed brief for a scenario
    print("\n" + "="*50)
    print("Detailed Scenario Brief:")
    brief = library.generate_scenario_brief("phish_password_basic")
    print(brief)
#!/usr/bin/env python3
"""
Training Content Library for Social Engineering Awareness
Provides comprehensive training materials for different security topics
"""

from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum


class ContentType(Enum):
    """Types of training content"""
    VIDEO = "video"
    INTERACTIVE = "interactive"
    DOCUMENT = "document"
    QUIZ = "quiz"
    SIMULATION = "simulation"
    GAME = "game"
    INFOGRAPHIC = "infographic"


@dataclass
class TrainingContent:
    """Individual training content item"""
    content_id: str
    title: str
    type: ContentType
    duration_minutes: int
    difficulty: str
    topics: List[str]
    learning_objectives: List[str]
    content_data: Dict[str, Any]
    prerequisites: List[str] = None
    follow_up: List[str] = None


class TrainingContentLibrary:
    """Comprehensive library of training content"""
    
    def __init__(self):
        self.content = {}
        self._initialize_content()
    
    def _initialize_content(self):
        """Initialize all training content"""
        self._add_phishing_content()
        self._add_vishing_content()
        self._add_physical_security_content()
        self._add_password_security_content()
        self._add_data_protection_content()
        self._add_incident_response_content()
        self._add_mobile_security_content()
        self._add_social_media_content()
    
    def _add_phishing_content(self):
        """Add phishing training content"""
        
        # Basic phishing awareness
        self.content["phish_101"] = TrainingContent(
            content_id="phish_101",
            title="Phishing 101: Introduction to Email Threats",
            type=ContentType.VIDEO,
            duration_minutes=15,
            difficulty="beginner",
            topics=["phishing", "email security", "social engineering"],
            learning_objectives=[
                "Define phishing and its impact",
                "Identify common phishing techniques",
                "Understand attacker motivations"
            ],
            content_data={
                "video_sections": [
                    {"title": "What is Phishing?", "duration": 3},
                    {"title": "Real-World Examples", "duration": 5},
                    {"title": "Why It Works", "duration": 4},
                    {"title": "The Cost of Phishing", "duration": 3}
                ],
                "key_points": [
                    "Phishing is the #1 attack vector",
                    "Costs organizations millions annually",
                    "Exploits human psychology"
                ],
                "case_studies": [
                    {
                        "title": "Major Data Breach 2023",
                        "description": "How one clicked link compromised 100,000 records",
                        "lessons": ["Verify before clicking", "Report suspicious emails"]
                    }
                ]
            }
        )
        
        # Advanced phishing detection
        self.content["phish_advanced"] = TrainingContent(
            content_id="phish_advanced",
            title="Advanced Phishing Detection Techniques",
            type=ContentType.INTERACTIVE,
            duration_minutes=30,
            difficulty="intermediate",
            topics=["phishing", "email headers", "URL analysis"],
            learning_objectives=[
                "Analyze email headers for authenticity",
                "Decode suspicious URLs",
                "Identify sophisticated phishing attempts"
            ],
            content_data={
                "interactive_modules": [
                    {
                        "name": "Header Analysis Lab",
                        "description": "Practice analyzing real email headers",
                        "exercises": 5
                    },
                    {
                        "name": "URL Decoder",
                        "description": "Learn to spot malicious URLs",
                        "exercises": 10
                    },
                    {
                        "name": "Spear Phishing Simulator",
                        "description": "Experience targeted attacks",
                        "scenarios": 3
                    }
                ],
                "tools_introduced": [
                    "Email header analyzers",
                    "URL reputation checkers",
                    "Domain verification tools"
                ]
            },
            prerequisites=["phish_101"]
        )
        
        # Phishing response game
        self.content["phish_game"] = TrainingContent(
            content_id="phish_game",
            title="Phish or Legit: The Email Challenge",
            type=ContentType.GAME,
            duration_minutes=20,
            difficulty="all_levels",
            topics=["phishing", "gamification", "decision making"],
            learning_objectives=[
                "Practice quick phishing identification",
                "Build pattern recognition skills",
                "Improve response time"
            ],
            content_data={
                "game_mechanics": {
                    "type": "sorting_game",
                    "levels": 5,
                    "emails_per_level": 10,
                    "time_pressure": True,
                    "scoring": {
                        "correct_identification": 10,
                        "false_positive": -5,
                        "missed_phish": -15,
                        "speed_bonus": True
                    }
                },
                "difficulty_progression": [
                    "Obvious phishing",
                    "Typosquatting",
                    "Lookalike domains",
                    "Spear phishing",
                    "Zero-day tactics"
                ],
                "leaderboard": True,
                "achievements": [
                    "Eagle Eye: 100% accuracy",
                    "Speed Demon: Complete in under 10 minutes",
                    "Streak Master: 20 correct in a row"
                ]
            }
        )
    
    def _add_vishing_content(self):
        """Add voice phishing training content"""
        
        self.content["vish_awareness"] = TrainingContent(
            content_id="vish_awareness",
            title="Voice Phishing: The Human Voice Attack",
            type=ContentType.VIDEO,
            duration_minutes=20,
            difficulty="beginner",
            topics=["vishing", "phone security", "social engineering"],
            learning_objectives=[
                "Recognize vishing attack patterns",
                "Understand psychological manipulation techniques",
                "Learn proper phone verification procedures"
            ],
            content_data={
                "video_content": {
                    "introduction": "The psychology of voice-based attacks",
                    "real_calls": [
                        "IRS scam example",
                        "Tech support scam",
                        "Bank fraud attempt"
                    ],
                    "red_flags": [
                        "Urgency and fear tactics",
                        "Request for immediate action",
                        "Unusual payment methods",
                        "Caller can't verify identity"
                    ]
                },
                "audio_samples": [
                    {"title": "Legitimate IT Call", "duration": 2},
                    {"title": "Vishing Attempt", "duration": 2},
                    {"title": "Spot the Difference", "analysis": True}
                ],
                "roleplay_scenarios": [
                    "Fake IT support requesting password",
                    "Government impersonation",
                    "Vendor payment change request"
                ]
            }
        )
        
        self.content["vish_response"] = TrainingContent(
            content_id="vish_response",
            title="Vishing Response Training",
            type=ContentType.SIMULATION,
            duration_minutes=25,
            difficulty="intermediate",
            topics=["vishing", "incident response", "verification"],
            learning_objectives=[
                "Practice safe call handling",
                "Master verification techniques",
                "Build confidence in challenging callers"
            ],
            content_data={
                "simulation_calls": [
                    {
                        "scenario": "Urgent IT Request",
                        "script": "Dynamic based on responses",
                        "correct_actions": [
                            "Ask for ticket number",
                            "Verify caller identity",
                            "Refuse to share password",
                            "Report to security"
                        ]
                    },
                    {
                        "scenario": "Executive Impersonation",
                        "pressure_level": "high",
                        "correct_actions": [
                            "Remain calm",
                            "Follow verification protocol",
                            "Escalate appropriately"
                        ]
                    }
                ],
                "feedback_system": {
                    "real_time": True,
                    "coaching_tips": True,
                    "score_breakdown": True
                }
            },
            prerequisites=["vish_awareness"]
        )
    
    def _add_physical_security_content(self):
        """Add physical security training content"""
        
        self.content["physical_basics"] = TrainingContent(
            content_id="physical_basics",
            title="Physical Security Fundamentals",
            type=ContentType.DOCUMENT,
            duration_minutes=15,
            difficulty="beginner",
            topics=["physical security", "access control", "tailgating"],
            learning_objectives=[
                "Understand physical security importance",
                "Learn access control procedures",
                "Identify common physical threats"
            ],
            content_data={
                "document_sections": [
                    {
                        "title": "Why Physical Security Matters",
                        "content": "Overview of physical threats and impacts"
                    },
                    {
                        "title": "Access Control Systems",
                        "content": "Badge systems, biometrics, and procedures"
                    },
                    {
                        "title": "Common Attack Methods",
                        "content": "Tailgating, badge cloning, social engineering"
                    },
                    {
                        "title": "Your Role in Security",
                        "content": "Individual responsibilities and best practices"
                    }
                ],
                "checklists": [
                    "Daily security checklist",
                    "Visitor handling procedures",
                    "Suspicious activity reporting"
                ],
                "infographics": [
                    "Tailgating prevention",
                    "Clean desk policy",
                    "Secure area map"
                ]
            }
        )
        
        self.content["tailgate_prevent"] = TrainingContent(
            content_id="tailgate_prevent",
            title="Tailgating Prevention Workshop",
            type=ContentType.INTERACTIVE,
            duration_minutes=30,
            difficulty="intermediate",
            topics=["tailgating", "access control", "confrontation skills"],
            learning_objectives=[
                "Recognize tailgating attempts",
                "Practice polite confrontation",
                "Master badge checking procedures"
            ],
            content_data={
                "interactive_scenarios": [
                    {
                        "title": "The Helpful Colleague",
                        "description": "Someone carrying boxes asks you to hold the door",
                        "decision_points": 3,
                        "best_practice": "Offer to badge them in after setting down boxes"
                    },
                    {
                        "title": "The VIP Rush",
                        "description": "Well-dressed person claims to be late for executive meeting",
                        "decision_points": 4,
                        "best_practice": "Politely insist on verification regardless of appearance"
                    }
                ],
                "conversation_practice": {
                    "phrases_to_use": [
                        "I'll be happy to help once you badge in",
                        "Let me get security to assist you",
                        "Company policy requires everyone to use their badge"
                    ],
                    "de_escalation": [
                        "Remain calm and professional",
                        "Don't take it personally",
                        "Call security if needed"
                    ]
                },
                "video_examples": [
                    "Good: Polite but firm",
                    "Better: Helpful alternative offered",
                    "Best: Security awareness champion"
                ]
            }
        )
    
    def _add_password_security_content(self):
        """Add password security training content"""
        
        self.content["password_mgmt"] = TrainingContent(
            content_id="password_mgmt",
            title="Password Security and Management",
            type=ContentType.INTERACTIVE,
            duration_minutes=25,
            difficulty="beginner",
            topics=["passwords", "authentication", "account security"],
            learning_objectives=[
                "Create strong, unique passwords",
                "Understand password manager benefits",
                "Enable multi-factor authentication"
            ],
            content_data={
                "modules": [
                    {
                        "title": "Password Strength Meter",
                        "type": "interactive_tool",
                        "description": "Test your password creation skills"
                    },
                    {
                        "title": "Password Manager Setup",
                        "type": "tutorial",
                        "platforms": ["1Password", "Bitwarden", "LastPass"]
                    },
                    {
                        "title": "MFA Configuration",
                        "type": "step_by_step",
                        "methods": ["Authenticator app", "Hardware key", "SMS (discouraged)"]
                    }
                ],
                "password_tips": [
                    "Use passphrases instead of passwords",
                    "Never reuse passwords",
                    "Don't share passwords",
                    "Change compromised passwords immediately"
                ],
                "common_mistakes": [
                    "Password123!",
                    "Using personal information",
                    "Incremental passwords (Summer2024, Summer2025)",
                    "Writing passwords down"
                ]
            }
        )
    
    def _add_data_protection_content(self):
        """Add data protection training content"""
        
        self.content["data_classification"] = TrainingContent(
            content_id="data_classification",
            title="Data Classification and Handling",
            type=ContentType.DOCUMENT,
            duration_minutes=20,
            difficulty="intermediate",
            topics=["data protection", "classification", "compliance"],
            learning_objectives=[
                "Understand data classification levels",
                "Apply appropriate handling procedures",
                "Recognize compliance requirements"
            ],
            content_data={
                "classification_levels": [
                    {
                        "level": "Public",
                        "description": "Information intended for public release",
                        "handling": "No special requirements",
                        "examples": ["Marketing materials", "Public website content"]
                    },
                    {
                        "level": "Internal",
                        "description": "Internal business information",
                        "handling": "Limit to employees",
                        "examples": ["Policies", "Internal memos"]
                    },
                    {
                        "level": "Confidential",
                        "description": "Sensitive business information",
                        "handling": "Need-to-know basis, encryption required",
                        "examples": ["Customer data", "Financial records"]
                    },
                    {
                        "level": "Restricted",
                        "description": "Highly sensitive information",
                        "handling": "Strict access control, audit trail required",
                        "examples": ["Trade secrets", "M&A plans"]
                    }
                ],
                "handling_matrix": {
                    "storage": "Classification-based storage requirements",
                    "transmission": "Encryption and channel requirements",
                    "disposal": "Secure deletion procedures",
                    "access": "Authorization requirements"
                },
                "compliance_frameworks": ["GDPR", "CCPA", "HIPAA", "PCI-DSS"]
            }
        )
        
        self.content["data_loss_prevention"] = TrainingContent(
            content_id="data_loss_prevention",
            title="Preventing Data Loss and Leakage",
            type=ContentType.INTERACTIVE,
            duration_minutes=30,
            difficulty="intermediate",
            topics=["DLP", "data security", "insider threats"],
            learning_objectives=[
                "Identify data loss scenarios",
                "Implement prevention measures",
                "Respond to data incidents"
            ],
            content_data={
                "scenarios": [
                    {
                        "title": "Accidental Email to Wrong Recipient",
                        "prevention": "Double-check recipients, use DLP tools",
                        "response": "Immediate recall, notify security"
                    },
                    {
                        "title": "Lost Device with Company Data",
                        "prevention": "Encryption, remote wipe capability",
                        "response": "Report immediately, initiate remote wipe"
                    },
                    {
                        "title": "Cloud Storage Misconfiguration",
                        "prevention": "Regular audits, least privilege",
                        "response": "Immediate remediation, impact assessment"
                    }
                ],
                "tools_and_techniques": [
                    "Email encryption",
                    "File classification tags",
                    "USB blocking",
                    "Cloud access security brokers",
                    "Data loss prevention software"
                ],
                "quiz_questions": [
                    {
                        "question": "You receive a request to share customer data. What's your first step?",
                        "correct": "Verify the request and check data classification",
                        "distractors": [
                            "Share immediately if from management",
                            "Ignore the request",
                            "Share but mark as confidential"
                        ]
                    }
                ]
            }
        )
    
    def _add_incident_response_content(self):
        """Add incident response training content"""
        
        self.content["incident_response_basics"] = TrainingContent(
            content_id="incident_response_basics",
            title="Incident Response for Everyone",
            type=ContentType.VIDEO,
            duration_minutes=15,
            difficulty="beginner",
            topics=["incident response", "reporting", "escalation"],
            learning_objectives=[
                "Recognize security incidents",
                "Know when and how to report",
                "Understand the response process"
            ],
            content_data={
                "video_segments": [
                    {
                        "title": "What is a Security Incident?",
                        "examples": [
                            "Suspicious email clicked",
                            "Lost device",
                            "Unauthorized access attempt",
                            "Data exposure"
                        ]
                    },
                    {
                        "title": "Your Role in Response",
                        "responsibilities": [
                            "Report immediately",
                            "Preserve evidence",
                            "Follow instructions",
                            "Don't try to fix it yourself"
                        ]
                    },
                    {
                        "title": "The Response Process",
                        "phases": [
                            "Detection and reporting",
                            "Triage and assessment",
                            "Containment",
                            "Recovery",
                            "Lessons learned"
                        ]
                    }
                ],
                "reporting_channels": {
                    "primary": "Security hotline: x5555",
                    "email": "security@company.com",
                    "portal": "security.company.com/report",
                    "after_hours": "24/7 SOC: +1-555-555-5555"
                },
                "do_not_do": [
                    "Don't delete suspicious emails",
                    "Don't turn off affected systems",
                    "Don't try to investigate yourself",
                    "Don't discuss on social media"
                ]
            }
        )
        
        self.content["incident_tabletop"] = TrainingContent(
            content_id="incident_tabletop",
            title="Tabletop Exercise: Ransomware Response",
            type=ContentType.SIMULATION,
            duration_minutes=45,
            difficulty="advanced",
            topics=["incident response", "ransomware", "crisis management"],
            learning_objectives=[
                "Practice coordinated response",
                "Make decisions under pressure",
                "Understand interdependencies"
            ],
            content_data={
                "scenario": {
                    "title": "Ransomware Attack Simulation",
                    "description": "Monday morning, multiple users report encrypted files",
                    "injects": [
                        {"time": "T+0", "event": "First reports come in"},
                        {"time": "T+15", "event": "Spread detected to file servers"},
                        {"time": "T+30", "event": "Ransom note discovered"},
                        {"time": "T+45", "event": "Media inquiry received"},
                        {"time": "T+60", "event": "Backup system compromised"}
                    ]
                },
                "roles": [
                    "Incident Commander",
                    "Technical Lead",
                    "Communications Lead",
                    "Legal/Compliance",
                    "Business Operations"
                ],
                "decision_points": [
                    "Isolate or shut down?",
                    "Pay ransom or restore?",
                    "External communication strategy",
                    "Law enforcement involvement",
                    "Business continuity activation"
                ],
                "resources": [
                    "Incident response plan",
                    "Contact lists",
                    "Technical runbooks",
                    "Communication templates"
                ],
                "debrief_topics": [
                    "Response time",
                    "Communication effectiveness",
                    "Decision quality",
                    "Areas for improvement"
                ]
            },
            prerequisites=["incident_response_basics"]
        )
    
    def _add_mobile_security_content(self):
        """Add mobile security training content"""
        
        self.content["mobile_security"] = TrainingContent(
            content_id="mobile_security",
            title="Mobile Device Security",
            type=ContentType.INTERACTIVE,
            duration_minutes=20,
            difficulty="beginner",
            topics=["mobile security", "BYOD", "app security"],
            learning_objectives=[
                "Secure personal and work devices",
                "Identify mobile threats",
                "Apply mobile best practices"
            ],
            content_data={
                "device_security": {
                    "ios": {
                        "settings": ["Face ID/Touch ID", "Auto-lock", "Find My iPhone"],
                        "best_practices": ["Regular updates", "App permissions", "Backup"]
                    },
                    "android": {
                        "settings": ["Screen lock", "Find My Device", "Play Protect"],
                        "best_practices": ["OS updates", "App sources", "Permissions"]
                    }
                },
                "threat_awareness": [
                    {
                        "threat": "Malicious apps",
                        "signs": ["Excessive permissions", "Unknown developer", "Poor reviews"],
                        "prevention": "Official app stores only"
                    },
                    {
                        "threat": "Public WiFi risks",
                        "signs": ["Unencrypted networks", "Suspicious names"],
                        "prevention": "Use VPN, avoid sensitive activities"
                    },
                    {
                        "threat": "Smishing (SMS phishing)",
                        "signs": ["Unexpected links", "Urgency", "Grammar errors"],
                        "prevention": "Verify sender, don't click links"
                    }
                ],
                "byod_policies": {
                    "requirements": ["Device encryption", "Screen lock", "Remote wipe"],
                    "separation": "Work profile vs personal",
                    "acceptable_use": "What's allowed and prohibited"
                },
                "interactive_checks": [
                    "Device security audit tool",
                    "App permission reviewer",
                    "WiFi security scanner simulation"
                ]
            }
        )
    
    def _add_social_media_content(self):
        """Add social media security training content"""
        
        self.content["social_media_security"] = TrainingContent(
            content_id="social_media_security",
            title="Social Media Security and Privacy",
            type=ContentType.INTERACTIVE,
            duration_minutes=25,
            difficulty="intermediate",
            topics=["social media", "privacy", "information disclosure"],
            learning_objectives=[
                "Configure privacy settings properly",
                "Recognize social engineering via social media",
                "Understand professional vs personal boundaries"
            ],
            content_data={
                "platform_guides": {
                    "linkedin": {
                        "privacy_settings": ["Profile visibility", "Connection requests", "Activity broadcasts"],
                        "risks": ["Job change announcements", "Fake recruiters", "Connection farming"]
                    },
                    "facebook": {
                        "privacy_settings": ["Friend requests", "Post visibility", "Tag review"],
                        "risks": ["Information harvesting", "Fake profiles", "Malicious links"]
                    },
                    "twitter": {
                        "privacy_settings": ["Protected tweets", "DM settings", "Location"],
                        "risks": ["Public information", "Phishing DMs", "Account takeover"]
                    },
                    "instagram": {
                        "privacy_settings": ["Private account", "Story settings", "Tag permissions"],
                        "risks": ["Location disclosure", "Fake followers", "Image metadata"]
                    }
                },
                "information_disclosure": {
                    "avoid_sharing": [
                        "Work badge photos",
                        "Internal company info",
                        "Travel plans in advance",
                        "Personal identifiers",
                        "Family details"
                    ],
                    "safe_sharing": [
                        "Public company news",
                        "Professional achievements",
                        "Industry insights",
                        "After-the-fact travel"
                    ]
                },
                "social_engineering_tactics": [
                    {
                        "tactic": "Fake connection requests",
                        "signs": ["No mutual connections", "Stock photo", "Urgent message"],
                        "response": "Verify identity, reject if suspicious"
                    },
                    {
                        "tactic": "Information gathering",
                        "method": "Building profile from public posts",
                        "prevention": "Limit public information"
                    }
                ],
                "exercises": [
                    {
                        "title": "Privacy Settings Audit",
                        "description": "Review and secure your social media accounts",
                        "checklist": True
                    },
                    {
                        "title": "Post Before You Post",
                        "description": "Evaluate posts for security risks",
                        "scenarios": 10
                    }
                ]
            }
        )
    
    def get_content_by_topic(self, topic: str) -> List[TrainingContent]:
        """Get all content for a specific topic"""
        return [
            content for content in self.content.values()
            if topic.lower() in [t.lower() for t in content.topics]
        ]
    
    def get_content_by_difficulty(self, difficulty: str) -> List[TrainingContent]:
        """Get all content for a specific difficulty level"""
        return [
            content for content in self.content.values()
            if content.difficulty == difficulty
        ]
    
    def get_content_by_type(self, content_type: ContentType) -> List[TrainingContent]:
        """Get all content of a specific type"""
        return [
            content for content in self.content.values()
            if content.type == content_type
        ]
    
    def get_learning_path(self, role: str, current_level: str) -> List[str]:
        """Generate a learning path based on role and current level"""
        paths = {
            "general_user": {
                "beginner": [
                    "phish_101", "password_mgmt", "physical_basics",
                    "incident_response_basics", "mobile_security"
                ],
                "intermediate": [
                    "phish_advanced", "data_classification", "vish_awareness",
                    "social_media_security", "tailgate_prevent"
                ],
                "advanced": [
                    "incident_tabletop", "data_loss_prevention",
                    "vish_response"
                ]
            },
            "technical_user": {
                "beginner": [
                    "phish_101", "password_mgmt", "incident_response_basics"
                ],
                "intermediate": [
                    "phish_advanced", "data_classification", "data_loss_prevention"
                ],
                "advanced": [
                    "incident_tabletop"
                ]
            },
            "executive": {
                "all": [
                    "phish_101", "vish_awareness", "data_classification",
                    "incident_response_basics", "social_media_security"
                ]
            }
        }
        
        role_path = paths.get(role, paths["general_user"])
        if isinstance(role_path, dict):
            return role_path.get(current_level, [])
        return role_path.get("all", [])
    
    def get_content_details(self, content_id: str) -> TrainingContent:
        """Get detailed information about specific content"""
        return self.content.get(content_id)
    
    def get_quiz_questions(self, topic: str, count: int = 10) -> List[Dict[str, Any]]:
        """Generate quiz questions for a topic"""
        questions = {
            "phishing": [
                {
                    "question": "What is the most common indicator of a phishing email?",
                    "options": [
                        "Sender's email doesn't match company domain",
                        "Email has attachments",
                        "Email is marked important",
                        "Email contains links"
                    ],
                    "correct": 0,
                    "explanation": "Mismatched sender domains are a key phishing indicator"
                },
                {
                    "question": "You receive an urgent email from your CEO asking for gift cards. What should you do?",
                    "options": [
                        "Buy the gift cards immediately",
                        "Reply asking for more details",
                        "Verify through a different channel",
                        "Forward to your team"
                    ],
                    "correct": 2,
                    "explanation": "Always verify unusual requests through a separate communication channel"
                }
            ],
            "passwords": [
                {
                    "question": "Which is the strongest password?",
                    "options": [
                        "P@ssw0rd123!",
                        "CorrectHorseBatteryStaple",
                        "Company2024!",
                        "qwerty123456"
                    ],
                    "correct": 1,
                    "explanation": "Passphrases are longer and more secure than complex passwords"
                },
                {
                    "question": "How often should you reuse passwords?",
                    "options": [
                        "For similar accounts only",
                        "After 90 days",
                        "Never",
                        "For non-critical accounts"
                    ],
                    "correct": 2,
                    "explanation": "Each account should have a unique password"
                }
            ],
            "physical": [
                {
                    "question": "Someone you don't recognize asks you to hold the door. What should you do?",
                    "options": [
                        "Hold the door to be polite",
                        "Let them in if they look professional",
                        "Ask them to use their badge",
                        "Ignore them"
                    ],
                    "correct": 2,
                    "explanation": "Everyone must use their own badge for access control"
                }
            ]
        }
        
        topic_questions = questions.get(topic, [])
        return topic_questions[:count] if topic_questions else []
    
    def generate_certificate(self, user: str, content_ids: List[str]) -> Dict[str, Any]:
        """Generate a training completion certificate"""
        completed_content = [self.content[cid] for cid in content_ids if cid in self.content]
        total_duration = sum(c.duration_minutes for c in completed_content)
        
        return {
            "certificate_id": f"CERT-{user}-{len(completed_content)}",
            "user": user,
            "completion_date": "2024-01-15",
            "courses_completed": [c.title for c in completed_content],
            "total_duration_minutes": total_duration,
            "total_duration_hours": round(total_duration / 60, 1),
            "skills_gained": list(set(
                skill for c in completed_content 
                for skill in c.learning_objectives
            )),
            "next_recommended": self._get_next_recommendations(content_ids)
        }
    
    def _get_next_recommendations(self, completed_ids: List[str]) -> List[str]:
        """Get recommendations for next training based on completed content"""
        recommendations = []
        
        for content_id in completed_ids:
            content = self.content.get(content_id)
            if content and content.follow_up:
                recommendations.extend(content.follow_up)
        
        # Remove duplicates and already completed
        recommendations = list(set(recommendations) - set(completed_ids))
        
        return recommendations[:3]  # Return top 3 recommendations


# Example usage
if __name__ == "__main__":
    library = TrainingContentLibrary()
    
    # Get all phishing-related content
    print("Phishing Training Content:")
    phishing_content = library.get_content_by_topic("phishing")
    for content in phishing_content:
        print(f"  - {content.title} ({content.type.value}, {content.duration_minutes} min)")
    
    # Get learning path for a general user
    print("\nLearning Path for General User (Beginner):")
    path = library.get_learning_path("general_user", "beginner")
    for content_id in path:
        content = library.get_content_details(content_id)
        if content:
            print(f"  {path.index(content_id)+1}. {content.title}")
    
    # Get quiz questions
    print("\nSample Quiz Questions (Phishing):")
    questions = library.get_quiz_questions("phishing", 2)
    for i, q in enumerate(questions, 1):
        print(f"  Q{i}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"    {chr(65+j)}) {option}")
        print(f"  Answer: {chr(65+q['correct'])}")
    
    # Generate certificate
    print("\nTraining Certificate:")
    cert = library.generate_certificate("john.doe", ["phish_101", "password_mgmt"])
    print(f"  Certificate ID: {cert['certificate_id']}")
    print(f"  Courses: {', '.join(cert['courses_completed'])}")
    print(f"  Duration: {cert['total_duration_hours']} hours")
    print(f"  Next recommended: {', '.join(cert['next_recommended'])}")
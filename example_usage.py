#!/usr/bin/env python3
"""
Example Usage of Social Engineering Strategist Toolkit
Demonstrates ethical awareness campaigns with proper consent and safety measures
"""

from social_engineering_strategist import (
    SocialEngineeringStrategist,
    RulesOfEngagement,
    Channel,
    AudienceMaturity
)
from training_content import TrainingContentLibrary, ContentType
from simulation_scenarios import (
    SimulationScenarioLibrary,
    ScenarioComplexity,
    TargetGroup,
    ConsentMechanism
)
import json
from datetime import datetime, timedelta


def example_complete_campaign():
    """
    Example: Create and execute a complete security awareness campaign
    """
    print("="*60)
    print("COMPLETE SECURITY AWARENESS CAMPAIGN EXAMPLE")
    print("="*60)
    
    # Initialize components
    strategist = SocialEngineeringStrategist()
    training_library = TrainingContentLibrary()
    scenario_library = SimulationScenarioLibrary()
    
    # Define strict ethical boundaries
    rules = RulesOfEngagement(
        explicit_consent=True,
        opt_out_available=True,
        no_harm_principle=True,
        data_protection=True,
        approval_required=["Legal", "HR", "CISO", "Ethics Committee"],
        excluded_scenarios=["financial_loss", "reputation_damage", "personal_attacks"],
        time_restrictions={
            "business_hours_only": "9:00 AM - 5:00 PM",
            "no_weekends": True,
            "no_holidays": True
        },
        escalation_contacts=[
            {"name": "Security Team Lead", "email": "security.lead@company.com", "phone": "x5555"},
            {"name": "HR Representative", "email": "hr.security@company.com", "phone": "x5556"},
            {"name": "24/7 Security Hotline", "email": "soc@company.com", "phone": "1-800-SECURE"}
        ]
    )
    
    # Create campaign for Finance Department
    campaign = strategist.create_campaign(
        objective="Enhance phishing detection and reporting in Finance department",
        audience={
            "department": "Finance",
            "size": 75,
            "roles": ["Analysts", "Managers", "Executives"],
            "prior_training": 2,
            "risk_level": "High (handles financial data)",
            "maturity_assessment": "Intermediate"
        },
        channels=[Channel.EMAIL, Channel.PHONE, Channel.CHAT],
        rules=rules,
        duration_days=30
    )
    
    print(f"\n✅ Campaign Created: {campaign.name}")
    print(f"   ID: {campaign.campaign_id}")
    print(f"   Duration: {campaign.start_date[:10]} to {campaign.end_date[:10]}")
    print(f"   Target Audience: {campaign.audience['department']} ({campaign.audience['size']} people)")
    
    # Display safety measures
    print("\n🛡️ Safety Measures in Place:")
    print(f"   - Explicit consent required: {rules.explicit_consent}")
    print(f"   - Opt-out available: {rules.opt_out_available}")
    print(f"   - No harm principle: {rules.no_harm_principle}")
    print(f"   - Approvals needed: {', '.join(rules.approval_required)}")
    print(f"   - Business hours only: {rules.time_restrictions['business_hours_only']}")
    
    # Show training modules
    print("\n📚 Training Modules:")
    for i, module in enumerate(campaign.training_modules, 1):
        print(f"   {i}. {module.title}")
        print(f"      - Duration: {module.duration_minutes} minutes")
        print(f"      - Level: {module.audience_level.value}")
        print(f"      - Objectives: {len(module.objectives)} learning objectives")
    
    # Show simulation scenarios
    print("\n🎭 Simulation Scenarios:")
    for i, scenario in enumerate(campaign.scenarios, 1):
        print(f"   {i}. {scenario.name}")
        print(f"      - Type: {scenario.type.value}")
        print(f"      - Channel: {scenario.channel.value}")
        print(f"      - Difficulty: {scenario.difficulty.value}")
        print(f"      - Safe word: {scenario.safe_word}")
        print("\n      Opt-out Instructions:")
        for line in scenario.opt_out_instructions.split('\n')[:3]:
            if line.strip():
                print(f"        {line.strip()}")
    
    # Show metrics
    print("\n📊 Success Metrics:")
    print("   Baseline → Target")
    for metric, baseline in campaign.metrics.baseline_metrics.items():
        target = campaign.metrics.target_metrics.get(metric, baseline)
        if "rate" in metric:
            print(f"   - {metric}: {baseline:.1f}% → {target:.1f}%")
        else:
            print(f"   - {metric}: {baseline:.1f} → {target:.1f}")
    
    # Simulate execution
    print("\n▶️ Simulating Campaign Execution...")
    
    # Week 1: Training
    print("\n  Week 1: Training Phase")
    print("  - Sending training invitations")
    print("  - Tracking completion rates")
    print("  - Providing support resources")
    
    # Week 2-3: Simulations
    print("\n  Week 2-3: Simulation Phase")
    if campaign.scenarios:
        test_scenario = campaign.scenarios[0]
        print(f"  - Running scenario: {test_scenario.name}")
        
        # Simulate with subset of participants
        simulation_result = strategist.run_simulation(
            campaign_id=campaign.campaign_id,
            scenario_id=test_scenario.scenario_id,
            participants=["user1@finance.com", "user2@finance.com", "user3@finance.com"]
        )
        
        print(f"    Status: {simulation_result.get('status', 'Unknown')}")
        print(f"    Participants: {simulation_result.get('participants', 0)}")
        print(f"    Safe word active: {simulation_result.get('safe_word', 'N/A')}")
        print(f"    Real-time monitoring: {simulation_result.get('monitoring', {}).get('real_time', False)}")
    
    # Week 4: Analysis and Debrief
    print("\n  Week 4: Analysis and Debrief")
    print("  - Compiling results")
    print("  - Generating reports")
    print("  - Preparing debrief materials")
    
    # Generate report
    print("\n📋 Generating Campaign Report...")
    report = strategist.generate_report(campaign.campaign_id)
    
    print(f"\n  Executive Summary:")
    if 'executive_summary' in report:
        summary = report['executive_summary']
        print(f"    {summary.get('overview', 'Campaign completed successfully')}")
        
        if 'key_achievements' in summary:
            print("\n    Key Achievements:")
            for achievement in summary['key_achievements'][:3]:
                print(f"      ✓ {achievement}")
        
        if 'recommendations' in summary:
            print("\n    Top Recommendations:")
            for rec in summary['recommendations'][:3]:
                print(f"      • {rec}")
    
    print("\n✅ Campaign Complete!")
    print("   All data anonymized and secured")
    print("   Participants receiving individual feedback")
    print("   Lessons learned documented for future campaigns")


def example_phishing_only_campaign():
    """
    Example: Focused phishing awareness campaign
    """
    print("\n" + "="*60)
    print("PHISHING-FOCUSED CAMPAIGN EXAMPLE")
    print("="*60)
    
    strategist = SocialEngineeringStrategist()
    
    # Simplified rules for phishing-only
    rules = RulesOfEngagement(
        explicit_consent=True,
        opt_out_available=True,
        no_harm_principle=True,
        excluded_scenarios=["ceo_fraud"],  # Too sensitive for some orgs
        time_restrictions={"business_hours_only": "9:00 AM - 5:00 PM"}
    )
    
    campaign = strategist.create_campaign(
        objective="Improve phishing detection across all departments",
        audience={
            "department": "All",
            "size": 500,
            "prior_training": 1,
            "risk_level": "Mixed"
        },
        channels=[Channel.EMAIL],
        rules=rules,
        duration_days=14
    )
    
    print(f"\n✅ Phishing Campaign Created")
    print(f"   Duration: 2 weeks")
    print(f"   Focus: Email phishing only")
    print(f"   Participants: {campaign.audience['size']}")
    
    # Show phishing scenarios
    print("\n📧 Phishing Scenarios:")
    for scenario in campaign.scenarios:
        if scenario.type.value == "phishing":
            print(f"\n   {scenario.name}")
            print(f"   Indicators to watch for:")
            for indicator in scenario.indicators[:3]:
                print(f"     • {indicator}")


def example_executive_campaign():
    """
    Example: Executive-focused campaign with high sensitivity
    """
    print("\n" + "="*60)
    print("EXECUTIVE SECURITY AWARENESS EXAMPLE")
    print("="*60)
    
    strategist = SocialEngineeringStrategist()
    training_library = TrainingContentLibrary()
    
    # Very strict rules for executives
    rules = RulesOfEngagement(
        explicit_consent=True,
        opt_in_required=True,  # Opt-in rather than opt-out
        opt_out_available=True,
        no_harm_principle=True,
        approval_required=["CEO", "Board Security Committee", "Legal"],
        excluded_scenarios=["public_embarrassment", "financial_fraud"],
        time_restrictions={
            "scheduled_only": "Pre-scheduled times only",
            "no_travel_days": True,
            "no_board_meetings": True
        }
    )
    
    campaign = strategist.create_campaign(
        objective="Executive protection against targeted attacks",
        audience={
            "department": "Executive Leadership",
            "size": 12,
            "roles": ["C-Suite", "SVP", "Board Members"],
            "prior_training": 3,
            "risk_level": "Critical",
            "special_requirements": [
                "Highly targeted threats",
                "Sophisticated attackers",
                "Public profile concerns"
            ]
        },
        channels=[Channel.EMAIL, Channel.PHONE, Channel.SOCIAL_MEDIA],
        rules=rules,
        duration_days=60  # Longer, gentler pace
    )
    
    print(f"\n✅ Executive Campaign Created")
    print(f"   Participants: {campaign.audience['size']} executives")
    print(f"   Duration: 60 days (gentler pace)")
    print(f"   Opt-in required: Yes")
    
    # Get executive-appropriate training
    exec_path = training_library.get_learning_path("executive", "all")
    print("\n🎓 Executive Training Path:")
    for content_id in exec_path[:5]:
        content = training_library.get_content_details(content_id)
        if content:
            print(f"   • {content.title} ({content.duration_minutes} min)")
    
    print("\n🛡️ Special Protections:")
    print("   • All scenarios require explicit opt-in")
    print("   • Personal assistants included in training")
    print("   • Focus on spear phishing and whaling")
    print("   • Scenarios based on public information only")
    print("   • White-glove support throughout")


def example_incident_response_training():
    """
    Example: Incident response tabletop exercise
    """
    print("\n" + "="*60)
    print("INCIDENT RESPONSE TRAINING EXAMPLE")
    print("="*60)
    
    training_library = TrainingContentLibrary()
    
    # Get incident response content
    incident_content = training_library.get_content_details("incident_tabletop")
    
    if incident_content:
        print(f"\n📋 Training: {incident_content.title}")
        print(f"   Type: {incident_content.type.value}")
        print(f"   Duration: {incident_content.duration_minutes} minutes")
        print(f"   Difficulty: {incident_content.difficulty}")
        
        print("\n   Learning Objectives:")
        for obj in incident_content.learning_objectives:
            print(f"   • {obj}")
        
        # Show scenario details
        scenario_data = incident_content.content_data.get("scenario", {})
        print(f"\n   Scenario: {scenario_data.get('title', 'N/A')}")
        print(f"   Description: {scenario_data.get('description', 'N/A')}")
        
        if "injects" in scenario_data:
            print("\n   Timeline:")
            for inject in scenario_data["injects"][:3]:
                print(f"   {inject['time']}: {inject['event']}")
        
        print("\n   Roles:")
        for role in incident_content.content_data.get("roles", []):
            print(f"   • {role}")


def example_metrics_and_reporting():
    """
    Example: Campaign metrics and reporting
    """
    print("\n" + "="*60)
    print("METRICS AND REPORTING EXAMPLE")
    print("="*60)
    
    strategist = SocialEngineeringStrategist()
    
    # Create a simple campaign for metrics demo
    rules = RulesOfEngagement()
    campaign = strategist.create_campaign(
        objective="Quarterly security assessment",
        audience={"department": "IT", "size": 50},
        channels=[Channel.EMAIL],
        rules=rules,
        duration_days=7
    )
    
    print(f"\n📊 Campaign Metrics Framework")
    
    print("\n   Baseline Metrics:")
    for metric, value in campaign.metrics.baseline_metrics.items():
        print(f"   • {metric}: {value:.1f}{'%' if 'rate' in metric else ''}")
    
    print("\n   Target Metrics:")
    for metric, value in campaign.metrics.target_metrics.items():
        print(f"   • {metric}: {value:.1f}{'%' if 'rate' in metric else ''}")
    
    print("\n   Measurement Methods:")
    for method in campaign.metrics.measurement_methods:
        print(f"   • {method}")
    
    print("\n   Success Criteria:")
    criteria = campaign.metrics.success_criteria
    print(f"   Primary: {criteria.get('primary', 'N/A')}")
    if 'secondary' in criteria:
        print("   Secondary:")
        for criterion in criteria['secondary'][:3]:
            print(f"   • {criterion}")
    
    # Generate sample certificate
    print("\n🏆 Training Certificate Example:")
    training_library = TrainingContentLibrary()
    cert = training_library.generate_certificate(
        "john.smith",
        ["phish_101", "password_mgmt", "incident_response_basics"]
    )
    
    print(f"   Certificate ID: {cert['certificate_id']}")
    print(f"   User: {cert['user']}")
    print(f"   Courses Completed: {len(cert['courses_completed'])}")
    print(f"   Total Training Time: {cert['total_duration_hours']} hours")
    print(f"   Skills Gained: {len(cert['skills_gained'])}")
    
    if cert['next_recommended']:
        print(f"   Next Recommended: {', '.join(cert['next_recommended'])}")


def example_scenario_planning():
    """
    Example: Planning scenarios with progression
    """
    print("\n" + "="*60)
    print("SCENARIO PLANNING EXAMPLE")
    print("="*60)
    
    scenario_library = SimulationScenarioLibrary()
    
    # Create a progressive campaign plan
    plan = scenario_library.create_campaign_plan(
        duration_weeks=6,
        target_groups=[TargetGroup.GENERAL_STAFF, TargetGroup.FINANCE, TargetGroup.HR],
        complexity_progression=True
    )
    
    print(f"\n📅 6-Week Progressive Campaign Plan")
    print(f"   Target Groups: {', '.join(plan['target_groups'])}")
    print(f"   Duration: {plan['duration_weeks']} weeks")
    
    for week_data in plan["schedule"]:
        print(f"\n   Week {week_data['week']}: {week_data['focus']}")
        for scenario in week_data["scenarios"]:
            print(f"     Day {scenario['day']:2d}: {scenario['name'][:40]:<40} [{scenario['complexity']}]")
    
    # Show detailed scenario brief
    print("\n" + "="*60)
    print("DETAILED SCENARIO BRIEF")
    print("="*60)
    
    # Get a specific scenario for detailed view
    brief = scenario_library.generate_scenario_brief("phish_spear_advanced")
    print(brief)


def example_safety_and_consent():
    """
    Example: Demonstrating safety and consent mechanisms
    """
    print("\n" + "="*60)
    print("SAFETY AND CONSENT MECHANISMS")
    print("="*60)
    
    from simulation_scenarios import ConsentMechanism
    
    # Create consent mechanism
    consent = ConsentMechanism(
        pre_campaign_notification=True,
        opt_in_required=False,
        opt_out_available=True,
        opt_out_methods=[
            "Reply to email with 'OPT-OUT'",
            "Click opt-out link in any simulation",
            "Call security team at x5555",
            "Use safe word: SECURITY-STOP-2024",
            "Submit opt-out form on intranet"
        ],
        safe_word="SECURITY-STOP-2024",
        excluded_individuals=["CEO", "CFO", "Employees on leave"],
        excluded_departments=["Legal", "Compliance"],
        time_restrictions={
            "business_hours": "9 AM - 5 PM only",
            "no_weekends": "True",
            "no_holidays": "True",
            "blackout_dates": ["2024-12-20 to 2025-01-05"]
        }
    )
    
    print("\n✅ Consent and Safety Framework")
    
    print("\n📋 Pre-Campaign Notification:")
    print(consent.notification_text)
    
    print("\n🛑 Opt-Out Methods Available:")
    for method in consent.opt_out_methods:
        print(f"   • {method}")
    
    print(f"\n🔐 Safe Word: {consent.safe_word}")
    print("   (Immediately stops any simulation when used)")
    
    print("\n🚫 Excluded from Simulations:")
    print(f"   Individuals: {', '.join(consent.excluded_individuals)}")
    print(f"   Departments: {', '.join(consent.excluded_departments)}")
    
    print("\n⏰ Time Restrictions:")
    for restriction, value in consent.time_restrictions.items():
        print(f"   • {restriction}: {value}")
    
    print("\n📝 Consent Form Template:")
    print(consent.consent_form_template)
    
    print("\n💡 Best Practices:")
    print("   • Always prioritize participant well-being")
    print("   • Make opt-out easy and judgment-free")
    print("   • Respect all boundaries and restrictions")
    print("   • Document consent and opt-outs properly")
    print("   • Provide support throughout the campaign")
    print("   • Focus on learning, not catching people")


def main():
    """
    Run all examples
    """
    print("""
╔══════════════════════════════════════════════════════════════╗
║     SOCIAL ENGINEERING STRATEGIST - ETHICAL USAGE EXAMPLES    ║
║                                                                ║
║  This toolkit is designed for ETHICAL security awareness      ║
║  training with clear consent boundaries and safety measures.  ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Run examples
    example_complete_campaign()
    example_phishing_only_campaign()
    example_executive_campaign()
    example_incident_response_training()
    example_metrics_and_reporting()
    example_scenario_planning()
    example_safety_and_consent()
    
    print("\n" + "="*60)
    print("EXAMPLES COMPLETE")
    print("="*60)
    print("""
Remember: The goal of security awareness is to educate and protect,
not to trick or embarrass. Always prioritize:

  • Clear consent and opt-out mechanisms
  • Participant well-being and dignity
  • Learning over catching mistakes
  • Blameless culture
  • Data protection and privacy
  • Compliance with laws and regulations

Use this toolkit responsibly to build a stronger security culture!
    """)


if __name__ == "__main__":
    main()
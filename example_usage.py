#!/usr/bin/env python3
"""
Comprehensive Example Usage of the Social Engineering Strategist System

This file demonstrates how to use all components of the system together
to create a complete security awareness campaign.
"""

import datetime
from social_engineering_strategist import (
    SocialEngineeringStrategist, 
    CampaignInputs, 
    Channel, 
    RulesOfEngagement
)
from safety_guardrails import SafetyGuardrails, SafetyLevel
from success_metrics import SuccessMetricsFramework
from debrief_materials import DebriefMaterialsGenerator, DebriefType, LearningLevel
from training_module_templates import TrainingModuleTemplates
from simulation_scenarios import SimulationScenarioLibrary, DifficultyLevel


def example_basic_campaign():
    """Example 1: Basic Phishing Awareness Campaign"""
    print("=== EXAMPLE 1: BASIC PHISHING AWARENESS CAMPAIGN ===")
    
    # Initialize the strategist
    strategist = SocialEngineeringStrategist()
    
    # Define campaign inputs
    inputs = CampaignInputs(
        objective="Improve phishing awareness among all employees",
        audience="all employees",
        channels=[Channel.EMAIL],
        rules_of_engagement=[RulesOfEngagement.CONSENT, RulesOfEngagement.OPT_OUT],
        department="Company-wide",
        role="Employee"
    )
    
    # Create the campaign
    campaign = strategist.create_campaign(inputs)
    
    print(f"Campaign ID: {campaign['id']}")
    print(f"Objective: {campaign['inputs']['objective']}")
    print(f"Training Modules: {len(campaign['training_modules'])}")
    print(f"Simulation Scenarios: {len(campaign['simulation_scenarios'])}")
    print(f"Safety Compliance: {campaign['safety_compliance']['approval_status']}")
    
    return campaign


def example_advanced_campaign():
    """Example 2: Advanced Multi-Channel Security Awareness Program"""
    print("\n=== EXAMPLE 2: ADVANCED MULTI-CHANNEL CAMPAIGN ===")
    
    # Initialize the strategist
    strategist = SocialEngineeringStrategist()
    
    # Define comprehensive campaign inputs
    inputs = CampaignInputs(
        objective="Comprehensive security awareness program for IT department",
        audience="IT department staff",
        channels=[Channel.EMAIL, Channel.CHAT, Channel.PHONE, Channel.IN_PERSON],
        rules_of_engagement=[RulesOfEngagement.CONSENT, RulesOfEngagement.NO_HARM, RulesOfEngagement.OPT_OUT],
        department="Information Technology",
        role="System Administrator"
    )
    
    # Create the campaign
    campaign = strategist.create_campaign(inputs)
    
    print(f"Campaign ID: {campaign['id']}")
    print(f"Audience: {campaign['inputs']['audience']}")
    print(f"Channels: {[ch.value for ch in campaign['inputs']['channels']]}")
    print(f"Training Modules: {len(campaign['training_modules'])}")
    print(f"Simulation Scenarios: {len(campaign['simulation_scenarios'])}")
    
    # Display training module details
    print("\nTraining Modules:")
    for i, module in enumerate(campaign['training_modules'], 1):
        print(f"  {i}. {module['title']} ({module['duration_minutes']} minutes)")
        print(f"     Audience Level: {module['audience_level']}")
        print(f"     Learning Objectives: {len(module['learning_objectives'])}")
    
    # Display simulation scenario details
    print("\nSimulation Scenarios:")
    for i, scenario in enumerate(campaign['simulation_scenarios'], 1):
        print(f"  {i}. {scenario['name']}")
        print(f"     Channel: {scenario['channel'].value}")
        print(f"     Difficulty: {scenario['difficulty_level']}")
        print(f"     Duration: {scenario['estimated_duration_minutes']} minutes")
    
    return campaign


def example_safety_controlled_campaign():
    """Example 3: Safety-First Campaign with Comprehensive Controls"""
    print("\n=== EXAMPLE 3: SAFETY-FIRST CAMPAIGN ===")
    
    # Initialize all systems
    strategist = SocialEngineeringStrategist()
    guardrails = SafetyGuardrails()
    metrics = SuccessMetricsFramework()
    debrief_generator = DebriefMaterialsGenerator()
    
    # Create campaign
    campaign_id = "safety_campaign_001"
    inputs = CampaignInputs(
        objective="High-security awareness campaign for executive team",
        audience="executive team",
        channels=[Channel.EMAIL, Channel.PHONE],
        rules_of_engagement=[RulesOfEngagement.CONSENT, RulesOfEngagement.NO_HARM, RulesOfEngagement.OPT_OUT],
        department="Executive",
        role="C-Level Executive"
    )
    
    campaign = strategist.create_campaign(inputs)
    
    # Set up safety controls
    print("Setting up safety controls...")
    
    # Request consent for participants
    participants = ["CEO", "CTO", "CFO", "CISO"]
    consent_records = []
    
    for participant in participants:
        consent_id = guardrails.request_consent(
            participant_id=f"exec_{participant.lower()}",
            participant_name=participant,
            campaign_id=campaign_id,
            consent_type="executive_simulation",
            consent_method="in_person"
        )
        guardrails.grant_consent(consent_id, witness="Security Team Lead")
        consent_records.append(consent_id)
    
    print(f"Consent records created: {len(consent_records)}")
    
    # Conduct safety assessment
    assessment = guardrails.conduct_safety_assessment(
        campaign_id=campaign_id,
        activity_type="executive_simulation",
        risk_factors=["high_authority_impersonation", "sensitive_data_involved", "phone_communications"]
    )
    
    print(f"Safety Assessment ID: {assessment.assessment_id}")
    print(f"Safety Level: {assessment.safety_level.value}")
    print(f"Approval Required: {assessment.approval_required}")
    print(f"Mitigation Measures: {len(assessment.mitigation_measures)}")
    
    # Set up metrics tracking
    campaign_metrics = metrics.create_campaign_metrics(
        campaign_id=campaign_id,
        campaign_name="Executive Security Awareness Campaign",
        start_date=datetime.datetime.now()
    )
    
    print(f"Metrics tracking initialized for campaign: {campaign_metrics.campaign_id}")
    
    # Add baseline measurements
    metrics.add_measurement(
        campaign_id=campaign_id,
        metric_name="phishing_recognition_rate",
        value=60.0,  # Baseline
        measurement_date=datetime.datetime.now(),
        confidence_level=0.95,
        sample_size=4,
        notes="Pre-campaign baseline measurement"
    )
    
    metrics.add_measurement(
        campaign_id=campaign_id,
        metric_name="social_engineering_awareness_score",
        value=70.0,  # Baseline
        measurement_date=datetime.datetime.now(),
        confidence_level=0.90,
        sample_size=4,
        notes="Pre-campaign awareness assessment"
    )
    
    # Validate campaign safety
    safety_validation = guardrails.validate_campaign_safety(campaign_id)
    print(f"Campaign Safety Valid: {safety_validation['is_safe']}")
    print(f"Risk Level: {safety_validation['risk_level'].value}")
    print(f"Safety Issues: {len(safety_validation['safety_issues'])}")
    
    if safety_validation['recommendations']:
        print("Recommendations:")
        for rec in safety_validation['recommendations']:
            print(f"  - {rec}")
    
    return campaign, guardrails, metrics, debrief_generator


def example_training_modules():
    """Example 4: Working with Training Module Templates"""
    print("\n=== EXAMPLE 4: TRAINING MODULE TEMPLATES ===")
    
    templates = TrainingModuleTemplates()
    
    # Get all available templates
    all_templates = templates.get_all_templates()
    print(f"Available Templates: {len(all_templates)}")
    
    for name, template in all_templates.items():
        print(f"\n{template.name}:")
        print(f"  Type: {template.module_type.value}")
        print(f"  Audience Levels: {', '.join(template.audience_levels)}")
        print(f"  Duration: {template.duration_minutes} minutes")
        print(f"  Learning Objectives: {len(template.learning_objectives)}")
    
    # Get templates for specific audience level
    print("\nTemplates for Beginner Audience:")
    beginner_templates = templates.get_template_by_audience("beginner")
    for template in beginner_templates:
        print(f"  - {template.name}")
    
    # Get templates for intermediate audience
    print("\nTemplates for Intermediate Audience:")
    intermediate_templates = templates.get_template_by_audience("intermediate")
    for template in intermediate_templates:
        print(f"  - {template.name}")


def example_simulation_scenarios():
    """Example 5: Working with Simulation Scenarios"""
    print("\n=== EXAMPLE 5: SIMULATION SCENARIOS ===")
    
    library = SimulationScenarioLibrary()
    
    # Get all available scenarios
    all_scenarios = library.get_all_scenarios()
    print(f"Available Scenarios: {len(all_scenarios)}")
    
    for name, scenario in all_scenarios.items():
        print(f"\n{scenario.name}:")
        print(f"  Type: {scenario.scenario_type.value}")
        print(f"  Difficulty: {scenario.difficulty_level.value}")
        print(f"  Duration: {scenario.estimated_duration_minutes} minutes")
        print(f"  Learning Objectives: {len(scenario.learning_objectives)}")
        print(f"  Safety Considerations: {len(scenario.safety_considerations)}")
    
    # Get scenarios by difficulty level
    print("\nHigh Difficulty Scenarios:")
    high_difficulty = library.get_scenarios_by_difficulty(DifficultyLevel.HIGH)
    for scenario in high_difficulty:
        print(f"  - {scenario.name}")
    
    # Get scenarios by type
    print("\nPhishing Scenarios:")
    phishing_scenarios = library.get_scenarios_by_type(scenario.scenario_type.PHISHING)
    for scenario in phishing_scenarios:
        print(f"  - {scenario.name}")


def example_metrics_tracking():
    """Example 6: Comprehensive Metrics Tracking"""
    print("\n=== EXAMPLE 6: METRICS TRACKING ===")
    
    metrics = SuccessMetricsFramework()
    
    # Create campaign metrics
    campaign_id = "metrics_example_001"
    campaign_metrics = metrics.create_campaign_metrics(
        campaign_id=campaign_id,
        campaign_name="Metrics Example Campaign",
        start_date=datetime.datetime.now()
    )
    
    print(f"Created metrics for campaign: {campaign_metrics.campaign_id}")
    
    # Add various measurements over time
    measurement_dates = [
        datetime.datetime.now() - datetime.timedelta(days=30),  # 30 days ago
        datetime.datetime.now() - datetime.timedelta(days=15),  # 15 days ago
        datetime.datetime.now()  # Now
    ]
    
    # Simulate phishing recognition rate improvement
    phishing_rates = [45.0, 65.0, 80.0]
    for date, rate in zip(measurement_dates, phishing_rates):
        metrics.add_measurement(
            campaign_id=campaign_id,
            metric_name="phishing_recognition_rate",
            value=rate,
            measurement_date=date,
            confidence_level=0.95,
            sample_size=100,
            notes=f"Monthly measurement - {date.strftime('%Y-%m-%d')}"
        )
    
    # Simulate training completion rate
    completion_rates = [0.0, 75.0, 95.0]
    for date, rate in zip(measurement_dates, completion_rates):
        metrics.add_measurement(
            campaign_id=campaign_id,
            metric_name="training_completion_rate",
            value=rate,
            measurement_date=date,
            confidence_level=1.0,
            sample_size=150,
            notes=f"Training completion tracking - {date.strftime('%Y-%m-%d')}"
        )
    
    # Calculate progress
    progress = metrics.calculate_campaign_progress(campaign_id)
    
    print(f"\nCampaign Progress: {progress['overall_progress']:.1f}%")
    print(f"Recommendations: {len(progress['recommendations'])}")
    
    # Display metric progress
    print("\nMetric Progress:")
    for metric_name, data in progress['metric_progress'].items():
        print(f"  {metric_name}:")
        print(f"    Current: {data['current_value']:.1f}")
        print(f"    Target: {data['target_value']:.1f}")
        print(f"    Progress: {data['progress_percentage']:.1f}%")
        print(f"    Status: {data['status']}")
    
    # Generate comprehensive report
    report = metrics.generate_metrics_report(campaign_id)
    print(f"\nGenerated comprehensive report ({len(report)} characters)")
    
    # Get trend data
    trends = metrics.get_metric_trends(campaign_id, "phishing_recognition_rate")
    print(f"\nPhishing Recognition Rate Trends: {len(trends)} data points")
    for trend in trends:
        print(f"  {trend['date']}: {trend['value']:.1f}%")


def example_debrief_sessions():
    """Example 7: Debrief Session Management"""
    print("\n=== EXAMPLE 7: DEBRIEF SESSION MANAGEMENT ===")
    
    generator = DebriefMaterialsGenerator()
    
    # Create a debrief session
    session = generator.create_debrief_session(
        scenario_id="phishing_sim_001",
        participants=["Alice", "Bob", "Charlie", "Diana"],
        debrief_type=DebriefType.GROUP,
        learning_level=LearningLevel.BEGINNER,
        facilitator="Security Team Lead"
    )
    
    print(f"Created debrief session: {session.id}")
    print(f"Participants: {len(session.participants)}")
    print(f"Duration: {session.duration_minutes} minutes")
    print(f"Facilitator: {session.facilitator}")
    
    # Generate debrief materials
    materials = generator.generate_debrief_materials(session.id)
    
    print(f"\nDebrief Materials Generated:")
    print(f"  Agenda Items: {len(materials['agenda'])}")
    print(f"  Discussion Questions: {len(materials['discussion_questions'])}")
    print(f"  Learning Outcomes: {len(materials['learning_outcomes'])}")
    print(f"  Action Items: {len(materials['action_items'])}")
    print(f"  Materials Needed: {len(materials['materials_needed'])}")
    
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
    print(f"\nFollow-up Plan Generated:")
    print(f"  Action Items: {len(follow_up['action_items'])}")
    print(f"  Key Learnings: {len(follow_up['key_learnings'])}")
    print(f"  Next Steps: {len(follow_up['next_steps'])}")
    
    # Get session summary
    summary = generator.get_session_summary(session.id)
    print(f"\nSession Summary:")
    print(f"  Type: {summary['type']}")
    print(f"  Learning Level: {summary['learning_level']}")
    print(f"  Participants: {summary['participants_count']}")
    print(f"  Key Learnings: {summary['key_learnings_count']}")
    print(f"  Action Items: {summary['action_items_count']}")


def example_complete_workflow():
    """Example 8: Complete End-to-End Workflow"""
    print("\n=== EXAMPLE 8: COMPLETE END-TO-END WORKFLOW ===")
    
    # Initialize all systems
    strategist = SocialEngineeringStrategist()
    guardrails = SafetyGuardrails()
    metrics = SuccessMetricsFramework()
    debrief_generator = DebriefMaterialsGenerator()
    
    # Step 1: Create Campaign
    print("Step 1: Creating Campaign...")
    campaign_id = "complete_workflow_001"
    inputs = CampaignInputs(
        objective="Complete security awareness program for customer service team",
        audience="customer service representatives",
        channels=[Channel.EMAIL, Channel.CHAT, Channel.PHONE],
        rules_of_engagement=[RulesOfEngagement.CONSENT, RulesOfEngagement.NO_HARM, RulesOfEngagement.OPT_OUT],
        department="Customer Service",
        role="Representative"
    )
    
    campaign = strategist.create_campaign(inputs)
    print(f"  Campaign created: {campaign['id']}")
    
    # Step 2: Set up Safety Controls
    print("\nStep 2: Setting up Safety Controls...")
    participants = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    consent_records = []
    
    for participant in participants:
        consent_id = guardrails.request_consent(
            participant_id=f"cs_{participant.lower()}",
            participant_name=participant,
            campaign_id=campaign_id,
            consent_type="comprehensive_simulation"
        )
        guardrails.grant_consent(consent_id)
        consent_records.append(consent_id)
    
    print(f"  Consent records created: {len(consent_records)}")
    
    # Step 3: Conduct Safety Assessment
    print("\nStep 3: Conducting Safety Assessment...")
    assessment = guardrails.conduct_safety_assessment(
        campaign_id=campaign_id,
        activity_type="comprehensive_simulation",
        risk_factors=["email_simulations", "phone_communications", "data_collection"]
    )
    
    print(f"  Safety Level: {assessment.safety_level.value}")
    print(f"  Mitigation Measures: {len(assessment.mitigation_measures)}")
    
    # Step 4: Set up Metrics Tracking
    print("\nStep 4: Setting up Metrics Tracking...")
    campaign_metrics = metrics.create_campaign_metrics(
        campaign_id=campaign_id,
        campaign_name="Complete Workflow Campaign",
        start_date=datetime.datetime.now()
    )
    
    # Add baseline measurements
    metrics.add_measurement(
        campaign_id=campaign_id,
        metric_name="phishing_recognition_rate",
        value=50.0,
        measurement_date=datetime.datetime.now(),
        confidence_level=0.95,
        sample_size=5,
        notes="Pre-campaign baseline"
    )
    
    print(f"  Metrics tracking initialized")
    
    # Step 5: Conduct Training
    print("\nStep 5: Conducting Training...")
    print(f"  Training modules available: {len(campaign['training_modules'])}")
    for module in campaign['training_modules']:
        print(f"    - {module['title']} ({module['duration_minutes']} minutes)")
    
    # Step 6: Run Simulations
    print("\nStep 6: Running Simulations...")
    print(f"  Simulation scenarios available: {len(campaign['simulation_scenarios'])}")
    for scenario in campaign['simulation_scenarios']:
        print(f"    - {scenario['name']} ({scenario['channel'].value})")
    
    # Step 7: Conduct Debrief Sessions
    print("\nStep 7: Conducting Debrief Sessions...")
    debrief_session = debrief_generator.create_debrief_session(
        scenario_id="phishing_sim_001",
        participants=participants,
        debrief_type=DebriefType.GROUP,
        learning_level=LearningLevel.BEGINNER,
        facilitator="Security Team Lead"
    )
    
    print(f"  Debrief session created: {debrief_session.id}")
    
    # Step 8: Complete Session and Generate Follow-up
    print("\nStep 8: Completing Session and Generating Follow-up...")
    debrief_generator.complete_session(
        session_id=debrief_session.id,
        key_learnings=[
            "Participants improved phishing recognition skills",
            "Verification procedures were reinforced",
            "Confidence in reporting increased"
        ],
        action_items=[
            "Review email security policies",
            "Practice verification procedures",
            "Report suspicious activity"
        ],
        notes="Successful debrief session with good participation"
    )
    
    follow_up = debrief_generator.generate_follow_up_plan(debrief_session.id)
    print(f"  Follow-up plan generated with {len(follow_up['action_items'])} action items")
    
    # Step 9: Add Post-Campaign Measurements
    print("\nStep 9: Adding Post-Campaign Measurements...")
    metrics.add_measurement(
        campaign_id=campaign_id,
        metric_name="phishing_recognition_rate",
        value=85.0,
        measurement_date=datetime.datetime.now(),
        confidence_level=0.95,
        sample_size=5,
        notes="Post-campaign measurement"
    )
    
    metrics.add_measurement(
        campaign_id=campaign_id,
        metric_name="training_completion_rate",
        value=100.0,
        measurement_date=datetime.datetime.now(),
        confidence_level=1.0,
        sample_size=5,
        notes="Training completion achieved"
    )
    
    # Step 10: Generate Final Report
    print("\nStep 10: Generating Final Report...")
    progress = metrics.calculate_campaign_progress(campaign_id)
    print(f"  Overall Progress: {progress['overall_progress']:.1f}%")
    print(f"  Recommendations: {len(progress['recommendations'])}")
    
    safety_report = guardrails.export_safety_report(campaign_id)
    print(f"  Safety Report: {safety_report['safety_validation']['is_safe']}")
    
    print("\n=== COMPLETE WORKFLOW FINISHED ===")
    print("All systems working together successfully!")


def main():
    """Run all examples"""
    print("SOCIAL ENGINEERING STRATEGIST - COMPREHENSIVE EXAMPLES")
    print("=" * 60)
    
    # Run all examples
    example_basic_campaign()
    example_advanced_campaign()
    example_safety_controlled_campaign()
    example_training_modules()
    example_simulation_scenarios()
    example_metrics_tracking()
    example_debrief_sessions()
    example_complete_workflow()
    
    print("\n" + "=" * 60)
    print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
    print("The Social Engineering Strategist system is ready for use.")


if __name__ == "__main__":
    main()
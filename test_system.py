#!/usr/bin/env python3
"""
Test Script for Social Engineering Strategist System

This script tests all components of the system to ensure they work correctly.
"""

import sys
import traceback
from datetime import datetime

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    
    try:
        from social_engineering_strategist import SocialEngineeringStrategist, CampaignInputs, Channel, RulesOfEngagement
        print("✓ Main strategist module imported successfully")
    except Exception as e:
        print(f"✗ Failed to import main strategist: {e}")
        return False
    
    try:
        from safety_guardrails import SafetyGuardrails
        print("✓ Safety guardrails module imported successfully")
    except Exception as e:
        print(f"✗ Failed to import safety guardrails: {e}")
        return False
    
    try:
        from success_metrics import SuccessMetricsFramework
        print("✓ Success metrics module imported successfully")
    except Exception as e:
        print(f"✗ Failed to import success metrics: {e}")
        return False
    
    try:
        from debrief_materials import DebriefMaterialsGenerator, DebriefType, LearningLevel
        print("✓ Debrief materials module imported successfully")
    except Exception as e:
        print(f"✗ Failed to import debrief materials: {e}")
        return False
    
    try:
        from training_module_templates import TrainingModuleTemplates
        print("✓ Training module templates imported successfully")
    except Exception as e:
        print(f"✗ Failed to import training module templates: {e}")
        return False
    
    try:
        from simulation_scenarios import SimulationScenarioLibrary, DifficultyLevel
        print("✓ Simulation scenarios module imported successfully")
    except Exception as e:
        print(f"✗ Failed to import simulation scenarios: {e}")
        return False
    
    return True


def test_basic_campaign_creation():
    """Test basic campaign creation"""
    print("\nTesting basic campaign creation...")
    
    try:
        from social_engineering_strategist import SocialEngineeringStrategist, CampaignInputs, Channel, RulesOfEngagement
        
        strategist = SocialEngineeringStrategist()
        
        inputs = CampaignInputs(
            objective="Test campaign for system validation",
            audience="test users",
            channels=[Channel.EMAIL],
            rules_of_engagement=[RulesOfEngagement.CONSENT, RulesOfEngagement.OPT_OUT]
        )
        
        campaign = strategist.create_campaign(inputs)
        
        if campaign and 'id' in campaign:
            print("✓ Basic campaign created successfully")
            print(f"  Campaign ID: {campaign['id']}")
            print(f"  Training Modules: {len(campaign['training_modules'])}")
            print(f"  Simulation Scenarios: {len(campaign['simulation_scenarios'])}")
            return True
        else:
            print("✗ Campaign creation failed - invalid response")
            return False
            
    except Exception as e:
        print(f"✗ Campaign creation failed: {e}")
        traceback.print_exc()
        return False


def test_safety_guardrails():
    """Test safety guardrails functionality"""
    print("\nTesting safety guardrails...")
    
    try:
        from safety_guardrails import SafetyGuardrails
        
        guardrails = SafetyGuardrails()
        
        # Test consent management
        consent_id = guardrails.request_consent(
            participant_id="test_user_001",
            participant_name="Test User",
            campaign_id="test_campaign_001",
            consent_type="test_simulation"
        )
        
        if consent_id:
            print("✓ Consent request created successfully")
        else:
            print("✗ Consent request failed")
            return False
        
        # Test consent granting
        success = guardrails.grant_consent(consent_id)
        if success:
            print("✓ Consent granted successfully")
        else:
            print("✗ Consent granting failed")
            return False
        
        # Test safety assessment
        assessment = guardrails.conduct_safety_assessment(
            campaign_id="test_campaign_001",
            activity_type="test_simulation",
            risk_factors=["email_simulations"]
        )
        
        if assessment and assessment.assessment_id:
            print("✓ Safety assessment conducted successfully")
            print(f"  Safety Level: {assessment.safety_level.value}")
            print(f"  Mitigation Measures: {len(assessment.mitigation_measures)}")
        else:
            print("✗ Safety assessment failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Safety guardrails test failed: {e}")
        traceback.print_exc()
        return False


def test_metrics_framework():
    """Test success metrics framework"""
    print("\nTesting success metrics framework...")
    
    try:
        from success_metrics import SuccessMetricsFramework
        
        metrics = SuccessMetricsFramework()
        
        # Create campaign metrics
        campaign_metrics = metrics.create_campaign_metrics(
            campaign_id="test_metrics_001",
            campaign_name="Test Metrics Campaign",
            start_date=datetime.now()
        )
        
        if campaign_metrics and campaign_metrics.campaign_id:
            print("✓ Campaign metrics created successfully")
        else:
            print("✗ Campaign metrics creation failed")
            return False
        
        # Add measurement
        metrics.add_measurement(
            campaign_id="test_metrics_001",
            metric_name="phishing_recognition_rate",
            value=75.0,
            measurement_date=datetime.now(),
            confidence_level=0.95,
            sample_size=10
        )
        
        print("✓ Measurement added successfully")
        
        # Calculate progress
        progress = metrics.calculate_campaign_progress("test_metrics_001")
        
        if progress and 'overall_progress' in progress:
            print("✓ Progress calculation successful")
            print(f"  Overall Progress: {progress['overall_progress']:.1f}%")
        else:
            print("✗ Progress calculation failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Metrics framework test failed: {e}")
        traceback.print_exc()
        return False


def test_debrief_materials():
    """Test debrief materials generator"""
    print("\nTesting debrief materials generator...")
    
    try:
        from debrief_materials import DebriefMaterialsGenerator, DebriefType, LearningLevel
        
        generator = DebriefMaterialsGenerator()
        
        # Create debrief session
        session = generator.create_debrief_session(
            scenario_id="test_scenario_001",
            participants=["Alice", "Bob"],
            debrief_type=DebriefType.GROUP,
            learning_level=LearningLevel.BEGINNER,
            facilitator="Test Facilitator"
        )
        
        if session and session.id:
            print("✓ Debrief session created successfully")
        else:
            print("✗ Debrief session creation failed")
            return False
        
        # Generate materials
        materials = generator.generate_debrief_materials(session.id)
        
        if materials and 'agenda' in materials:
            print("✓ Debrief materials generated successfully")
            print(f"  Agenda Items: {len(materials['agenda'])}")
            print(f"  Discussion Questions: {len(materials['discussion_questions'])}")
        else:
            print("✗ Debrief materials generation failed")
            return False
        
        # Complete session
        generator.complete_session(
            session_id=session.id,
            key_learnings=["Test learning 1", "Test learning 2"],
            action_items=["Test action 1", "Test action 2"],
            notes="Test session completed successfully"
        )
        
        print("✓ Session completed successfully")
        
        return True
        
    except Exception as e:
        print(f"✗ Debrief materials test failed: {e}")
        traceback.print_exc()
        return False


def test_training_templates():
    """Test training module templates"""
    print("\nTesting training module templates...")
    
    try:
        from training_module_templates import TrainingModuleTemplates
        
        templates = TrainingModuleTemplates()
        
        # Get all templates
        all_templates = templates.get_all_templates()
        
        if all_templates and len(all_templates) > 0:
            print("✓ Training templates loaded successfully")
            print(f"  Available Templates: {len(all_templates)}")
        else:
            print("✗ Training templates loading failed")
            return False
        
        # Get templates by audience
        beginner_templates = templates.get_template_by_audience("beginner")
        
        if beginner_templates and len(beginner_templates) > 0:
            print("✓ Beginner templates retrieved successfully")
            print(f"  Beginner Templates: {len(beginner_templates)}")
        else:
            print("✗ Beginner templates retrieval failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Training templates test failed: {e}")
        traceback.print_exc()
        return False


def test_simulation_scenarios():
    """Test simulation scenarios library"""
    print("\nTesting simulation scenarios library...")
    
    try:
        from simulation_scenarios import SimulationScenarioLibrary, DifficultyLevel
        
        library = SimulationScenarioLibrary()
        
        # Get all scenarios
        all_scenarios = library.get_all_scenarios()
        
        if all_scenarios and len(all_scenarios) > 0:
            print("✓ Simulation scenarios loaded successfully")
            print(f"  Available Scenarios: {len(all_scenarios)}")
        else:
            print("✗ Simulation scenarios loading failed")
            return False
        
        # Get scenarios by difficulty
        high_difficulty = library.get_scenarios_by_difficulty(DifficultyLevel.HIGH)
        
        if high_difficulty is not None:
            print("✓ Difficulty-based scenario retrieval successful")
            print(f"  High Difficulty Scenarios: {len(high_difficulty)}")
        else:
            print("✗ Difficulty-based scenario retrieval failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Simulation scenarios test failed: {e}")
        traceback.print_exc()
        return False


def test_integration():
    """Test integration between components"""
    print("\nTesting component integration...")
    
    try:
        from social_engineering_strategist import SocialEngineeringStrategist, CampaignInputs, Channel, RulesOfEngagement
        from safety_guardrails import SafetyGuardrails
        from success_metrics import SuccessMetricsFramework
        
        # Create campaign
        strategist = SocialEngineeringStrategist()
        inputs = CampaignInputs(
            objective="Integration test campaign",
            audience="test users",
            channels=[Channel.EMAIL],
            rules_of_engagement=[RulesOfEngagement.CONSENT, RulesOfEngagement.OPT_OUT]
        )
        campaign = strategist.create_campaign(inputs)
        
        # Set up safety controls
        guardrails = SafetyGuardrails()
        consent_id = guardrails.request_consent(
            participant_id="integration_test_user",
            participant_name="Integration Test User",
            campaign_id=campaign['id'],
            consent_type="integration_test"
        )
        guardrails.grant_consent(consent_id)
        
        # Set up metrics
        metrics = SuccessMetricsFramework()
        campaign_metrics = metrics.create_campaign_metrics(
            campaign_id=campaign['id'],
            campaign_name="Integration Test Campaign",
            start_date=datetime.now()
        )
        
        # Validate safety
        safety_validation = guardrails.validate_campaign_safety(campaign['id'])
        
        if (campaign and safety_validation and campaign_metrics):
            print("✓ Component integration successful")
            print(f"  Campaign ID: {campaign['id']}")
            print(f"  Safety Valid: {safety_validation['is_safe']}")
            print(f"  Metrics Campaign ID: {campaign_metrics.campaign_id}")
        else:
            print("✗ Component integration failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Integration test failed: {e}")
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("SOCIAL ENGINEERING STRATEGIST - SYSTEM TEST")
    print("=" * 50)
    
    tests = [
        ("Import Tests", test_imports),
        ("Basic Campaign Creation", test_basic_campaign_creation),
        ("Safety Guardrails", test_safety_guardrails),
        ("Metrics Framework", test_metrics_framework),
        ("Debrief Materials", test_debrief_materials),
        ("Training Templates", test_training_templates),
        ("Simulation Scenarios", test_simulation_scenarios),
        ("Component Integration", test_integration)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            if test_func():
                passed += 1
                print(f"✓ {test_name} PASSED")
            else:
                print(f"✗ {test_name} FAILED")
        except Exception as e:
            print(f"✗ {test_name} FAILED with exception: {e}")
    
    print(f"\n{'='*50}")
    print(f"TEST RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! System is ready for use.")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
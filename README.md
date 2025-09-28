# Social Engineering Strategist Toolkit

Ethical security awareness campaign planning toolkit with consent boundaries and safety mechanisms.

## Purpose
Plan ethical awareness campaigns and simulations to improve organizational security posture through education.

## Components

- **social_engineering_strategist.py** - Main campaign management
- **training_content.py** - Training material library  
- **simulation_scenarios.py** - Simulation templates with safety features
- **example_usage.py** - Usage examples and best practices

## Key Features

- Explicit consent mechanisms
- Clear opt-out procedures  
- Safety guardrails and safe words
- Comprehensive training modules
- Metrics tracking and reporting
- Debrief materials

## Quick Start

```python
from social_engineering_strategist import SocialEngineeringStrategist, RulesOfEngagement

strategist = SocialEngineeringStrategist()
rules = RulesOfEngagement(
    explicit_consent=True,
    opt_out_available=True
)

campaign = strategist.create_campaign(
    objective="Improve security awareness",
    audience={"department": "Finance", "size": 50},
    channels=[Channel.EMAIL],
    rules=rules
)
```

## Ethical Use Only

- Authorized testing only
- Respect opt-outs immediately
- Focus on education, not catching
- Protect participant data
- Follow all laws and regulations

See example_usage.py for detailed examples.
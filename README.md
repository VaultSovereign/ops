# Social Engineering Strategist

A comprehensive tool for planning ethical awareness campaigns and simulations with clear consent boundaries.

## Purpose

The Social Engineering Strategist helps organizations:
- Plan ethical security awareness campaigns
- Create educational simulation scenarios
- Implement proper consent and opt-out mechanisms
- Measure campaign effectiveness
- Ensure compliance with safety and ethical guidelines

## Quick Start

```python
from social_engineering_strategist import SocialEngineeringStrategist, CampaignInputs, Channel, RulesOfEngagement

# Initialize the strategist
strategist = SocialEngineeringStrategist()

# Define campaign inputs
inputs = CampaignInputs(
    objective="Improve phishing awareness among customer service team",
    audience="customer service representatives",
    channels=[Channel.EMAIL, Channel.CHAT, Channel.PHONE],
    rules_of_engagement=[RulesOfEngagement.CONSENT, RulesOfEngagement.NO_HARM, RulesOfEngagement.OPT_OUT]
)

# Create the campaign
campaign = strategist.create_campaign(inputs)
```

## Features

- **Campaign Planning**: Input validation and audience assessment
- **Training Modules**: Audience-specific content with opt-out mechanisms
- **Simulation Scenarios**: Pre-built scenarios with safety controls
- **Success Metrics**: Comprehensive tracking and measurement
- **Debrief Materials**: Structured post-simulation discussions
- **Safety Guardrails**: Consent management and risk assessment

## Safety and Ethics

- Explicit consent required for all activities
- Clear opt-out mechanisms provided
- No actual harm or damage to participants
- Educational focus only
- Privacy protection and data anonymization

## Installation

No external dependencies required. Uses only Python standard library.

```bash
python social_engineering_strategist.py
```

## Usage Examples

See individual module files for detailed examples and documentation.
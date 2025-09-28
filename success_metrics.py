#!/usr/bin/env python3
"""
Success Metrics and Measurement Framework for Social Engineering Awareness Campaigns

This module provides comprehensive metrics tracking and measurement capabilities for
social engineering awareness training and simulation campaigns.
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
import datetime
import json
import statistics
from collections import defaultdict


class MetricType(Enum):
    AWARENESS = "awareness"
    BEHAVIOR = "behavior"
    INCIDENT = "incident"
    TRAINING = "training"
    CULTURE = "culture"


class MeasurementMethod(Enum):
    ASSESSMENT = "assessment"
    SIMULATION = "simulation"
    SURVEY = "survey"
    OBSERVATION = "observation"
    INCIDENT_DATA = "incident_data"
    BEHAVIORAL_ANALYTICS = "behavioral_analytics"


@dataclass
class MetricDefinition:
    """Definition of a specific metric to be measured"""
    name: str
    description: str
    metric_type: MetricType
    measurement_method: MeasurementMethod
    baseline_value: float
    target_value: float
    unit: str
    frequency: str  # daily, weekly, monthly, quarterly
    data_source: str
    calculation_method: str
    success_threshold: float
    weight: float = 1.0  # Weight for composite scoring


@dataclass
class MeasurementResult:
    """Result of a specific metric measurement"""
    metric_name: str
    value: float
    measurement_date: datetime.datetime
    confidence_level: float
    sample_size: int
    notes: str = ""


@dataclass
class CampaignMetrics:
    """Complete metrics package for a social engineering awareness campaign"""
    campaign_id: str
    campaign_name: str
    start_date: datetime.datetime
    end_date: Optional[datetime.datetime]
    metrics: Dict[str, MetricDefinition]
    measurements: List[MeasurementResult]
    composite_score: float = 0.0
    overall_success: bool = False
    recommendations: List[str] = field(default_factory=list)


class SuccessMetricsFramework:
    """
    Comprehensive framework for measuring social engineering awareness campaign success.
    
    This framework provides:
    - Pre-defined metrics for different campaign types
    - Measurement collection and analysis
    - Progress tracking and reporting
    - Success determination and recommendations
    """
    
    def __init__(self):
        self.campaigns = {}
        self.metric_definitions = self._initialize_metric_definitions()
    
    def _initialize_metric_definitions(self) -> Dict[str, MetricDefinition]:
        """Initialize standard metric definitions for social engineering awareness campaigns"""
        return {
            # Awareness Metrics
            "phishing_recognition_rate": MetricDefinition(
                name="Phishing Recognition Rate",
                description="Percentage of participants who correctly identify phishing attempts",
                metric_type=MetricType.AWARENESS,
                measurement_method=MeasurementMethod.ASSESSMENT,
                baseline_value=0.0,
                target_value=85.0,
                unit="percentage",
                frequency="monthly",
                data_source="Pre/post training assessments",
                calculation_method="(Correct identifications / Total attempts) * 100",
                success_threshold=80.0,
                weight=1.2
            ),
            
            "social_engineering_awareness_score": MetricDefinition(
                name="Social Engineering Awareness Score",
                description="Overall awareness score from comprehensive assessment",
                metric_type=MetricType.AWARENESS,
                measurement_method=MeasurementMethod.ASSESSMENT,
                baseline_value=0.0,
                target_value=80.0,
                unit="score (0-100)",
                frequency="quarterly",
                data_source="Standardized awareness assessment",
                calculation_method="Weighted average of knowledge areas",
                success_threshold=75.0,
                weight=1.5
            ),
            
            # Behavior Metrics
            "verification_procedure_compliance": MetricDefinition(
                name="Verification Procedure Compliance",
                description="Percentage of participants following verification procedures",
                metric_type=MetricType.BEHAVIOR,
                measurement_method=MeasurementMethod.SIMULATION,
                baseline_value=0.0,
                target_value=90.0,
                unit="percentage",
                frequency="monthly",
                data_source="Simulation scenario results",
                calculation_method="(Proper verifications / Total scenarios) * 100",
                success_threshold=85.0,
                weight=1.3
            ),
            
            "incident_reporting_rate": MetricDefinition(
                name="Incident Reporting Rate",
                description="Percentage of suspicious activities reported",
                metric_type=MetricType.BEHAVIOR,
                measurement_method=MeasurementMethod.INCIDENT_DATA,
                baseline_value=0.0,
                target_value=95.0,
                unit="percentage",
                frequency="weekly",
                data_source="Security incident reports",
                calculation_method="(Reported incidents / Total incidents) * 100",
                success_threshold=90.0,
                weight=1.1
            ),
            
            # Training Metrics
            "training_completion_rate": MetricDefinition(
                name="Training Completion Rate",
                description="Percentage of participants completing required training",
                metric_type=MetricType.TRAINING,
                measurement_method=MeasurementMethod.ASSESSMENT,
                baseline_value=0.0,
                target_value=95.0,
                unit="percentage",
                frequency="monthly",
                data_source="Learning management system",
                calculation_method="(Completed modules / Assigned modules) * 100",
                success_threshold=90.0,
                weight=1.0
            ),
            
            "training_effectiveness_score": MetricDefinition(
                name="Training Effectiveness Score",
                description="Average score improvement from training",
                metric_type=MetricType.TRAINING,
                measurement_method=MeasurementMethod.ASSESSMENT,
                baseline_value=0.0,
                target_value=25.0,
                unit="percentage improvement",
                frequency="quarterly",
                data_source="Pre/post training assessments",
                calculation_method="(Post-score - Pre-score) / Pre-score * 100",
                success_threshold=20.0,
                weight=1.2
            ),
            
            # Incident Metrics
            "social_engineering_incidents": MetricDefinition(
                name="Social Engineering Incidents",
                description="Number of successful social engineering attacks",
                metric_type=MetricType.INCIDENT,
                measurement_method=MeasurementMethod.INCIDENT_DATA,
                baseline_value=0.0,
                target_value=-50.0,  # Negative target (reduction)
                unit="count",
                frequency="monthly",
                data_source="Security incident database",
                calculation_method="Total incidents in period",
                success_threshold=-30.0,  # 30% reduction
                weight=1.4
            ),
            
            "incident_response_time": MetricDefinition(
                name="Incident Response Time",
                description="Average time to respond to security incidents",
                metric_type=MetricType.INCIDENT,
                measurement_method=MeasurementMethod.INCIDENT_DATA,
                baseline_value=0.0,
                target_value=-50.0,  # 50% reduction
                unit="minutes",
                frequency="weekly",
                data_source="Incident response logs",
                calculation_method="Average response time per incident",
                success_threshold=-30.0,  # 30% improvement
                weight=1.1
            ),
            
            # Culture Metrics
            "security_culture_index": MetricDefinition(
                name="Security Culture Index",
                description="Overall security culture assessment score",
                metric_type=MetricType.CULTURE,
                measurement_method=MeasurementMethod.SURVEY,
                baseline_value=0.0,
                target_value=80.0,
                unit="score (0-100)",
                frequency="quarterly",
                data_source="Employee security culture survey",
                calculation_method="Weighted average of culture indicators",
                success_threshold=75.0,
                weight=1.3
            ),
            
            "peer_reporting_confidence": MetricDefinition(
                name="Peer Reporting Confidence",
                description="Confidence level in reporting security concerns",
                metric_type=MetricType.CULTURE,
                measurement_method=MeasurementMethod.SURVEY,
                baseline_value=0.0,
                target_value=85.0,
                unit="percentage",
                frequency="monthly",
                data_source="Employee confidence survey",
                calculation_method="Average confidence rating",
                success_threshold=80.0,
                weight=1.0
            )
        }
    
    def create_campaign_metrics(self, campaign_id: str, campaign_name: str, 
                              start_date: datetime.datetime,
                              selected_metrics: Optional[List[str]] = None) -> CampaignMetrics:
        """Create a new campaign metrics package"""
        
        if selected_metrics is None:
            selected_metrics = list(self.metric_definitions.keys())
        
        campaign_metrics = CampaignMetrics(
            campaign_id=campaign_id,
            campaign_name=campaign_name,
            start_date=start_date,
            end_date=None,
            metrics={name: self.metric_definitions[name] for name in selected_metrics},
            measurements=[]
        )
        
        self.campaigns[campaign_id] = campaign_metrics
        return campaign_metrics
    
    def add_measurement(self, campaign_id: str, metric_name: str, value: float,
                       measurement_date: datetime.datetime, confidence_level: float = 1.0,
                       sample_size: int = 1, notes: str = "") -> None:
        """Add a measurement result to a campaign"""
        
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign {campaign_id} not found")
        
        if metric_name not in self.campaigns[campaign_id].metrics:
            raise ValueError(f"Metric {metric_name} not defined for campaign {campaign_id}")
        
        measurement = MeasurementResult(
            metric_name=metric_name,
            value=value,
            measurement_date=measurement_date,
            confidence_level=confidence_level,
            sample_size=sample_size,
            notes=notes
        )
        
        self.campaigns[campaign_id].measurements.append(measurement)
    
    def calculate_campaign_progress(self, campaign_id: str) -> Dict[str, Any]:
        """Calculate progress and success metrics for a campaign"""
        
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign {campaign_id} not found")
        
        campaign = self.campaigns[campaign_id]
        progress = {
            "campaign_id": campaign_id,
            "campaign_name": campaign.campaign_name,
            "overall_progress": 0.0,
            "metric_progress": {},
            "success_metrics": {},
            "recommendations": []
        }
        
        # Calculate progress for each metric
        for metric_name, metric_def in campaign.metrics.items():
            measurements = [m for m in campaign.measurements if m.metric_name == metric_name]
            
            if not measurements:
                progress["metric_progress"][metric_name] = {
                    "current_value": 0.0,
                    "target_value": metric_def.target_value,
                    "progress_percentage": 0.0,
                    "status": "no_data"
                }
                continue
            
            # Get latest measurement
            latest_measurement = max(measurements, key=lambda x: x.measurement_date)
            current_value = latest_measurement.value
            
            # Calculate progress percentage
            if metric_def.target_value > metric_def.baseline_value:
                # Positive target (increase)
                progress_pct = ((current_value - metric_def.baseline_value) / 
                              (metric_def.target_value - metric_def.baseline_value)) * 100
            else:
                # Negative target (decrease)
                progress_pct = ((metric_def.baseline_value - current_value) / 
                              (metric_def.baseline_value - metric_def.target_value)) * 100
            
            # Determine status
            if progress_pct >= 100:
                status = "exceeded"
            elif progress_pct >= 80:
                status = "on_track"
            elif progress_pct >= 50:
                status = "behind"
            else:
                status = "at_risk"
            
            progress["metric_progress"][metric_name] = {
                "current_value": current_value,
                "target_value": metric_def.target_value,
                "baseline_value": metric_def.baseline_value,
                "progress_percentage": min(progress_pct, 100.0),
                "status": status,
                "success_threshold_met": current_value >= metric_def.success_threshold
            }
        
        # Calculate overall progress
        total_weight = sum(metric.weight for metric in campaign.metrics.values())
        weighted_progress = sum(
            progress["metric_progress"][name]["progress_percentage"] * metric.weight
            for name, metric in campaign.metrics.items()
        )
        progress["overall_progress"] = weighted_progress / total_weight if total_weight > 0 else 0.0
        
        # Generate recommendations
        progress["recommendations"] = self._generate_recommendations(campaign, progress)
        
        return progress
    
    def _generate_recommendations(self, campaign: CampaignMetrics, 
                                progress: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on campaign progress"""
        recommendations = []
        
        # Check for metrics that are behind
        behind_metrics = [
            name for name, data in progress["metric_progress"].items()
            if data["status"] in ["behind", "at_risk"]
        ]
        
        if behind_metrics:
            recommendations.append(
                f"Focus on improving {', '.join(behind_metrics)} metrics. "
                "Consider additional training or targeted interventions."
            )
        
        # Check for metrics exceeding targets
        exceeded_metrics = [
            name for name, data in progress["metric_progress"].items()
            if data["status"] == "exceeded"
        ]
        
        if exceeded_metrics:
            recommendations.append(
                f"Excellent progress on {', '.join(exceeded_metrics)}. "
                "Consider sharing best practices with other teams."
            )
        
        # Check for low completion rates
        if "training_completion_rate" in progress["metric_progress"]:
            completion_data = progress["metric_progress"]["training_completion_rate"]
            if completion_data["current_value"] < 90:
                recommendations.append(
                    "Training completion rate is below target. "
                    "Consider additional communication or incentives."
                )
        
        # Check for high incident rates
        if "social_engineering_incidents" in progress["metric_progress"]:
            incident_data = progress["metric_progress"]["social_engineering_incidents"]
            if incident_data["current_value"] > 0:
                recommendations.append(
                    "Social engineering incidents detected. "
                    "Review and strengthen security controls."
                )
        
        return recommendations
    
    def generate_metrics_report(self, campaign_id: str, 
                              format: str = "json") -> str:
        """Generate a comprehensive metrics report for a campaign"""
        
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign {campaign_id} not found")
        
        campaign = self.campaigns[campaign_id]
        progress = self.calculate_campaign_progress(campaign_id)
        
        report = {
            "campaign_info": {
                "id": campaign_id,
                "name": campaign.campaign_name,
                "start_date": campaign.start_date.isoformat(),
                "end_date": campaign.end_date.isoformat() if campaign.end_date else None
            },
            "overall_progress": progress["overall_progress"],
            "metric_details": progress["metric_progress"],
            "recommendations": progress["recommendations"],
            "measurement_summary": self._summarize_measurements(campaign),
            "generated_at": datetime.datetime.now().isoformat()
        }
        
        if format.lower() == "json":
            return json.dumps(report, indent=2, default=str)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _summarize_measurements(self, campaign: CampaignMetrics) -> Dict[str, Any]:
        """Summarize measurement data for reporting"""
        summary = {}
        
        for metric_name in campaign.metrics.keys():
            measurements = [m for m in campaign.measurements if m.metric_name == metric_name]
            
            if not measurements:
                summary[metric_name] = {"count": 0, "latest_value": None}
                continue
            
            values = [m.value for m in measurements]
            latest_measurement = max(measurements, key=lambda x: x.measurement_date)
            
            summary[metric_name] = {
                "count": len(measurements),
                "latest_value": latest_measurement.value,
                "average_value": statistics.mean(values),
                "min_value": min(values),
                "max_value": max(values),
                "latest_date": latest_measurement.measurement_date.isoformat()
            }
        
        return summary
    
    def get_metric_trends(self, campaign_id: str, metric_name: str) -> List[Dict[str, Any]]:
        """Get trend data for a specific metric"""
        
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign {campaign_id} not found")
        
        campaign = self.campaigns[campaign_id]
        measurements = [m for m in campaign.measurements if m.metric_name == metric_name]
        
        # Sort by date
        measurements.sort(key=lambda x: x.measurement_date)
        
        trends = []
        for measurement in measurements:
            trends.append({
                "date": measurement.measurement_date.isoformat(),
                "value": measurement.value,
                "confidence_level": measurement.confidence_level,
                "sample_size": measurement.sample_size,
                "notes": measurement.notes
            })
        
        return trends
    
    def export_campaign_data(self, campaign_id: str) -> Dict[str, Any]:
        """Export complete campaign data for external analysis"""
        
        if campaign_id not in self.campaigns:
            raise ValueError(f"Campaign {campaign_id} not found")
        
        campaign = self.campaigns[campaign_id]
        
        return {
            "campaign_info": {
                "id": campaign.campaign_id,
                "name": campaign.campaign_name,
                "start_date": campaign.start_date.isoformat(),
                "end_date": campaign.end_date.isoformat() if campaign.end_date else None
            },
            "metrics": {name: {
                "name": metric.name,
                "description": metric.description,
                "type": metric.metric_type.value,
                "target_value": metric.target_value,
                "baseline_value": metric.baseline_value,
                "unit": metric.unit,
                "weight": metric.weight
            } for name, metric in campaign.metrics.items()},
            "measurements": [{
                "metric_name": m.metric_name,
                "value": m.value,
                "date": m.measurement_date.isoformat(),
                "confidence_level": m.confidence_level,
                "sample_size": m.sample_size,
                "notes": m.notes
            } for m in campaign.measurements]
        }


def main():
    """Example usage of the success metrics framework"""
    
    # Initialize the framework
    framework = SuccessMetricsFramework()
    
    # Create a new campaign
    campaign_id = "campaign_001"
    campaign_name = "Q1 Security Awareness Campaign"
    start_date = datetime.datetime.now()
    
    campaign_metrics = framework.create_campaign_metrics(
        campaign_id=campaign_id,
        campaign_name=campaign_name,
        start_date=start_date
    )
    
    # Add some sample measurements
    framework.add_measurement(
        campaign_id=campaign_id,
        metric_name="phishing_recognition_rate",
        value=75.0,
        measurement_date=datetime.datetime.now(),
        confidence_level=0.95,
        sample_size=100,
        notes="Pre-training baseline measurement"
    )
    
    framework.add_measurement(
        campaign_id=campaign_id,
        metric_name="training_completion_rate",
        value=92.0,
        measurement_date=datetime.datetime.now(),
        confidence_level=1.0,
        sample_size=150,
        notes="Monthly training completion check"
    )
    
    # Calculate progress
    progress = framework.calculate_campaign_progress(campaign_id)
    
    print("=== SUCCESS METRICS FRAMEWORK ===")
    print(f"Campaign: {progress['campaign_name']}")
    print(f"Overall Progress: {progress['overall_progress']:.1f}%")
    print(f"Recommendations: {len(progress['recommendations'])}")
    
    # Generate report
    report = framework.generate_metrics_report(campaign_id)
    print(f"\nReport generated ({len(report)} characters)")


if __name__ == "__main__":
    main()
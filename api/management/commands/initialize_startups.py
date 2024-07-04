import json
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from api.models import Startup

class Command(BaseCommand):
    help = 'Initialize startup models with meaningful values'

    def handle(self, *args, **options):
        # Ensure there is at least one user to assign as the creator of the startups
        User = get_user_model()
        if not User.objects.exists():
            self.stdout.write(self.style.ERROR('No users found in the database. Create at least one user before running this script.'))
            return

        user = User.objects.first()

        startups_data = [
            {
                "name": "Tech Innovators",
                "code": "TI001",
                "location": "San Francisco, CA",
                "industry": "Technology",
                "founding_date": "2020-01-01",
                "legal_form": "LLC",
                "type_of_business": "Software Development",
                "website": "https://techinnovators.com",
                "facebook": "https://facebook.com/techinnovators",
                "linkedin": "https://linkedin.com/company/techinnovators",
                "twitter": "https://twitter.com/techinnovators",
                "description": "Innovative tech solutions for modern problems.",
                "mission": "To revolutionize technology.",
                "product_description": "Cutting-edge software solutions.",
                "customer_problem": "Need for advanced tech solutions.",
                "usp": "Unique tech innovations.",
                "capital": 1000000.0,
                "stage": "Seed",
                "target_investor_n": "Angel Investors",
                "use_of_funds": {"R&D": 500000, "Marketing": 300000, "Operations": 200000},
                "financial_tables": "Financial data here.",
                "already_invested_n": 200000.0,
                "impact_value": 8.5,
                "team_values": {"integrity": "high", "innovation": "high"},
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "experienced", "series_a": "none"},
                "team_languages": {"english": "fluent", "spanish": "basic"},
                "investore_expertise": {"tech": "high", "business": "medium"},
                "investore_expectations": {"returns": "high", "involvement": "low"},
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Global tech market.",
                "sdg": {"goal1": "No Poverty", "goal9": "Industry, Innovation, and Infrastructure"},
            },
            # Add 4 more startup dictionaries here with similar structure
            # ...
        ]

        for startup_data in startups_data:
            Startup.objects.create(
                user=user,
                **startup_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully initialized startup models.'))
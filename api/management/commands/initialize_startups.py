import json
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from api.models import Startup
from users.models import CustomUser


#Funzionante, associa le starup alla variabile 'user'
class Command(BaseCommand):
    help = 'Initialize startup models with meaningful values'

    def handle(self, *args, **options):
        # Ensure there is at least one user to assign as the creator of the startups
        User = get_user_model()
        if not User.objects.exists():
            self.stdout.write(self.style.ERROR('No users found in the database. Create at least one user before running this script.'))
            return

        user = list(User.objects.all())

        startups_data = [
            {
                "name": "Green Innovate",
                "code": "GI101",
                "location": "Austin, TX",
                "industry": "Real Estate",
                "founding_date": "2023-04-15",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://greeninnovate.com",
                "facebook": "https://facebook.com/greeninnovate",
                "linkedin": "https://linkedin.com/company/greeninnovate",
                "twitter": "https://twitter.com/greeninnovate",
                "description": "Pioneering renewable energy solutions.",
                "mission": "To empower sustainable living.",
                "product_description": "Solar panels and wind turbines.",
                "customer_problem": "Lack of affordable green energy options.",
                "usp": "Low-cost, high-efficiency solar solutions.",
                "capital": 2000000,
                "stage": "Series A",
                "target_investor_n": 4,
                "use_of_funds": {"R&D": 40, "Marketing": 30, "Operations": 30}, # the sum of the keys must be 100
                "financial_tables": "Financial data here.",
                "already_invested_n": 3,
                "impact_value": 9.0,
                "team_values": ["Integrity", "Innovation"],
                "team_motives": ["Resource Management"],
                "funding_experience": 'Yes',# or No
                "team_languages": ["English"],
                "investor_expertise": ["Management", "HR"],
                "investor_expectations": ["has a big network"],
                "exit_strategy": "IPO",
                "type_of_investment": "Equity",
                "market": "Global energy market.",
                "sdg": {
                    "SDG 7": "Affordable and Clean Energy",
                    "SDG 13": "Climate Action",
                    'SDG 6': 'Clean Water and Sanitation',
                }# sdg field must contain only sdg goals values
            },
            {
                "name": "TechPioneers",
                "code": "TP202",
                "location": "San Francisco, CA",
                "industry": "Technology",
                "founding_date": "2021-06-10",
                "legal_form": "LLC",
                "type_of_business": "B2C",
                "website": "https://techpioneers.com",
                "facebook": "https://facebook.com/techpioneers",
                "linkedin": "https://linkedin.com/company/techpioneers",
                "twitter": "https://twitter.com/techpioneers",
                "description": "Innovative AI-driven solutions.",
                "mission": "To revolutionize tech through AI.",
                "product_description": "AI-powered software tools.",
                "customer_problem": "Complexity in adopting AI technology.",
                "usp": "User-friendly AI solutions for businesses.",
                "capital": 5000000,
                "stage": "Series B",
                "target_investor_n": 5,
                "use_of_funds": {"R&D": 50, "Marketing": 25, "Operations": 25},
                "financial_tables": "Financial data here.",
                "already_invested_n": 2,
                "impact_value": 8.5,
                "team_values": ["Innovation", "Customer Focus"],
                "team_motives": ["Technological Advancement"],
                "funding_experience": "Yes",
                "team_languages": ["English", "Spanish"],
                "investor_expertise": ["Technology", "Marketing"],
                "investor_expectations": ["provides strategic guidance"],
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Global tech market.",
                "sdg": {
                    "SDG 9": "Industry, Innovation and Infrastructure",
                    "SDG 8": "Decent Work and Economic Growth"
                }
            },
            {
                "name": "EcoFarm",
                "code": "EF303",
                "location": "Portland, OR",
                "industry": "Agriculture",
                "founding_date": "2020-09-05",
                "legal_form": "Cooperative",
                "type_of_business": "B2B",
                "website": "https://ecofarm.com",
                "facebook": "https://facebook.com/ecofarm",
                "linkedin": "https://linkedin.com/company/ecofarm",
                "twitter": "https://twitter.com/ecofarm",
                "description": "Sustainable farming solutions.",
                "mission": "To promote sustainable agriculture.",
                "product_description": "Organic farming products.",
                "customer_problem": "Harmful agricultural practices.",
                "usp": "Eco-friendly farming techniques.",
                "capital": 1500000,
                "stage": "Seed",
                "target_investor_n": 3,
                "use_of_funds": {"R&D": 30, "Marketing": 40, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 1,
                "impact_value": 9.2,
                "team_values": ["Sustainability", "Community"],
                "team_motives": ["Environmental Conservation"],
                "funding_experience": "No",
                "team_languages": ["English"],
                "investor_expertise": ["Agriculture", "Sustainability"],
                "investor_expectations": ["supports long-term growth"],
                "exit_strategy": "Merger",
                "type_of_investment": "Debt",
                "market": "National agriculture market.",
                "sdg": {
                    "SDG 2": "Zero Hunger",
                    "SDG 12": "Responsible Consumption and Production"
                }
            },
            {
                "name": "HealthBoost",
                "code": "HB404",
                "location": "Boston, MA",
                "industry": "Healthcare",
                "founding_date": "2019-11-20",
                "legal_form": "Corporation",
                "type_of_business": "B2C",
                "website": "https://healthboost.com",
                "facebook": "https://facebook.com/healthboost",
                "linkedin": "https://linkedin.com/company/healthboost",
                "twitter": "https://twitter.com/healthboost",
                "description": "Cutting-edge health supplements.",
                "mission": "To enhance health and wellness.",
                "product_description": "Natural health supplements.",
                "customer_problem": "Lack of effective health supplements.",
                "usp": "Scientifically proven health benefits.",
                "capital": 3000000,
                "stage": "Series A",
                "target_investor_n": 6,
                "use_of_funds": {"R&D": 35, "Marketing": 35, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 4,
                "impact_value": 8.0,
                "team_values": ["Health", "Integrity"],
                "team_motives": ["Public Health Improvement"],
                "funding_experience": "Yes",
                "team_languages": ["English"],
                "investor_expertise": ["Healthcare", "Finance"],
                "investor_expectations": ["has experience in healthcare"],
                "exit_strategy": "IPO",
                "type_of_investment": "Equity",
                "market": "Global health market.",
                "sdg": {
                    "SDG 3": "Good Health and Well-being",
                    "SDG 6": "Clean Water and Sanitation"
                }
            },
            {
                "name": "EduTech",
                "code": "ET505",
                "location": "New York, NY",
                "industry": "Education",
                "founding_date": "2018-02-28",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://edutech.com",
                "facebook": "https://facebook.com/edutech",
                "linkedin": "https://linkedin.com/company/edutech",
                "twitter": "https://twitter.com/edutech",
                "description": "Transformative educational technologies.",
                "mission": "To democratize quality education.",
                "product_description": "Online learning platforms.",
                "customer_problem": "Limited access to quality education.",
                "usp": "Accessible and affordable education tools.",
                "capital": 4000000,
                "stage": "Series B",
                "target_investor_n": 7,
                "use_of_funds": {"R&D": 40, "Marketing": 30, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 5,
                "impact_value": 9.5,
                "team_values": ["Education", "Equality"],
                "team_motives": ["Knowledge Sharing"],
                "funding_experience": "Yes",
                "team_languages": ["English", "French"],
                "investor_expertise": ["Education", "Technology"],
                "investor_expectations": ["has educational sector insights"],
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Global education market.",
                "sdg": {
                    "SDG 4": "Quality Education",
                    "SDG 10": "Reduced Inequalities"
                }
            },
            {
                "name": "CleanWaters",
                "code": "CW606",
                "location": "Miami, FL",
                "industry": "Environmental Services",
                "founding_date": "2022-01-15",
                "legal_form": "Corporation",
                "type_of_business": "B2G",
                "website": "https://cleanwaters.com",
                "facebook": "https://facebook.com/cleanwaters",
                "linkedin": "https://linkedin.com/company/cleanwaters",
                "twitter": "https://twitter.com/cleanwaters",
                "description": "Innovative water purification systems.",
                "mission": "To ensure clean water for all.",
                "product_description": "Advanced water filtration devices.",
                "customer_problem": "Contaminated water sources.",
                "usp": "Highly efficient and sustainable filtration.",
                "capital": 2500000,
                "stage": "Series A",
                "target_investor_n": 4,
                "use_of_funds": {"R&D": 45, "Marketing": 25, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 3,
                "impact_value": 9.8,
                "team_values": ["Sustainability", "Innovation"],
                "team_motives": ["Environmental Protection"],
                "funding_experience": "No",
                "team_languages": ["English"],
                "investor_expertise": ["Environmental Science", "Engineering"],
                "investor_expectations": ["supports sustainability initiatives"],
                "exit_strategy": "Merger",
                "type_of_investment": "Debt",
                "market": "Global water treatment market.",
                "sdg": {
                    "SDG 6": "Clean Water and Sanitation",
                    "SDG 14": "Life Below Water"
                }
            }
        ]


        for i in range(16):
            Startup.objects.create(
                        user=user[i],
                        **startups_data[i]
                    )
        self.stdout.write(self.style.SUCCESS('Successfully initialized startup models.'))



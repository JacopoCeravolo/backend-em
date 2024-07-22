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
                "type_of_business": "Investment Group",
                "website": "https://greeninnovate.com",
                "facebook": "https://facebook.com/greeninnovate",
                "linkedin": "https://linkedin.com/company/greeninnovate",
                "twitter": "https://twitter.com/greeninnovate",
                "description": "Pioneering renewable energy solutions.",
                "mission": "To empower sustainable living.",
                "product_description": "Solar panels and wind turbines.",
                "customer_problem": "Lack of affordable green energy options.",
                "usp": "Low-cost, high-efficiency solar solutions.",
                "capital": 2000000.0,
                "stage": "Series A",
                "target_investor_n": "Venture Capitalists",
                "use_of_funds": {"R&D": 40, "Marketing": 30, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 500000.0,
                "impact_value": 9.0,
                "team_values": ["integrity", "innovation"],
                "team_motives": ["Resource Management"],
                "funding_experience": {"seed": "completed", "series_a": "none"},
                "team_languages": ["English"],
                "investor_expertise": ["green tech", "finance"],
                "investor_expectations": {"returns": "moderate", "involvement": "medium"},
                "exit_strategy": "Public Offering",
                "type_of_investment": "Equity",
                "market": "Global energy market.",
                "sdg": {
                    "SDG 7": "Affordable and Clean Energy",
                    "SDG 13": "Climate Action"
                }
            },
            {
                "name": "Health Hub",
                "code": "HH202",
                "location": "Boston, MA",
                "industry": "Healthcare",
                "founding_date": "2021-05-22",
                "legal_form": "Partnership",
                "type_of_business": "B2B",
                "website": "https://healthhub.com",
                "facebook": "https://facebook.com/healthhub",
                "linkedin": "https://linkedin.com/company/healthhub",
                "twitter": "https://twitter.com/healthhub",
                "description": "Innovative health monitoring platforms.",
                "mission": "To enhance global health standards.",
                "product_description": "Wearable health tech.",
                "customer_problem": "Inadequate health monitoring tools.",
                "usp": "Real-time health analytics.",
                "capital": 1500000.0,
                "stage": "Seed",
                "target_investor_n": "Health-focused investors",
                "use_of_funds": {"R&D": 50, "Marketing": 20, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 300000.0,
                "impact_value": 9.2,
                "team_values": ["integrity", "innovation"],
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "experienced", "series_a": "planning"},
                "team_languages": ["english"],
                "investor_expertise": ["healthcare", "technology"],
                "investor_expectations": {"returns": "high", "involvement": "low"},
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Global healthcare market.",
                "sdg": {
                    "SDG 3": "Good Health and Well-being",
                    "SDG 9": "Industry, Innovation, and Infrastructure"
                }
            },
            {
                "name": "EduTech Leaders",
                "code": "ET303",
                "location": "San Diego, CA",
                "industry": "Education",
                "founding_date": "2022-02-14",
                "legal_form": "LLC",
                "type_of_business": "B2C",
                "website": "https://edutechleaders.com",
                "facebook": "https://facebook.com/edutechleaders",
                "linkedin": "https://linkedin.com/company/edutechleaders",
                "twitter": "https://twitter.com/edutechleaders",
                "description": "Revolutionizing learning through technology.",
                "mission": "To make learning accessible to all.",
                "product_description": "Interactive educational software.",
                "customer_problem": "High costs and inaccessibility of quality education.",
                "usp": "Personalized learning experiences.",
                "capital": 800000.0,
                "stage": "Pre-Seed",
                "target_investor_n": "Educational institutions",
                "use_of_funds": {"R&D": 60, "Marketing": 20, "Operations": 20},
                "financial_tables": "Financial data here.",
                "already_invested_n": 100000.0,
                "impact_value": 8.7,
                "team_values": ["integrity", "innovation"],
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "none", "series_a": "none"},
                "team_languages": ["english"],
                "investor_expertise": ["education", "tech"],
                "investor_expectations": {"returns": "moderate", "involvement": "medium"},
                "exit_strategy": "Public Offering",
                "type_of_investment": "Equity",
                "market": "Global education market.",
                "sdg": {
                    "SDG 4": "Quality Education",
                    "SDG 9": "Industry, Innovation, and Infrastructure"
                }
            },
            {
                "name": "BioFuture Labs",
                "code": "BFL404",
                "location": "Seattle, WA",
                "industry": "Biotechnology",
                "founding_date": "2022-09-05",
                "legal_form": "S-Corp",
                "type_of_business": "B2B",
                "website": "https://biofuturelabs.com",
                "facebook": "https://facebook.com/biofuturelabs",
                "linkedin": "https://linkedin.com/company/biofuturelabs",
                "twitter": "https://twitter.com/biofuturelabs",
                "description": "Advanced biotech for a sustainable future.",
                "mission": "To innovate biotechnologies for environmental solutions.",
                "product_description": "Biodegradable materials and biofuels.",
                "customer_problem": "Environmental impact of traditional materials.",
                "usp": "Eco-friendly biotechnologies.",
                "capital": 2500000.0,
                "stage": "Series A",
                "target_investor_n": "Eco-focused venture capital",
                "use_of_funds": {"R&D": 50, "Marketing": 20, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 600000.0,
                "impact_value": 9.5,
                "team_values": ["integrity", "innovation"],
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "completed", "series_a": "in progress"},
                "team_languages": ["english"],
                "investor_expertise": ["biotech", "sustainability"],
                "investor_expectations": {"returns": "high", "involvement": "medium"},
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Global biotech market.",
                "sdg": {
                    "SDG 12": "Responsible Consumption and Production",
                    "SDG 13": "Climate Action"
                }
            },
            {
                "name": "FinTech Revolution",
                "code": "FTR505",
                "location": "New York, NY",
                "industry": "Financial Technology",
                "founding_date": "2023-01-20",
                "legal_form": "LLC",
                "type_of_business": "B2C",
                "website": "https://fintechrevolution.com",
                "facebook": "https://facebook.com/fintechrevolution",
                "linkedin": "https://linkedin.com/company/fintechrevolution",
                "twitter": "https://twitter.com/fintechrevolution",
                "description": "Disruptive financial tools for the digital age.",
                "mission": "To democratize financial services.",
                "product_description": "Blockchain-based financial platforms.",
                "customer_problem": "Lack of transparency in financial transactions.",
                "usp": "Secure, transparent financial services.",
                "capital": 1200000.0,
                "stage": "Seed",
                "target_investor_n": "Tech-savvy investors",
                "use_of_funds": {"R&D": 30, "Marketing": 40, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 250000.0,
                "impact_value": 8.9,
                "team_values": ["integrity", "innovation"],
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "experienced", "series_a": "planning"},
                "team_languages": ["english"],
                "investor_expertise": ["fintech", "blockchain"],
                "investor_expectations": {"returns": "high", "involvement": "low"},
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Global financial market.",
                "sdg": {
                    "SDG 8": "Decent Work and Economic Growth",
                    "SDG 9": "Industry, Innovation, and Infrastructure"
                }
            },
            {
                "name": "AgroTech Solutions",
                "code": "ATS606",
                "location": "Fresno, CA",
                "industry": "Agriculture Technology",
                "founding_date": "2023-03-30",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://agrotechsolutions.com",
                "facebook": "https://facebook.com/agrotechsolutions",
                "linkedin": "https://linkedin.com/company/agrotechsolutions",
                "twitter": "https://twitter.com/agrotechsolutions",
                "description": "Next-gen tech for sustainable farming.",
                "mission": "To revolutionize agriculture with technology.",
                "product_description": "Smart farming systems.",
                "customer_problem": "High costs and inefficiencies in farming.",
                "usp": "Automated, precision agriculture systems.",
                "capital": 1800000.0,
                "stage": "Seed",
                "target_investor_n": "Agricultural investors",
                "use_of_funds": {"R&D": 50, "Marketing": 25, "Operations": 25},
                "financial_tables": "Financial data here.",
                "already_invested_n": 400000.0,
                "impact_value": 9.0,
                "team_values": ["integrity", "innovation"],
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "completed", "series_a": "none"},
                "team_languages": ["english"],
                "investor_expertise": ["agritech", "sustainability"],
                "investor_expectations": {"returns": "moderate", "involvement": "medium"},
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Global agricultural market.",
                "sdg": {
                    "SDG 2": "Zero Hunger",
                    "SDG 12": "Responsible Consumption and Production"
                }
            },
            {
                "name": "CleanWater Tech",
                "code": "CWT707",
                "location": "Miami, FL",
                "industry": "Water Purification",
                "founding_date": "2021-11-11",
                "legal_form": "Partnership",
                "type_of_business": "B2C",
                "website": "https://cleanwatertech.com",
                "facebook": "https://facebook.com/cleanwatertech",
                "linkedin": "https://linkedin.com/company/cleanwatertech",
                "twitter": "https://twitter.com/cleanwatertech",
                "description": "Innovative solutions for clean water access.",
                "mission": "To provide clean water globally.",
                "product_description": "Advanced water purification systems.",
                "customer_problem": "Lack of access to clean water in many regions.",
                "usp": "Affordable and efficient water purification.",
                "capital": 1000000.0,
                "stage": "Seed",
                "target_investor_n": "Impact investors",
                "use_of_funds": {"R&D": 30, "Marketing": 40, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 200000.0,
                "impact_value": 9.3,
                "team_values": ["integrity", "innovation"],
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "experienced", "series_a": "none"},
                "team_languages": ["english"],
                "investor_expertise": ["water tech", "environment"],
                "investor_expectations": {"returns": "high", "involvement": "low"},
                "exit_strategy": "Public Offering",
                "type_of_investment": "Equity",
                "market": "Global water purification market.",
                "sdg": {
                    "SDG 6": "Clean Water and Sanitation",
                    "SDG 13": "Climate Action"
                }
            },
            {
                "name": "Urban Green Spaces",
                "code": "UGS808",
                "location": "Portland, OR",
                "industry": "Urban Development",
                "founding_date": "2022-07-17",
                "legal_form": "LLC",
                "type_of_business": "B2C",
                "website": "https://urbangreenspaces.com",
                "facebook": "https://facebook.com/urbangreenspaces",
                "linkedin": "https://linkedin.com/company/urbangreenspaces",
                "twitter": "https://twitter.com/urbangreenspaces",
                "description": "Designing green spaces for urban environments.",
                "mission": "To enhance urban living with sustainable green spaces.",
                "product_description": "Green roofs and urban gardens.",
                "customer_problem": "Lack of greenery in urban areas.",
                "usp": "Customizable and sustainable urban landscapes.",
                "capital": 1200000.0,
                "stage": "Seed",
                "target_investor_n": "Real estate and urban developers",
                "use_of_funds": {"R&D": 30, "Marketing": 40, "Operations": 30},
                "financial_tables": "Financial data here.",
                "already_invested_n": 300000.0,
                "impact_value": 9.1,
                "team_values": ["integrity", "innovation"],
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "experienced", "series_a": "planning"},
                "team_languages": ["english"],
                "investor_expertise": ["real estate", "sustainability"],
                "investor_expectations": {"returns": "moderate", "involvement": "medium"},
                "exit_strategy": "Acquisition",
                "type_of_investment": "Equity",
                "market": "Urban development market.",
                "sdg": {
                    "SDG 11": "Sustainable Cities and Communities",
                    "SDG 15": "Life on Land"
                }
            },
            {
                "name": "Global Tech Innovators",
                "code": "GTI909",
                "location": "London, UK",
                "industry": "Software Development",
                "founding_date": "2022-12-01",
                "legal_form": "Corporation",
                "type_of_business": "B2B",
                "website": "https://globaltechinnovators.com",
                "facebook": "https://facebook.com/globaltechinnovators",
                "linkedin": "https://linkedin.com/company/globaltechinnovators",
                "twitter": "https://twitter.com/globaltechinnovators",
                "description": "Next-gen software for global challenges.",
                "mission": "To lead in global tech innovation.",
                "product_description": "Cloud solutions and AI services.",
                "customer_problem": "Complexity in managing large data.",
                "usp": "Scalable and secure cloud platforms.",
                "capital": 3000000.0,
                "stage": "Series A",
                "target_investor_n": "Global tech investors",
                "use_of_funds": {"R&D": 50, "Marketing": 25, "Operations": 25},
                "financial_tables": "Financial data here.",
                "already_invested_n": 800000.0,
                "impact_value": 9.8,
                "team_values": ["integrity", "innovation"],
                "team_motives": {"growth": "high", "success": "high"},
                "funding_experience": {"seed": "completed", "series_a": "in progress"},
                "team_languages": ["english"],
                "investor_expertise": ["software", "AI"],
                "investor_expectations": {"returns": "high", "involvement": "low"},
                "exit_strategy": "Public Offering",
                "type_of_investment": "Equity",
                "market": "Global software market.",
                "sdg": {
                    "SDG 9": "Industry, Innovation, and Infrastructure",
                    "SDG 17": "Partnerships for the Goals"
                }
            }
        ]
        for i in range(9):
            Startup.objects.create(
                        user=user[i],
                        **startups_data[i]
                    )
        self.stdout.write(self.style.SUCCESS('Successfully initialized startup models.'))



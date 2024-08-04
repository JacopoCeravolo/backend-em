

# import json
# from django.core.management.base import BaseCommand
# from django.utils.timezone import now
# from django.contrib.auth import get_user_model
# from api.models import Startup
# from users.models import CustomUser

STP_NUM =150
INV_NUM =150
from api.models import Startup
import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Investor
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Initialize an Investor instance with meaningful data'
    def handle(self, *args, **kwargs):
        # Assuming you have a user to assign to the investor
        users = list(get_user_model().objects.all())
        names =[
    "support@cyberSphere.org",
    "connect@aquaGen.co",
    "contact@techNova.com",
    "connect@aquaPulse.co",
    "admin@hyperNet.io",
    "team@ecoTech.co",
    "hello@bioWave.net",
    "hello@bioGrid.net",
    "services@skyFusion.com",
    "team@ecoGrid.co",
    "connect@aquaWave.co",
    "inquiries@solarNet.net",
    "support@aeroSynth.org",
    "contact@neuroSync.io",
    "support@cyberGrid.org",
    "inquiries@solarPulse.net",
    "connect@aquaMinds.co",
    "services@skySphere.com",
    "info@quantumLeap.io",
    "support@cyberHaven.org",
    "inquiries@solarGrid.net",
    "team@ecoLink.co",
    "sales@nanoWave.org",
    "info@futureVibes.com",
    "admin@hyperFusion.io",
    "inquiries@solarFlare.net",
    "info@futureFusion.com",
    "services@skyNet.com",
    "admin@hyperVision.io",
    "info@futurePulse.com",
    "contact@astroNova.com",
    "info@galacticLeap.io",
    "support@orbitalSynth.org",
    "hello@cosmoFusion.net",
    "team@stellarWave.co",
    "services@stratoLink.com",
    "admin@metaNet.io",
    "sales@quantaGrid.org",
    "inquiries@lunarFlare.net",
    "connect@nebulaMinds.co",
    "info@astroVibes.com",
    "contact@neuroSync.org",
    "support@cosmicHaven.net",
    "hello@bioPulse.org",
    "team@ecoSphere.net",
    "services@aeroTech.com",
    "admin@stellarVision.io",
    "sales@nanoGrid.com",
    "inquiries@solarNet.org",
    "connect@hydroGen.co",
    "info@quantumSphere.com",
    "contact@neuroLink.net",
    "support@astroPulse.org",
    "hello@cyberLink.net",
    "team@ecoFusion.net",
    "services@stratoNet.com",
    "admin@stellarGrid.io",
    "sales@quantumWave.org",
    "inquiries@lunarFusion.net",
    "connect@astroTech.co",
    "info@futureLeap.com",
    "contact@quantumFusion.io",
    "support@stellarGrid.org",
    "hello@bioSphere.org",
    "team@ecoPulse.net",
    "services@aeroFusion.com",
    "admin@cosmicWave.io",
    "sales@quantaPulse.org",
    "inquiries@solarGrid.org",
    "connect@nebulaFusion.co",
    "info@futurePulse.org",
    "contact@cosmicGrid.io",
    "support@astroSphere.org",
    "hello@bioTech.org",
    "team@ecoLink.net",
    "services@stratoPulse.com",
    "admin@metaSphere.io",
    "sales@nanoFusion.com",
    "info@stellarFusion.io",
    "contact@bioNet.io",
    "support@cosmicLink.org",
    "hello@nanoWave.net",
    "team@aeroGrid.co",
    "services@quantumNet.com",
    "admin@futureVision.io",
    "connect@techPulse.co",
    "inquiries@astroNet.net",
    "support@hyperSphere.org",
    "info@solarVision.io",
    "team@ecoWave.net",
    "sales@nanoMinds.org",
    "services@bioGrid.com",
    "admin@quantumLink.io",
    "hello@astroPulse.net",
    "support@techFusion.org",
    "connect@lunarWave.co",
    "contact@skyMinds.com",
    "team@futureTech.co",
    "info@stellarWave.io",
    "services@bioTech.com",
    "admin@astroVision.io",
    "connect@cosmicNet.co",
    "support@quantumFusion.org",
    "hello@ecoNet.net",
    "sales@stellarGrid.org",
    "inquiries@nanoPulse.net",
    "team@futureGrid.co",
    "info@bioSphere.com",
    "services@hyperTech.com",
    "admin@astroGrid.io",
    "connect@stellarFusion.co",
    "support@ecoPulse.org",
    "hello@quantumNet.net",
    "sales@techGrid.org",
    "inquiries@aeroPulse.net",
    "team@cosmicWave.co",
    "info@bioPulse.com",
    "services@futureNet.com",
    "admin@stellarLink.io",
    "connect@techGrid.co",
    "support@nanoFusion.org",
    "hello@ecoGrid.net",
    "team@astroWave.co",
    "sales@quantumPulse.org",
    "inquiries@bioTech.net",
    "info@futureGrid.io",
    "services@cosmicTech.com",
    "admin@quantumGrid.io",
    "connect@ecoNet.co",
    "support@stellarPulse.org",
    "hello@astroTech.net",
    "team@quantumWave.co",
    "sales@bioGrid.org",
    "inquiries@techFusion.net",
    "info@ecoTech.com",
    "services@stellarNet.com",
    "admin@futureLink.io",
    "connect@astroNet.co",
    "support@quantumTech.org",
    "hello@nanoNet.net",
    "team@techPulse.co",
    "sales@ecoWave.org",
    "inquiries@cosmicGrid.net",
    "info@stellarTech.com",
    "services@astroFusion.com",
    "admin@nanoGrid.io",
    "connect@futureNet.co",
    "support@bioPulse.org",
    "hello@techWave.net",
    "team@quantumLink.co",
    "sales@cosmicFusion.org",
    "inquiries@ecoGrid.net",
    "info@astroNet.com",
    "services@techNet.com",
    "admin@stellarPulse.io",
    "connect@bioGrid.co",
    "support@futureFusion.org",
    "hello@astroLink.net",
    "team@quantumNet.co",
    "sales@futureWave.org",
    "inquiries@techPulse.net",
    "info@ecoWave.com",
    "services@stellarFusion.com",
    "admin@astroPulse.io",
    "connect@quantumGrid.co",
    "support@techNet.org",
    "hello@cosmicGrid.net",
    "team@bioFusion.co",
    "sales@astroGrid.org",
    "inquiries@nanoTech.net",
    "info@futureNet.com",
    "services@ecoFusion.com",
    "admin@quantumPulse.io",
    "connect@stellarNet.co",
    "support@astroTech.org"
]

        languages =[
            "English",
            "German",
            "French",
            "Italian",
            "Spanish",
            "Chinese",
            "Arabic"
        ]

        industry =[
            "Real estate",
            "Nature protection",
            "Woman Empowerment",
            "Poverty alleviation",
            "Greentech",
            "Smart City",
            "Mobility",
            "Energy",
            "Education",
            "Health",
            "Sports",
            "Cosmetics",
            "Financial & Insurance",
            "Food",
            "Legal",
            "Rental & Repair",
            "Transportation & storage",
            "Information & Communication",
            "Arts, entertainment & recreation",
            "Support services",
            "Technical services",
            "Environmental Consulting",
            "Other"
        ]

        type_of_business =[
            "B2B",
            "B2C",
            "Consultancy",
            "All"
        ]

        team_values =[
        "nability",
        "Customer Orientation",
        "Efficiency",
        "Collaboration",
        "Common good",
        "Value-oriented",
        "Engagement",
        "Transparency",
        "Ethical Behavior",
        "Punctuality",
        "Quickness",
        "Ethics",
        "Integrity",
        "Openness to innovation",
        "Support and network",
        "Risk-taking",
        "Transparency",
        "Trust",
        "Long-term focus",
        "Social responsability",
        "Flexibility and adaptability",
        "Win-win-mentality"
        ]

        stage = [
            "Pre-Seed Phase",
            "Seed Stage",
            "Pre-Series A",
            "Series A",
            "Pre-Series B",
            "Series B",
            "Series C",
            "Bridge",
        ]

        expertice = [
            "Accounting / Bookkeeping",
            "Controlling",
            "Fundraising",
            "HR / Personnel",
            "Legal / Legal Affairs",
            "Logistics / Logistics",
            "Management",
            "Marketing",
            "PR",
            "Procurement / Purchasing",
            "Product Development",
            "Production",
            "Sales / Distribution",
            "Strategy",
            "Technology"
        ]

        type_of_investment =[
            "Equity",
            "Loan",
            "Convertible Loan"
        ]

        team_motives =[
        "extravagant",
        "Romantic",
        "Security",
        "activating",
        "Charming",
        "Clarity",
        "risk",
        "Friendly",
        "Functional",
        "daring",
        "Soft",
        "Diligent",
        "youthful",
        "Cosy",
        "Competence",
        "adventure",
        "Health",
        "Disciplined",
        "festive",
        "Gentle",
        "Powerful",
        "vivid",
        "Security",
        "Force",
        "joy",
        "Down to earth",
        "Superior",
        "indulgence",
        "Trust",
        "Status",
        "open-minded",
        "Reliable",
        "Exclusive",
        "Openness",
        "Traditional",
        "Responsibility"
        ]

        sdg_goals = {
            "SDG-1": "No Poverty",
            "SDG-2": "Zero Hunger",
            "SDG-3": "Good Health and Well-being",
            "SDG-4": "Quality Education",
            "SDG-5": "Gender Equality",
            "SDG-6": "Clean Water and Sanitation",
            "SDG-7": "Affordable and Clean Energy",
            "SDG-8": "Decent Work and Economic Growth",
            "SDG-9": "Industry, Innovation and Infrastructure",
            "SDG-10": "Reduced Inequalities",
            "SDG-11": "Sustainable Cities and Communities",
            "SDG-12": "Responsible Consumption and Production",
            "SDG-13": "Climate Action",
            "SDG-14": "Life Below Water",
            "SDG-15": "Life on Land",
            "SDG-16": "Peace, Justice and Strong Institutions",
            "SDG-17": "Partnerships for the Goals"
        }


        random.seed(120)
        investor_data =[]
        # initialize investor data 
        for i in range(INV_NUM):
            sdg_format  = random.sample(list(sdg_goals.keys()), k=8)
            investor_sample={
                'company_name': names[i],
                'location': 'San Francisco, CA',
                'industry': random.choice(industry),
                'type_of_business': random.choice(type_of_business),  # B2B or B2C
                'linkedin': 'https://linkedin.com/company/ecovenures',
                'twitter': 'https://twitter.com/ecovenures',
                'description': 'Investing in water saving technologies and businesses.',
                'mission': 'To alleviate global water scarcity through smart investments.',
                'capital': random.choice(range(100000, 1000000)),
                'stage': random.choices(stage, k =4),  # stage of the startup: Series A, Series B, Series C, Seed, Pre Seed, Bridge
                'impact_value': random.choice(range(5, 9)),
                'team_values': random.sample(team_values, k=4),
                'team_motives': random.sample(team_motives, k=6),
                'languages': random.sample(languages, k=3),
                'investor_expertise': random.sample(expertice, k=6),
                'investor_offering': ['Has a big network'],
                'investor_value': ['Sustainability', 'Long-term Gains'],
                'exit_strategy': 'IPO',
                'type_of_investment': random.choice(type_of_investment),
                'market': 'Global water conservation sector',
                'sdg': {sdg_format[0]: sdg_goals[sdg_format[0]], sdg_format[1]: sdg_goals[sdg_format[1]], sdg_format[2]: sdg_goals[sdg_format[2]],  sdg_format[3]: sdg_goals[sdg_format[3]], sdg_format[4]: sdg_goals[sdg_format[4]], sdg_format[5]: sdg_goals[sdg_format[5]], sdg_format[6]: sdg_goals[sdg_format[6]],  sdg_format[7]: sdg_goals[sdg_format[7]]}  # sdg must be in the sdg goals
            }
            investor_data.append(investor_sample)

        startups_data =[]

        # initialize startup data 
        for i in range(STP_NUM):
            sdg_format  = random.sample(list(sdg_goals.keys()), k=8)
            startup_sample ={
                            "name": names[i],
                            "code": "GI101",
                            "location": "Austin, TX",
                            "industry": random.choice(industry),
                            "founding_date": "2023-04-15",
                            "legal_form": "Corporation",
                            "type_of_business":  random.choice(type_of_business),
                            "website": "https://greeninnovate.com",
                            "facebook": "https://facebook.com/greeninnovate",
                            "linkedin": "https://linkedin.com/company/greeninnovate",
                            "twitter": "https://twitter.com/greeninnovate",
                            "description": "Pioneering renewable energy solutions.",
                            "mission": "To empower sustainable living.",
                            "product_description": "Solar panels and wind turbines.",
                            "customer_problem": "Lack of affordable green energy options.",
                            "usp": "Low-cost, high-efficiency solar solutions.",
                            "capital": random.choice(range(5000, 100000)), 
                            "stage": random.choice(stage),
                            "target_investor_n": 4,
                            "use_of_funds": {"R&D": 40, "Marketing": 30, "Operations": 30}, 
                            "financial_tables": "Financial data here.",
                            "already_invested_n": 3,
                            "impact_value": random.choice(range(5, 9)),
                            "team_values":  random.sample(team_values, k = 4 ),
                            "team_motives": random.sample(team_motives, k = 4 ),
                            "funding_experience": 'Yes',
                            "team_languages": random.sample(languages, k = 3 ),
                            "investor_expertise": random.sample(expertice, k = 6 ),
                            "investor_expectations": ["has a big network"],
                            "exit_strategy": "IPO",
                            "type_of_investment": random.choice(type_of_investment),
                            "market": "Global energy market.",
                            "sdg": {sdg_format[0]: sdg_goals[sdg_format[0]], sdg_format[1]: sdg_goals[sdg_format[1]], sdg_format[2]: sdg_goals[sdg_format[2]],  sdg_format[3]: sdg_goals[sdg_format[3]], sdg_format[4]: sdg_goals[sdg_format[4]], sdg_format[5]: sdg_goals[sdg_format[5]], sdg_format[6]: sdg_goals[sdg_format[6]],  sdg_format[7]: sdg_goals[sdg_format[7]]}, 
                        }
            startups_data.append(startup_sample)

        #create Investor objects
        for i in range(INV_NUM):
            Investor.objects.create(
                        user = users[i],
                        **investor_data[i]
                    )
        
        # create startup objects
        for i in range(STP_NUM):
            Startup.objects.create(
                        user=users[i],
                        **startups_data[i]
                    )

            
        self.stdout.write(self.style.SUCCESS('Successfully created Data'))


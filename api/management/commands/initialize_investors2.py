
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Investor
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Initialize an Investor instance with meaningful data'
    def handle(self, *args, **kwargs):
        # Assuming you have a user to assign to the investor
        users = list(get_user_model().objects.all())  # Get the first user (you should adjust this query according to your needs)
        investor_data = [
            {
            'company_name': 'Eco Ventures',
            'location': 'San Francisco, CA',
            'industry': 'Real Estate',
            'type_of_business': 'B2B', # B2B or B2C 
            'linkedin': 'https://linkedin.com/company/ecovenures',
            'twitter': 'https://twitter.com/ecovenures',
            'description': 'Investing in water saving technologies and businesses.',
            'mission': 'To alleviate global water scarcity through smart investments.',
            'capital': 20000000,
            'stage':  ['Series A', 'Pre Seed'], # stage of the startup: Series A, Series B, Series C, Seed, Pre Seed, Bridge
            'impact_value': 9.0,
            'team_values': ['Sustainability', 'Efficiency', 'Innovation'],
            'team_motives': ['Resource Management', 'Tech Advancement', 'Sustainability'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Water Management', 'HR'],
            'investor_offering':['Has a big network'], 
            'investor_value': ['Sustainability', 'Long-term Gains'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global water conservation sector',
            'sdg': {
                'SDG 6': 'Clean Water and Sanitation',
                'SDG 9': 'Industry, Innovation, and Infrastructure'
            } # sdg must to be n the sdg goals
        },
        {
            'company_name': 'Green Horizons',
            'location': 'New York, NY',
            'industry': 'Renewable Energy',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/greenhorizons',
            'twitter': 'https://twitter.com/greenhorizons',
            'description': 'Focused on investing in solar and wind energy startups.',
            'mission': 'To accelerate the transition to renewable energy sources worldwide.',
            'capital': 50000000,
            'stage': ['Series B', 'Series C'],
            'impact_value': 8.5,
            'team_values': ['Innovation', 'Sustainability', 'Growth'],
            'team_motives': ['Environmental Impact', 'Tech Leadership', 'Sustainability'],
            'languages': ['English', 'German'],
            'investor_expertise': ['Renewable Energy', 'Finance'],
            'investor_offering': ['Extensive industry connections'],
            'investor_value': ['Environmental Impact', 'High Returns'],
            'exit_strategy': 'Acquisition',
            'type_of_investment': 'Equity',
            'market': 'Global renewable energy sector',
            'sdg': {
                'SDG 7': 'Affordable and Clean Energy',
                'SDG 13': 'Climate Action'
            }
        },
        {
            'company_name': 'Tech Innovators',
            'location': 'Austin, TX',
            'industry': 'Technology',
            'type_of_business': 'B2C',
            'linkedin': 'https://linkedin.com/company/techinnovators',
            'twitter': 'https://twitter.com/techinnovators',
            'description': 'Investing in cutting-edge consumer technology products.',
            'mission': 'To foster innovation in consumer technology.',
            'capital': 30000000,
            'stage': ['Seed', 'Series A'],
            'impact_value': 7.5,
            'team_values': ['Innovation', 'User Experience', 'Scalability'],
            'team_motives': ['Tech Advancement', 'Market Disruption', 'User Satisfaction'],
            'languages': ['English', 'Chinese'],
            'investor_expertise': ['Consumer Tech', 'Product Development'],
            'investor_offering': ['Product development expertise'],
            'investor_value': ['Innovation', 'Market Leadership'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global consumer technology market',
            'sdg': {
                'SDG 9': 'Industry, Innovation, and Infrastructure',
                'SDG 8': 'Decent Work and Economic Growth'
            }
        },
        {
            'company_name': 'Health Ventures',
            'location': 'Boston, MA',
            'industry': 'Healthcare',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/healthventures',
            'twitter': 'https://twitter.com/healthventures',
            'description': 'Investing in innovative healthcare solutions and biotech.',
            'mission': 'To improve global health through strategic investments.',
            'capital': 40000000,
            'stage': ['Series A', 'Series B'],
            'impact_value': 9.0,
            'team_values': ['Health', 'Innovation', 'Patient Care'],
            'team_motives': ['Medical Advancements', 'Patient Outcomes', 'Innovation'],
            'languages': ['English', 'French'],
            'investor_expertise': ['Healthcare', 'Biotechnology'],
            'investor_offering': ['Medical industry insights'],
            'investor_value': ['Health Impact', 'Sustainable Growth'],
            'exit_strategy': 'Merger',
            'type_of_investment': 'Equity',
            'market': 'Global healthcare sector',
            'sdg': {
                'SDG 3': 'Good Health and Well-being',
                'SDG 9': 'Industry, Innovation, and Infrastructure'
            }
        },
        {
            'company_name': 'AgriFund',
            'location': 'Chicago, IL',
            'industry': 'Agriculture',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/agrifund',
            'twitter': 'https://twitter.com/agrifund',
            'description': 'Investing in sustainable agriculture and food technology.',
            'mission': 'To support sustainable agricultural practices and food security.',
            'capital': 35000000,
            'stage': ['Pre Seed', 'Seed'],
            'impact_value': 8.0,
            'team_values': ['Sustainability', 'Innovation', 'Food Security'],
            'team_motives': ['Sustainable Farming', 'Food Innovation', 'Resource Management'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Agriculture', 'Sustainability'],
            'investor_offering': ['Agricultural expertise'],
            'investor_value': ['Sustainability', 'Long-term Growth'],
            'exit_strategy': 'Acquisition',
            'type_of_investment': 'Debt',
            'market': 'Global agriculture and food technology sector',
            'sdg': {
                'SDG 2': 'Zero Hunger',
                'SDG 12': 'Responsible Consumption and Production'
            }
        },
        {
            'company_name': 'Urban Growth Partners',
            'location': 'Los Angeles, CA',
            'industry': 'Urban Development',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/urbangrowthpartners',
            'twitter': 'https://twitter.com/urbangrowthpartners',
            'description': 'Investing in urban development and smart city technologies.',
            'mission': 'To create sustainable and smart urban spaces.',
            'capital': 45000000,
            'stage': ['Series A', 'Series B'],
            'impact_value': 8.8,
            'team_values': ['Sustainability', 'Innovation', 'Community'],
            'team_motives': ['Urban Innovation', 'Community Development', 'Sustainability'],
            'languages': ['English', 'Japanese'],
            'investor_expertise': ['Urban Development', 'Technology'],
            'investor_offering': ['Urban planning insights'],
            'investor_value': ['Sustainability', 'Community Impact'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global urban development sector',
            'sdg': {
                'SDG 11': 'Sustainable Cities and Communities',
                'SDG 9': 'Industry, Innovation, and Infrastructure'
            }
        }
    ]


        for i in range(5):
            Investor.objects.create(
                        user = users[i],
                        **investor_data[i]
                    )

        
        self.stdout.write(self.style.SUCCESS('Successfully created Investors'))

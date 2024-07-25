# management/commands/initialize_investor.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Investor
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Initialize an Investor instance with meaningful data'

    def handle(self, *args, **kwargs):
        # Assuming you have a user to assign to the investor
        users = get_user_model().objects.all()  # Get the first user (you should adjust this query according to your needs)
        
        investor_data = investors=[
        {
            'company_name': 'Eco Ventures',
            'location': 'San Francisco, CA',
            'industry': 'Real Estate',
            'type_of_business': 'B2B',
            'linkedin': 'https://linkedin.com/company/ecovenures',
            'twitter': 'https://twitter.com/ecovenures',
            'description': 'Investing in water saving technologies and businesses.',
            'mission': 'To alleviate global water scarcity through smart investments.',
            'capital': 20000000,
            'stage':  ['Series A', 'Pre Seed'],
            'impact_value': 9.0,
            'team_values': ['Sustainability', 'Efficiency', 'Innovation'],
            'team_motives': ['Resource Management', 'Tech Advancement', 'Sustainability'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Water Management', 'HR'],
            'investor_value': ['Sustainability', 'Long-term Gains'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global water conservation sector',
            'sdg': {
                'SDG 6': 'Clean Water and Sanitation',
                'SDG 9': 'Industry, Innovation, and Infrastructure'
            }
        },
        {
            'company_name': 'Health Impact Partners',
            'location': 'Boston, MA',
            'industry': 'Healthcare',
            'type_of_business': 'Private Equity',
            'linkedin': 'https://linkedin.com/company/healthimpactpartners',
            'twitter': 'https://twitter.com/healthimpact',
            'description': 'Dedicated to improving healthcare access worldwide.',
            'mission': 'To support healthcare initiatives that provide scalable solutions.',
            'capital': 50000000,
            'stage': ['Series B', 'Series C'],
            'impact_value': 5.0,
            'team_values': ['Compassion', 'Innovation', 'Quality'],
            'team_motives': ['Health Improvement', 'Access to Care', 'Innovation'],
            'languages': ['English', 'German', 'French'],
            'investor_expertise': ['Healthcare Technology', 'Pharmaceuticals'],
            'investor_value': ['Social Impact', 'Financial Returns'],
            'exit_strategy': 'Merger',
            'type_of_investment': 'Debt and Equity',
            'market': 'Global healthcare market',
            'sdg': {
                'SDG 3': 'Good Health and Well-being'
            }
        },
        {
            'company_name': 'Clean Tech Capital',
            'location': 'Berlin, Germany',
            'industry': 'Clean Technology',
            'type_of_business': 'Venture Capital',
            'linkedin': 'https://linkedin.com/company/cleantechcapital',
            'twitter': 'https://twitter.com/cleantechcap',
            'description': 'Investor in innovative clean technology ventures.',
            'mission': 'To accelerate the transition to a sustainable economy.',
            'capital': 25000000,
            'stage': ['Series A', 'Series B'],
            'impact_value': 4.8,
            'team_values': ['Efficiency', 'Sustainability', 'Ethics'],
            'team_motives': ['Climate Change', 'Tech Innovation', 'Ethical Investing'],
            'languages': ['English', 'Dutch'],
            'investor_expertise': ['Renewable Energy', 'Eco-Friendly Products'],
            'investor_value': ['Environmental Impact', 'Innovation'],
            'exit_strategy': 'Sale to Strategic Investor',
            'type_of_investment': 'Equity',
            'market': 'European clean tech market',
            'sdg': {
                'SDG 7': 'Affordable and Clean Energy',
                'SDG 13': 'Climate Action'
            }
        },
        {
            'company_name': 'Urban Green',
            'location': 'London, UK',
            'industry': 'Urban Development',
            'type_of_business': 'Real Estate Investment',
            'linkedin': 'https://linkedin.com/company/urbangreen',
            'twitter': 'https://twitter.com/urbangreen',
            'description': 'Investing in sustainable urban development projects.',
            'mission': 'To create eco-friendly, livable urban spaces.',
            'capital': 30000000,
            'stage': ['Series C', 'Growth'],
            'impact_value': 4.7,
            'team_values': ['Community', 'Sustainability', 'Design'],
            'team_motives': ['Urban Regeneration', 'Sustainable Living', 'Community Building'],
            'languages': ['English', 'Italian'],
            'investor_expertise': ['Sustainable Construction', 'Green Buildings'],
            'investor_value': ['Community Impact', 'Stable Returns'],
            'exit_strategy': 'Long-term Hold',
            'type_of_investment': 'Equity',
            'market': 'Sustainable urban projects in Europe',
            'sdg': {
                'SDG 11': 'Sustainable Cities and Communities',
                'SDG 12': 'Responsible Consumption and Production'
            }
        },
        {
            'company_name': 'AgriGrowth Ventures',
            'location': 'Nairobi, Kenya',
            'industry': 'Agriculture',
            'type_of_business': 'Impact Investing',
            'linkedin': 'https://linkedin.com/company/agrigrowthventures',
            'twitter': 'https://twitter.com/agrigrowth',
            'description': 'Investor in agricultural innovations to improve food security.',
            'mission': 'To revolutionize agriculture in Africa through sustainable practices.',
            'capital': 22000000,
            'stage': ['Seed', 'Series A'],
            'impact_value': 4.9,
            'team_values': ['Innovation', 'Sustainability', 'Community'],
            'team_motives': ['Food Security', 'Innovative Farming', 'Community Support'],
            'languages': ['English', 'Swahili'],
            'investor_expertise': ['Sustainable Agriculture', 'Agri-tech'],
            'investor_value': ['Community Development', 'High Returns'],
            'exit_strategy': 'Acquisition by a Major Corporation',
            'type_of_investment': 'Equity and Grants',
            'market': 'Sub-Saharan agricultural sector',
            'sdg': {
                'SDG 2': 'Zero Hunger',
                'SDG 15': 'Life on Land'
            }
        },
                {
            'company_name': 'Blue Ocean Equity',
            'location': 'Sydney, Australia',
            'industry': 'Marine Conservation',
            'type_of_business': 'Equity Fund',
            'linkedin': 'https://linkedin.com/company/blueoceanequity',
            'twitter': 'https://twitter.com/blueocean',
            'description': 'Funding innovations in marine biodiversity and conservation.',
            'mission': 'To protect and sustainably manage marine resources.',
            'capital': 18000000,
            'stage': ['Series B', 'Series C'],
            'impact_value': 4.6,
            'team_values': ['Conservation', 'Sustainability', 'Innovation'],
            'team_motives': ['Marine Protection', 'Sustainable Fisheries', 'Biodiversity'],
            'languages': ['English', 'Japanese'],
            'investor_expertise': ['Marine Technology', 'Conservation Strategies'],
            'investor_value': ['Environmental Preservation', 'Sustainable Profit'],
            'exit_strategy': 'Public Offering',
            'type_of_investment': 'Equity',
            'market': 'Global marine conservation efforts',
            'sdg': {
                'SDG 14': 'Life Below Water'
            }
        },
        {
            'company_name': 'Future Education Fund',
            'location': 'Toronto, Canada',
            'industry': 'Education Technology',
            'type_of_business': 'Venture Fund',
            'linkedin': 'https://linkedin.com/company/futureeducationfund',
            'twitter': 'https://twitter.com/futureedufund',
            'description': 'Investing in technologies and platforms that democratize education globally.',
            'mission': 'To make quality education accessible to all.',
            'capital': 12000000,
            'stage': ['Seed', 'Series A'],
            'impact_value': 4.3,
            'team_values': ['Access', 'Quality', 'Innovation'],
            'team_motives': ['Education Access', 'Technology in Learning', 'Global Reach'],
            'languages': ['English', 'Mandarin'],
            'investor_expertise': ['EdTech', 'Online Learning Platforms'],
            'investor_value': ['Social Good', 'Growth Potential'],
            'exit_strategy': 'Acquisition by Global Tech Company',
            'type_of_investment': 'Equity',
            'market': 'Global education market',
            'sdg': {
                'SDG 4': 'Quality Education'
            }
        },
        {
            'company_name': 'Green Building Investors',
            'location': 'Amsterdam, Netherlands',
            'industry': 'Real Estate',
            'type_of_business': 'Investment Group',
            'linkedin': 'https://linkedin.com/company/greenbuildinginvestors',
            'twitter': 'https://twitter.com/greenbuildinvest',
            'description': 'Investing in high-efficiency green buildings across Europe.',
            'mission': 'To lead the shift towards sustainable construction and property management.',
            'capital': 35000000,
            'stage': 'Series A',
            'impact_value': 9.0,
            'team_values': ['integrity', 'Durability', 'Design'],
            'team_motives': ['Energy Efficiency', 'Sustainable Materials', 'Architectural Innovation'],
            'languages': ['English', 'German', 'Dutch'],
            'investor_expertise': ['Sustainable Building Projects', 'Energy Efficiency'],
            'investor_value': ['Long-term Sustainability', 'Profitability'],
            'exit_strategy': 'Real Estate Investment Trust (REIT) Listing',
            'type_of_investment': 'Equity',
            'market': 'European sustainable real estate market',
            'sdg': {
                'SDG 11': 'Sustainable Cities and Communities',
                'SDG 13': 'Climate Action'
            }
        },
        {
            'company_name': 'NextGen Energy Partners',
            'location': 'Denver, CO',
            'industry': 'Energy Storage',
            'type_of_business': 'Venture Capital',
            'linkedin': 'https://linkedin.com/company/nextgenenergypartners',
            'twitter': 'https://twitter.com/nextgenenergy',
            'description': 'Investing in next-generation energy storage solutions.',
            'mission': 'To enhance global energy security and efficiency.',
            'capital': 20000000,
            'stage': ['Series A', 'Series B'],
            'impact_value': 4.5,
            'team_values': ['Innovation', 'Sustainability', 'Efficiency'],
            'team_motives': ['Energy Storage', 'Technological Advancement', 'Market Leadership'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Energy Storage Technologies', 'Renewable Integration'],
            'investor_value': ['Technology Leadership', 'High Returns'],
            'exit_strategy': 'Strategic Sale',
            'type_of_investment': 'Equity',
            'market': 'Global energy storage and renewable integration market',
            'sdg': {
                'SDG 7': 'Affordable and Clean Energy',
                'SDG 9': 'Industry, Innovation, and Infrastructure'
            }
        },
        {
            'company_name': 'Global Health Innovations',
            'location': 'Geneva, Switzerland',
            'industry': 'Healthcare',
            'type_of_business': 'Venture Capital',
            'linkedin': 'https://linkedin.com/company/globalhealthinnovations',
            'twitter': 'https://twitter.com/globalhealthinnov',
            'description': 'Funding innovative health solutions that have a global impact.',
            'mission': 'To improve global health standards through innovation.',
            'capital': 40000000,
            'stage': ['Series B', 'Series C'],
            'impact_value': 4.9,
            'team_values': ['Innovation', 'Quality', 'Access'],
            'team_motives': ['Global Health', 'Medical Technology', 'Accessible Healthcare'],
            'languages': ['English', 'French', 'Arabic'],
            'investor_expertise': ['Public Health Innovations', 'Healthcare Technology'],
            'investor_value': ['Impact', 'Financial Returns'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global health technology market',
            'sdg': {
                'SDG 3': 'Good Health and Well-being'
            }
        },
        {
            'company_name': 'Green Capital',
            'location': 'Austin, TX',
            'industry': 'Renewable Energy',
            'type_of_business': 'Investment',
            'linkedin': 'https://linkedin.com/company/greencapital',
            'twitter': 'https://twitter.com/greencapital',
            'description': 'Focusing on sustainable energy investments.',
            'mission': 'To promote renewable energy solutions.',
            'capital': 15000000,
            'stage': ['Series A', 'Series B'],
            'impact_value': 5.0,
            'team_values': ['Sustainability', 'Innovation', 'Transparency'],
            'team_motives': ['Environmental Impact', 'Growth', 'Leadership'],
            'languages': ['English', 'French'],
            'investor_expertise': ['Renewable Energy', 'Sustainability'],
            'investor_value': ['Impact', 'Returns'],
            'exit_strategy': 'Acquisition',
            'type_of_investment': 'Debt',
            'market': 'Global renewable energy market',
            'sdg': {
                'SDG 7': 'Affordable and Clean Energy',
                'SDG 13': 'Climate Action'
            }
        }
    ]
    
        for i in range(10):
            Investor.objects.create(
                        user=users[i],
                        **investor_data[i]
                    )

        
        self.stdout.write(self.style.SUCCESS('Successfully created Investors'))


# crea nel database locale gli utenti con le email nella lista 'users' tutti con password bar
def users_samples():
    users = ['alexi@mail.com',
            'brielle@mail.com', 
            'caden@mail.com', 
            'daria@mail.com', 
            'elton@mail.com', 
            'fiona@mail.com', 
            'gareth@mail.com', 
            'helena@mail.com', 
            'ivan@mail.com', 
            'juliet@mail.com'
        ]
    for u in users:
        CustomUser.objects.create_user(email = u, password = 'bar')
    return users

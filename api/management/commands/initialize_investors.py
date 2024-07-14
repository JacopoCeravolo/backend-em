# management/commands/initialize_investor.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Investor
from users.models import CustomUser

class CommandInv(BaseCommand):
    help = 'Initialize an Investor instance with meaningful data'

    def handle(self, *args, **kwargs):
        # Assuming you have a user to assign to the investor
        user = get_user_model().objects.first()  # Get the first user (you should adjust this query according to your needs)
        
        investor_data = {
            'user': user,
            'company_name': 'Example Company',
            'location': 'Example Location',
            'industry': 'Example Industry',
            'type_of_business': 'Example Business Type',
            'linkedin': 'https://linkedin.com/example',
            'twitter': 'https://twitter.com/example',
            'description': 'Example description about the company',
            'mission': 'Example mission statement',
            'capital': '$10,000,000',
            'stage': ['Seed', 'Series A'],
            'impact_value': 4.5,
            'team_values': ['Innovation', 'Integrity', 'Diversity'],
            'team_motives': ['Growth', 'Impact', 'Excellence'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Technology', 'Healthcare'],
            'investor_value': ['Sustainability', 'Impact'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global market for XYZ',
            'sdg': ['SDG 1', 'SDG 8']
        }


        
        investor = Investor.objects.create(**investor_data)
        self.stdout.write(self.style.SUCCESS(f'Successfully created Investor: {investor.company_name}'))


# crea nel database locale gli utenti con le email nella lista 'users' tutti con password bar
def users_samples():
    users = [
    'emily.jones@fakemail.com',
    'michael.brown@mockemail.com',
    'sarah.connor@fauxmail.com',
    'david_lee@phantommail.com',
    'laura.wilson@bogusmail.com',
    'john.doe@fictionalemail.com',
    'jane_doe@samplemail.com'
    ]
    for u in users:
        user = CustomUser.objects.create_user(email = u, password = 'bar')
    return users

# inserisce il modello CustomUser in ogni dataset di un investitore
# con questo codice vengono creati 7 nuovi utenti e vengono creati 8 investitori ognuno associato a un utente diverso 
# (il primo è quello preimpostato 'jacopo@mail.com')
def investor_test():
    users = CustomUser.objects.all()
    investors=[
        {
            'user': users[0],
            'company_name': 'Tech Angels',
            'location': 'San Francisco, CA',
            'industry': 'Technology',
            'type_of_business': 'Venture Capital',
            'linkedin': 'https://linkedin.com/company/techangels',
            'twitter': 'https://twitter.com/techangels',
            'description': 'Investing in cutting-edge tech startups.',
            'mission': 'To support technological innovation.',
            'capital': '$10,000,000',
            'stage': ['Seed', 'Series A'],
            'impact_value': 4.5,
            'team_values': ['Innovation', 'Integrity', 'Diversity'],
            'team_motives': ['Growth', 'Impact', 'Excellence'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Technology', 'Healthcare'],
            'investor_value': ['Sustainability', 'Impact'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global technology market',
            'sdg': ['SDG 1', 'SDG 8']
        },
        {
            'user': users[1],
            'company_name': 'Green Capital',
            'location': 'Austin, TX',
            'industry': 'Renewable Energy',
            'type_of_business': 'Investment',
            'linkedin': 'https://linkedin.com/company/greencapital',
            'twitter': 'https://twitter.com/greencapital',
            'description': 'Focusing on sustainable energy investments.',
            'mission': 'To promote renewable energy solutions.',
            'capital': '$15,000,000',
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
            'sdg': ['SDG 7', 'SDG 13']
        },
        {
            'user': users[2],
            'company_name': 'Health Ventures',
            'location': 'Boston, MA',
            'industry': 'Healthcare',
            'type_of_business': 'Investment',
            'linkedin': 'https://linkedin.com/company/healthventures',
            'twitter': 'https://twitter.com/healthventures',
            'description': 'Investing in innovative healthcare solutions.',
            'mission': 'To improve global health through technology.',
            'capital': '$20,000,000',
            'stage': ['Seed', 'Series A'],
            'impact_value': 4.8,
            'team_values': ['Integrity', 'Innovation', 'Compassion'],
            'team_motives': ['Patient Care', 'Growth', 'Innovation'],
            'languages': ['English', 'Mandarin'],
            'investor_expertise': ['Healthcare', 'Biotechnology'],
            'investor_value': ['Mentorship', 'Funding'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global healthcare market',
            'sdg': ['SDG 3', 'SDG 9']
        },
        {
            'user': users[3],
            'company_name': 'Eco Investors',
            'location': 'Seattle, WA',
            'industry': 'Sustainability',
            'type_of_business': 'Investment',
            'linkedin': 'https://linkedin.com/company/ecoinvestors',
            'twitter': 'https://twitter.com/ecoinvestors',
            'description': 'Supporting eco-friendly startups.',
            'mission': 'To reduce environmental impact.',
            'capital': '$12,000,000',
            'stage': ['Seed', 'Series B'],
            'impact_value': 5.2,
            'team_values': ['Sustainability', 'Ethics', 'Innovation'],
            'team_motives': ['Environmental Impact', 'Growth', 'Success'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Sustainability', 'Manufacturing'],
            'investor_value': ['Impact', 'Returns'],
            'exit_strategy': 'Acquisition',
            'type_of_investment': 'Equity',
            'market': 'Global sustainability market',
            'sdg': ['SDG 12', 'SDG 13']
        },
        {
            'user': users[4],
            'company_name': 'Edu Invest',
            'location': 'New York, NY',
            'industry': 'Education',
            'type_of_business': 'Venture Capital',
            'linkedin': 'https://linkedin.com/company/eduinvest',
            'twitter': 'https://twitter.com/eduinvest',
            'description': 'Funding innovative educational technologies.',
            'mission': 'To transform education through technology.',
            'capital': '$25,000,000',
            'stage': ['Seed', 'Series A'],
            'impact_value': 4.9,
            'team_values': ['Education', 'Innovation', 'Access'],
            'team_motives': ['Learning', 'Growth', 'Excellence'],
            'languages': ['English', 'French'],
            'investor_expertise': ['Education', 'Technology'],
            'investor_value': ['Mentorship', 'Funding'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global education market',
            'sdg': ['SDG 4', 'SDG 9']
        },
        {
            'user': users[5],
            'company_name': 'Agri Fund',
            'location': 'Des Moines, IA',
            'industry': 'Agriculture',
            'type_of_business': 'Investment',
            'linkedin': 'https://linkedin.com/company/agrifund',
            'twitter': 'https://twitter.com/agrifund',
            'description': 'Investing in agricultural innovation.',
            'mission': 'To enhance agricultural productivity.',
            'capital': '$18,000,000',
            'stage': ['Seed', 'Series A'],
            'impact_value': 4.7,
            'team_values': ['Sustainability', 'Innovation', 'Growth'],
            'team_motives': ['Productivity', 'Growth', 'Success'],
            'languages': ['English', 'Spanish'],
            'investor_expertise': ['Agriculture', 'Technology'],
            'investor_value': ['Funding', 'Mentorship'],
            'exit_strategy': 'Acquisition',
            'type_of_investment': 'Equity',
            'market': 'Global agriculture market',
            'sdg': ['SDG 2', 'SDG 9']
        },
        {
            'user': users[6],
            'company_name': 'Smart Home Ventures',
            'location': 'San Jose, CA',
            'industry': 'Smart Home Technology',
            'type_of_business': 'Investment',
            'linkedin': 'https://linkedin.com/company/smarthomeventures',
            'twitter': 'https://twitter.com/smarthomeventures',
            'description': 'Investing in smart home technology.',
            'mission': 'To make homes smarter and more efficient.',
            'capital': '$22,000,000',
            'stage': ['Seed', 'Series A'],
            'impact_value': 4.6,
            'team_values': ['Innovation', 'Quality', 'Efficiency'],
            'team_motives': ['Growth', 'Success', 'Impact'],
            'languages': ['English', 'German'],
            'investor_expertise': ['Technology', 'Business'],
            'investor_value': ['Funding', 'Mentorship'],
            'exit_strategy': 'Acquisition',
            'type_of_investment': 'Equity',
            'market': 'Global smart home market',
            'sdg': ['SDG 9', 'SDG 11']
        },
        {
            'user': users[7],
            'company_name': 'BioTech Ventures',
            'location': 'San Diego, CA',
            'industry': 'Biotechnology',
            'type_of_business': 'Investment',
            'linkedin': 'https://linkedin.com/company/biotechventures',
            'twitter': 'https://twitter.com/biotechventures',
            'description': 'Supporting biotech startups.',
            'mission': 'To advance biotech research.',
            'capital': '$30,000,000',
            'stage': ['Seed', 'Series A'],
            'impact_value': 5.0,
            'team_values': ['Innovation', 'Integrity', 'Excellence'],
            'team_motives': ['Growth', 'Success', 'Impact'],
            'languages': ['English', 'Japanese'],
            'investor_expertise': ['Biotechnology', 'Healthcare'],
            'investor_value': ['Funding', 'Mentorship'],
            'exit_strategy': 'IPO',
            'type_of_investment': 'Equity',
            'market': 'Global biotechnology market',
            'sdg': ['SDG 3', 'SDG 9']
        }
    ]
    return investors



# crea gli investitori, prende come argomento il risultato di investor_test()
def bind_inv_users(investors):

    for i in investors:
       inv = Investor.objects.create(**i) 
       print(inv.user)


# se si esegue: python initialize_investors.py da shell lo script crea tutto
# per controllare i risultati bisogna eseguire:
# python3 manage.py shell 
# from api.models import Investor (dentro la shell)
# from users.models import CustomUser (dentro la shell)
# Investor.objects.all() (dentro la shell)
users = users_samples()
investors = investor_test()
bind_inv_users(investors)
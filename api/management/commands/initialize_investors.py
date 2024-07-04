# management/commands/initialize_investor.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Investor

class Command(BaseCommand):
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
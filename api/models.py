from django.conf import settings
from django.db import models

class Startup(models.Model):
    # User information
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Company Information
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    founding_date = models.DateField()
    legal_form = models.CharField(max_length=255)
    type_of_business = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    description = models.TextField()
    mission = models.TextField()
    
    # Product Information
    product_description = models.TextField()
    customer_problem = models.TextField()
    usp = models.TextField()
    
    # Financial Information
    capital = models.FloatField()
    stage = models.CharField(max_length=255)
    target_investor_n = models.CharField(max_length=255)
    use_of_funds = models.JSONField()
    financial_tables = models.TextField()
    already_invested_n = models.FloatField()
    
    # Impact Information
    impact_value = models.FloatField()
    
    # Team Information
    team_values = models.JSONField()
    team_motives = models.JSONField()
    funding_experience = models.JSONField()
    team_languages = models.JSONField()
    
    # Preferences Information
    investor_expertise = models.JSONField()
    investor_expectations = models.JSONField()
    exit_strategy = models.CharField(max_length=255)
    type_of_investment = models.CharField(max_length=255)

    
    # Market Information
    market = models.TextField()
    sdg = models.JSONField()

    def __str__(self):
        return self.name
    

class Investor(models.Model):
    # User information
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # General Information
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    type_of_business = models.CharField(max_length=255)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    description = models.TextField()
    mission = models.TextField()
    
    
    # Financial Information
    capital = models.JSONField()
    stage = models.JSONField()
    
    # Impact Information
    impact_value = models.FloatField()
    
    # Team Information
    team_values = models.JSONField()
    team_motives = models.JSONField()
    languages = models.JSONField()
    
    # Preferences Information
    investor_expertise = models.JSONField()
    investor_offering = models.JSONField(default='')
    investor_value = models.JSONField()
    exit_strategy = models.CharField(max_length=255)
    type_of_investment = models.CharField(max_length=255)

    
    # Market Information
    market = models.TextField()
    sdg = models.JSONField()

    def __str__(self):
        return self.company_name
    
    def get_user(self):
        return self.user.get_email()
    


from django.conf import settings
from django.db import models

class StartupDetails(models.Model):
    startup = models.OneToOneField('Startup', on_delete=models.CASCADE, related_name='details_section')
    company_address = models.CharField(max_length=255)
    company_code = models.CharField(max_length=50)
    company_city = models.CharField(max_length=100)
    mission = models.TextField()
    industry = models.CharField(max_length=100)
    legal_form = models.CharField(max_length=50)
    target_group = models.TextField()
    founding_date = models.DateField()
    website_url = models.URLField()
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)

class StartupOffering(models.Model):
    startup = models.OneToOneField('Startup', on_delete=models.CASCADE, related_name='offerings_section')
    product_description = models.TextField()
    customer_problem = models.TextField()
    unique_selling_point = models.TextField()

class StartupFinancials(models.Model):
    startup = models.OneToOneField('Startup', on_delete=models.CASCADE, related_name='financials_section')
    funding_required = models.DecimalField(max_digits=20, decimal_places=2)
    stage = models.CharField(max_length=100)
    investor_count = models.PositiveIntegerField()
    use_of_funds = models.JSONField()  # JSONField for storing detailed use of funds
    financial_statement = models.JSONField()  # JSONField for storing financial statements (e.g., revenue, costs)

class StartupImpact(models.Model):
    startup = models.OneToOneField('Startup', on_delete=models.CASCADE, related_name='impact_section')
    product_description = models.TextField()
    customer_problem = models.TextField()
    unique_selling_point = models.TextField()

class StartupTeam(models.Model):
    startup = models.OneToOneField('Startup', on_delete=models.CASCADE, related_name='team_section')
    founding_experience = models.TextField()
    languages = models.TextField()
    values = models.TextField()
    motivation = models.TextField()
    members = models.JSONField()  # Store team members details like name, email, job title, LinkedIn profile, etc.

class StartupMarket(models.Model):
    startup = models.OneToOneField('Startup', on_delete=models.CASCADE, related_name='market_section')
    target_market = models.TextField()
    number_of_competitors = models.PositiveIntegerField()
    market_size = models.DecimalField(max_digits=20, decimal_places=2)
    CAGR = models.DecimalField(max_digits=5, decimal_places=2)  # Compound Annual Growth Rate
    scalability = models.TextField()
    competitors = models.TextField()

class StartupMatchingPreferences(models.Model):
    startup = models.OneToOneField('Startup', on_delete=models.CASCADE, related_name='preferences_section')
    investor_type = models.CharField(max_length=100)
    investor_qualities = models.TextField()
    investment_instrument = models.CharField(max_length=100)
    exit_strategy = models.CharField(max_length=100)
    investor_expertise = models.TextField()

class Startup(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_startup')
    name = models.CharField(max_length=255)
    details = models.OneToOneField(StartupDetails, on_delete=models.CASCADE, related_name='startup_details', null=True, blank=True)
    offerings = models.OneToOneField(StartupOffering, on_delete=models.CASCADE, related_name='startup_offerings', null=True, blank=True)
    financials = models.OneToOneField(StartupFinancials, on_delete=models.CASCADE, related_name='startup_financials', null=True, blank=True)
    impact = models.OneToOneField(StartupImpact, on_delete=models.CASCADE, related_name='startup_impact', null=True, blank=True)
    team = models.OneToOneField(StartupTeam, on_delete=models.CASCADE, related_name='startup_team', null=True, blank=True)
    market = models.OneToOneField(StartupMarket, on_delete=models.CASCADE, related_name='startup_market', null=True, blank=True)
    preferences = models.OneToOneField(StartupMatchingPreferences, on_delete=models.CASCADE, related_name='startup_preferences', null=True, blank=True)

    def __str__(self):
        return self.name
    
class InvestorPreferences(models.Model):
    investor = models.OneToOneField('Investor', on_delete=models.CASCADE, related_name='preferences_section')
    target_market = models.TextField()
    languages = models.JSONField()  # Array of strings
    funding_stage = models.JSONField()  # Array of strings
    investment_instrument = models.JSONField()  # Array of strings
    exit_strategy = models.JSONField()  # Array of strings
    qualities = models.JSONField()  # Array of strings
    expertise = models.JSONField()  # Array of strings
    team_values = models.TextField()
    impact_level = models.PositiveIntegerField()  # Assuming impact level as integer range
    target_group = models.JSONField()  # Array of strings

class InvestorPortfolio(models.Model):
    investor = models.OneToOneField('Investor', on_delete=models.CASCADE, related_name='portfolio_section')
    previously_invested = models.JSONField()
    
class Investor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_investor')
    name = models.CharField(max_length=255)
    preferences = models.OneToOneField(InvestorPreferences, on_delete=models.CASCADE, related_name='investor_preferences', null=True, blank=True)
    portfolio =  models.OneToOneField(InvestorPortfolio, on_delete=models.CASCADE, related_name='investor_porfolio', null=True, blank=True)

    def __str__(self):
        return self.name

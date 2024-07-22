from django.db import models
from django.conf import settings
from api.models import Investor
from users.models import CustomUser
from api.models import Startup

# Create your models here.
class Matching(models.Model):
    startup = models.OneToOneField(Startup, on_delete=models.CASCADE)
    investor = models.OneToOneField(Investor, on_delete=models.CASCADE)
    match_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)

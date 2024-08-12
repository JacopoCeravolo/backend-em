from django.db import models
from django.conf import settings
from api.models import Investor
from users.models import CustomUser
from api.models import Startup


# Create your models here.
class Matching(models.Model):
    startup_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name= 'startup_user')
    investor_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='investor_user')
    match_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)



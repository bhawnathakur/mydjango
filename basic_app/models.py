from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    #create relationship not inherit
    user=models.OneToOneField(User,on_delete='CASCADE')
    #add any additional attribute
    portfolio_site=models.URLField(blank=True)
    picture_pic=models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
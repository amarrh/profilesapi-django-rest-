from django.db import models
from django.contrib.auth.models import User # nasljeđuje AbstractUser model koji ima korisne stvari poput username, emal itd

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOneField služi da bi svaki user imao pristup samo 1 profilu
    biography = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username # username je povučeno iz importovanog modela User, može se ovako vezati


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "statuses" # u djangi, doda ono "s"

    def __str__(self):
        return str(self.user_profile)
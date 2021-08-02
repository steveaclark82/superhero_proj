from django.db import models

# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego_name = models.CharField(max_length=50)
    primary_super_ability = models.CharField(max_length=50)
    secondary_super_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)

    def __str__(self):
        return self.name
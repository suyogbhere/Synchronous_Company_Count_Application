from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='files')    


def validate_year(value):
    if value and not value.isdigit():
        raise ValidationError(f"{value} is not a valid year.")
    if value and (int(value) < 1000 or int(value) > 9999):
        raise ValidationError(f"{value} is not a realistic year.")

class Company_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    year_founded = models.CharField(max_length=4,null=True,blank=True, validators=[validate_year])
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=200)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=200)
    linkedin_url = models.URLField()
    current_employee_estimate = models.IntegerField()
    total_employee_estimate = models.IntegerField()


    def save(self, *args, **kwargs):
        if self.year_founded:
            # Convert year_founded to string if it's not already
            self.year_founded = str(self.year_founded)
            # Remove decimals if present
            if '.' in self.year_founded:
                self.year_founded = str(int(float(self.year_founded)))
        super().save(*args, **kwargs)


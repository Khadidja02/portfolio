from django.db import models

# Create your models here.
class AboutMe(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    profession = models.CharField(max_length=500)
    github = models.URLField(max_length=300)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Skills(models.Model):
    skill_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skill_pictures/', blank=True, null=True)

    def __str__(self):
        return self.skill_name

class Services(models.Model):
    service_name = models.CharField(max_length=250)
    icon = models.CharField(max_length=300, default='default_icon') 
    description_services = models.TextField(blank=True, null=True)
    color_code = models.CharField(max_length=7, default='000000')
    
    def __str__(self):
        return self.service_name

class Portfolio(models.Model):  # Corrected the class name here
    project_title = models.CharField(max_length=250)
    project_description = models.TextField(blank=True, null=True)
    project_first_image = models.ImageField(upload_to='project_pictures/', blank=True, null=True)
    project_image = models.ManyToManyField('ProjectImage', blank=True)
    category = models.CharField(max_length=100)
    project_url = models.URLField(max_length=300)

    def __str__(self):
        return self.project_title

class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project_pictures/')

    def __str__(self):
        return self.image.name        

class ContactForm(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'

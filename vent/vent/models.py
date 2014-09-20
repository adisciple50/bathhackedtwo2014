from django.db import models
# Create your models here.


class Contributer (models.Model):
    Name = models.CharField(max_length=100, primary_key=True)
    ContactEmail = models.EmailField(name='Contact Email Address')
    def __unicode__(self):
        return self.Name
    def __str__(self):
        return self.Name

class PortfolioExample(models.Model):
    PEID = models.AutoField(primary_key=True, null=False)
    Title = models.CharField(unique=True, max_length=200)
    Picture = models.ImageField(upload_to='media/')  # folder '/UploadImages'
    Description = models.TextField(max_length=800)
    DateFinished = models.DateField(name='Date Completed')
    MainContributer = models.ForeignKey(Contributer)
    def __unicode__(self):  # really import to have this at the end of each model.Model
        return self.Title

    def __str__(self):
        return self.Title




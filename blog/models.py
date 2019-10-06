from django.db import models

# Create your models here. blog
#title
#pub_date
#text inside
#image
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    textinside = models.CharField(max_length= 200)
    title = models.CharField(max_length= 200)
    pubdate= models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.textinside[:100]

    def pub_date_pretty(self):
        return self.pubdate.strftime('%b %e %Y')

# add the blog app to the local_settings

# create migration

# migrate

#add to teh admin

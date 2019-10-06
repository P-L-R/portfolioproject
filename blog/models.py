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



# add the blog app to the local_settings

# create migration

# migrate

#add to teh admin

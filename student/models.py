from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#student.user.username
    middleName = models.CharField(max_length=200, null=True)#student.middlename
    phoneNo = models.CharField(max_length=14, null=True)
    school = models.CharField(max_length=255, null=False)
    course = models.CharField(max_length=255, null=False)
    yearOfStudy = models.CharField(max_length=10, null=False)
    headline = models.CharField(max_length=50, null=True)
    field = models.CharField(max_length=50, null=True)
    profilePic = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):#overwriting the save method so as to resize the image before saving
        super().save(*args, **kwargs)

        img = Image.open(self.profilePic.path) #overwriting the save method to resize the image before saving
        if img.height>300 or img.width>300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profilePic.path)

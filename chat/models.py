from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='profile-image/')
    frinds = models.ManyToManyField("Frind",related_name='frinds')

    class Meta:
        '''Meta definition for Profile.'''

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return  self.user.username 
    

class Frind(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for Frind.'''

        verbose_name = 'Frind'
        verbose_name_plural = 'Frinds'

    def __str__(self):
        return self.profile.name
    

class ChatMessage(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(Profile, related_name="sender_msg",on_delete=models.CASCADE)
    reciever = models.ForeignKey(Profile, related_name="recieve_msg",on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Meta definition for ChatMessage.'''

        verbose_name = 'ChatMessage'
        verbose_name_plural = 'ChatMessages'

    def __str__(self):
        return f'Msg From > {self.sender} - To > {self.reciever}'
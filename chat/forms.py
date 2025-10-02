from django import forms
from .models  import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ChatForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class':'flex items-center h-10 w-full rounded px-3 text-sm rounded-2xl','placeholder':'Enter A Message'}),label='')  
    class Meta:
      model = ChatMessage
      fields = ['body',]


class UserForm(UserCreationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder':'Ahmed Ragep'}))
   email = forms.CharField(widget=forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder':'Youremail@gmail.com'}))
   password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder':'••••••••'}))
   password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder':'••••••••'}))
   class Meta:
      model = User
      fields = ('username','email','password1','password2')



from django.contrib.auth.forms import AuthenticationForm

class loginclassForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(loginclassForm, self).__init__(*args, **kwargs)
        # قم بتعيين الكلاسات CSS المطلوبة لكل حقل
        self.fields['username'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['password'].widget.attrs.update({'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})

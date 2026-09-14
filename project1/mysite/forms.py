from django import forms
from django.contrib.auth import get_user_model

class UserCreationForm(forms.ModelForm):
    password = forms.forms.CharField(max_length=20)
    
    class Meta:
        model = get_user_model()
        fields = ("email")
        
    def clan_password(self):
        password = self.cleaned_data.get("password")
        return password
        
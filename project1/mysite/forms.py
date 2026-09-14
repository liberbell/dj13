from django import forms
from django.contrib.auth import get_user_model

class UserCreationForm(forms.ModelForm):
    password = forms.forms.CharField(max_length=20)
    
    class Meta:
        model = get_user_model()
        fields = ("email")
        
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password
    
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            
        return user
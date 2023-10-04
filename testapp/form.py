from django import forms
from testapp.models import Login

class Loginform(forms.ModelForm):
    firstname=forms.CharField()
    lastname=forms.CharField()
    Phone=forms.CharField()
    email=forms.EmailField()
    
    class Meta:
        model = Login
        fields = '__all__'
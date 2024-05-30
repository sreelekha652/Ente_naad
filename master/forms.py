from django import forms
from django.forms import ModelForm
from .models import *
class Panchayath_Add_Form(forms.ModelForm):

    class Meta:
        model = Panchayath
        fields = ['district','name', 'Phone', 'email','username', 'password']
        widgets = {
            'district':forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            
          
        }

    def __init__(self, *args, **kwargs):
        super(Panchayath_Add_Form, self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.all()


class Panchayath_Edit_Form(forms.ModelForm):

    class Meta:
        model = Panchayath
        fields = ['district','name', 'Phone', 'email','username',]
        widgets = {
            'district':forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
           
            
          
        }

    def __init__(self, *args, **kwargs):
        super(Panchayath_Edit_Form, self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.all()


class Corporation_Add_Form(forms.ModelForm):

    class Meta:
        model = Corporation
        fields = ['district','name', 'Phone', 'email','username', 'password']
        widgets = {
            'district':forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            
          
        }

    def __init__(self, *args, **kwargs):
        super(Corporation_Add_Form, self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.all()


class Corporation_Edit_Form(forms.ModelForm):

    class Meta:
        model = Corporation
        fields = ['district','name', 'Phone', 'email','username',]
        widgets = {
            'district':forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
           
            
          
        }

    def __init__(self, *args, **kwargs):
        super(Corporation_Edit_Form, self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.all()


class Muncipality_Add_Form(forms.ModelForm):

    class Meta:
        model = Muncipality
        fields = ['district','name', 'Phone', 'email','username', 'password']
        widgets = {
            'district':forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            
          
        }

    def __init__(self, *args, **kwargs):
        super(Muncipality_Add_Form, self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.all()


class Muncipality_Edit_Form(forms.ModelForm):

    class Meta:
        model = Muncipality
        fields = ['district','name', 'Phone', 'email','username',]
        widgets = {
            'district':forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
           
            
          
        }

    def __init__(self, *args, **kwargs):
        super(Muncipality_Edit_Form, self).__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.all()
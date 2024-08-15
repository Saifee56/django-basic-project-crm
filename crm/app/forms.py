from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"First Name"}), label="")
	last_name = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name"}), label="")
	email = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Email"}), label="")
	address = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Address"}), label="")
	city = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"City"}), label="")
	state = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"State"}), label="")


	class Meta:
		model = Record
		exclude = ("user",)    
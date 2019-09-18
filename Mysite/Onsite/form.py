from django import forms
from .models import Student
from .models import Emp


class EmpForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = "__all__"
        # fields=['first_name','last_name','contact','emial','age']



class eneform(forms.Form):
    username=forms.CharField(label="enter the username",max_length=20)
    password=forms.CharField(label="enter the password",max_length=20)
    forget=forms.CharField(label="forget the password",max_length=20)
    file=forms.FileField()# creating file input
    class Meta:
        model=Emp
        fields="__all__"
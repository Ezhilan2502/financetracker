from django import forms
from .models import Transaction,Goal
from decimal import Decimal

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=['title','amount','transaction_type','category','date']
        widgets={
            'date':forms.DateInput(attrs={'type':'date'}),
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model=Goal
        fields=['name','target_amount','target_date']
        widgets={
            'target_date':forms.DateInput(attrs={'type':'date'}),
        }
class RegisterForm(forms.Form):
    name = forms.CharField(max_length=150)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
class ForgetPasswordForm(forms.Form):
    email=forms.EmailField()
    otp=forms.CharField(max_length=6,required=False)
    new_password=forms.CharField(widget=forms.PasswordInput(),required=False)
    confirm_password=forms.CharField(widget=forms.PasswordInput(),required=False)

    def clean(self):
        cleaned_data=super().clean()
        pw1=cleaned_data.get('new_password')
        pw2=cleaned_data.get('confirm_password')

        if pw1 and pw2 and pw1!=pw2:
            raise forms.ValidationError("Passwords do not match")
        
        
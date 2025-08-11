from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal,ROUND_HALF_UP
from django.utils import timezone
from datetime import timedelta
import random
# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES=[
        ('IN','Income'),
        ('EX','Expense'),
        ('SA','Savings'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    transaction_type=models.CharField(max_length=2,choices=TRANSACTION_TYPES)
    category=models.CharField(max_length=50,blank=True,null=True)
    date=models.DateField(editable=True)

    goal=models.ForeignKey('Goal',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.title} -  ₹{self.amount}"
    
class Goal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    target_amount=models.DecimalField(max_digits=10,decimal_places=2)
    current_saved_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    target_date=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ₹{self.target_amount}"
    
    @property
    def percentage_complete(self):
        if self.target_amount>0:
            return round((self.current_saved_amount/self.target_amount)*100,2)
        return Decimal('0.00')
    
    @property
    def amount_remaining(self):
        remaining=self.target_amount-self.current_saved_amount
        return max(Decimal('0.00'),remaining)
    
    @property
    def days_remaining(self):
        if self.target_date:
            delta=self.target_date-timezone.now().date()
            return max(delta.days,0)
        return None
   
    @property
    def monthly_contribution_needed(self):
        days_left=self.days_remaining
        if days_left and days_left>0:
            remaining_amount=self.target_amount-self.current_saved_amount
            months_remaining=Decimal(days_left/Decimal(30))
            if months_remaining>0:
                monthly_amount=remaining_amount/months_remaining
                return monthly_amount.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
        return Decimal('0.00')

class EmailOTP(models.Model):
    email=models.EmailField()
    otp=models.CharField(max_length=6)
    created_at=models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now()>self.created_at+timedelta(minutes=3)
    def __str__(self):
        return f"{self.email} - {self.otp}"
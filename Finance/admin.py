from django.contrib import admin
from . models import Transaction,Goal
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display=('user','title','amount','transaction_type','category','date')
    list_filter=('transaction_type','category','date')
    search_fields=('title','user__username')

admin.site.register(Goal)

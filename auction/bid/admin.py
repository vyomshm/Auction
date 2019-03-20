from django.contrib import admin
from .models import *

class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'bid_count', 'current_highest_bid', 'active', 'start_day', 'end_day']

class BidAdmin(admin.ModelAdmin):
    list_display = ['auction', 'bid_amount', 'bidder', 'created_at', 'email_sent', 'email_sent_at']
    list_filter = (
        ('auction',)
    )

admin.site.register(AuctionItem, AuctionItemAdmin)
admin.site.register(Bid, BidAdmin)
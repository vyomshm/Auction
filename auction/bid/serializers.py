from rest_framework import serializers
from auction.bid import models

class AuctionItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.AuctionItem
		fields = (
			'id', 
			'name', 
			'description', 
			'image_url', 
			'created_at', 
			'current_highest_bid', 
			'starting_amount', 
			'start_day', 
			'end_day', 
			'active',
			'owner', 
			'bid_count',
		)

class BidSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Bid
		fields = (
			'id', 
			'auction',
			'bid_amount',
			'bidder',
			'created_at',
			'email_sent',
			'email_sent_at',
		)
		
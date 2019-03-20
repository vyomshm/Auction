from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from auction.bid.managers import AuctionManager, BidManager
import pendulum

class AuctionItem(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	image_url = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	current_highest_bid = models.FloatField(default=100)
	starting_amount = models.FloatField()
	start_day = models.DateField(default=pendulum.today)
	end_day = models.DateField(default=pendulum.tomorrow)
	active = models.BooleanField(default=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	bid_count = models.IntegerField(default=0)

	objects = models.Manager()
	AuctionManager = AuctionManager()

class Bid(models.Model):
	auction = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
	bid_amount = models.FloatField()
	bidder = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	email_sent = models.BooleanField(default=False)
	email_sent_at = models.DateTimeField(blank=True, null=True)

	objects = models.Manager()
	BidManager = BidManager()
    
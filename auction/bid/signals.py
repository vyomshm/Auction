from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from auction.bid.models import *

@receiver(post_save, sender=Bid)
def update_auction_1(sender, instance, created, **kwargs):
	if created:
		auction = instance.auction
		auction.bid_count = Bid.BidManager.current(auction).count()
		if(instance.bid_amount > auction.current_highest_bid):
			auction.current_highest_bid = instance.bid_amount
		auction.save()

@receiver(post_delete, sender=Bid)
def update_auction_2(sender, instance, **kwargs):
	auction = instance.auction
	bids = Bid.BidManager.current(auction)

	# update current_highest_bid and bid_count for an auction
	auction.bid_count = bids.count()
	current_highest_bid = 0
	if instance.bid_amount == auction.current_highest_bid:
		for bid in bids:
			if bid.bid_amount > current_highest_bid:
				current_highest_bid = bid.bid_amount
	auction.current_highest_bid = current_highest_bid
	auction.save()
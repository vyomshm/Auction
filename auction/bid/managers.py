from django.db import models

class AuctionManager(models.Manager):
	def active(self):
		return super().get_queryset().filter(active=True)

	def expired(self):
		return super().get_queryset().filter(active=False)

class BidManager(models.Manager):
	def current(self, auction):
		return super().get_queryset().filter(auction=auction).order_by('-created_at')

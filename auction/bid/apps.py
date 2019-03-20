from django.apps import AppConfig

class BidConfig(AppConfig):
    name = 'auction.bid'

    def ready(self):
    	from auction.bid import signals

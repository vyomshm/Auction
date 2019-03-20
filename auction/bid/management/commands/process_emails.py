from django.core.management.base import BaseCommand, CommandError
from auction.bid.models import *
from django.core.mail import send_mail
import pendulum


class Command(BaseCommand):
    help = 'Runs through email queue and sends emails'
    
    def handle(self, *args, **options):
        self.send_auction_email()     

    def send_auction_email(self):
        auctions = AuctionItem.AuctionManager.active()
        for auction in auctions:
            print(auction.end_day)
            highest_bid = 0
            if auction.end_day == pendulum.tomorrow().date():
                highest_bid = auction.current_highest_bid
                bids = Bid.BidManager.current(auction)
                for idx, bid in enumerate(bids):
                    self.send_email(bid, highest_bid)

    def send_email(self, bid):
        try:
            ## SMTP mail integration SendGrid
            if(bid.bidder.email != ''):
                send_mail(
                    'Auction Concluded',
                    'Winning Bid = ${} by {}'.format(
                        bid.bid_amount, bid.bidder.username),
                    'vyom.sharma@auction.com',
                    [bid.bidder.email],
                    fail_silently=False
                )
                print("Email sent to - {0}".format(bid.bidder.email))
                self.update_bid(bid)
            else:
                print("Email not registered by bidder")
        except:
            raise CommandError("Email could not send for reason XYZ")
    
    def update_bid(self, bid):
        bid.email_sent = True
        bid.email_sent_at = pendulum.now()
        bid.save()

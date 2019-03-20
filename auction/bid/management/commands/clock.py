from auction.bid.models import *
from django.core.mail import send_mail
import pendulum
from apscheduler.schedulers.blocking import BlockingScheduler

def send_auction_email():
    auctions = AuctionItem.AuctionManager.active()
    for auction in auctions:
        highest_bid = 0
        if auction.end_day == pendulum.tomorrow().date():
            highest_bid = auction.current_highest_bid
            bids = Bid.BidManager.current(auction)
            for idx, bid in enumerate(bids):
                send_email(bid, highest_bid)

def send_email(bid):
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
            update_bid(bid)
        else:
            print("Email not registered by bidder")
    except:
        print("Email could not send for reason XYZ")

def update_bid(bid):
    bid.email_sent = True
    bid.email_sent_at = pendulum.now()
    bid.save()

sched = BlockingScheduler()

@sched.scheduled_job('cron', minute=59, hour=23, second=0)
def scheduled_job():
    send_auction_email()

sched.start()
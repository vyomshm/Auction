from rest_framework import routers
from auction.bid import views

router = routers.DefaultRouter()
router.register(r'auctions', views.AuctionItemViewSet)
router.register(r'active', views.ActiveItemsViewSet, basename='active')
router.register(r'expired', views.ExpiredItemsViewSet, basename='expired')
router.register(r'concluded', views.PreviousItemsViewSet, basename='concluded')
router.register(r'upcoming', views.UpcomingItemsViewSet, basename='upcoming')
router.register(r'bids', views.BidViewSet)

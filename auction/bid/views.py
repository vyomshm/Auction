from rest_framework import viewsets
from rest_framework.response import Response
from auction.bid import models, serializers
import pendulum

class AuctionItemViewSet(viewsets.ModelViewSet):
	queryset = models.AuctionItem.objects.all()
	serializer_class = serializers.AuctionItemSerializer

class ActiveItemsViewSet(viewsets.ViewSet):
	def list(self, request):
		queryset = models.AuctionItem.AuctionManager.active()
		serializer = serializers.AuctionItemSerializer(queryset, many=True)
		return Response(serializer.data)

class ExpiredItemsViewSet(viewsets.ViewSet):
	def list(self, request):
		queryset = models.AuctionItem.AuctionManager.expired()
		serializer = serializers.AuctionItemSerializer(queryset, many=True)
		return Response(serializer.data)

class PreviousItemsViewSet(viewsets.ViewSet):
	def list(self, request):
		queryset = models.AuctionItem.objects.filter(end_day__lt=pendulum.today())
		serializer = serializers.AuctionItemSerializer(queryset, many=True)
		return Response(serializer.data)

class UpcomingItemsViewSet(viewsets.ViewSet):
	def list(self, request):
		queryset = models.AuctionItem.objects.filter(start_day__gt=pendulum.today())
		serializer = serializers.AuctionItemSerializer(queryset, many=True)
		return Response(serializer.data)

class BidViewSet(viewsets.ModelViewSet):
	queryset = models.Bid.objects.all()
	serializer_class = serializers.BidSerializer

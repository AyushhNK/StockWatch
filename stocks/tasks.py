from celery import shared_task
from .models import Stock, StockPrice
import random

@shared_task
def fetch_stock_price(stock_id):
    stock = Stock.objects.get(id=stock_id)
    price = random.uniform(100, 500)
    StockPrice.objects.create(stock=stock, price=price)

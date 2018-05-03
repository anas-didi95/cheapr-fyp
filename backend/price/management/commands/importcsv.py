from django.core.management.base import BaseCommand, CommandError
import csv
from random import random, randint
from supermarket.models import Supermarket
from product.models import Product
from price.models import Price

class Command(BaseCommand):
  help = 'Import CSV file into database'

  def add_arguments(self, parser):
    parser.add_argument('name', 
      nargs='?',
      help='The name of CSV file')
    parser.add_argument('-m', '--mock',
      action='store_true',
      dest='mock',
      help='Import CSV file into database append with dummy data',
    )

  def handle(self, *args, **options):
    file_name = options['name']
    oldcount = Price.objects.count()
    if options['mock']:
      supermarkets = ['EconSave', 'Tesco', 'Giant']
      for supermarket in supermarkets:
        self.importCSV(file_name, supermarket=supermarket)
    else:
      self.importCSV(file_name)
    newcount = Price.objects.count()
    self.stdout.write(self.style.SUCCESS(
      'Import completed. New item insert: %d' % (newcount-oldcount)
    ))

  def importCSV(self, file_name, **kwargs):
    with open(file_name) as csv_file:
      read_csv = csv.reader(csv_file, delimiter=',')
      for row in read_csv:
        (name, description, category, price, currency, 
          day_start, day_end, month_start, month_end, year_start, year_end, 
          supermarket) = row
        if 'supermarket' in kwargs:
          if supermarket != kwargs['supermarket']:
            supermarket = kwargs['supermarket']
            op = randint(0,1)
            price = float(price)+random() if (op==1) else float(price)-random()
            # price = (op == 0 ? float(price)+random() : float(price)-random()) 
        supermarket_obj, _ = Supermarket.objects.get_or_create(
          name=supermarket
        )
        product_obj, _ = Product.objects.get_or_create(
          name=name,
          category=category,
        )
        price_obj, _ = Price.objects.get_or_create(
          price_value=price,
          currency_value=currency,
          day_start=day_start,
          day_end=day_end,
          month_start=month_start,
          month_end=month_end,
          year_start=year_start,
          year_end=year_end,
          description=description,
          product=product_obj,
          supermarket=supermarket_obj,
        )
        self.stdout.write('%s' % (price_obj))
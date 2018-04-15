from django.test import TestCase
from faker import Faker
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from supermarket.models import Supermarket
from product.models import Product
from .models import Price

class ModelTestCase(TestCase):
  """Test suite for model Price"""
  faker = Faker()
  price_value = 1.20
  currency_value = 1.20
  date_start = '18/04/15'
  date_end = '18/04/15'
  description = faker.text()
  product_category = 'snack'

  def setUp(self):
    self.supermarket = Supermarket.objects.create(
      name=self.faker.company()
    )
    self.product = Product.objects.create(
      name=self.faker.name(),
      category=self.product_category,
      supermarket=self.supermarket,
    )
    self.price = Price(
      price_value=self.price_value,
      currency_value=self.currency_value,
      date_start=self.date_start,
      date_end=self.date_end,
      description=self.description,
      product=self.product,
    )
    self.price.save()

  def testModelPriceCreate(self):
    old_count = Price.objects.count()
    Price.objects.create(
      price_value=self.price_value,
      currency_value=self.currency_value,
      date_start=self.date_start,
      date_end=self.date_end,
      description=self.description,
      product_id=self.product.id,
    )
    new_count = Price.objects.count()
    self.assertNotEqual(old_count, new_count)

  def testModelPriceRetrieve(self):
    price = Price.objects.get(
      price_value=self.price_value,
      currency_value=self.currency_value,
      date_start=self.date_start,
      date_end=self.date_end,
      description=self.description,
    )
    self.assertEqual(price.id, self.price.id)

  def testModelPriceUpdate(self):
    price_new_price_value = 2.00
    Price.objects.filter(pk=self.price.id).update(
      price_value=price_new_price_value
    )
    self.price.refresh_from_db()
    self.assertEqual(self.price.price_value, price_new_price_value)

  def testModelPriceDestroy(self):
    old_count = Price.objects.count()
    Price.objects.get(
      pk=self.price.id
    ).delete()
    new_count = Price.objects.count()
    self.assertNotEqual(old_count, new_count)

class ViewTestCase(APITestCase):
  """Test suite for view Price"""

  faker = Faker()
  price_value = 1.20
  currency_value = 1.20
  date_start = '18/04/15'
  date_end = '18/04/15'
  description = faker.text()
  product_category = 'snack'
  client = APIClient()

  def setUp(self):
    self.supermarket = Supermarket.objects.create(
      name=self.faker.company()
    )
    self.product = Product.objects.create(
      name=self.faker.name(),
      category=self.product_category,
      supermarket=self.supermarket,
    )
    self.product_data = {
      'price_value':self.price_value,
      'currency_value':self.currency_value,
      'date_start':self.date_start,
      'date_end':self.date_end,
      'description':self.description,
      'product':self.product.id,
    }
    self.response = self.client.post(
      reverse('price.l-c'),
      self.product_data,
      format='json',
    )

  def testViewPriceCreate(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def testViewPriceList(self):
   response = self.client.get(
     reverse('price.l-c'),
     format='json',
   ) 
   self.assertEqual(response.status_code, status.HTTP_200_OK)
   self.assertContains(response, self.price_value)
   self.assertContains(response, self.currency_value)

  def testViewPriceRetrieve(self):
    price = Price.objects.get(
      price_value=self.price_value,
      currency_value=self.currency_value,
      date_start=self.date_start,
      date_end=self.date_end,
      description=self.description,
    )
    response = self.client.get(
      reverse('price.r-u-d', kwargs={'pk':price.id}),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, price.price_value)
    self.assertContains(response, price.currency_value)

  def testViewPriceUpdate(self):
    price = Price.objects.get(
      price_value=self.price_value,
      currency_value=self.currency_value,
      date_start=self.date_start,
      date_end=self.date_end,
      description=self.description,
    )
    price_new_data = {
      'price_value':4.12,
      'description':self.faker.sentence()
    }
    response = self.client.patch(
      reverse('price.r-u-d', kwargs={'pk':price.id}),
      price_new_data,
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, price_new_data['price_value'])
    self.assertContains(response, price_new_data['description'])

  def testViewProductDestroy(self):
    price = Price.objects.get(
      price_value=self.price_value,
      currency_value=self.currency_value,
      date_start=self.date_start,
      date_end=self.date_end,
      description=self.description,
    )
    response = self.client.delete(
      reverse('price.r-u-d', kwargs={'pk':price.id}),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 
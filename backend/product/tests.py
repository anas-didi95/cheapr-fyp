from django.test import TestCase
from rest_framework.test import APITestCase
from faker import Faker
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from supermarket.models import Supermarket
from .models import Product

class ModelTestCase(TestCase):
  """Test suite for model Product"""
  faker = Faker()
  product_name = faker.name()
  product_category = 'snack'
  supermarket_name = faker.company()

  def setUp(self):
    self.supermarket = Supermarket.objects.create(name=self.supermarket_name)
    self.product = Product(
      name=self.product_name,
      category=self.product_category,
      supermarket=self.supermarket,
    )
    self.product.save()

  def testModelProductCreate(self):
    old_count = Product.objects.count()
    Product.objects.create(
      name=self.faker.name(),
      category=self.product_category,
      supermarket_id=self.supermarket.id,
    )
    new_count = Product.objects.count()
    self.assertNotEqual(old_count, new_count)

  def testModelProductRetrieve(self):
    product = Product.objects.get(
      name=self.product_name,
    )
    self.assertEqual(product.name, self.product_name)

  def testModelProductUpdate(self):
    product_new_name = self.faker.name()
    product = Product.objects.get(
      name=self.product_name,
    )
    Product.objects.filter(pk=product.id).update(
      name=product_new_name
    )
    product.refresh_from_db()
    self.assertEqual(product.name, product_new_name)

  def testModelProductDestroy(self):
    old_count = Product.objects.count()
    Product.objects.get(
      name=self.product_name
    ).delete()
    new_count = Product.objects.count()
    self.assertNotEqual(old_count, new_count)

class ViewTestCase(APITestCase):
  """Test suite for view Product"""
  faker = Faker()
  product_name = faker.name()
  product_category = 'snack'
  client = APIClient()

  def setUp(self):
    self.supermarket = Supermarket.objects.create(
      name=self.faker.company()
    )
    self.product_data = {
      'name':self.product_name,
      'category':self.product_category,
      'supermarket':self.supermarket.name,
    }
    self.response = self.client.post(
      reverse('product.l-c'),
      self.product_data,
      format='json',
    )
  
  def testViewProductCreate(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

  def testViewProductList(self):
    response = self.client.get(
      reverse('product.l-c'),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, self.product_name)

  def testViewProductRetrieve(self):
    product = Product.objects.get()
    response = self.client.get(
      reverse('product.r-u-d', kwargs={'pk':product.id}),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, self.product_name)
  
  def testViewProductUpdate(self):
    product = Product.objects.get()
    product_new_data = {
      'name':self.faker.name(),
      'category':product.category,
      'supermarket':product.supermarket.name,
    }
    response = self.client.patch(
      reverse('product.r-u-d', kwargs={'pk':product.id}),
      product_new_data,
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, product_new_data['name'])

  def testViewProductDestroy(self):
    product = Product.objects.get()
    response = self.client.delete(
      reverse('product.r-u-d', kwargs={'pk':product.id}),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
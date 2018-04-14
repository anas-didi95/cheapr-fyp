from django.test import TestCase
from faker import Faker
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Supermarket

class ModelTestCase(TestCase):
  """Test suite for model Supermarket"""
  faker = Faker()
  supermarket_name = faker.company()

  def setUp(self):
    self.supermarket = Supermarket(name=self.supermarket_name)
    self.supermarket.save()

  def testModelSupermarketCreate(self):
    old_count = Supermarket.objects.count()
    Supermarket.objects.create(name=self.faker.company())
    new_count = Supermarket.objects.count()
    self.assertNotEqual(old_count, new_count)

  def testModelSupermarketRetrieve(self):
    supermarket = Supermarket.objects.get(name=self.supermarket_name)
    self.assertEquals(supermarket.name, self.supermarket_name)

  def testModelSupermarketUpdate(self):
    new_supermarket_name = self.faker.company()
    supermarket = Supermarket.objects.get(name=self.supermarket_name)
    Supermarket.objects.filter(pk=supermarket.pk).update(name=new_supermarket_name)
    supermarket.refresh_from_db()
    self.assertEquals(supermarket.name, new_supermarket_name)

  def testModelSupermarketDestroy(self):
    old_count = Supermarket.objects.count()
    Supermarket.objects.get(name=self.supermarket_name).delete()
    new_count = Supermarket.objects.count()
    self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
  """Test suite for view Supermarket"""
  faker = Faker()
  supermarket_name = faker.company()

  def setUp(self):
    self.client = APIClient()
    self.supermarket_data = {'name': self.supermarket_name}
    self.response = self.client.post(
      reverse('supermarket.l-c'),
      self.supermarket_data,
      format='json'
    )

  def testViewSupermarketCreate(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
  
  def testViewSupermarketList(self):
    response = self.client.get(
      reverse('supermarket.l-c'),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def testViewSupermarketRetrieve(self):
    supermarket = Supermarket.objects.get()
    response = self.client.get(
      reverse('supermarket.r-u-d', kwargs={'pk':supermarket.id}),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, supermarket)

  def testViewSupermarketUpdate(self):
    supermarket = Supermarket.objects.get()
    supermarket_new_data = {'name': self.faker.company()}
    response = self.client.put(
      reverse('supermarket.r-u-d', kwargs={'pk':supermarket.id}),
      supermarket_new_data,
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, supermarket_new_data['name'])

  def testViewSupermarketDestroy(self):
    supermarket = Supermarket.objects.get()
    response = self.client.delete(
      reverse('supermarket.r-u-d', kwargs={'pk':supermarket.id}),
      format='json',
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
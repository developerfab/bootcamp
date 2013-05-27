"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

def fibo(x):
    if x==1 or x==2:
        return x
    return fibo(x-1)+fibo(x-2)

class FibonacciTest(TestCase):
    def test_fibo_de_1_es_1(self):
        """
        Tests que prueba que fibo de 1 sea 1.
        """
        self.assertEqual(fibo(1), 1)

    def test_fibo_de_2_es_2(self):
	"""
	Test que prueba que fibo de 2 sea 2
	"""
	self.assertEqual(fibo(2),2)

    def test_fibo_de_3_es_3(self):
	"""
	Test que prueba que fibo de 3 sea 3
	"""
	self.asserEqual(fibo(3),3)

    def test_fibo_n_es_la_suma_de_los_2_anterioes
	self.asserEqual(fibo(10),89)

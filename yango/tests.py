"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class Primo(TestCase):

    def test_primo_de_4_es_2(self):
	"""
	Test que comprueba 
	"""
	num=primo(4)
        self.assertEqual(num[2],True)

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

def multiplos(lim):
    x=1
    sum=0
    mult3=0
    mult5=0
    while mult3<lim:
        sum=sum+mult3
        mult3=3*x
        x=x+1
    x=1
    while mult5<lim:
        sum=sum+mult5
        mult5=5*x
        x=x+1
    print sum
    return sum

class Multiplos(TestCase):
    def test_suma_multiplos_3_y_5_de_10_es_23(self):
	"""
	Test que prueba que la suma de las multiplos de 3 y 5 menores que 10 es 23
	"""
	self.assertEqual(multiplos(10),23)

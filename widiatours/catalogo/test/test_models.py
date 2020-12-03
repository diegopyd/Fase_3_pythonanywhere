from django.test import TestCase
from catalogo.models import Compra

class CompraTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Compra.objects.create(codigo='054cfe92-6e6c-45cc-972b-68896913bfdb', name='zapatilla', precio=1234, descripcion="hola")

    def test_first_name_label(self):
        compra = Compra.objects.get(codigo='054cfe92-6e6c-45cc-972b-68896913bfdb')
        field_label= compra._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

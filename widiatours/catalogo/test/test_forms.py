from django.test import TestCase
from catalogo.models import Compra

class CompraTest(TestCase):

   class CompraFormsTest(TestCase):
    def test_valid_form(self):
        g = Genre.objects.create(name='Prueba1', summary='Prueba')
        data = {'name': g.name, 'summary': g.summary,}
        form = GenreForm(data=data)
        self.assertTrue(form.is_valid())
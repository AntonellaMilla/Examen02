# biblioteca/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Libro, Autor, Categoria

class LibroApiTests(APITestCase):
    
    def setUp(self):
        """
        Configura los datos necesarios antes de cada prueba.
        """
        # Crear un autor y una categoría para los libros
        self.autor = Autor.objects.create(nombre="Autor 1", biografia="Biografía del autor")
        self.categoria = Categoria.objects.create(nombre="Ficción")

        # Crear un libro de ejemplo
        self.libro_data = {
            'titulo': 'Libro de Prueba',
            'autor': self.autor.id,
            'categoria': self.categoria.id,
            'fecha_publicacion': '2021-01-01',
            'isbn': '1234567890123'
        }
        
        # Crear un libro en la base de datos
        self.libro = Libro.objects.create(**self.libro_data)
        
        # Definir la URL para acceder a los libros
        self.url = reverse('libro-list')  # Asumiendo que la ruta para listar libros es 'libro-list'

    def test_create_libro(self):
        """
        Prueba la creación de un nuevo libro.
        """
        response = self.client.post(self.url, self.libro_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Libro.objects.count(), 2)  # Ahora debería haber 2 libros en la base de datos

    def test_read_libro(self):
        """
        Prueba que se puede leer los detalles de un libro.
        """
        response = self.client.get(reverse('libro-detail', kwargs={'pk': self.libro.id}))  # Accede a los detalles del libro
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], self.libro_data['titulo'])

    def test_update_libro(self):
        """
        Prueba la actualización de un libro.
        """
        updated_data = {'titulo': 'Libro Actualizado'}
        response = self.client.put(reverse('libro-detail', kwargs={'pk': self.libro.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.libro.refresh_from_db()  # Refresca el objeto del libro desde la base de datos
        self.assertEqual(self.libro.titulo, 'Libro Actualizado')

    def test_delete_libro(self):
        """
        Prueba la eliminación de un libro.
        """
        response = self.client.delete(reverse('libro-detail', kwargs={'pk': self.libro.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Libro.objects.count(), 0)  # El libro debe ser eliminado


class LibroSearchApiTests(APITestCase):
    
    def setUp(self):
        """
        Configura los datos necesarios antes de cada prueba.
        """
        self.autor = Autor.objects.create(nombre="Autor 1", biografia="Biografía del autor")
        self.categoria = Categoria.objects.create(nombre="Ficción")
        self.libro = Libro.objects.create(
            titulo="Libro de Prueba",
            autor=self.autor,
            categoria=self.categoria,
            fecha_publicacion="2021-01-01",
            isbn="1234567890123"
        )
        self.url = reverse('libro-list')

    def test_search_libro(self):
        """
        Prueba la búsqueda de libros por título.
        """
        response = self.client.get(f'{self.url}?query=Prueba')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Debería devolver el libro de prueba
        self.assertEqual(response.data[0]['titulo'], "Libro de Prueba")

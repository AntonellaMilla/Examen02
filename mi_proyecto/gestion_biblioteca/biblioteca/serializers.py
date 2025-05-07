from rest_framework import serializers
from .models import Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'biografia', 'fecha_nacimiento']

from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

from .models import Libro
from .serializers import AutorSerializer, CategoriaSerializer

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)  # Relacionado con el modelo Autor
    categoria = CategoriaSerializer(read_only=True)  # Relacionado con el modelo Categoria

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'categoria', 'fecha_publicacion', 'isbn']

from .models import Prestamo
from .serializers import LibroSerializer

class PrestamoSerializer(serializers.ModelSerializer):
    libro = LibroSerializer(read_only=True)  # Relacionado con el modelo Libro

    class Meta:
        model = Prestamo
        fields = ['id', 'libro', 'fecha_prestamo', 'fecha_devolucion', 'usuario', 'estado']

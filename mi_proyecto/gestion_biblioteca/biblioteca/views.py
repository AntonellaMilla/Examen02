from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Libro, Autor, Categoria, Prestamo
from .serializers import LibroSerializer, AutorSerializer, CategoriaSerializer, PrestamoSerializer



# Vista para Autor
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# Vista para Categoria
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Vista para Libro
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

# Vista para Prestamo
class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer



# Vista para buscar libros por título, autor o categoría
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    @action(detail=False, methods=['get'])
    def buscar(self, request):
        # Obtener parámetros de búsqueda
        query = request.query_params.get('query', None)
        if query:
            libros = Libro.objects.filter(
                titulo__icontains=query
            ) | Libro.objects.filter(
                autor__nombre__icontains=query
            ) | Libro.objects.filter(
                categoria__nombre__icontains=query
            )
            serializer = LibroSerializer(libros, many=True)
            return Response(serializer.data)
        return Response({"detail": "No query provided"}, status=400)



# Vista para registrar un préstamo
class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    @action(detail=True, methods=['post'])
    def registrar_prestamo(self, request, pk=None):
        libro = self.get_object()  # Obtener el libro por su ID
        usuario = request.data.get('usuario')
        if not usuario:
            return Response({"detail": "El campo 'usuario' es obligatorio"}, status=400)

        prestamo = Prestamo.objects.create(
            libro=libro,
            usuario=usuario,
            estado='Prestado'
        )
        serializer = PrestamoSerializer(prestamo)
        return Response(serializer.data, status=201)

    @action(detail=True, methods=['post'])
    def devolver(self, request, pk=None):
        prestamo = self.get_object()
        prestamo.estado = 'Devuelto'
        prestamo.fecha_devolucion = request.data.get('fecha_devolucion', None)
        prestamo.save()
        serializer = PrestamoSerializer(prestamo)
        return Response(serializer.data)


# Vista para listar libros disponibles
class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    @action(detail=False, methods=['get'])
    def disponibles(self, request):
        libros_disponibles = Libro.objects.filter(prestamos__estado='Devuelto')
        serializer = LibroSerializer(libros_disponibles, many=True)
        return Response(serializer.data)

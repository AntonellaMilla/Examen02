from django.db import models

# Modelo Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# Modelo Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Modelo Libro
class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)  # Código ISBN único

    def __str__(self):
        return self.titulo


# Modelo Prestamo
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    fecha_prestamo = models.DateField(auto_now_add=True)  # Fecha de préstamo se genera automáticamente
    fecha_devolucion = models.DateField(blank=True, null=True)  # Puede ser nula si no ha sido devuelto
    usuario = models.CharField(max_length=200)  # Nombre del usuario que realiza el préstamo
    estado = models.CharField(
        max_length=50,
        choices=[('Prestado', 'Prestado'), ('Devuelto', 'Devuelto')],
        default='Prestado'
    )

    def __str__(self):
        return f"Préstamo de {self.libro.titulo} a {self.usuario}"


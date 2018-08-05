from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    # Foreign key = Link para outro modelo
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Char field = Campo de texto tamanho limitado
    title = models.CharField(max_length=200)

    # Text field = Campo de texto tamanho ilimitado
    text = models.TextField()

    # DateTime Field = Data e hora
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank = True, null = True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
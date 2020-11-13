from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    celular = models.CharField(max_length=12)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
        
    class Meta:
        permissions = (
            ('administrador',_('Es administrador')),
            ('cliente',_('Es cliente')),
        )

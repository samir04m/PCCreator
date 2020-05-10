from django.db import models
from django.contrib.auth.models import User

class Pc(models.Model):
    name = models.CharField('Nombre del PC', max_length=50)
    budget = models.IntegerField('Presupueto', null=True, blank=True)
    create_at = models.DateTimeField('Fecha de creación', auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'PC'
        verbose_name_plural = 'PCs'
        # ordering = ['name']

    def __str__(self):
        return "{} - {}".format(self.user.username, self.name)
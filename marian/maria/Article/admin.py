from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.categorie)
admin.site.register(models.Offre)
admin.site.register(models.Tag)
admin.site.register(models.Article)

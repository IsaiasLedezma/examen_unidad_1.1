from django.contrib import admin

# Register your models here.

from libros.models import libro

class books(admin.ModelAdmin):
    list_display= ["ISBN","name","autor","editorial","precio"]
    search_field= ["autor","editorial"]
    list_editable= ["precio", "name"]

    class Meta:
        model = libro

admin.site.register(libro, books)

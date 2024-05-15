from django.contrib import admin
from .models import Mutation, Diseases, GeneticCrossing

# Register your models here.

@admin.register(Mutation)
class MutationAdmin(admin.ModelAdmin):
    pass


@admin.register(Diseases)
class DiseasesAdmin(admin.ModelAdmin):
    pass


@admin.register(GeneticCrossing)
class GeneticCrossingAdmin(admin.ModelAdmin):
    pass































































































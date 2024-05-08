from django.contrib import admin
from .models import Mutation, Diseases

# Register your models here.

@admin.register(Mutation)
class MutationAdmin(admin.ModelAdmin):
    pass


@admin.register(Diseases)
class DiseasesAdmin(admin.ModelAdmin):
    pass

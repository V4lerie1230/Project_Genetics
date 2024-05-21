from django.contrib import admin
from .models import Mutation, Diseases, Crossing

# Register your models here.

@admin.register(Mutation)
class MutationAdmin(admin.ModelAdmin):
    pass


@admin.register(Diseases)
class DiseasesAdmin(admin.ModelAdmin):
    pass

@admin.register(Crossing)
class CrossingAdmin(admin.ModelAdmin):
    pass
































































































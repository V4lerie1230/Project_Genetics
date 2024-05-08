from django.contrib import admin
from .models import Mutation

# Register your models here.

@admin.register(Mutation)
class MutationAdmin(admin.ModelAdmin):
    pass



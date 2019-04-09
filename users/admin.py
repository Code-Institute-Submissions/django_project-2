from django.contrib import admin
from .models import Profile

""" Make Profile and Comment accessible in Django Admin"""
admin.site.register(Profile)

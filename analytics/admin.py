from django.contrib import admin
from .models import ObjectViewed
from .manager import ViewedObjectManager


admin.site.register(ObjectViewed)

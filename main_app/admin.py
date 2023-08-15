from django.contrib import admin

# Register your models here.
from .models import Plant
# this will give us full crud operations in our admin app for the cat table in our db
admin.site.register(Plant)

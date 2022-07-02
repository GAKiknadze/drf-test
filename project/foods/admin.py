from django.contrib import admin


from .models import FoodCategory, Food


admin.site.register([FoodCategory, Food])

from django.contrib import admin
from .models import Rest_list

# Register your models here.
# Register your models here.

class REST_APP_admin(admin.ModelAdmin):
    list_display = ("restaurant_name", "type", "address",)


admin.site.register(Rest_list, REST_APP_admin)
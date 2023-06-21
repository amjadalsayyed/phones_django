from django.contrib import admin

# Register your models here.
from .models import Phones

class CustomPhoneAdmin(admin.ModelAdmin):
    model = Phones
    list_display = ['name', 'purchaser', 'desc',]
    fieldsets= (
        ('Owner',{
            'fields':('purchaser',
            )}
        ),
        ('phone info',{
            'fields':('name','desc',
            )}
        )
    )
admin.site.register(Phones,CustomPhoneAdmin)    
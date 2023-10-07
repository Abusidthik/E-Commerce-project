from django.contrib import admin
from .models import *

admin.site.register(category)
admin.site.register(product)


'''class  categoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')
    admin.site.register(catagory,categoryAdmin)'''




# Register your models here.

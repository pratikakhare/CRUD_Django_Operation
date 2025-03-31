from django.contrib import admin

# Register your models here.
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('ID','data1','data2')
    
admin.site.register(Entry, EntryAdmin)
from django.contrib import admin
from .models import Location,Image,Category

admin.site.site_header ='Pics Gallery Admin'
admin.site.site_title = 'Pics Gallery Area'
admin.site.index_title = 'Welcome to the Pics Gallery Area'

# class ChoiceInline(admin.TabularInline):
#     model = Location
#     model = Category

# class ImageAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields':['group']}),
#     ("Date Information", {'fields':[str('post_date')], 'classes': ['collapse']}),]  
#     inlines = [ChoiceInline('ForeignKey')]

# admin.site.register(Image, ImageAdmin)      
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(Category)

# Register your models here.

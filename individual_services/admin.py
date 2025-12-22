from django.contrib import admin
from .models import IndivService, IndividualType


# Register IndivService with IndivServiceAdmin
@admin.register(IndivService)
class IndivServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'price', 'image')
    ordering = ('id',)


# Register IndividualType with IndividualTypeAdmin
@admin.register(IndividualType)
class IndividualTypeAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')

from django.contrib import admin
from store.admin import ProductAdmin
from tags.models import TagList
from django.contrib.contenttypes.admin import GenericTabularInline
from store.models import Product


class TagInline(GenericTabularInline):
    model = TagList


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)

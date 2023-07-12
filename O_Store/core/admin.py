from django.contrib import admin
from store.admin import ProductAdmin, ProductImageInline
from tags.models import TagList
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from store.models import Product
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


class TagInline(GenericTabularInline):
    model = TagList


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline, ProductImageInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)

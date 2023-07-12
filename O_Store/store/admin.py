from django.contrib import admin
from . import models
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ["thumbnail"]

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(f"<img class='thumbnail' src='{instance.image.url}'/>")
        return ''


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "inventory_status", "collection_title"]
    list_editable = ["price"]
    list_per_page = 10
    list_select_related = ["collection"]
    inlines = [ProductImageInline]

    def collection_title(self, product):
        return product.collection.title

    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        else:
            return "Ok"
        
    class Media:
        css = {
            'all':['store/styles.css']
        }


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
    list_per_page = 10


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "unit_price"]
    list_per_page = 10


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "product_count"]
    list_per_page = 10

    @admin.display(ordering="product_count")
    def product_count(self, collection):
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode({"collection_id": str(collection.id)})
        )
        return format_html('<a href = "{}">{}</a>', url, collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count("products"))


@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ["description", "discount"]
    list_per_page = 10

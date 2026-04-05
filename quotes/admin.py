from django.contrib import admin
from .models import Quote, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("author", "category", "created_by", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("author", "text")
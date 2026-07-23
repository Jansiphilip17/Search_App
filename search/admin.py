from django.contrib import admin

from .models import WebsiteContent


@admin.register(WebsiteContent)
class WebsiteContentAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url")
    list_filter = ("category",)
    search_fields = ("title", "description", "keywords")

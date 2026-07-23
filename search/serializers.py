from rest_framework import serializers

from .models import WebsiteContent


class WebsiteContentSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = WebsiteContent
        fields = ["id", "title", "category", "category_display", "description", "keywords", "url"]

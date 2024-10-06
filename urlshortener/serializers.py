from rest_framework import serializers
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = URL
        exclude = ("created_date", )
    
    def get_short_url(self, obj):
        return f"{self.context['request'].build_absolute_uri('/')}{obj.short_url}"

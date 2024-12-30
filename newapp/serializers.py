#Takes models and turns them inot JSON compatible data

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['title','content','published_date']
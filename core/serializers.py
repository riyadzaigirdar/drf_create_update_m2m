from . import models
from rest_framework import serializers

class CategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'post_id', 'name']

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerilizer(many = True, read_only=True)

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'body', 'categories']



    
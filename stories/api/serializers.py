from rest_framework import serializers
from stories.models import Category, Receipe, Tag

class CategorySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )

class TagSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'name',
        )


class RecipeSerialzier(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')
    category = CategorySerialzier()
    tags = TagSerialzier(many=True)
    class Meta:
        model = Receipe
        fields = (
            'id',
            'title',
            'content',
            'author',
            'author_name',
            'category',
            'cover',
            'tags',
            'slug'
        )
        extra_kwargs = {
            'author_name': {"read_only": True},
            'author': {"write_only": True},
            'slug': {"read_only": True},
            'id': {"read_only": True},

        }
    # def create(self, validated_data):
    #     tag_data = validated_data.pop('tags')
    #     recipe = Receipe.objects.create(**validated_data)
    #     recipe.tags.set(tag_data)
    #     return recipe


class RecipeCreateSerialzier(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Receipe
        fields = (
            'title',
            'content',
            'author',
            'category',
            'cover',
            'tags'
        )

    def validate(self, attrs):
        data = super().validate(attrs)
        data['author'] = self.context['request'].user
        return data
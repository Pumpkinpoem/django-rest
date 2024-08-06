from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        if request is None:
            return False
        return obj.owner == request.user

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'created_at', 'updated_at', 'content', 'is_owner']


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')

    class Meta(CommentSerializer.Meta):
        fields = CommentSerializer.Meta.fields + ['post']
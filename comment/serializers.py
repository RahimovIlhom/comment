from rest_framework import serializers

from comment.models import Comment


class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'type', 'field', 'created_at', 'url']
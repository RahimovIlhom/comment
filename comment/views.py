from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from comment.checkComment.checkComment import checkText
from comment.checkComment.classificationText import checkNegComment
from comment.models import Comment
from comment.pagination import CustomPagination
from comment.serializers import CommentSerializers


# Create your views here.

class CommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.all()
        page = CustomPagination
        serializers = CommentSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.all()
        page = CustomPagination
        comment = get_object_or_404(queryset, pk=pk)
        serilizers = CommentSerializers(comment, context=self.get_serializers_context())
        return Response(serilizers.data)

    def create(self, request, *args, **kwargs):
        commentNew = Comment.objects.create()
        serializer = CommentSerializers(commentNew, data=request.data, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            commentNew.comment = serializer.validated_data['comment']
            commentText = f'{commentNew.comment}'
            checkC = checkText(commentText.lower())
            commentNew.type = checkC['label']
            print(commentNew.type)
            commentNew.save()
            serializer = CommentSerializers(commentNew, context=self.get_serializers_context())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializers(comment, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentSerializers(comment, partial=True, context=self.get_serializers_context())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}

    # def get_permissions(self):
    #     permission_class = [BasePermission]
    #     return [permission() for permission in permission_class]


class NegativeCommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.filter(type='negative')
        page = CustomPagination
        serializers = CommentSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.filter(type='negative')
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}


class PositiveCommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.filter(type='positive')
        page = CustomPagination
        serializers = CommentSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.filter(type='positive')
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}


class DiniyCommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.filter(type='diniy')
        page = CustomPagination
        serializers = CommentSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.filter(type='diniy')
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}


class TerrorCommentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comment.objects.filter(type='terroristik')
        page = CustomPagination
        serializers = CommentSerializers(queryset, many=True, context=self.get_serializers_context())
        return Response(serializers.data)

    def destroy(self, request, pk=None):
        queryset = Comment.objects.filter(type='terroristik')
        comment = get_object_or_404(queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializers_context(self):
        return {'request': self.request}
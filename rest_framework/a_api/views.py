from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.contrib.auth import get_user_model
from a_home.models import Comment
from .serializers import ProfileSerializer, CommentSerializer 

User = get_user_model()

@api_view(['GET'])
def profiles(request):
    users = User.objects.all()
    serializer = ProfileSerializer(users, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request):
    data = request.data.copy() 
    data['author_id'] = request.user.id
    serializer = CommentSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def comment_detail(request, id):
    comment = Comment.objects.get(id=id)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response()
    
    serializer = CommentSerializer(comment, context={'request': request})
    return Response(serializer.data)


@api_view(["GET"])
def me(request):
    if request.user.is_authenticated:
        serializer = ProfileSerializer(request.user, context={"request": request})
        return Response(serializer.data)
    return Response(None)

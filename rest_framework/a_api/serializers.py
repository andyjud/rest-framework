from rest_framework import serializers 
from django.contrib.auth import get_user_model
from a_home.models import Comment

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'displayname', 'avatar']
        
    def get_avatar(self, user):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(user.avatar)
        else:
            user.avatar
        
        
class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source='author',
        queryset=User.objects.all(),
        write_only=True  
    )
    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_id', 'body']
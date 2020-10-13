from rest_framework import serializers
from posts.models import PostUserDetails


class PostSerializerUser(serializers.ModelSerializer):

    class Meta:
        model = PostUserDetails
        fields = ['id', 'name', 'email', 'country', 'isbn',
                  'bookTitle', 'bookAuthor', 'date_Added']

from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedRelatedField(view_name='snippet-highlight',
                                                    format='html')
    
    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos',
                  'language', 'style')


class UserSerializer(serializers.ModelSerializer):

    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

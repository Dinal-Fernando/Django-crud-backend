from rest_framework import serializers

from postings.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        fields=[
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
            ]
        read_only_fields=['user']

# to validate a title or somethin u have to do it in serializer

    def validate_title(self,value):
        qs=BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs=qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("the title is used")
        return value


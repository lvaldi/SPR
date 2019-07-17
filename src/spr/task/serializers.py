from rest_framework import serializers
from task.models import Task,


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=50)
    due_date = serializers.DateField()
    priority = serializers.CharField(max_length=20, choices=[(
        'Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    def create(self, validated_data):
        """
        Create and return a new `Task` instance, given the validated data.
        """
        return task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Task` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
import datetime
from rest_framework import serializers

from todo.models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'id']


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'timestamp', 'title',
                  'description', 'due_date', 'tags', 'status']


    def create(self, validated_data):
        # creating the task model item

        # creating task_obj without tags
        task_obj = Task.objects.create(title=validated_data['title'], description=validated_data['description'],
                        due_date=validated_data['due_date'], status=validated_data['status'])
        
        # handling tags
        tags = validated_data['tags']
        task_obj.set_tags(tags)
        task_obj.save()

        return task_obj
    

    def update(self, instance, validated_data):

        '''
        UPDATING following fields
            title
            description
            status
            due_date
            tags
        '''
        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.status = validated_data['status']
        instance.due_date = validated_data['due_date']


        # UPDATING tags field
        tags = validated_data['tags']
        instance.set_tags(tags)

        instance.save()
        return instance
    

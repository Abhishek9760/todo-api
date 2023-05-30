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
        task_obj = Task.objects.create(title=validated_data['title'], description=validated_data['description'],
                        due_date=validated_data['due_date'], status=validated_data['status'])
        
        tags = validated_data['tags']
        for tag in tags:
            tag_obj = Tag.objects.filter(name__iexact=tag['name']).first()
            if not tag_obj:
                tag_obj = Tag.objects.create(name=tag['name'])
                tag_obj.save()
            task_obj.tags.add(tag_obj)

        task_obj.save()
        return task_obj
    

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.status = validated_data['status']
        instance.due_date = validated_data['due_date']

        tags = validated_data['tags']
        tag_obj_list = []
        for tag in tags:
            tag_obj = Tag.objects.filter(name__iexact=tag['name']).first()
            if not tag_obj:
                tag_obj = Tag.objects.create(name=tag['name'])
                tag_obj.save()
            tag_obj_list.append(tag_obj)
            

        instance.tags.set(tag_obj_list)
        instance.save()
        return instance
    

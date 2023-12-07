from rest_framework import serializers
from .models import Article
from datetime import datetime
from django.utils.timesince import timesince
from datetime import date


class ArticleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ["id", "created_time", "updated_time"]

    def get_time_since_pub(self, object):
        now = datetime.now()
        published_date = object.published_time
        time_delta = timesince(now, published_date)
        return time_delta

    def validate_published_time(self, datevalue):
        today = date.today()
        if datevalue > today:
            raise serializers.ValidationError("The date is not correct")

        return datevalue


class ArticleSerializerDefault(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    main_text = serializers.CharField()
    published_time = serializers.DateField()
    is_active = serializers.BooleanField()
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(
        self,
        validated_data,
        instance,
    ):
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.main_text = validated_data.get("main_text", instance.main_text)
        instance.published_time = validated_data.get(
            "published_time", instance.published_time
        )
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance

    # object level validation
    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "The title and the description cannot be the same"
            )
        return data

    # individual field level validation
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                f"The length of the title should be greater than 5"
            )
        return value

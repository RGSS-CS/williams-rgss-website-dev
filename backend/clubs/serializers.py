from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Club, ClubWhyJoin, ClubAnnouncement
from photologue_custom.serializers import GallerySerializer

class ClubWhyJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubWhyJoin
        fields = ["title", "description", "index"]

class ClubAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubAnnouncement
        fields = ["title", "description", "date_posted", "popup",'expiry']

class ClubSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = TagListSerializerField()
    why_join = ClubWhyJoinSerializer(source="why_join_reasons",many=True,max_length=10)
    gallery = GallerySerializer()
    announcement = ClubAnnouncementSerializer(source="club_announcement",many=True,max_length=1)

    class Meta:
        model = Club
        fields = [
            "id", "name", "preview_description", "description", 
            "tagline", "category", "day_of_meeting", "time", 
            "repetition", "room_number", "why_join", "classroom_code", 
            "accepting_applicants", "join_instructions", "application_form_link", 
            "teacher_advisor", "gallery", "announcement"
            ]

class PublicClubSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = TagListSerializerField()
    why_join = ClubWhyJoinSerializer(source="why_join_reasons", many=True, read_only=True)

    class Meta:
        model = Club
        fields = [
            "id", "name", "preview_description", "description", 
            "tagline", "category", "day_of_meeting", "time", 
            "repetition", "room_number", "why_join", "accepting_applicants",
            "teacher_advisor"
            ]

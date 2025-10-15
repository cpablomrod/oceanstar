from django.contrib import admin
from .models import Destination, TravelPackage, Review, TravelExperience, TravelRequest, TravelFeedback


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'created_at']
    list_filter = ['country', 'created_at']
    search_fields = ['name', 'country']
    ordering = ['name']


@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'destination', 'price', 'duration_days', 'package_type', 'is_featured']
    list_filter = ['package_type', 'is_featured', 'destination__country', 'created_at']
    search_fields = ['title', 'description', 'destination__name']
    list_editable = ['is_featured', 'price']
    ordering = ['-created_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'package', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'package__destination__country']
    search_fields = ['title', 'content', 'user__username', 'package__title']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(TravelExperience)
class TravelExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'travel_date', 'created_at']
    list_filter = ['travel_date', 'created_at', 'package__destination__country']
    search_fields = ['user__username', 'package__title', 'story']
    readonly_fields = ['created_at']
    ordering = ['-travel_date']


@admin.register(TravelRequest)
class TravelRequestAdmin(admin.ModelAdmin):
    list_display = ['people_count', 'destination', 'travel_dates', 'has_kids', 'created_at']
    list_filter = ['has_kids', 'created_at', 'people_count']
    search_fields = ['destination', 'requirements', 'travel_dates']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['people_count', 'has_kids', 'travel_dates', 'destination', 'requirements', 'created_at']
        return ['created_at']


@admin.register(TravelFeedback)
class TravelFeedbackAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'experience_preview', 'improvement_preview']
    list_filter = ['created_at']
    search_fields = ['experience', 'improvement']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    def experience_preview(self, obj):
        return obj.experience[:50] + "..." if len(obj.experience) > 50 else obj.experience
    experience_preview.short_description = "Experience (Preview)"
    
    def improvement_preview(self, obj):
        return obj.improvement[:50] + "..." if len(obj.improvement) > 50 else obj.improvement
    improvement_preview.short_description = "Improvement (Preview)"
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['experience', 'improvement', 'created_at']
        return ['created_at']

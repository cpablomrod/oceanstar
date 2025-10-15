from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.country}"


class TravelPackage(models.Model):
    PACKAGE_TYPES = [
        ('adventure', 'Adventure'),
        ('relaxation', 'Relaxation'),
        ('cultural', 'Cultural'),
        ('family', 'Family'),
        ('romantic', 'Romantic'),
        ('business', 'Business'),
    ]
    
    title = models.CharField(max_length=200)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()
    package_type = models.CharField(max_length=20, choices=PACKAGE_TYPES)
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    available_from = models.DateField()
    available_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('travel:package_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.rating} stars"
    
    class Meta:
        ordering = ['-created_at']


class TravelExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    travel_date = models.DateField()
    images = models.ImageField(upload_to='experiences/', blank=True, null=True)
    story = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.package.title}"
    
    class Meta:
        ordering = ['-travel_date']


class TravelRequest(models.Model):
    people_count = models.CharField(max_length=10)
    has_kids = models.CharField(max_length=5)
    travel_dates = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Travel Request - {self.people_count} people to {self.destination}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Travel Request"
        verbose_name_plural = "Travel Requests"


class TravelFeedback(models.Model):
    experience = models.TextField(max_length=300, help_text="Tell us about your experience (max 300 characters)")
    improvement = models.TextField(max_length=300, help_text="What could we do to improve? (max 300 characters)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Travel Feedback - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Travel Feedback"
        verbose_name_plural = "Travel Feedback"

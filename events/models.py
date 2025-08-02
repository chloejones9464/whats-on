from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField(
        "image",
        blank=True,
        null=True,
        default=(
            (
                "https://res.cloudinary.com/dcvyln5fy/image/upload/"
                "v1752856652/placeholder_image_rwbnhz.webp"
            )
        ),
    )
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    liked_by = models.ManyToManyField(
        User, related_name="liked_events", blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.image:
            self.image = (
                "https://res.cloudinary.com/dcvyln5fy/image/upload/"
                "v1752856652/placeholder_image_rwbnhz.webp"
            )
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    event = models.ForeignKey(
        Event, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manually_edited = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.title}"

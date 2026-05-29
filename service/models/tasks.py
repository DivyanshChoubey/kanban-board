from django.db import models
from service.models import User


class Tasks(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    time = models.PositiveIntegerField(null=True, blank=True, help_text="Time in minutes")
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    parent_task = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="subtasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "tasks"

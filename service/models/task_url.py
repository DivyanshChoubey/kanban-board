from django.db import models
from service.models import Tasks


class TaskURL(models.Model):
    URL_TYPES = [
        ("pr", "Pull Request"),
        ("branch", "Branch"),
        ("commit", "Commit"),
        ("ticket", "Ticket"),
        ("doc", "Document"),
        ("design", "Design"),
        ("api", "API"),
        ("other", "Other"),
    ]
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name="urls")
    url = models.URLField()
    url_type = models.CharField(max_length=30, choices=URL_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "task_url"

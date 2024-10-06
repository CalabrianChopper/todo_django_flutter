from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title[:20]
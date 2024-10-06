from django.db import models
from .utils import create_shortened_url


class URL(models.Model):
    url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self) -> str:
        return f"{self.url} -> {self.short_url}"
    
    def save(self, *args, **kwargs) -> None:
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        return super().save(*args, **kwargs)



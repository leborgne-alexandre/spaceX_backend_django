from django.db import models
# Create your models here.

# add this
class SpaceX(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()

  def _str_(self):
    return self.title
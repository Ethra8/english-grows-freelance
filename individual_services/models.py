import uuid
from django.db import models


class IndivService(models.Model):
    type = models.ForeignKey('IndividualType', null=True, blank=True,
                             on_delete=models.SET_NULL)  # noqa on_delete type, product don't delete, but set type to null
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    number_hours = models.IntegerField(default=0)
    duration_weeks = models.IntegerField(default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Only set the ID if it's a new instance
            last_service = IndivService.objects.all().order_by('-id').first()
            if last_service:
                self.id = last_service.id + 1
            else:
                self.id = 1  # Start with 1 if no services exist
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_indivservice_type(self):
        return self.type

    def get_indivservice_id(self):
        return self.id


class IndividualType(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=False,
                                     blank=False, default=name)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

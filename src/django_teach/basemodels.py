from django.db import models


class CustomManager(models.Manager):
    """
    Custom Manager class, that adds to all methods filter is_active=True
    except all()"""

    def _get_queryset(self):  # returns ordinary queryset
        return super().get_queryset()

    def get_queryset(self):  # returns filtered is_active=True queryset
        queryset = self._get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset

    def all(self):  # returns ordinary queryset.all()
        return self._get_queryset()

    def all_active(self):  # returns queryset.filter(is_active=True).all()
        return self.get_queryset()

    def delete(self):
        self.update(is_active=False)


class BaseModel(models.Model):
    """Base abstract class, that should be a parent class for other models
    overrides method delete"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = CustomManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()



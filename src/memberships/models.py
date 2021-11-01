from django.db import models

# Create your models here.

MEMBERSHIP_CHOICES = (
    ('Enterprice', 'ent'),
    ('Professional', 'pro'),
    ('Free', 'free')
)

class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=30)
    price = models.IntegerField(default=15)
    stripe_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type
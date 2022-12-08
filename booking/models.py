from django.conf import settings
from django.db import models
from .validators import image_resolution_check_big


class Rooms(models.Model):
    image = models.ImageField(validators=[image_resolution_check_big], null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=200)
    cost = models.DecimalField(decimal_places=2, max_digits=250, default=0)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"{self.title} - {self.cost}"


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name="Заказы"
    )
    date_come = models.DateField(blank=True, help_text="2022-4-3")
    date_out = models.DateField(blank=True, help_text="2022-5-3")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    purchase = models.ForeignKey(
        Rooms, related_name="rooms", on_delete=models.CASCADE, null=True,
    )
    count = models.IntegerField(null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=250, default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

    def __str__(self):
        return f"Order №{self.id}"

    def get_cost(self):
        return self.cost * self.count

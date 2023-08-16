from django.db import models
from django.urls import reverse
# Create your models here.

# adding a M:M relationship


class Pot(models.Model):
    size = models.CharField(max_length=100, default="blank")
    material = models.CharField(max_length=100, default="blank")
    color = models.CharField(max_length=100, default="blank")

    def __str__(self):
        return f"A {self.material}, {self.color} pot"

    def get_absolute_url(self):
        reverse('pots_detail', kwargs={'pk': self.id})


class Plant(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    pots = models.ManyToManyField(Pot)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})


AMOUNTS = (
    ('S', '1-2 in. of Water'),  # small
    ('M', '3-4 in. of Water'),  # medium
    ('L', '5-6 in. of Water')  # large
)


class Watering(models.Model):
    date = models.DateField()
    amount = models.CharField(
        max_length=1, choices=AMOUNTS, default=AMOUNTS[0][0])
    # ondelete method deletes all the waterings associated
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    # with the plant when the plant is deleted

    def __str__(self):
        return f"{self.get_amount_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

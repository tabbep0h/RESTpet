from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class PetStatus(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class OrderStatus(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pet(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.ForeignKey(PetStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    success = models.BooleanField()


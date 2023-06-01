from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "age",
                    "email",
                    "phone",
                    "address",
                ],
                name="unique_student",
            )
        ]
        ordering = ["-created_at", "name", "age"]

    def __str__(self):
        return (
            f"{self.name} - {self.age} - {self.email} - {self.phone} - {self.address}"
        )

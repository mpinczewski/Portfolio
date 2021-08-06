from django.db import models
import uuid


class Csv(models.Model):
    file_name = models.FileField(upload_to="csvs")
    upload = models.DateField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.file_name}: {self.upload}"


class SalesBranch(models.Model):
    short_name = models.CharField(max_length=3)
    full_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.short_name}"

    @classmethod
    def get_full_name(cls, short_name, full_name):
        return cls(short_name, "-", full_name)


class SalesManager(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    sales_branch = models.ForeignKey(
        SalesBranch, verbose_name="Oddzial", on_delete=models.DO_NOTHING
    )
    area = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    supervisor = models.CharField(null=True, blank=True, max_length=128)
    phone_number = models.CharField(max_length=18)
    email = models.EmailField()
    id_number = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return str(self.id_number)

    @classmethod
    def get_sales_manager_id(self):
        return (self.sales_branch)(self.id_number)

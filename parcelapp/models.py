from django.db import models
from phone_field import PhoneField


class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    description = models.CharField(
        max_length=500, help_text='Comprehensive location details')
    email = models.EmailField(max_length=254)
    phone = PhoneField(help_text='Contact phone number')

    def __str__(self):
        return self.branch_name


class Agent(models.Model):
    username = models.CharField(max_length=250)
    branch = models.ForeignKey(
        'Branch', related_name='agents', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username


class Parcel(models.Model):
    STATUS = (
        ('pending', ('Agent or Admin has received to be sent')),
        ('on-transit', ('Yet to confirmed by the receiving status')),
        ('arrived', ('Parcel has arrived to the receiving station')),
    )

    serial_number = models.CharField(max_length=250)
    status = models.CharField(max_length=50, choices=STATUS, default='pending')
    sending_station = models.ForeignKey(
        'Agent', default='Main', on_delete=models.CASCADE)
    recepient_station = models.ForeignKey(
        'Branch', related_name='recepient_station', on_delete=models.CASCADE)
    description = models.CharField(
        max_length=250, help_text='Give more details of the parcel')
    receiving_agent = models.ForeignKey(
        'Agent', related_name='receiving_agent', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.serial_number

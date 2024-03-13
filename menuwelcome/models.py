from django.db import models

# Create your models here.

class Feedback(models.Model):

    first_name = models.CharField(
        max_length =255,
        null =False,
        blank = False,
    )

    last_name = models.CharField(
        max_length= 225,
        null = True,
        blank = True
    )

    email = models.CharField(
        max_length= 225,
        null = False,
        blank = True,
    )

    phone = models.CharField(
        max_length=225,
        null = False,
        blank = True,
    )

    created_on = models.DateTimeField(
        auto_now_add= True
    )

    updated_on = models.DateTimeField(
        auto_now= True
    )


class Help(models.Model):

    first_name = models.CharField(
        max_length=225,
        null= False,
        blank = True,
    )

    last_name = models.CharField(
        max_length=225,
        null=True,
        blank=True,
    )

    phone = models.CharField(
        max_length=225,
        null=True,
        blank=True,
    )

    email = models.CharField(
        max_length=225,
        null=False,
        blank = True,
    )

    message = models.CharField(
        max_length=225,
        null=False,
        blank=True,
    )

    created_on = models.DateTimeField(
        auto_now_add= True
    )
    updated_on = models.DateTimeField(
        auto_now= True
    )



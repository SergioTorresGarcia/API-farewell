from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=50)
    when = models.DateField()
    where = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    invited = models.BooleanField(default=False)
    confirmed = models.BooleanField()
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    note = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname


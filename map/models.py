from django.db import models



class BankCoordinates(models.Model):
    station_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.station_name


class Bank(models.Model):
    name = models.CharField(max_length=255)
    coordinates = models.ForeignKey(BankCoordinates, related_name="banks", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BankBranch(models.Model):
    bank = models.ForeignKey(Bank, related_name="branches", on_delete=models.CASCADE)
    coordinates = models.ForeignKey(BankCoordinates, related_name="branches", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bank.name} Branch at {self.coordinates.station_name}'


class IndividualATM(models.Model):
    bank = models.ForeignKey(Bank, related_name="atms", on_delete=models.CASCADE)
    coordinates = models.ForeignKey(BankCoordinates, related_name="atms", on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.bank.name} ATM at {self.coordinates.station_name}'

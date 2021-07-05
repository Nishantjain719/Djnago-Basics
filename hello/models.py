from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination =  models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"
# django do it for me mapping indivisual passenger to flights and tabels created for me
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)  
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers") #May be passenger is not on any flight, sother flights field id blank.  

    
    def __str__(self):
        return f"{self.first} {self.last}"

    

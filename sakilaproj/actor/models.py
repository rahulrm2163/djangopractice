from django.db import models


# Create your models here.
class Actor(models.Model):
    actor_id = models.BigAutoField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actor'

    def __str__(self):
        return "{} - {}".format(self.actor_id, self.first_name,self.last_name,self.last_update)

from django.db import models

# Create your models here.

class Deal(models.Model):


    NEW = 'NEW'
    QUALIFIED = 'QUALIFIED'
    PROPOSAL = 'PROPOSAL'
    NEGOTIATION = 'NEGOTIATION'
    WON = 'WON'
    LOST = 'LOST'

    STAGE_CHOICE = [
        (NEW,'New Lead (10%)'),
        (QUALIFIED,'Qualified (30%)'),
        (PROPOSAL,'Proposal Sent (60%)'),
        (NEGOTIATION,'Negotiation (80%)'),
        (WON,'Closed Won (100%)'),
        (LOST,'Closed Lost (0%)'),
    ]


    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    stage = models.CharField(max_length=20,choices=STAGE_CHOICE,default=NEW)
    probability = models.PositiveIntegerField(default=10,editable=False)

    def save(self,*args, **kwargs):

        if self.stage == self.NEW:
            self.probability = 10
        elif self.stage == self.QUALIFIED:
            self.probability = 30
        elif self.stage == self.PROPOSAL:
            self.probability = 60
        elif self.stage == self.NEGOTIATION:
            self.probability = 80
        elif self.stage == self.WON:
            self.probability = 100
        elif self.stage == self.LOST:
            self.probability = 0
            
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title} - {self.get_stage_display()}"
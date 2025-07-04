# By default, Django signals run in the same database transaction as the caller.
#This means that if the signal is sent within a transaction, the signal handlers will also be executed within that transaction.

from django.db import transaction
from django.dispatch import Signal, receiver
from django.db import models

# Define a signal
my_signal = Signal()

# Define a receiver function
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal received from:", sender)
    # Simulate a database operation
    print("Database operation simulated.")

# Simulate a model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Using a transaction
with transaction.atomic():
    print("Before sending signal within transaction")
    my_signal.send(sender="Sender Object")
    print("After sending signal within transaction")

#Yes, Django signals run in the same thread as the caller by default.
#This means that the signal handlers are executed in the same thread that sent the signal.

import threading
from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

# Define a receiver function
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal received from:", sender)
    print("Current thread:", threading.current_thread().name)

# Sending the signal
print("Before sending signal in thread:", threading.current_thread().name)
my_signal.send(sender="Sender Object")
print("After sending signal in thread:", threading.current_thread().name)

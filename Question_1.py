#By default, Django signals are executed synchronously.
#This means that when a signal is sent, the connected signal handlers are executed immediately in the same thread and context as the sender.

from django.dispatch import Signal, receiver
# Define a signal
my_signal = Signal()
# Define a receiver function
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal received from:", sender)
# Sending the signal
print("Before sending signal")
my_signal.send(sender="Sender Object")
print("After sending signal")

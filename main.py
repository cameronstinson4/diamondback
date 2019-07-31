from classes.state import *
from classes.state_machine import *

pollTask = TaskState("aws:arn:123", {"JobName": "123"})

print(pollTask.__repr__())

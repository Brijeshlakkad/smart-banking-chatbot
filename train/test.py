from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import rasa_core.events as events
import rasa_core.trackers as tracker
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import config

wait_for_user=events.UserUtteranceReverted()
text=wait_for_user.apply_to(tracker)
print(text)

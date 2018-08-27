from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import config
class BankActiveCard(Action):
    def name(self):
        return "action_active_card"
    def run(self, dispatcher, tracker, domain):
        loc=tracker.get_slot('using_what')
        if loc=="text":
            response = "Please enter OTP"
        elif "pin" in loc or "pass" in loc:
            response="Please enter your passcode"
        else:
            response="You can do so at Personal Settings or can i do it for you?"
        dispatcher.utter_message(response)
        return [SlotSet['using_what'],loc]

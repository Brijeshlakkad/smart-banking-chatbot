from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings
warnings.filterwarnings('always')
from rasa_core.actions.action import Action,ActionListen
from rasa_core.actions.forms import FormAction,EntityFormField,FreeTextFormField
from rasa_core.events import *
from jon_working_with_db import *
class GetPasscode(Action):
    def name(self):
        return 'action_get_passcode'
    def run(self, dispatcher, tracker, domain):
        got_passcode=tracker.get_slot("get_passcode")
        r=0
        if got_passcode!=None:
            r=1
        return [SlotSet("status_access", r)]
class GetAccess(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("user"),
        FreeTextFormField("password")
        ]
    def name(self):
        return 'action_get_access'
    def submit(self, dispatcher, tracker, domain):
        results = BrijAPI().search(
            tracker.get_slot("user"),tracker.get_slot("password"))
        return [SlotSet("status_access", results)]
class GetName(Action):
    def name(self):
        return "action_get_name"
    def run(self, dispatcher, tracker, domain):
        n=tracker.get_slot('name')
        response="Hello!"
        if n!=None:
            response = "Hello, %s"%n
        dispatcher.utter_message(response)
        return [SlotSet('name',n)]

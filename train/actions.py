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
class GetPasscode(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("passcode")
        ]
    def name(self):
        return 'action_get_passcode'
    def submit(self, dispatcher, tracker, domain):
        results = BrijAPI().search(tracker.get_slot("passcode"))
        return [SlotSet("status_access", results)]
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
        return [SlotSet("access", results)]

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
        user,password,passcode=tracker.get_slot("user"),tracker.get_slot("password"),tracker.get_slot("passcode")
        if passcode==None:
            return [ActionReverted()]
        ConversationPaused().apply_to(tracker)
        results = check_passcode(user,password,passcode)
        ConversationResumed().apply_to(tracker)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted()]
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
        user=tracker.get_slot("user")
        password=tracker.get_slot("password")
        ConversationPaused().apply_to(tracker)
        results = check_indentity(user,password)
        ConversationResumed().apply_to(tracker)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        return [SlotSet("access", results)]
class CheckValidity(Action):
    def name(self):
        return "action_check_validity"
    def run(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("user"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        return []

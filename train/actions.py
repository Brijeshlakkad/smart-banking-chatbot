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
class GetActiveCard(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("passcode_active")
        ]
    def name(self):
        return 'action_active_card'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("user"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        user,password,passcode=tracker.get_slot("user"),tracker.get_slot("password"),tracker.get_slot("passcode_active")
        if passcode==None:
            return [ActionReverted()]
        ConversationPaused().apply_to(tracker)
        results = check_passcode(user,password,passcode)
        if results==1:
            results=get_active_card(user,password,passcode)
        else:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted()]
        ConversationResumed().apply_to(tracker)
        if int(results)!=1:
            dispatcher.utter_message("Please try again! or login again!")
            return [ActionReverted()]
        return [SlotSet("passcode_active",None)]
class GetDeactiveCard(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("passcode_deactive")
        ]
    def name(self):
        return 'action_deactive_card'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("user"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        user,password,passcode=tracker.get_slot("user"),tracker.get_slot("password"),tracker.get_slot("passcode_deactive")
        if passcode==None:
            return [ActionReverted()]
        ConversationPaused().apply_to(tracker)
        results = check_passcode(user,password,passcode)
        if results==1:
            results=get_deactive_card(user,password,passcode)
        else:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted()]
        ConversationResumed().apply_to(tracker)
        if int(results)!=1:
            dispatcher.utter_message("Please try again! or login again!")
            return [ActionReverted()]
        return [SlotSet("passcode_deactive",None)]
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

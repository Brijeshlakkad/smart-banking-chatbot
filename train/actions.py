from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings
warnings.filterwarnings('always')
from rasa_core.actions.action import Action,ActionListen
from rasa_core.actions.forms import FormAction
from rasa_core.events import *
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import config
class ActionReportCoI(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("coi_gi_receivername", "coi_gi_receivername"),
            EntityFormField("coi_gi_give_or_take", "coi_gi_give_or_take"),
            EntityFormField("coi_gi_is_publicofficial", "coi_gi_is_publicofficial"),
            EntityFormField("coi_amount", "coi_amount")
        ]

    def name(self):
        return 'action_report_coi'

    def submit(self, dispatcher, tracker, domain):
        results = RestaurantAPI().search(
            tracker.get_slot("coi_gi_receivername"),
            tracker.get_slot("coi_gi_give_or_take"),
            tracker.get_slot("coi_gi_is_publicofficial"),
            tracker.get_slot("coi_amount"))
        return [SlotSet("search_results", results)]
class BankActiveCard(Action):
    def name(self):
        return "action_active_card"
    def run(self, dispatcher, tracker, domain):
        print("Ddddddddddddddddddd")
        loc=tracker.get_slot('using_what')
        response= "Please enter passcode: "
        dispatcher.utter_message(response)
        inp="Nothing"
        inp = raw_input()
        print(inp)
        return [SlotSet("status_access",inp)]
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

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings
warnings.filterwarnings('always')

from rasa_core_sdk import *
from rasa_core_sdk.events import *
from rasa_core_sdk.forms import *
from jon_working_with_db import *
class GetAccess(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("email"),
        FreeTextFormField("password")
        ]
    def name(self):
        return 'action_get_access'
    def submit(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        ConversationPaused().apply_to(tracker)
        results = check_indentity(user,password)
        ConversationResumed().apply_to(tracker)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        dispatcher.utter_template("utter_access",tracker)
        return [SlotSet("access", results)]
class GetCardService(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        BooleanFormField("card_permission","affirm","deny"),
        FreeTextFormField("passcode")
        ]
    def name(self):
        return 'action_card_service'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        user,password,passcode=tracker.get_slot("email"),tracker.get_slot("password"),tracker.get_slot("passcode")
        card_permission=tracker.get_slot("card_permission")
        question_yes_no=tracker.get_slot("question_yes_no")
        using_what=tracker.get_slot("using_what")
        if passcode==None or card_permission!=True:
            return [ActionReverted()]
        results = check_passcode(user,password,passcode)
        ent="card"
        template="utter_fallback"
        if results==1:
            tracker.update(UserUtteranceReverted())
            tracker.update(UserUtteranceReverted())
            entities=tracker.latest_message.entities
            intent=tracker.latest_message.intent['name']
            if intent=="Banking_Activate_Card":
                results=get_active_card(user,password,passcode)
                template="utter_activated_card"
            elif intent=="Banking_Cancel_Card":
                results=get_deactive_card(user,password,passcode)
                template="utter_deactivated_card"
            len1=len(entities)
            for i in range(len1):
                if entities[i]["entity"]=="card_type":
                    ent=entities[i]['value']
                elif entities[i]["entity"]=="using_what":
                    using_what=entities[i]['value']
                elif entities[i]["entity"]=="question_yes_no":
                    question_yes_no=entities[i]['value']
            if question_yes_no!=None:
                template="utter_give_pos_ans"
                using=""
                if using_what!=None:
                    using=" ".join(["using",using_what])
                dispatcher.utter_template(template,tracker,using=using)
            else:
                dispatcher.utter_template(template,tracker,card_type=ent.capitalize())
        else:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted()]
        return [SlotSet("passcode",None),SlotSet("card_permission",None)]
class GetFeeInquiry(Action):
    def name(self):
        return 'action_fee_inquiry'
    def run(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        fees=get_fee_info(user,password)
        fees=int(fees)
        fees=round(fees,2)
        dispatcher.utter_template("utter_fee_inquiry_reply",tracker,fees=fees)
        return []
class CardReplaceService(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("card_replace_with"),
        BooleanFormField("card_perm","affirm","deny"),
        FreeTextFormField("passcode")
        ]
    def name(self):
        return 'action_card_replace'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        user,password,passcode=tracker.get_slot("email"),tracker.get_slot("password"),tracker.get_slot("passcode")
        card_perm=tracker.get_slot("card_perm")
        card_replace_with=tracker.get_slot("card_replace_with")
        if passcode==None or card_replace_with==None or card_perm!=True:
            return [ActionReverted()]
        results = check_passcode(user,password,passcode)
        if int(results)!=1:
            dispatcher.utter_message("Please try again! or login again!")
            return [ActionReverted()]
        results=card_replace(user,password,card_replace_with)
        if results!=1:
            dispatcher.utter_message("Please try again! or login again!")
        dispatcher.utter_template("utter_replace_card_reply",tracker)
        return [SlotSet("passcode",None),SlotSet("card_perm",None)]

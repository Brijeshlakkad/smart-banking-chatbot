from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings
warnings.filterwarnings('always')
from rasa_core.actions.action import *
from rasa_core.actions.forms import *
from rasa_core.events import *
from jon_working_with_db import *
import random,re
class ActionGetAccountBalance(Action):
    def name(self):
        return "action_get_account_balance"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        balance=get_account_info(user,password,"balance")
        acc=random.choice(['account','a/c','acc'])
        dispatcher.utter_template("utter_get_account_balance_reply",tracker,name=name,balance=balance,acc=acc)
        return []
class ActionGetAccountDetails(Action):
    def name(self):
        return "action_get_account_details"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        dispatcher.utter_template("utter_get_account_details_reply",tracker,name=name)
        return []
class ActionGetCardDetails(Action):
    def name(self):
        return "action_get_card_details"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        dispatcher.utter_template("utter_get_card_details_reply",tracker,name=name)
        return []
class ActionGetCardStatus(Action):
    def name(self):
        return "action_get_card_status"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        status=get_card_info(user,password,"status")
        if status==1:
            status="active"
        elif status==0:
            status="deactive"
        else:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        dispatcher.utter_template("utter_get_card_status_reply",tracker,name=name,status=status)
        return []
class ActionBotControlStartOver(Action):
    def name(self):
        return "action_bot_control_start_over"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        dispatcher.utter_template("utter_bot_control_start_over_reply",tracker,name=name)
        return [AllSlotsReset()]
class ActionBotControlStandby(Action):
    def name(self):
        return "action_bot_control_standby"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        dispatcher.utter_template("utter_bot_control_standby_reply",tracker,name=name)
        return []
class ActionBotControlConfirmPresence(Action):
    def name(self):
        return 'action_bot_control_confirm_presence'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        dispatcher.utter_template("utter_bot_control_confirm_presence_reply",tracker,name=name)
        return []
class ActionBotControlChangeSubject(Action):
    def name(self):
        return 'action_bot_control_change_subject'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        dispatcher.utter_template("utter_bot_control_change_subject_reply",tracker,name=name)
        return []
class ActionAskInputTransferMoney(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        BooleanFormField("transfer_perm","affirm","deny"),
        FreeTextFormField("where"),
        FreeTextFormField("amount")
        ]
    def name(self):
        return 'action_ask_input_transfer_money'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        name=tracker.get_slot("name")
        name=get_user_name(name)
        transfer_perm=tracker.get_slot("transfer_perm")
        where=tracker.get_slot("where")
        amount=tracker.get_slot("amount")
        amount=str(amount)
        if transfer_perm==None:
            return [SlotSet("transfer_perm",None),SlotSet("requested_slot","transfer_perm"),SlotSet("service_access",None)]
        if transfer_perm!=True:
            return [SlotSet("transfer_perm",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
        userid=get_personal_info(user,password,"cid")
        from_acc_no=get_account_info(user,password,"acc_no")
        result_where=str(check_acc_num_exists(where,userid))
        if not result_where.startswith("11"):
            dispatcher.utter_message("Please enter valid account number: ")
            return [SlotSet("where",None),SlotSet("amount",None),SlotSet("requested_slot","where")]
        if amount==None or (not re.match("[0-9]+",amount)):
            dispatcher.utter_message("Please enter valid amount: ")
            return [SlotSet("amount",None),SlotSet("requested_slot","amount")]
        amount=int(amount)
        if amount>50000:
            dispatcher.utter_message("Please enter valid amount less than Rs.50000: ")
            return [SlotSet("amount",None),SlotSet("requested_slot","amount")]
        return [SlotSet("service_access",1),SlotSet("requested_slot",None)]
class ActionTransferMoney(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
            FreeTextFormField("got_otp")
        ]
    def name(self):
        return 'action_transfer_money'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        name=tracker.get_slot("name")
        name=get_user_name(name)
        template="utter_sent_money_reply"
        transfer_perm=tracker.get_slot("transfer_perm")
        where=tracker.get_slot("where")
        amount=tracker.get_slot("amount")
        service_access=tracker.get_slot("service_access")
        if service_access==None or service_access!=1:
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        if transfer_perm==None or transfer_perm!=True:
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        userid=get_personal_info(user,password,"cid")
        from_acc_no=get_account_info(user,password,"acc_no")
        result_where=str(check_acc_num_exists(where,userid))
        if not result_where.startswith("11"):
            dispatcher.utter_message("Transaction Failed! Account number was not correct.")
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        to_acc_no=where
        amount=str(amount)
        if amount==None or (not re.match("[0-9]+",amount)):
            dispatcher.utter_message("Transaction Failed! Amount was incorrect!")
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        amount=int(amount)
        if amount>50000:
            dispatcher.utter_message("Transaction Failed! Amount was incorrect!")
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        acc_name=result_where[2:]
        got_otp=tracker.get_slot("got_otp")
        last_otp=tracker.get_slot("last_otp")
        last_otp=int(last_otp)
        if last_otp==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        got_otp=str(got_otp)
        if got_otp==None or (not re.match("[0-9]{6}",got_otp)):
            dispatcher.utter_message("Transaction Failed! OTP was not correct.")
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        got_otp=int(got_otp)
        if got_otp==1:
            otp=send_otp_to_customer(user,password)
            return [SlotSet("last_otp",otp),SlotSet("requested_slot","got_otp")]
        if got_otp==2:
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        if last_otp!=got_otp:
            dispatcher.utter_message("Transaction Failed! OTP was incorrect!")
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        result_transfer=str(make_transaction(from_acc_no,to_acc_no,amount))
        if not result_transfer.startswith("11"):
            dispatcher.utter_message("Transaction Failed!")
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        dispatcher.utter_template(template,tracker,name=name,to_acc_name=acc_name)
        ans=get_last_transaction_without_html_tags(from_acc_no,1)
        dispatcher.utter_template("utter_view_activity_reply",tracker,name=name,ans=ans)
        return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
class ActionSendOTPForTransaction(Action):
    def name(self):
        return 'action_send_otp_for_transaction'
    def run(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        service_access=tracker.get_slot("service_access")
        if service_access==None or service_access!=1:
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        #otp=send_otp_to_customer(user,password)
        otp=111111
        dispatcher.utter_template("utter_ask_got_otp",tracker)
        return [SlotSet("last_otp",otp),SlotSet("requested_slot","got_otp")]
class ActionViewActivity(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("num_trans")
        ]
    def name(self):
        return 'action_view_activity'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        name=tracker.get_slot("name")
        name=get_user_name(name)
        template="utter_view_activity_reply"
        num_trans=tracker.get_slot("num_trans")
        if num_trans=="any" or num_trans==None or num_trans=="" or type(num_trans)!=int:
            num_trans=2
        num_trans=int(num_trans)
        acc_no=get_account_info(user,password,"acc_no")
        if acc_no==0:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted()]
        ans=get_last_transaction_without_html_tags(acc_no,num_trans)
        dispatcher.utter_template(template,tracker,name=name,ans=ans)
        return [SlotSet("num_trans",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
class ActionReportMissingCard(Action):
    def name(self):
        return 'action_report_missing_card'
    def run(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        name=tracker.get_slot("name")
        name=get_user_name(name)
        template="utter_report_missing_card_reply"
        dispatcher.utter_template(template,tracker,name=name)
        return []
class ActionChangeContact(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("contact")
        ]
    def name(self):
        return 'action_change_contact'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        service_access=tracker.get_slot("service_access")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        contact=tracker.get_slot("contact")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted(),SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
        result=change_customer_details("contact",contact,user)
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted()]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="contact")
        return [SlotSet("contact",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
class ActionChangePasscode(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("new_passcode")
        ]
    def name(self):
        return 'action_change_passcode'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        service_access=tracker.get_slot("service_access")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        new_passcode=tracker.get_slot("new_passcode")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted(),SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
        result=change_customer_details("passcode",new_passcode,user)
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted()]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="passcode")
        return [SlotSet("new_passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
class ActionChangePassword(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("new_password")
        ]
    def name(self):
        return 'action_change_password'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        service_access=tracker.get_slot("service_access")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        new_password=tracker.get_slot("new_password")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted(),SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
        result=change_customer_details("password",new_password,user)
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted()]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="password")
        return [AllSlotsReset()]
class ActionGetOTPPermission(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("got_otp")
        ]
    def name(self):
        return 'action_get_otp_permission'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        user,password,got_otp=tracker.get_slot("email"),tracker.get_slot("password"),tracker.get_slot("got_otp")
        last_otp=tracker.get_slot("last_otp")
        last_otp=int(last_otp)
        if got_otp==None or last_otp==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted(),SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
        got_otp=int(got_otp)
        if got_otp==1:
            otp=send_otp_to_customer(user,password)
            return [SlotSet("last_otp",otp),SlotSet("requested_slot","got_otp")]
        if got_otp==2:
            return [SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
        if last_otp==got_otp:
            return [SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",1)]
        dispatcher.utter_message("OTP is not valid\nPlease enter valid OTP:\n")
        return [SlotSet("got_otp",None),SlotSet("requested_slot","got_otp"),SlotSet("service_access",0)]
class ActionSendOTP(Action):
    def name(self):
        return 'action_send_otp'
    def run(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        #otp=send_otp_to_customer(user,password)
        otp=111111
        dispatcher.utter_template("utter_ask_got_otp",tracker)
        return [SlotSet("last_otp",otp),SlotSet("requested_slot","got_otp")]
class ActionChangeUsername(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("username")
        ]
    def name(self):
        return 'action_change_username'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        service_access=tracker.get_slot("service_access")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        username=tracker.get_slot("username")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted(),SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
        result=change_customer_details("username",username,user)
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted()]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="username")
        return [SlotSet("username",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
class ActionChangeAddress(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("address1"),
        FreeTextFormField("address2")
        ]
    def name(self):
        return 'action_change_address'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        service_access=tracker.get_slot("service_access")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted(),SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
        address1=tracker.get_slot("address1")
        address2=tracker.get_slot("address2")
        address="%s, %s"%(address1,address2)
        result=change_customer_details("postal_add",address,user)
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [ActionReverted()]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="postal address")
        return [SlotSet("address1",None),SlotSet("address2",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
class ActionChangeCredentialInfo(Action):
    def name(self):
        return 'action_change_credential_info'
    def run(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        service_access=tracker.get_slot("service_access")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        entities=tracker.latest_message.entities
        ent=""
        if len(entities)>0:
            ent=entities[0]["value"]
        ent=get_pure_ent(ent)
        dispatcher.utter_template("utter_change_credential_info_reply",tracker,name=name,ent=ent)
        return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot",None),SlotSet("service_access",0)]
class ActionGetAccStatus(Action):
    def name(self):
        return 'action_get_acc_status'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        hasAcc=get_personal_info(user,password,"hasAcc")
        template="utter_get_acc_status_reply_"
        if hasAcc!=0:
            status=get_account_info(user,password,"status")
            status=int(status)
            if status in [0,1]:
                template+="%s"%status
            else:
                template="utter_error_caught_reply"
        else:
            template+="2"
        dispatcher.utter_template(template,tracker,name=name)
        return []
class ActionGetContact(Action):
    def name(self):
        return 'action_get_contact'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        contact=get_personal_info(user,password,"contact")
        dispatcher.utter_template("utter_got_asked_reply",tracker,name=name,key="contact number",value=contact)
        return []
class ActionGetEmail(Action):
    def name(self):
        return 'action_get_email'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        email=get_personal_info(user,password,"email")
        key=random.choice(['email id','email address','email'])
        dispatcher.utter_template("utter_got_asked_reply",tracker,name=name,key=key,value=email)
        return []
class ActionGetUsername(Action):
    def name(self):
        return 'action_get_username'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        username=get_personal_info(user,password,"username")
        dispatcher.utter_template("utter_got_asked_reply",tracker,name=name,key="username",value=username)
        return []
class ActionGetAccountNumber(Action):
    def name(self):
        return 'action_get_account_number'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        acc_no=get_account_info(user,password,"acc_no")
        dispatcher.utter_template("utter_got_asked_reply",tracker,name=name,key="account number",value=acc_no)
        return []
class ActionGetSecureInfo(Action):
    def name(self):
        return 'action_get_secure_info'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        entities=tracker.latest_message.entities
        template="utter_get_secure_info_reply"
        ent=""
        if len(entities)>0:
            ent=entities[0]["value"]
        dispatcher.utter_template(template,tracker,name=name,ent=ent)
        return []
class ActionGetCardNumber(Action):
    def name(self):
        return 'action_get_card_number'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        card_no=get_card_info(user,password,"card_no")
        dispatcher.utter_template("utter_got_asked_reply",tracker,name=name,key="card number",value=card_no)
        return []
class ActionGetAddress(Action):
    def name(self):
        return 'action_get_address'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        postal_add=get_personal_info(user,password,"postal_add")
        dispatcher.utter_template("utter_got_asked_reply",tracker,name=name,key="postal address",value=postal_add)
        return []
class ActionGetPermission(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("passcode"),
        BooleanFormField("card_perm","affirm","deny")
        ]
    def name(self):
        return 'action_get_permission'
    def submit(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        user,password,passcode=tracker.get_slot("email"),tracker.get_slot("password"),tracker.get_slot("passcode")
        card_perm=tracker.get_slot("card_perm")
        if passcode==None or card_perm==None:
            return [ActionReverted()]
        if card_perm!=True:
            return [SlotSet("passcode",None),SlotSet("card_permission",None),SlotSet("requested_slot",None)]
        results = check_passcode(user,password,passcode)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot",None),SlotSet("service_access",1)]
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
        results = check_indentity(user,password)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        name = get_personal_info(user,password,"fname")
        card_status=get_card_info(user,password,"status")
        dispatcher.utter_template("utter_access",tracker)
        return [SlotSet("access", results),SlotSet("name",name),SlotSet("requested_slot",None),SlotSet("card_status",card_status)]
class ActionGreeting(Action):
    def name(self):
        return 'action_greeting'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot("name")
        name=get_user_name(name)
        text=tracker.latest_message.text
        template="utter_greet_reply"
        if text.endswith("?"):
            template="utter_greet_with_question_reply"
        dispatcher.utter_template(template,tracker,name=name)
        return []
class ActionEnding(Action):
    def name(self):
        return 'action_ending'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot("name")
        name=get_user_name(name)
        dispatcher.utter_template("utter_ending_reply",tracker,name=name)
        return []
class ActionHumanOrBot(Action):
    def name(self):
        return 'action_human_or_bot'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot("name")
        name=get_user_name(name)
        dispatcher.utter_template("utter_human_or_bot_reply",tracker)
        return []
class ActionNegativeFeedback(Action):
    def name(self):
        return 'action_negative_feedback'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot("name")
        name=get_user_name(name)
        dispatcher.utter_template("utter_negative_feedback_reply",tracker,name=name)
        return []
class ActionPositiveFeedback(Action):
    def name(self):
        return 'action_positive_feedback'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot("name")
        name=get_user_name(name)
        dispatcher.utter_template("utter_positive_feedback_reply",tracker, name=name)
        return []
class ActionSecurityAssurance(Action):
    def name(self):
        return 'action_security_assurance'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot("name")
        name=get_user_name(name)
        dispatcher.utter_template("utter_security_assurance_reply",tracker)
        return []
class ActionFallback(Action):
    def name(self):
        return 'action_fallback'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot("name")
        name=get_user_name(name)
        dispatcher.utter_template("utter_fallback",tracker)
        return []
class ActivateCardService(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("passcode"),
        BooleanFormField("card_permission","affirm","deny")
        ]
    def name(self):
        return 'action_activate_card'
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
        if passcode==None:
            return [ActionReverted()]
        if card_permission!=True:
            return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
        results = check_passcode(user,password,passcode)
        ent="card"
        template="utter_fallback"
        if results==1:
            t1=tracker.copy()
            entities=t1.latest_message.entities
            intent=t1.latest_message.intent['name']
            while (intent!="Banking_Activate_Card"):
                t1.update(UserUtteranceReverted())
                entities=t1.latest_message.entities
                intent=t1.latest_message.intent['name']
            if intent=="Banking_Activate_Card":
                results=get_active_card(user,password,passcode)
                if results==-33:
                    dispatcher.utter_message("Your do not have any account yet.")
                    return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
                elif results==-22:
                    dispatcher.utter_message("Your card is already activated.")
                    return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
                template="utter_activated_card"
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
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
class CancelCardService(FormAction):
    RANDOMIZE = False
    @staticmethod
    def required_fields():
        return [
        FreeTextFormField("passcode"),
        BooleanFormField("card_permission","affirm","deny")
        ]
    def name(self):
        return 'action_cancel_card'
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
        if passcode==None:
            return [ActionReverted()]
        if card_permission!=True:
            return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
        results = check_passcode(user,password,passcode)
        ent="card"
        template="utter_fallback"
        if results==1:
            t1=tracker.copy()
            entities=t1.latest_message.entities
            intent=t1.latest_message.intent['name']
            while (intent!="Banking_Cancel_Card"):
                t1.update(UserUtteranceReverted())
                entities=t1.latest_message.entities
                intent=t1.latest_message.intent['name']
            if intent=="Banking_Cancel_Card":
                results=get_deactive_card(user,password,passcode)
                if results==-33:
                    dispatcher.utter_message("Your do not have any account yet.")
                    return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
                elif results==-22:
                    dispatcher.utter_message("Your card is already deactivated.")
                    return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
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
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
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
        FreeTextFormField("passcode"),
        BooleanFormField("card_perm","affirm","deny")
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
        if passcode==None or card_replace_with==None or card_perm==None:
            return [ActionReverted()]
        if card_perm!=True:
            return [SlotSet("passcode",None),SlotSet("card_permission",None),SlotSet("requested_slot",None),SlotSet("card_replace_with",None)]
        results = check_passcode(user,password,passcode)
        if int(results)!=1:
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        results = card_replace(user,password,card_replace_with)
        if results!=1:
            dispatcher.utter_message("Please enter valid card number: ")
            return [SlotSet("card_replace_with",None),SlotSet("requested_slot","card_replace_with")]
        dispatcher.utter_template("utter_replace_card_reply",tracker)
        return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot",None),SlotSet("card_replace_with",None)]

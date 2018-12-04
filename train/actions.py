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
import random,re
import security
class ActionBotDesc(Action):
    def name(self):
        return "action_get_bot_desc"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        dispatcher.utter_template("utter_bot_desc",tracker,name=name)
        return []
class ActionGetAccountBalance(Action):
    def name(self):
        return "action_get_account_balance"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        service_access=tracker.get_slot("service_access")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("requested_slot",None),SlotSet("service_access",None)]
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
        balance=get_account_info(user,password,"balance")
        acc=random.choice(['account','a/c','acc'])
        dispatcher.utter_template("utter_get_account_balance_reply",tracker,name=name,balance=balance,acc=acc)
        return [SlotSet("requested_slot",None),SlotSet("service_access",None)]
class ActionGetAccountDetails(Action):
    def name(self):
        return "action_get_account_details"
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
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
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
        cardExist=customer_card_has(userid)
        if cardExist==-22:
            dispatcher.utter_message("You do not have any card yet, But you can apply for a card application.")
            return []
        elif cardExist==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
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
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
        cardExist=customer_card_has(userid)
        if cardExist==-22:
            dispatcher.utter_message("You do not have any card yet, But you can apply for a card application.")
            return []
        elif cardExist==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
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
        if results!=1:
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
        if results!=1:
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
        if results!=1:
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
        if results!=1:
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
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return [SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        transfer_perm=tracker.get_slot("transfer_perm")
        where=tracker.get_slot("where")
        amount=tracker.get_slot("amount")
        amount=str(amount)
        if transfer_perm==None:
            return [SlotSet("transfer_perm",None),SlotSet("requested_slot","transfer_perm"),SlotSet("service_access",None)]
        if transfer_perm!=True:
            return [SlotSet("transfer_perm",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        userid=get_personal_info(user,password,"cid")
        from_acc_no=get_account_info(user,password,"acc_no")
        result_where=str(check_acc_num_exists(where,userid))
        if not result_where.startswith("11"):
            dispatcher.utter_message("Please enter valid account number: ")
            return [SlotSet("where",None),SlotSet("amount",None),SlotSet("requested_slot","where")]
        if amount==None or (not re.match("[0-9]+",amount)):
            dispatcher.utter_message("Please enter valid amount: ")
            return [SlotSet("amount",None),SlotSet("requested_slot","amount")]
        try:
            amount=int(amount)
        except:
            dispatcher.utter_message("Please enter valid amount: ")
            return [SlotSet("amount",None),SlotSet("requested_slot","amount")]
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
        if last_otp==-99 or got_otp==None:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        got_otp=str(got_otp)
        if (not re.match("[0-9]+",got_otp)):
            dispatcher.utter_message("Transaction Failed! OTP was not correct.")
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        got_otp=int(got_otp)
        if got_otp==1:
            otp=send_otp_to_customer(user,password)
            return [SlotSet("last_otp",otp),SlotSet("got_otp",None),SlotSet("requested_slot","got_otp")]
        if got_otp==2:
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        if last_otp!=got_otp:
            dispatcher.utter_message("Transaction Failed! OTP was incorrect!")
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        result_transfer=str(make_transaction(from_acc_no,to_acc_no,amount))
        if result_transfer=="-22":
            dispatcher.utter_message("Transaction Failed! You have inefficient money.")
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("transfer_perm",None),SlotSet("where",None),SlotSet("amount",None),SlotSet("service_access",None),SlotSet("requested_slot",None)]
        elif not result_transfer.startswith("11"):
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
        otp=send_otp_to_customer(user,password)
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
        service_access=tracker.get_slot("service_access")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("num_trans",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("num_trans",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return [SlotSet("num_trans",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
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
        ans=security.protect_data(str(ans))
        dispatcher.utter_template(template,tracker,name=name,ans=ans)
        return [SlotSet("num_trans",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
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
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
        cardExist=customer_card_has(userid)
        if cardExist==-22:
            dispatcher.utter_message("You do not have any card yet, But you can apply for a card application.")
            return []
        elif cardExist==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
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
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        result=change_customer_details("contact",contact,user)
        if result==-11:
            dispatcher.utter_message("This contact number is already registered with another account")
            return [SlotSet("contact",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("contact",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="contact")
        return [SlotSet("contact",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
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
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        new_passcode=str(new_passcode)
        if not re.match("[0-9]{6}",new_passcode):
            dispatcher.utter_message("Passcode should not contain character and it should be of 6 numbers.\nPlease enter valid Passcode:\n")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode"),SlotSet("service_access",service_access)]
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("new_passcode",None),SlotSet("passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return [SlotSet("new_passcode",None),SlotSet("passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        result=change_customer_details("passcode",new_passcode,user)
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("new_passcode",None),SlotSet("passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="passcode")
        return [SlotSet("new_passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
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
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        new_password=str(new_password)
        if not re.match("^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})",new_password):
            dispatcher.utter_message("Password should contain at least one number and at least one character. It also have at least length of 6 characters.\n Please enter new password:")
            return [SlotSet("new_password",None),SlotSet("requested_slot","new_password"),SlotSet("service_access",service_access)]
        result=change_customer_details("password",new_password,user)
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("requested_slot",None),SlotSet("service_access",None)]
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
            return [ActionReverted(),SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        got_otp=str(got_otp)
        if not re.match("[0-9]+",got_otp):
            dispatcher.utter_message("OTP is not valid\nPlease enter valid OTP:\n")
            return [SlotSet("got_otp",None),SlotSet("requested_slot","got_otp"),SlotSet("service_access",None)]
        got_otp=int(got_otp)
        if got_otp==1:
            otp=send_otp_to_customer(user,password)
            return [SlotSet("last_otp",otp),SlotSet("requested_slot","got_otp")]
        if got_otp==2:
            return [SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        if last_otp==got_otp:
            return [SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",1)]
        dispatcher.utter_message("OTP is not valid\nPlease enter valid OTP:\n")
        return [SlotSet("got_otp",None),SlotSet("requested_slot","got_otp"),SlotSet("service_access",None)]
class ActionSendOTP(Action):
    def name(self):
        return 'action_send_otp'
    def run(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        otp=send_otp_to_customer(user,password)
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
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        result=change_customer_details("username",username,user)
        if result==-11:
            dispatcher.utter_message("This contact number is already registered with another account")
            return [SlotSet("username",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("username",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="username")
        return [SlotSet("username",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
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
            return [SlotSet("last_otp",None),SlotSet("got_otp",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        address1=tracker.get_slot("address1")
        address2=tracker.get_slot("address2")
        address="%s, %s"%(address1,address2)
        result=change_customer_details("postal_add",address,user)
        if result!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("address1",None),SlotSet("address2",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        dispatcher.utter_template("utter_change_entity_reply",tracker,name=name,ent="postal address")
        return [SlotSet("address1",None),SlotSet("address2",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
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
        entities=tracker.latest_message["entities"]
        ent=""
        if len(entities)>0:
            ent=entities[0]["value"]
        ent=get_pure_ent(ent)
        dispatcher.utter_template("utter_change_credential_info_reply",tracker,name=name,ent=ent)
        return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
class ActionCardRequest(Action):
    def name(self):
        return 'action_card_request'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
        cardExist=customer_card_has(userid)
        if cardExist==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif cardExist!=-22:
            dispatcher.utter_message("You already have a card. If you have lost your card you can cancel your card and replace your card.")
            return []
        acc_id=get_account_details_by_id(userid,"acc_id")
        res=check_request_exist(acc_id)
        if res>0:
            mes="%s You already have raised a request for card application.\nYou can ask me about status of card application."%name
            dispatcher.utter_message(mes)
            return []
        elif res==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        results=str(request_services(acc_id,"card"))
        if results=="11":
            template="utter_card_request_reply"
            dispatcher.utter_template(template,tracker,name=name)
        else:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
        return []
class ActionGetCardRequestStatus(Action):
    def name(self):
        return 'action_get_card_request_status'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
        cardExist=customer_card_has(userid)
        if cardExist==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif cardExist!=-22:
            dispatcher.utter_message("You already have a card.")
            return []
        acc_id=get_account_details_by_id(userid,"acc_id")
        res=check_request_exist(acc_id)
        if res!=1:
            mes="%s You haven't raised any request for card application."%name
            dispatcher.utter_message(mes)
            return []
        elif res==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        hasCard=str(get_request_details_by_acc_id(acc_id,"status"))
        if hasCard=="1":
            value="approved."
        elif hasCard=="-1":
            value="rejected. Contact branch for more information."
        elif hasCard=="0":
            value="still pending."
        else:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        template="utter_get_card_exist_status_reply"
        dispatcher.utter_template(template,tracker,name=name,value=value)
        return []
class ActionGetAccStatus(Action):
    def name(self):
        return 'action_get_acc_status'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if results!=1:
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
        if results!=1:
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
        if results!=1:
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
        if results!=1:
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
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
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
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        entities=tracker.latest_message["entities"]
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
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
        cardExist=customer_card_has(userid)
        if cardExist==-22:
            dispatcher.utter_message("You do not have any card yet, But you can apply for a card application.")
            return []
        elif cardExist==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
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
        if results!=1:
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
        if passcode==None:
            return [ActionReverted()]
        passcode=str(passcode)
        if not re.match("[0-9]+",passcode):
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        results = check_passcode(user,password,passcode)
        if results==1:
            return [SlotSet("passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",1)]
        dispatcher.utter_message("Please enter valid passcode: ")
        return [SlotSet("passcode",None),SlotSet("requested_slot","passcode"),SlotSet("service_access",None)]
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
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        name = get_personal_info(user,password,"fname")
        access=tracker.get_slot("access")
        if access==1:
            template="utter_already_login"
        template="utter_access"
        dispatcher.utter_template(template,tracker)
        return [SlotSet("access", results),SlotSet("name",name),SlotSet("requested_slot",None)]
class ActionGreeting(Action):
    def name(self):
        return 'action_greeting'
    def run(self, dispatcher, tracker, domain):
        name=tracker.get_slot("name")
        name=get_user_name(name)
        text=tracker.latest_message['text']
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
        return [AllSlotsReset()]
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
        name=tracker.get_slot("name")
        name=get_user_name(name)
        service_access=tracker.get_slot("service_access")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("card_replace_with",None),SlotSet("requested_slot",None)]
        card_permission=tracker.get_slot("card_permission")
        question_yes_no=tracker.get_slot("question_yes_no")
        using_what=tracker.get_slot("using_what")
        if passcode==None:
            return [ActionReverted()]
        if card_permission!=True:
            return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
        passcode=str(passcode)
        if not re.match("[0-9]+",passcode):
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        results = check_passcode(user,password,passcode)
        template="utter_fallback"
        if results==1:
            results=get_active_card(user,password,passcode)
            if results==-33:
                dispatcher.utter_message("Your do not have any account yet.")
                return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
            elif results==-22:
                dispatcher.utter_message("Your card is already activated.")
                return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
            template="utter_activated_card"
            card_type=tracker.get_slot("card_type")
            using_what=tracker.get_slot("using_what")
            if card_type==None:
                card_type="card"
            if using_what==None:
                using_what=""
            else:
                using_what=" %s"%using_what
            dispatcher.utter_template(template,tracker,card_type=card_type.capitalize(),using_what=using_what)
        else:
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
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
        name=tracker.get_slot("name")
        name=get_user_name(name)
        service_access=tracker.get_slot("service_access")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        card_permission=tracker.get_slot("card_permission")
        question_yes_no=tracker.get_slot("question_yes_no")
        using_what=tracker.get_slot("using_what")
        if passcode==None:
            return [ActionReverted()]
        if card_permission!=True:
            return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        passcode=str(passcode)
        if not re.match("[0-9]+",passcode):
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        results = check_passcode(user,password,passcode)
        template="utter_fallback"
        if results==1:
            results=get_deactive_card(user,password,passcode)
            if results==-33:
                dispatcher.utter_message("Your do not have any account yet.")
                return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
            elif results==-22:
                dispatcher.utter_message("Your card is already deactivated.")
                return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None)]
            template="utter_deactivated_card"
            card_type=tracker.get_slot("card_type")
            using_what=tracker.get_slot("using_what")
            if card_type==None:
                card_type="card"
            if using_what==None:
                using_what=""
            else:
                using_what=" %s"%using_what
            dispatcher.utter_template(template,tracker,card_type=card_type.capitalize(),using_what=using_what)
        else:
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("requested_slot","passcode")]
        return [SlotSet("card_permission",None),SlotSet("passcode",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
class GetFeeInquiry(Action):
    def name(self):
        return 'action_fee_inquiry'
    def run(self, dispatcher, tracker, domain):
        user,password=tracker.get_slot("email"),tracker.get_slot("password")
        access=tracker.get_slot("access")
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        name=tracker.get_slot("name")
        name=get_user_name(name)
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return []
        cardExist=customer_card_has(userid)
        if cardExist==-22:
            dispatcher.utter_message("You do not have any card yet, But you can apply for a card application. You can always check status for card application in your Personal Settings Panel or you could ask me which will be easy for you i guess!")
            return []
        elif cardExist==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return []
        fees=get_fee_info(user,password)
        fees=int(fees)
        fees=round(fees,2)
        dispatcher.utter_template("utter_fee_inquiry_reply",tracker,fees=fees)
        return []
class ActionCheckAccAndCard(Action):
    def name(self):
        return 'action_check_account_and_card'
    def run(self, dispatcher, tracker, domain):
        user=tracker.get_slot("email")
        password=tracker.get_slot("password")
        name=tracker.get_slot("name")
        name=get_user_name(name)
        results = check_indentity(user,password)
        if results!=1:
            dispatcher.utter_message("Please enter valid information")
            return [ActionReverted(),AllSlotsReset()]
        userid=get_personal_info(user,password,"cid")
        hasAcc=get_personal_info(user,password,"hasAcc")
        if hasAcc==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("card_replace_with",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        elif hasAcc==0:
            dispatcher.utter_message("You do not have any account yet. You can apply for a card application after getting an JonSnow Bank account.")
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("card_replace_with",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        cardExist=customer_card_has(userid)
        if cardExist==-22:
            acc_id=get_account_details_by_id(userid,"acc_id")
            res=check_request_exist(acc_id)
            if res!=1:
                mes="%s You do not have any card yet, But you can apply for a card application."%name
                dispatcher.utter_message(mes)
                return []
            elif res==-99:
                dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
                return []
            dispatcher.utter_message("You do not have any card yet, But as i can see you already have raised a request for card application.")
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("card_replace_with",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        elif cardExist==-99:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("card_replace_with",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        return [SlotSet("service_access",1)]
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
        name=tracker.get_slot("name")
        name=get_user_name(name)
        if user==None or password==None or access!=1:
            dispatcher.utter_message("Please log in our service, to use Jon service!")
            return [ActionReverted(),AllSlotsReset()]
        user,password,passcode=tracker.get_slot("email"),tracker.get_slot("password"),tracker.get_slot("passcode")
        service_access=tracker.get_slot("service_access")
        if service_access!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("card_replace_with",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        card_perm=tracker.get_slot("card_perm")
        userid=get_personal_info(user,password,"cid")
        card_replace_with=tracker.get_slot("card_replace_with")
        if passcode==None or card_replace_with==None or card_perm==None:
            return [ActionReverted()]
        if card_perm!=True:
            return [SlotSet("passcode",None),SlotSet("card_permission",None),SlotSet("requested_slot",None),SlotSet("card_replace_with",None),SlotSet("service_access",None)]
        passcode=str(passcode)
        card_replace_with=str(card_replace_with)
        if not re.match("[0-9]+",card_replace_with):
            dispatcher.utter_message("Please enter valid card number: ")
            return [SlotSet("card_replace_with",None),SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot","card_replace_with")]
        f=customer_card_exists(userid,card_replace_with)
        if f!=1:
            dispatcher.utter_message("Please enter valid card number: ")
            return [SlotSet("card_replace_with",None),SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot","card_replace_with")]
        if not re.match("[0-9]+",passcode):
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot","passcode")]
        results = check_passcode(user,password,passcode)
        if results!=1:
            dispatcher.utter_message("Please enter valid passcode: ")
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("requested_slot","passcode")]
        results = card_replace(user,password,card_replace_with)
        if results!=1:
            dispatcher.utter_template("utter_error_caught_reply",tracker,name=name)
            return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("card_replace_with",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]
        dispatcher.utter_template("utter_replace_card_reply",tracker)
        return [SlotSet("passcode",None),SlotSet("card_perm",None),SlotSet("card_replace_with",None),SlotSet("requested_slot",None),SlotSet("service_access",None)]

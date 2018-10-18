import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from config import *
from security import *
from customer_details import *
from admin_control import *
from send_mail import Mail
from string import punctuation
def check_indentity(user,password):
    user=protect_data(user)
    password=protect_data(password)
    conn,cursor=connect_to_database()
    sql="select * from customers where email='%s' and password='%s'"%(user,password)
    try:
        cursor.execute(sql)
        num=cursor.rowcount
        if num==1:
            return 1
        else:
            return -99
    except:
        return -99

def check_passcode(user,password,passcode):
    f=check_indentity(user,password)
    if f!=1:
        return -99
    user=protect_data(user)
    password=protect_data(password)
    passcode=protect_data(passcode)
    ori_passcode=get_account_details_by_user(user,"passcode")
    try:
        if int(ori_passcode)==int(passcode):
            return 1
        else:
            return -99
    except:
        return -99

def get_active_card(user,password,passcode):
    f1=check_indentity(user,password)
    f3=get_any_value(user,"hasAcc")
    if f3!=1:
        return -33
    f2=check_passcode(user,password,passcode)
    if f1!=1 and f2!=1:
        return -99
    status=get_card_details_by_user(user,"status")
    if status==1:
        return -22
    return change_customer_card_status(user,1)

def get_deactive_card(user,password,passcode):
    f1=check_indentity(user,password)
    f2=check_passcode(user,password,passcode)
    if f1!=1 and f2!=1:
        return -99
    status=get_card_details_by_user(user,"status")
    if status==0:
        return -22
    return change_customer_card_status(user,0)

def get_fee_info(user,password):
    f=check_indentity(user,password)
    if f!=1:
        return -99
    user=protect_data(user)
    password=protect_data(password)
    f=get_card_details_by_user(user,"card_type")
    if f==0:
        return -99
    else:
        if f=="Mastercard":
            return "10"
        elif f=="Visacard":
            return "20"
        else:
            return "05"
def card_replace(user,password,old_card):
    f=check_indentity(user,password)
    if f!=1:
        return -99
    user=protect_data(user)
    password=protect_data(password)
    acc_id=get_account_details_by_user(user,"acc_id")
    card_no=get_card_details_by_user(user,"card_no")
    if str(card_no)!=str(old_card):
        return -99
    b=delete_customer_card("card_no",card_no)
    c=delete_customer_request(acc_id,"card")
    if b==11 and c==11:
        b=str(request_services(acc_id,"card"))
        if b=="11":
            return 1
    return -99
def get_personal_info(user,password,field):
    f=check_indentity(user,password)
    if f!=1:
        return -99
    return get_any_value(user,field)
def get_account_info(user,password,field):
    f=check_indentity(user,password)
    if f!=1:
        return -99
    return get_account_details_by_user(user,field)
def get_card_info(user,password,field):
    f=check_indentity(user,password)
    if f!=1:
        return -99
    return get_card_details_by_user(user,field)
def get_user_name(name):
    if name!=None:
        name=str(name)
        name2="Mr. %s"%name
        name=random.choice(['Human','',"Boss","Sir",name,name2])
    else:
        name=random.choice(['Human','',"Boss","Sir"])
    return name
def get_pure_ent(ent):
    l1=list(punctuation)
    for i in range(len(l1)):
        ent=ent.replace(l1[i]," ")
    return ent
def get_final_entity(ent):
    "still remained"
    acc_num=["acc number","account number","acc number","account no","acc no","acc_no",'no of account','number of acc','no of acc','number of account']
    card_num=["card number","card no","card num"]
    till_month=["till_month","till month","expiry month"]
    till_year=["till_year","till year","expiry year"]
    cvv=['csv','cv','cvv']
    card_type=['card type','card_type','type of card','type of my card']
    holder_name=['holder name','final name','name','account name','acc name','acc_name','accountname','holder_name','holder','name of holder']
    gender=['gender','sexuality','sex']
    ent=get_pure_ent(ent)
    if ent in acc_num:
        return "acc_no"
    elif ent in card_num:
        return "card_no"
    elif ent in till_month:
        return "till_month"
    elif ent in till_year:
        return "till_year"
def send_otp_to_customer(user,password):
    f=check_indentity(user,password)
    if f!=1:
        return -99
    m=Mail()
    return m.send_otp_mail(user)

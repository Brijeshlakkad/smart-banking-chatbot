import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from config import *
from security import *
from customer_details import *
from admin_control import *
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
    f2=check_passcode(user,password,passcode)
    if f1!=1 and f2!=1:
        return -99
    return change_customer_card_status(user,1)

def get_deactive_card(user,password,passcode):
    f1=check_indentity(user,password)
    f2=check_passcode(user,password,passcode)
    if f1!=1 and f2!=1:
        return -99
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
    if b==11:
        b=int(create_card(acc_id))
        if b==11:
            return 1
    return -99
def get_personal_info(user,password,field):
    f=check_indentity(user,password)
    if f!=1:
        return -99
    return get_any_value(user,field)
def get_user_name(name):
    if name!=None:
        name=str(name)
        name2="Mr. %s"%name
        name=random.choice(['Human','',"Boss","Sir",name,name2])
    else:
        name=random.choice(['Human','',"Boss","Sir"])
    return name

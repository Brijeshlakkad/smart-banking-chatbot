ALL:
* General_Greetings
    - utter_first_access
    - action_get_access
    - slot{"requested_slot": "email"}
* Banking_Email
    - action_get_access
    - slot{"email": "brijeshlakkad22@gmail.com"}
    - slot{"requested_slot": "password"}
* Banking_Password
    - action_get_access
    - slot{"password": "123456bB"}
    - slot{"access": 1}
    - slot{"name": "Brijesh"}
    - slot{"requested_slot": null}

* affirm
    - utter_just_reply
* deny
    - utter_just_reply
* General_Greetings
    - action_greeting
* None
    - action_fallback
* Banking_Email
    - action_fallback
* Banking_Password
    - action_fallback
* Banking_Card_Number
    - action_fallback
* Banking_Card_Number
    - action_fallback
* Banking_Activate_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_activate_card
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_activate_card
    - slot{"passcode": "683240"}
    - slot{"requested_slot": "card_permission"}
* affirm
    - action_activate_card
    - slot{"card_permission": true}
    - slot{"card_permission": null}
    - slot{"passcode": null}
    - slot{"requested_slot": null}

* Banking_Cancel_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_cancel_card
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_cancel_card
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_permission"}
* affirm
    - action_cancel_card
    - slot{"card_permission": true}
    - slot{"card_permission": null}
    - slot{"passcode": null}
    - slot{"requested_slot": null}

* Banking_Fee_Inquiry
    - action_fee_inquiry

* Banking_Replace_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_card_replace
    - slot{"requested_slot": "card_replace_with"}
* Banking_Card_Number
    - action_card_replace
    - slot{"card_replace_with": "3667609902587292"}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683240"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"card_replace_with": null}
    - slot{"requested_slot": null}

* General_Human_or_Bot
    - action_human_or_bot
* General_Security_Assurance
    - action_security_assurance
* affirm
    - utter_just_reply
* General_Positive_Feedback
    - action_positive_feedback
* General_Negative_Feedback
    - action_negative_feedback
* Banking_Get_Card_Number{"to_change": "card number"}
    - action_get_card_number
* Banking_Get_Email
    - action_get_email
* Banking_Get_Address
    - action_get_address
* Banking_Get_Secure_Info{"to_get": "password"}
    - action_get_secure_info
* Banking_Get_Secure_Info{"to_get": "passcode"}
    - action_get_secure_info
* Banking_Get_Account_Number
    - action_get_account_number
* Banking_Get_Username
    - action_get_username
* Banking_Get_Acc_Status
    - action_get_acc_status
* Banking_Get_Contact
    - action_get_contact

* Banking_Change_Address
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "111111"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_address
    - slot{"requested_slot": "address1"}
* Bot_Control_Change_Subject
    - action_change_address
    - slot{"address1": "line 333"}
    - slot{"requested_slot": "address2"}
* Bot_Control_Change_Subject
    - action_change_address
    - slot{"address2": "line 444"}
    - slot{"address1": null}
    - slot{"address2": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Change_Credential_Info{"to_change": "email i d"}
    - action_change_credential_info
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_Change_Credential_Info{"to_change": "cvv"}
    - action_change_credential_info
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_Change_Credential_Info{"to_change": "card number"}
    - action_change_credential_info
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Change_Username
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "111111"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_username
    - slot{"requested_slot": "username"}
* Banking_Password
    - action_change_username
    - slot{"username": "brij79"}
    - slot{"username": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Change_Passcode
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "111111"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_passcode
    - slot{"requested_slot": "new_passcode"}
* Banking_Card_Number
    - action_change_passcode
    - slot{"new_passcode": "683249"}
    - slot{"new_passcode": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Change_Password
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "111111"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_password
    - slot{"requested_slot": "new_password"}
* Banking_Password
    - action_change_password
    - slot{"new_password": "123456bB"}
    - reset_slots
    - utter_first_access
    - action_get_access
    - slot{"requested_slot": "email"}
* Banking_Email
    - action_get_access
    - slot{"email": "brijeshlakkad22@gmail.com"}
    - slot{"requested_slot": "password"}
* Banking_Password
    - action_get_access
    - slot{"password": "123456bB"}
    - slot{"access": 1}
    - slot{"name": "Brijesh"}
    - slot{"requested_slot": null}


* Banking_Change_Contact
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "111111"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_contact
    - slot{"requested_slot": "contact"}
* Banking_Card_Number
    - action_change_contact
    - slot{"contact": "7046167268"}
    - slot{"contact": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Report_Missing_Card
    - action_report_missing_card

* Banking_View_Activity{"num_trans": "3"}
    - slot{"num_trans": "3"}
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_view_activity
    - slot{"num_trans": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_View_Activity
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_view_activity
    - slot{"requested_slot": "num_trans"}
* Banking_Password
    - action_view_activity
    - slot{"num_trans": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Transfer_Money
    - action_ask_input_transfer_money
    - slot{"requested_slot": "transfer_perm"}
* affirm
    - action_ask_input_transfer_money
    - slot{"transfer_perm": true}
    - slot{"requested_slot": "where"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"where": "007046167268"}
    - slot{"requested_slot": "amount"}
* Banking_Password
    - action_ask_input_transfer_money
    - slot{"amount": "112"}
    - slot{"service_access": 1}
    - slot{"requested_slot": null}
    - action_send_otp_for_transaction
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_transfer_money
    - slot{"got_otp": "111111"}
    - slot{"last_otp": null}
    - slot{"got_otp": null}
    - slot{"transfer_perm": null}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"service_access": null}
    - slot{"requested_slot": null}

* Bot_Control_Change_Subject
    - action_bot_control_change_subject

* Bot_Control_Standby
    - action_bot_control_standby

* Bot_Control_Confirm_Presence
    - action_bot_control_confirm_presence

* Bot_Control_Start_Over
    - action_bot_control_start_over
    - reset_slots
    - utter_first_access
    - action_get_access
    - slot{"requested_slot": "email"}
* Banking_Email
    - action_get_access
    - slot{"email": "brijeshlakkad22@gmail.com"}
    - slot{"requested_slot": "password"}
* Banking_Password
    - action_get_access
    - slot{"password": "123456bB"}
    - slot{"access": 1}
    - slot{"name": "Brijesh"}
    - slot{"requested_slot": null}

* Banking_Get_Card_Status
    - action_get_card_status

* Banking_Get_Card_Details
    - action_get_card_details

* Banking_Get_Account_Details
    - action_get_account_details

* Banking_Get_Account_Balance
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_get_permission
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_get_permission
    - slot{"passcode": "683249"}
    - slot{"passcode": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_get_account_balance
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Get_Card_Request_Status
    - action_get_card_request_status

* Banking_Card_Request
    - action_card_request

* General_Ending
    - action_ending
    - reset_slots
* Bot_Dec
    - action_get_bot_desc
* Banking_Find_Operator
    - action_find_operator

deny:
* Banking_Activate_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_activate_card
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_activate_card
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_permission"}
* deny
    - action_activate_card
    - slot{"card_permission": false}
    - slot{"card_permission": null}
    - slot{"passcode": null}
    - slot{"requested_slot": null}


* Banking_Cancel_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_cancel_card
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_cancel_card
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_permission"}
* deny
    - action_cancel_card
    - slot{"card_permission": false}
    - slot{"card_permission": null}
    - slot{"passcode": null}
    - slot{"requested_slot": null}

* Banking_Replace_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_card_replace
    - slot{"requested_slot": "card_replace_with"}
* Banking_Card_Number
    - action_card_replace
    - slot{"card_replace_with": "8243641221541506"}
    - slot{"requested_slot": "passcode"}
* Banking_Passcode
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_perm"}
* deny
    - action_card_replace
    - slot{"card_permission": false}
    - slot{"card_permission": null}
    - slot{"passcode": null}
    - slot{"requested_slot": null}


* Banking_Transfer_Money
    - action_ask_input_transfer_money
    - slot{"requested_slot": "transfer_perm"}
* deny
    - action_ask_input_transfer_money
    - slot{"transfer_perm": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

hasAcc==0
* Banking_Activate_Card
    - action_check_account_and_card
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"card_replace_with": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}


* Banking_Cancel_Card
    - action_check_account_and_card
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"card_replace_with": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}


* Banking_Replace_Card
    - action_check_account_and_card
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"card_replace_with": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}


* Banking_View_Activity{"num_trans": "10"}
    - slot{"num_trans": "10"}
    - action_check_account_and_card
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"card_replace_with": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_View_Activity
    - action_check_account_and_card
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"card_replace_with": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Transfer_Money
    - action_ask_input_transfer_money
    - slot{"transfer_perm": null}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"service_access": null}
    - slot{"requested_slot": null}


* Banking_Get_Account_Balance
    - action_check_account_and_card
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"card_replace_with": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

Wrong info:

* Banking_Activate_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_activate_card
    - slot{"requested_slot": "passcode"}
* Banking_Passcode
    - action_activate_card
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_permission"}
* affirm
    - action_activate_card
    - slot{"card_permission": true}
    - slot{"passcode": null}
    - slot{"requested_slot": "passcode"}
* Banking_Passcode
    - action_activate_card
    - slot{"passcode": "683249"}
    - slot{"card_permission": null}
    - slot{"passcode": null}
    - slot{"requested_slot": null}


* Banking_Cancel_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_cancel_card
    - slot{"requested_slot": "passcode"}
* Banking_Passcode
    - action_cancel_card
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_permission"}
* affirm
    - action_cancel_card
    - slot{"card_permission": true}
    - slot{"passcode": null}
    - slot{"requested_slot": "passcode"}
* Banking_Passcode
    - action_cancel_card
    - slot{"passcode": "683249"}
    - slot{"card_permission": null}
    - slot{"passcode": null}
    - slot{"requested_slot": null}

* Banking_Replace_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_card_replace
    - slot{"requested_slot": "card_replace_with"}
* Banking_Password
    - action_card_replace
    - slot{"card_replace_with": "31t237t12873"}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"card_replace_with": null}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": "card_replace_with"}
* Banking_Card_Number
    - action_card_replace
    - slot{"card_replace_with": "5743344187443345"}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"card_replace_with": null}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": "card_replace_with"}
* Banking_Card_Number
    - action_card_replace
    - slot{"card_replace_with": "5743344187443345"}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"card_replace_with": null}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": "card_replace_with"}
* Banking_Card_Number
    - action_card_replace
    - slot{"card_replace_with": "5743344187443345"}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"card_replace_with": null}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": "card_replace_with"}
* Banking_Card_Number
    - action_card_replace
    - slot{"card_replace_with": "5743344187443345"}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": null}
    - slot{"card_replace_with": null}

* Banking_Replace_Card
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_card_replace
    - slot{"requested_slot": "card_replace_with"}
* Banking_Card_Number
    - action_card_replace
    - slot{"card_replace_with": "3667609902587292"}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_card_replace
    - slot{"passcode": "683240"}
    - slot{"requested_slot": "card_perm"}
* affirm
    - action_card_replace
    - slot{"card_perm": true}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"card_replace_with": null}
    - slot{"requested_slot": null}
* Banking_Passcode
    - action_card_replace
    - slot{"passcode": "683249"}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": null}
    - slot{"card_replace_with": null}

* Banking_Transfer_Money
    - action_ask_input_transfer_money
    - slot{"requested_slot": "transfer_perm"}
* affirm
    - action_ask_input_transfer_money
    - slot{"transfer_perm": true}
    - slot{"requested_slot": "where"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"where": "007046167267"}
    - slot{"requested_slot": "amount"}
* Banking_Password
    - action_ask_input_transfer_money
    - slot{"amount": "112"}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"requested_slot": "where"}
* Banking_Password
    - action_ask_input_transfer_money
    - slot{"where": "004234df"}
    - slot{"requested_slot": "amount"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"amount": "34324"}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"requested_slot": "where"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"where": "007046167268"}
    - slot{"requested_slot": "amount"}
* Banking_Password
    - action_ask_input_transfer_money
    - slot{"amount": "112"}
    - slot{"service_access": 1}
    - slot{"requested_slot": null}
    - action_send_otp_for_transaction
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_transfer_money
    - slot{"got_otp": "2"}
    - slot{"last_otp": null}
    - slot{"got_otp": null}
    - slot{"transfer_perm": null}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"service_access": null}
    - slot{"requested_slot": null}

* Banking_Get_Account_Balance
    - action_check_account_and_card
    - slot{"service_access": 1}
    - action_get_permission
    - slot{"requested_slot": "passcode"}
* Banking_Card_Number
    - action_get_permission
    - slot{"passcode": "68323223"}
    - slot{"passcode": null}
    - slot{"requested_slot": "passcode"}
    - slot{"service_access": null}
* Banking_Passcode
    - action_get_permission
    - slot{"passcode": "34324234"}
    - slot{"passcode": null}
    - slot{"requested_slot": "passcode"}
    - slot{"service_access": null}
* Banking_Password
    - action_get_permission
    - slot{"passcode": "1212121"}
    - slot{"passcode": null}
    - slot{"requested_slot": "passcode"}
    - slot{"service_access": null}
* Banking_Card_Number
    - action_get_permission
    - slot{"passcode": "342433"}
    - slot{"passcode": null}
    - slot{"requested_slot": "passcode"}
    - slot{"service_access": null}
* Banking_Card_Number
    - action_get_permission
    - slot{"passcode": "128830"}
    - slot{"passcode": null}
    - slot{"requested_slot": "passcode"}
    - slot{"service_access": null}
* Banking_Card_Number
    - action_get_permission
    - slot{"passcode": "683240"}
    - slot{"passcode": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_get_account_balance
    - slot{"requested_slot": null}
    - slot{"service_access": null}

OTP with 1st option
* Banking_Transfer_Money
    - action_ask_input_transfer_money
    - slot{"requested_slot": "transfer_perm"}
* affirm
    - action_ask_input_transfer_money
    - slot{"transfer_perm": true}
    - slot{"requested_slot": "where"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"where": "007046167268"}
    - slot{"requested_slot": "amount"}
* Banking_Password
    - action_ask_input_transfer_money
    - slot{"amount": "12"}
    - slot{"service_access": 1}
    - slot{"requested_slot": null}
    - action_send_otp_for_transaction
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_transfer_money
    - slot{"got_otp": "1"}
    - slot{"last_otp": "128830"}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_transfer_money
    - slot{"got_otp": "111111"}
    - slot{"last_otp": null}
    - slot{"got_otp": null}
    - slot{"transfer_perm": null}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"service_access": null}
    - slot{"requested_slot": null}

* Banking_Change_Username
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "254431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "254431"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_username
    - slot{"requested_slot": "username"}
* Banking_Password
    - action_change_username
    - slot{"username": "brijeshlakkad"}
    - slot{"username": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Change_Address
    - action_send_otp
    - slot{"last_otp": "293872"}
    - action_get_otp_permission
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "254431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "254421"}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "344431"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_address
    - slot{"requested_slot": "address1"}
* Banking_Get_Address
    - action_change_address
    - slot{"address1": "line 111"}
    - slot{"requested_slot": "address2"}
* General_Security_Assurance
    - action_change_address
    - slot{"address2": "line 333"}
    - slot{"passcode": null}
    - slot{"card_perm": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}


* Banking_Change_Passcode{"to_get": "pincode"}
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "683249"}
    - slot{"got_otp": null}
    - slot{"requested_slot": "got_otp"}
    - slot{"service_access": null}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "344431"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_passcode
    - slot{"requested_slot": "new_passcode"}
* Banking_Passcode
    - action_change_passcode
    - slot{"new_passcode": "683240"}
    - slot{"new_passcode": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Change_Passcode{"to_get": "pincode"}
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "344431"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_passcode
    - slot{"requested_slot": "new_passcode"}
* Banking_Passcode
    - action_change_passcode
    - slot{"new_passcode": "683240"}
    - slot{"new_passcode": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}

* Banking_Change_Password{"to_get": "password"}
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "1"}
    - slot{"last_otp": "344431"}
    - slot{"requested_slot": "got_otp"}
* Banking_Card_Number
    - action_get_otp_permission
    - slot{"got_otp": "344431"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": 1}
    - action_change_password
    - slot{"requested_slot": "new_password"}
* Banking_Password
    - action_change_password
    - slot{"new_password": "123456bb"}
    - reset_slots
    - utter_first_access
    - action_get_access
    - slot{"requested_slot": "email"}
* Banking_Email
    - action_get_access
    - slot{"email": "brijeshlakkad22@gmail.com"}
    - slot{"requested_slot": "password"}
* Banking_Password
    - action_get_access
    - slot{"password": "123456bb"}
    - slot{"access": 1}
    - slot{"name": "Brijesh"}
    - slot{"requested_slot": null}


OTP with 2nd option

* Banking_Change_Address
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "2"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_Change_Username
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "2"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_Change_Password
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "2"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_Change_Passcode
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "2"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_Change_Contact
    - action_send_otp
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_get_otp_permission
    - slot{"got_otp": "2"}
    - slot{"got_otp": null}
    - slot{"requested_slot": null}
    - slot{"service_access": null}
* Banking_Transfer_Money
    - action_ask_input_transfer_money
    - slot{"requested_slot": "transfer_perm"}
* affirm
    - action_ask_input_transfer_money
    - slot{"transfer_perm": true}
    - slot{"requested_slot": "where"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"where": "007046167267"}
    - slot{"requested_slot": "amount"}
* Banking_Password
    - action_ask_input_transfer_money
    - slot{"amount": "112"}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"requested_slot": "where"}
* Banking_Password
    - action_ask_input_transfer_money
    - slot{"where": "004234df"}
    - slot{"requested_slot": "amount"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"amount": "34324"}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"requested_slot": "where"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"where": "007046167268"}
    - slot{"requested_slot": "amount"}
* Banking_Card_Number
    - action_ask_input_transfer_money
    - slot{"amount": "683240"}
    - slot{"amount": null}
    - slot{"requested_slot": "amount"}
* Banking_Password
    - action_ask_input_transfer_money
    - slot{"amount": "112"}
    - slot{"service_access": 1}
    - slot{"requested_slot": null}
    - action_send_otp_for_transaction
    - slot{"last_otp": 111111}
    - slot{"requested_slot": "got_otp"}
* Banking_Password
    - action_transfer_money
    - slot{"got_otp": "2"}
    - slot{"last_otp": null}
    - slot{"got_otp": null}
    - slot{"transfer_perm": null}
    - slot{"where": null}
    - slot{"amount": null}
    - slot{"service_access": null}
    - slot{"requested_slot": null}

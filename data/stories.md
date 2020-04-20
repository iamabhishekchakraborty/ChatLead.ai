## happy path 1
* greet
  - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - form{"name": null} 
* thank OR goodbye
  - utter_noworries

## thank
* thank OR goodbye
  - utter_noworries

## sales form
* greet
  - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}  

## rating form
* greet
  - utter_greet
* ask_rating
    - utter_ask_rating 
    - get_rating_form
    - form{"name": "get_rating_form"}
    - form{"name": null}  

## unhappy path 1
* greet
  - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
* chitchat
    - utter_chitchat
    - sales_form
    - form{"name": null}
* thank OR goodbye
  - utter_noworries

## unhappy path 2
* greet
  - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - utter_noworries

## interactive_story_1
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* form: inform{"job_function": "consultant"}
    - slot{"job_function": "consultant"}
    - form: sales_form
    - slot{"job_function": "consultant"}
    - slot{"requested_slot": "use_case"}
* form: inform{"use_case": "interactive assistant"}
    - slot{"use_case": "interactive assistant"}
    - form: sales_form
    - slot{"use_case": "interactive assistant"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "100K INR"}
    - slot{"budget": "100K INR"}
    - form: sales_form
    - slot{"budget": "100K INR"}
    - slot{"requested_slot": "person_name"}
* form: inform{"person_name": "abhibot"}
    - slot{"person_name": "abhibot"}
    - form: sales_form
    - slot{"person_name": "abhibot"}
    - slot{"requested_slot": "company"}
* form: inform{"company": "freelance"}
    - slot{"company": "freelance"}
    - form: sales_form
    - slot{"company": "freelance"}
    - slot{"requested_slot": "business_email"}
* form: inform{"business_email": "abhibot@bot.com"}
    - slot{"business_email": "abhibot@bot.com"}
    - form: sales_form
    - slot{"business_email": "abhibot@bot.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thank OR goodbye
    - utter_noworries

## interactive_story_2
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* form: inform{"job_function": "engineer"}
    - slot{"job_function": "engineer"}
    - form: sales_form
    - slot{"job_function": "engineer"}
    - slot{"requested_slot": "use_case"}
* form: inform{"use_case": "support"}
    - slot{"use_case": "support"}
    - form: sales_form
    - slot{"use_case": "support"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "fifty thousand inr"}
    - slot{"budget": "fifty thousand inr"}
    - form: sales_form
    - slot{"budget": "fifty thousand inr"}
    - slot{"requested_slot": "person_name"}
* form: inform{"person_name": "abhishek"}
    - slot{"person_name": "abhishek"}
    - form: sales_form
    - slot{"person_name": "abhishek"}
    - slot{"requested_slot": "company"}
* form: inform{"company": "kompani"}
    - slot{"company": "kompani"}
    - form: sales_form
    - slot{"company": "kompani"}
    - slot{"requested_slot": "business_email"}
* form: inform{"business_email": "abc@bot.com"}
    - slot{"business_email": "abc@bot.com"}
    - form: sales_form
    - slot{"business_email": "abc@bot.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thank OR goodbye
    - utter_noworries

## interactive_story_3
* greet
    - utter_greet
* chitchat
    - utter_chitchat
* thank OR goodbye
    - utter_noworries

## interactive_story_4
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* form: inform{"job_function": "engineer"}
    - slot{"job_function": "engineer"}
    - form: sales_form
    - slot{"job_function": "engineer"}
    - slot{"requested_slot": "use_case"}
* form: inform{"use_case": "systems upgrade"}
    - slot{"use_case": "systems upgrade"}
    - form: sales_form
    - slot{"use_case": "systems upgrade"}
    - slot{"requested_slot": "budget"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - utter_noworries

## interactive_story_5
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* form: inform{"job_function": "manager"}
    - slot{"job_function": "manager"}
    - form: sales_form
    - slot{"job_function": "manager"}
    - slot{"requested_slot": "use_case"}
* form: inform{"use_case": "systems upgrade"}
    - slot{"use_case": "systems upgrade"}
    - form: sales_form
    - slot{"use_case": "systems upgrade"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "100K"}
    - slot{"budget": "100K"}
    - form: sales_form
    - slot{"budget": "100K"}
    - slot{"requested_slot": "person_name"}
* form: inform{"person_name": "vinay"}
    - slot{"person_name": "vinay"}
    - form: sales_form
    - slot{"person_name": "vinay"}
    - slot{"requested_slot": "company"}
* form: inform{"company": "botfarm"}
    - slot{"company": "botfarm"}
    - form: sales_form
    - slot{"company": "botfarm"}
    - slot{"requested_slot": "business_email"}
* form: inform{"business_email": "vinay@botfarm.com"}
    - slot{"business_email": "vinay@botfarm.com"}
    - form: sales_form
    - slot{"business_email": "vinay@botfarm.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* thank OR goodbye
    - utter_noworries

## interactive_story_6
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* stop
    - action_deactivate_form
    - form{"name": null}
    - utter_noworries

## interactive_story_7
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* form: inform{"job_function": "program manager"}
    - slot{"job_function": "program manager"}
    - form: sales_form
    - slot{"job_function": "program manager"}
    - slot{"requested_slot": "use_case"}
* form: inform{"use_case": "cloud migration"}
    - slot{"use_case": "cloud migration"}
    - form: sales_form
    - slot{"use_case": "cloud migration"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "250K USD"}
    - slot{"budget": "250K USD"}
    - form: sales_form
    - slot{"budget": "250K USD"}
    - slot{"requested_slot": "person_name"}
* form: inform{"person_name": "wilson h"}
    - slot{"person_name": "wilson h"}
    - form: sales_form
    - slot{"person_name": "wilson h"}
    - slot{"requested_slot": "company"}
* form: inform{"company": "ItBp Ltd."}
    - slot{"company": "ItBp Ltd."}
    - form: sales_form
    - slot{"company": "ItBp Ltd."}
    - slot{"requested_slot": "business_email"}
* form: inform{"business_email": "wilson@itbp.cln"}
    - slot{"business_email": "wilson@itbp.cln"}
    - form: sales_form
    - slot{"business_email": "wilson@itbp.cln"}
    - slot{"requested_slot": "additional_information"}
* form: inform
    - form: sales_form
    - slot{"additional_information": "additional support contract for 6 months"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - slot{"requested_slot": "rating"}
* ask_rating
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
* thank OR goodbye
    - utter_noworries
    
## interactive_story_8
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* form: inform{"job_function": "Engineer"}
    - slot{"job_function": "Engineer"}
    - form: sales_form
    - slot{"job_function": "Engineer"}
    - slot{"requested_slot": "use_case"}
* form: inform{"use_case": "L1/L2 Support"}
    - slot{"use_case": "L1/L2 Support"}
    - form: sales_form
    - slot{"use_case": "L1/L2 Support"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "120K"}
    - slot{"budget": "120K"}
    - form: sales_form
    - slot{"budget": "120K"}
    - slot{"requested_slot": "person_name"}
* form: inform{"person_name": "O. Heck"}
    - slot{"person_name": "O. Heck"}
    - form: sales_form
    - slot{"person_name": "O. Heck"}
    - slot{"requested_slot": "company"}
* form: inform{"company": "Sioux Falls"}
    - slot{"company": "Sioux Falls"}
    - form: sales_form
    - slot{"company": "Sioux Falls"}
    - slot{"requested_slot": "business_email"}
* form: inform{"business_email": "OHeck@SF.com"}
    - slot{"business_email": "OHeck@SF.com"}
    - form: sales_form
    - slot{"business_email": "OHeck@SF.com"}
    - slot{"requested_slot": "additional_information"}
* form: inform
    - form: sales_form
    - slot{"additional_information": "weekend support"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_noworries

## interactive_story_9
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* form: inform{"job_function": "engineer"}
    - slot{"job_function": "engineer"}
    - form: sales_form
    - slot{"job_function": "engineer"}
    - slot{"requested_slot": "use_case"}
* form: inform{"use_case": "L3 Support"}
    - slot{"use_case": "L3 Support"}
    - form: sales_form
    - slot{"use_case": "L3 Support"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "50K USD"}
    - slot{"budget": "50K USD"}
    - form: sales_form
    - slot{"budget": "50K USD"}
    - slot{"requested_slot": "person_name"}
* form: inform{"person_name": "Dodd"}
    - slot{"person_name": "Dodd"}
    - form: sales_form
    - slot{"person_name": "Dodd"}
    - slot{"requested_slot": "company"}
* form: inform{"company": "Butch"}
    - slot{"company": "Butch"}
    - form: sales_form
    - slot{"company": "Butch"}
    - slot{"requested_slot": "business_email"}
* form: inform{"business_email": "dodd@butch.com"}
    - slot{"business_email": "dodd@butch.com"}
    - form: sales_form
    - slot{"business_email": "dodd@butch.com"}
    - slot{"requested_slot": "additional_information"}
* form: inform
    - form: sales_form
    - slot{"additional_information": "NA"}
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_rating form1
* greet
    - utter_greet
* ask_rating
    - utter_ask_rating
* feedback{"rating": "Impressive"}
    - slot{"rating": "Impressive"}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - slot{"rating": "Impressive"}
    - slot{"rating": "Impressive"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_rating form2
* greet
    - utter_greet
* ask_rating
    - utter_ask_rating
* feedback{"rating": "Unstriking"}
    - slot{"rating": "Unstriking"}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - slot{"rating": "Unstriking"}
    - slot{"rating": "Unstriking"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_rating form3
* ask_rating
    - utter_ask_rating
* feedback{"rating": "Impressive"}
    - slot{"rating": "Impressive"}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - slot{"rating": "Impressive"}
    - slot{"rating": "Impressive"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_rating form4
* ask_rating
    - utter_ask_rating
* feedback{"rating": "Unstriking"}
    - slot{"rating": "Unstriking"}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - slot{"rating": "Unstriking"}
    - slot{"rating": "Unstriking"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* ask_rating
    - utter_ask_rating
* feedback{"rating": "Impressive"}
    - slot{"rating": "Impressive"}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - slot{"rating": "Impressive"}
    - slot{"rating": "Impressive"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_rating form5
* greet
    - utter_greet
* ask_rating
    - utter_ask_rating
* feedback{"rating": "Impressive"}
    - slot{"rating": "Impressive"}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - slot{"rating": "Impressive"}
    - slot{"rating": "Impressive"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_10
* greet
    - utter_greet
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}
* form: inform{"job_function": "Sales Director"}
    - slot{"job_function": "Sales Director"}
    - form: sales_form
    - slot{"job_function": "Sales Director"}
    - slot{"requested_slot": "use_case"}
* form: inform{"use_case": "chat bot"}
    - slot{"use_case": "chat bot"}
    - form: sales_form
    - slot{"use_case": "chat bot"}
    - slot{"requested_slot": "budget"}
* form: inform{"budget": "200K USD"}
    - slot{"budget": "200K USD"}
    - form: sales_form
    - slot{"budget": "200K USD"}
    - slot{"requested_slot": "person_name"}
* form: inform{"person_name": "Emmit Stussy"}
    - slot{"person_name": "Emmit Stussy"}
    - form: sales_form
    - slot{"person_name": "Emmit Stussy"}
    - slot{"requested_slot": "company"}
* form: inform{"company": "Stussy Lots Pvt Ltd"}
    - slot{"company": "Stussy Lots Pvt Ltd"}
    - form: sales_form
    - slot{"company": "Stussy Lots Pvt Ltd"}
    - slot{"requested_slot": "business_email"}
* form: inform{"business_email": "emmits@stussylots.com"}
    - slot{"business_email": "emmits@stussylots.com"}
    - form: sales_form
    - slot{"business_email": "emmits@stussylots.com"}
    - slot{"requested_slot": "additional_information"}
* form: inform
    - form: sales_form
    - slot{"additional_information": "NA"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_rating
* feedback{"rating": "Unstriking"}
    - slot{"rating": "Unstriking"}
    - get_rating_form
    - form{"name": "get_rating_form"}
    - slot{"rating": "Unstriking"}
    - slot{"rating": "Unstriking"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_noworries

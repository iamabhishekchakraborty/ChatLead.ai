# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
import logging
import pprint
import re
from datetime import datetime
from typing import Any, Dict, List, Text, Union, Optional
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, ActionExecutionRejection
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    ActionExecuted,
    UserUttered,
    AllSlotsReset
)

# import GDriveService

logger = logging.getLogger(__name__)


class GetRatingForm(FormAction):
    """Collects rating information and adds it to the spreadsheet"""

    def name(self):
        return "get_rating_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["rating"]

    def slot_mappings(self):  # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
                    - an extracted entity
                    - intent: value pairs
                    - a whole message
                    or a list of them, where a first match will be picked"""

        return {
            "rating": self.from_entity(entity="rating"),
        }

    def submit(self, dispatcher, tracker,
               domain):  # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
            after all required slots are filled"""

        # decide if the rating is low and ask for influence
        rating_post = tracker.get_slot("rating")
        # print(rating_post)
        match = re.search(r'impressive', rating_post, flags=re.IGNORECASE)
        if match:
            dispatcher.utter_message(template="utter_ask_good_rating")
        else:
            dispatcher.utter_message(template="utter_ask_bad_rating")

        return [AllSlotsReset()]


class SalesForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return [
            "job_function",
            "use_case",
            "budget",
            "person_name",
            "company",
            "business_email",
            "additional_information"
        ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter_slots_values template
        dispatcher.utter_message(template="utter_slots_values")
        #   dispatcher.utter_message("All done. Thanks for getting in touch, we’ll contact you soon")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "job_function": [
                self.from_entity(entity="job_function"),
                self.from_text(intent="inform"),
            ],
            "use_case": [
                self.from_text(intent="enter_data"),
                self.from_entity(entity="use_case"),
            ],
            "budget": [
                self.from_entity(entity="budget", not_intent="chitchat"),
                self.from_text(intent="enter_data"),
            ],
            "person_name": [
                self.from_entity(entity="person_name"),
                self.from_text(intent="inform"),
            ],
            "company": [
                self.from_entity(entity="company"),
                self.from_text(intent="inform"),
            ],
            "business_email": [
                self.from_entity(entity="business_email"),
                self.from_text(intent="inform"),
            ],
            "additional_information": [
                self.from_entity(entity="additional_information"),
                self.from_text(intent="inform"),
            ],
        }

    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    #     """A dictionary to map required slots to
    #         - an extracted entity
    #         - intent: value pairs
    #         - a whole message
    #         or a list of them, where a first match will be picked"""
    #
    #     return {
    #         "job_function": [
    #             self.from_entity(entity="job_function"),
    #             self.from_text(intent="enter_data"),
    #         ],
    #         "use_case": [
    #             self.from_text(intent="enter_data"),
    #             self.from_intent(intent="ask_faq_voice", value="voice"),
    #         ],
    #         "budget": [
    #             self.from_entity(entity="amount-of-money"),
    #             self.from_entity(entity="number"),
    #             self.from_text(intent="enter_data"),
    #         ],
    #         "person_name": [
    #             self.from_entity(entity="name"),
    #             self.from_text(intent="enter_data"),
    #         ],
    #         "company": [
    #             self.from_entity(entity="company"),
    #             self.from_text(intent="enter_data"),
    #         ],
    #         "business_email": [
    #             self.from_entity(entity="email"),
    #             self.from_text(intent="enter_data"),
    #         ],
    #     }

    # def validate_business_email(
    #         self, value, dispatcher, tracker, domain
    # ) -> Dict[Text, Any]:
    #     """Check to see if an email entity was actually picked up by duckling."""
    #
    #     if any(tracker.get_latest_entity_values("email")):
    #         # entity was picked up, validate slot
    #         return {"business_email": value}
    #     else:
    #         # no entity was picked up, we want to ask again
    #         dispatcher.utter_message(template="utter_no_email")
    #         return {"business_email": None}

    # def submit(
    #         self,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any],
    # ) -> List[EventType]:

    """Once we have all the information, attempt to add it to the
    Google Drive database"""

    # import datetime
    #
    # budget = tracker.get_slot("budget")
    # company = tracker.get_slot("company")
    # email = tracker.get_slot("business_email")
    # job_function = tracker.get_slot("job_function")
    # person_name = tracker.get_slot("person_name")
    # use_case = tracker.get_slot("use_case")
    # date = datetime.datetime.now().strftime("%d/%m/%Y")
    #
    # sales_info = [company, use_case, budget, date, person_name, job_function, email]
    #
    # try:
    #     gdrive = GDriveService()
    #     gdrive.store_data(sales_info)
    #     dispatcher.utter_message(template="utter_confirm_salesrequest")
    #     return []
    # except Exception as e:
    #     logger.error(
    #         "Failed to write data to gdocs. Error: {}" "".format(e.message),
    #         exc_info=True,
    #     )
    #     dispatcher.utter_message(template="utter_salesrequest_failed")
    #     return []

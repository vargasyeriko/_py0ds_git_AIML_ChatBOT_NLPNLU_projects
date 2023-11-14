# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, List, Text, Dict

class ActionGetBestOffers(Action):
    def name(self) -> Text:
        return "action_get_best_offers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Define a list of best flight offers (you can replace this with your data)
        best_offers = [
            {"destination": "New York", "price": "$300"},
            {"destination": "Paris", "price": "$400"},
            {"destination": "London", "price": "$350"},
            {"destination": "Tokyo", "price": "$500"},
        ]

        # Randomly select one of the best offers
        selected_offer = random.choice(best_offers)

        # Extract the offer details
        destination = selected_offer["destination"]
        price = selected_offer["price"]

        # Create a response message with the selected offer
        response = f"The best flight offer right now is to {destination} for {price}. Would you like to book this flight?"

        # Send the response to the user
        dispatcher.utter_message(response)

        return []

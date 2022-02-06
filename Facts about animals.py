import json
import requests
from enum import IntEnum

Menu_Facts = IntEnum("Menu_Facts", "cat dog")


def choose_animal_to_see_fact():
    print("Hi! Choose an animal, to see the fact about it: ")
    print("(1) Cat")
    print("(2) Dog ")
    chosenAnimal = int(input())
    return chosenAnimal


def choose_amount_of_facts_to_display():
    amountOFFactsToDisplay = int(input("How many facts, you want display?"))
    return amountOFFactsToDisplay


def show_facts_about_chosen_animal(chosenAnimal, amountOfFactsToDisplay):

    params = {
        "animal_type": chosenAnimal,
        "amount": amountOfFactsToDisplay
    }

    r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

    try:
        facts = r.json()
    except json.decoder.JSONDecodeError:
        print("Upsss...something went wrong")
    else:
        if params["amount"] < 2:
            print(facts["text"])
        else:
            for fact in facts:
                print(fact["text"])


def show_message_due_incorrect_choice():
    print("Choose between (1) or (2)")


while True:
    chosenAnimal = choose_animal_to_see_fact()
    amountOfFactsToDisplay = choose_amount_of_facts_to_display()

    if chosenAnimal == Menu_Facts.cat:
        show_facts_about_chosen_animal(
            Menu_Facts.cat.name, amountOfFactsToDisplay)

    elif chosenAnimal == Menu_Facts.dog:
        show_facts_about_chosen_animal(
            Menu_Facts.dog.name, amountOfFactsToDisplay)

    else:
        show_message_due_incorrect_choice()

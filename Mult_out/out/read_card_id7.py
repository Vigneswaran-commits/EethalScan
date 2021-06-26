#!/usr/bin/env python

# class for reading card with id=7
class card_id7:
    solnopt_related_cards = {}

    # initiliaze the member data during object creation
    def __init__(self):
        self.solnopt_related_cards = {}

    # read card
    def read_card(self, card_lines):
        card_lines = card_lines[2:len(card_lines)]

        for card_line in card_lines:
            solncard = card_line.split(':')[0]
            elements = card_line.split(':')[1]

            if (elements.startswith('[') and elements.endswith(']')): # write only comma sep. numbers
                elements = elements[1:-1]

            self.solnopt_related_cards[solncard] = elements

        #print("self.solnopt_related_cards :", self.solnopt_related_cards)

    def retrieve_data(self):
        pass
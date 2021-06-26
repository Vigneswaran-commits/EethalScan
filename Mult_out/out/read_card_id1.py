#!/usr/bin/env python

# class for reading card with id=1
class card_id1:
    solncard_elements = {}

    # initiliaze the member data during object creation
    def __init__(self):
        self.solncard_elements = {}

    # get element(s) suitable for this analysis type
    def read_card(self, card_lines):
        card_lines = card_lines[2:len(card_lines)]

        for card_line in card_lines:
            solncard = card_line.split(':')[0]
            elements = card_line.split(':')[1]
            
            if (elements.startswith('[') and elements.endswith(']')): # write only comma sep. numbers
                elements = elements[1:-1]

            self.solncard_elements[solncard] = elements

        #print("self.solncard_elements :", self.solncard_elements)

    def retrieve_data(self):
        pass
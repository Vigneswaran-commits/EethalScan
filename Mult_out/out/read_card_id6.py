#!/usr/bin/env python

# class for reading card with id=5
class card_id6:
    soltype_usedelems = {}

    # initiliaze the member data during object creation
    def __init__(self):
        self.soltype_usedelems = {}

    # get element(s) suitable for this analysis type
    def read_card(self, card_lines):
        card_lines = card_lines[2:len(card_lines)]

        if(len(card_lines) == 0):
            return
        
        card_line = card_lines[0]
        
        solntype = card_line.split(':')[0]
        elements = card_line.split(':')[1]

        if (elements.startswith('[') and elements.endswith(']')): # write only comma sep. numbers
            elements = elements[1:-1]

        self.soltype_usedelems[solntype] = elements # dict with one key, value pair

        #print("self.soltype_usedelems :", self.soltype_usedelems)

    def retrieve_data(self):
        pass
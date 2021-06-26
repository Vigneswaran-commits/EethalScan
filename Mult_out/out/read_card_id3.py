#!/usr/bin/env python

# class for reading card with id=3
class card_id3:
    card3_dict = {}

    # initiliaze the member data during object creation
    def __init__(self):
        self.card3_dict = {}

    # read card
    def read_card(self, card_lines):
        card_lines = card_lines[2:len(card_lines)]
        #print("card_lines: ", card_lines)
        for card_line in card_lines:
            key = card_line.split(':')[0]
            value = card_line.split(':')[1]

            if (value.startswith('[') and value.endswith(']')): # write only comma sep. numbers
                value = value[1:-1]

            self.card3_dict[key] = value

        #print("self.card3_dict :", self.card3_dict)

    def retrieve_data(self):
        pass
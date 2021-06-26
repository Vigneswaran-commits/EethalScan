#!/usr/bin/env python

# class for reading card with id=2
class card_id2:
    elem_desc = {}

    # initiliaze the member data during object creation
    def __init__(self):
        self.elem_desc = {}

    # get element(s) suitable for this analysis type
    def read_card(self, card_lines):
        card_lines = card_lines[2:len(card_lines)]
        
        for card_line in card_lines:
            elem_no = card_line.split(':')[0]
            elem_desc = card_line.split(':')[1]

            self.elem_desc[elem_no] = elem_desc

        #print("self.elem_desc :", self.elem_desc)

    def retrieve_data(self):
        pass
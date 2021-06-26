#!/usr/bin/env python

# class for reading card with id=5
class card_id5:
    eltype_solopts = {}

    # initiliaze the member data during object creation
    def __init__(self):
        self.eltype_solopts = {}

    # read card
    def read_card(self, card_lines):
        card_lines = card_lines[2:len(card_lines)]

        for card_line in card_lines:
            eltype = card_line.split(':')[0]
            solopts = card_line.split(':')[1]

            self.eltype_solopts[eltype] = solopts[:-1] # remove last comma is removed from output txt files

        #print("self.eltype_solopts :", self.eltype_solopts)

    def retrieve_data(self):
        pass
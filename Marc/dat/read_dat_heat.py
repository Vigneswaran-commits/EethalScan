#!/usr/bin/env python

# class for reading the HEAT card
class heat:
    linecount = 0,
    free_field = False

    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.free_field = False

    # get total number of lines in this card
    def get_linecount(self, dataline):
        if dataline.endswith(","):
            listdata = dataline.split(",")  # free field
            free_field = True
        else:
            listdata = dataline.split()    # fixed field
            free_field = False
        self.linecount = 1
        return self.linecount

    # get heat input
    def read_card(self, card_lines):
        pass

    def retrieve_data(self):
        pass
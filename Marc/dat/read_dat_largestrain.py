#!/usr/bin/env python

# class for reading the LARGE STRAIN card
class large_strain:
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
    
    # read large strain card
    def read_card(self, card_lines):
        pass
        #print("", )

    def retrieve_data(self):
        pass
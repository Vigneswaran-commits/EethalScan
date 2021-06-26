#!/usr/bin/env python

# class for reading the ELASTIC card
class elastic:
    linecount = 0,
    elem_storage_param = None, # element storage parameter, to reduce storage in elastic analysis.
    free_field = False

    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.elem_storage_param = None
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

    # get element id and nodes and store it as a dictionary
    def read_card(self, card_lines):
        card_line = card_lines[0]

        field = 20

        self.elem_storage_param = int(card_line[field:field+10])
        
        #print("elem_storage_param: ", self.elem_storage_param)

    def retrieve_data(self):
        pass
#!/usr/bin/env python
# class for reading the card TITLE in parameters sections
class title:
    linecount = 0,
    title = "",
    free_field = False

    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.title = ""
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
        field = 20
        card_line = card_lines[0]
        self.title = card_line[field:field+140]
        #print("title: ", len(self.title))

    def retrieve_data(self):
        pass

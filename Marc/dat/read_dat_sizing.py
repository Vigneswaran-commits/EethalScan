#!/usr/bin/env python

# class for reading the SIZING card
class sizing:
    linecount = 0,
    max_nof_elems = None,     # maximum number of elements
    max_nof_nodal_pts = None, # maximum number of nodal points
    dummy = None,
    free_field = False

    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.max_nof_elems = None
        self.max_nof_nodal_pts = None
        self.dummy = None
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

        self.dummy = int(card_line[field:field+20])
        field += 20

        self.max_nof_elems = int(card_line[field:field+10])
        field += 10

        self.max_nof_nodal_pts = int(card_line[field:field+10])
        field += 10
        
        #print("max nof elements: ", self.max_nof_elems)
        #print("max nof nodal pts: ", self.max_nof_nodal_pts)

    def retrieve_data(self):
        pass
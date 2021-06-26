#!/usr/bin/env python

# class for reading the VERSION card
class version:
    linecount = 0,
    analysis_version = None,        # input/analysis version to be used
    multiphysics_input_type = None, # 1 for Marc 2008 or earlier versions (default)
                                    # 2 for input based upon defining physics type on material & control options.
    free_field = False

    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.analysis_version = None
        self.multiphysics_input_type = None
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

    # get version input
    def read_card(self, card_lines):
        card_line = card_lines[0]

        field = 20

        self.analysis_version = int(card_line[field:field+10])
        field += 10

        if(self.analysis_version == 0):
            self.analysis_version = 9 # default input associated with MSC.Marc 2001

        self.multiphysics_input_type = int(card_line[field:field+10])
        
        #print("analysis_version: ", self.analysis_version)
        #print("multiphysics_input_type: ", self.multiphysics_input_type)

    def retrieve_data(self):
        pass
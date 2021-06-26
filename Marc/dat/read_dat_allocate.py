#!/usr/bin/env python

# class for reading the ALLOCATE card
class allocate:
    linecount = 0,
    size_workspace_general_memory = None, # Size of workspace in MByte for general memory
    size_workspace_solver_memory = None,  # Size of workspace in MByte for solver memory
    dummy = None,
    free_field = False

    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.size_workspace_general_memory = None
        self.size_workspace_solver_memory = None
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

        self.size_workspace_general_memory = int(card_line[field:field+10])
        field += 10

        #print("size_workspace_general_memory", self.size_workspace_general_memory)

        value = card_line[field:field+10]
        if(value == "" or value == "\n"): # only general memory size is available
            return

        self.size_workspace_solver_memory = int(card_line[field:field+10])
        field += 10

        #print("size_workspace_solver_memory", self.size_workspace_solver_memory)

    def retrieve_data(self):
        pass
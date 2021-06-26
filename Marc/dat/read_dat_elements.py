#!/usr/bin/env python
# class for reading the card ELEMENTS in parameters sections
class elements:
    linecount = 0,
    elem_codes = [],
    free_field = False

    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.elem_codes = []
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
        card_line.rstrip("\r\n")
        for x in range(0, 14):
            tmp_str = card_line[field:field+10]
            #print("length", len(tmp_str))
            #print("string: ", tmp_str)
            if(len(tmp_str) == 0):
                break
            self.elem_codes.append(int(tmp_str))
            field += 10

        #print(self.elem_codes)
        #for elem_code in self.elem_codes:
        #    print(elem_code)

    def retrieve_data(self):
        pass

#!/usr/bin/env python

# class for reading card with id=4
class card_id4:
    elem_props = []
    tmp_dict = {}

    # initiliaze the member data during object creation
    def __init__(self):
        self.elem_props = []
        self.tmp_dict = {}

    # read card
    def read_card(self, card_lines, input_file_name):
        card_lines = card_lines[2:len(card_lines)]

        iter = 0
        for card_line in card_lines:

            key = card_line.split(':')[0]
            value = card_line.split(':')[1]

            self.tmp_dict[key] = value

            if (iter == 7):
                self.tmp_dict['Filename'] = input_file_name
                self.elem_props.append(self.tmp_dict)
                self.tmp_dict = {}
                iter = 0
            else:
                iter += 1

        #print("self.elem_props :", self.elem_props)

    def retrieve_data(self):
        pass
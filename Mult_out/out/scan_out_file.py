
#!/usr/bin/env python

import io, sys, os, platform
import getopt

from dataclasses import dataclass
import numpy as np

from read_card_id1 import card_id1
from read_card_id2 import card_id2
from read_card_id3 import card_id3
from read_card_id4 import card_id4
from read_card_id5 import card_id5
from read_card_id6 import card_id6
from read_card_id7 import card_id7

# dataclass containing
@dataclass
class out_objects:
    card_id1 = None
    card_id2 = None
    card_id3 = None
    card_id4 = None
    card_id5 = None
    card_id6 = None
    card_id7 = None

# class for scanning all the cards in output file
class out_reader:
    linelist = []
    linepos = 0
    input_file_name = None
    objects = out_objects()

    def __init__(self):
        self.linelist = []
        self.linepos = 0
        self.input_file_name = None
        self.objects = out_objects()

    # scans all the cards in the file
    def scan_file(self):
        
        listlength = len(self.linelist)
        for line in range(listlength):       # loop from line=0 to line=listlength-1
            if(self.linepos <= line):        # enter, if current line <= to for loop line
                # print("line scanned", line)
        
                # get the card id using its name
                card_id = self.get_line(self.linepos).split()[1]
                card_id = int(card_id)
                # print("card_id", card_id)
                # scan each card
                if(card_id == 1):      # Element(s) suitable for this analysis option:
                    self.objects.card_id1 = card_id1()
                    linecount = self.get_linecount(self.linepos+1) # +1 for card's next line
                    # print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.card_id1.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(card_id == 2):      # Element description:
                    self.objects.card_id2 = card_id2()
                    linecount = self.get_linecount(self.linepos+1) # +1 for card's next line
                    # print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.card_id2.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(card_id == 3):      # Element class and other elements in the class:
                    self.objects.card_id3 = card_id3()
                    linecount = self.get_linecount(self.linepos+1) # +1 for card's next line
                    # print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.card_id3.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(card_id == 4):      # Element(s) Properties:
                    self.objects.card_id4 = card_id4()
                    linecount = self.get_linecount(self.linepos+1) # +1 for card's next line
                    # print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.card_id4.read_card(self.linelist[slice_from:slice_till], self.input_file_name)
                    self.linepos += linecount
                elif(card_id == 5):      # Analysis options to use:
                    self.objects.card_id5 = card_id5()
                    linecount = self.get_linecount(self.linepos+1) # +1 for card's next line
                    # print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.card_id5.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(card_id == 6):      # Analysis type:
                    self.objects.card_id6 = card_id6()
                    linecount = self.get_linecount(self.linepos+1) # +1 for card's next line
                    # print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.card_id6.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(card_id == 7):      # Card related to analysis options used:
                    self.objects.card_id7 = card_id7()
                    linecount = self.get_linecount(self.linepos+1) # +1 for card's next line
                    # print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.card_id7.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(card_id == 0):      # End card:
                    linecount = 0
                    # print("linecount: ", linecount)
                    self.linepos += linecount
                    continue
                else:                       # UNSUPPORTED
                    linecount = self.get_linecount(self.linepos+1) # +1 for card's next line
                    # print("linecount: ", linecount)
                    self.linepos += linecount
                    continue
            else:
                continue
                #print("line skipped", line)
    
    # stores all the lines as a list from the dat file
    def store_file_as_linelist(self, input_file_path):
        # store dat name, to write in csv
        head, tail = os.path.split(input_file_path)
        self.input_file_name = tail.split('.')[0]
        self.input_file_name = self.input_file_name + ".dat"

        if(platform.system() == "Windows"):
            with open(input_file_path, 'r', encoding='cp1252') as file:  # windows
                self.linelist = file.readlines()
        else:
            with open(input_file_path, 'r', encoding='utf-8') as file:   # linux/macos
                self.linelist = file.readlines()
           
        # remove line endings in all the lines
        nof_lines = len(self.linelist)
        for i in range(0, nof_lines):
            line = self.linelist[i]
            line = line.replace("\n", "")
            self.linelist[i] = line
            #print(self.linelist[i])

    # returns each line as a string
    # convert fixed and free field into a single format
    def get_line(self, linepos):
        line = self.linelist[linepos]
        return line

    # linecount is card's next line to next card line 
    def get_linecount(self, linepos):
        line_count = 0
        nof_lines = len(self.linelist)
        for i in range(linepos, nof_lines):
            line_count += 1
            line = self.get_line(i)
            if(len(line) > 0 and line.split()[0] == "Card"):
                break
        return line_count
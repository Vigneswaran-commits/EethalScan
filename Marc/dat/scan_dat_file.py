#!/usr/bin/env python
import io, sys, platform
import getopt

from dataclasses import dataclass

# specific to dat reader
from dat_supported_cards import dat_cards
from read_dat_title import title
from read_dat_sizing import sizing
from read_dat_allocate import allocate
from read_dat_elements import elements
from read_dat_version import version
from read_dat_elastic import elastic
from read_dat_largestrain import large_strain
from read_dat_structural import structural
from read_dat_heat import heat
from read_dat_solver import solver
from read_dat_coordinates import coordinates
from read_dat_connectivity import connectivity

# dataclass containing all the objects read from the dat file
@dataclass
class dat_objects:
    sizing     = None
    allocate   = None
    elements   = []
    version    = None
    elastic    = None
    large_strain = None
    structural = None
    heat       = None
    solver     = None
    connectivity = []

    analysis_type = None
    analysis_opts = []
    elemid_type_nodes = {}

# class for scanning all the cards in dat file and read the supported cards
class dat_reader:
    linelist = []
    linepos = 0
    objects = dat_objects()

    def __init__(self):
        self.linelist = []
        self.linepos = 0
        self.objects = dat_objects()

    # scans all the cards in the file
    def scan_file(self):
        
        listlength = len(self.linelist)
        for line in range(listlength):       # loop from line=0 to line=listlength-1
            if(self.linepos <= line):        # current line less or equal to max line count
                #print("line scanned", line)

                # skip empty lines
                empty_line_check = self.get_line(self.linepos)
                if(len(empty_line_check) == 0):
                    linecount = 1
                    self.linepos += linecount
                    continue
                
                # skip comment lines
                first_char = (self.get_line(self.linepos))[0]
                if(first_char == '$'):
                    linecount = 1
                    self.linepos += linecount
                    continue
        
                # get the card id using its name, and skip unsupported cards
                card_name = self.get_line(self.linepos).split()[0] # may fail for cards with two keywords, eg. shell sect
                if(card_name.islower()):
                    card_name = card_name.upper()
                cards = dat_cards()
                name_list = list(cards.names_ids.keys())
                id_list = list(cards.names_ids.values())
                try:
                    name_pos = name_list.index(card_name)
                except ValueError:
                    name_pos = name_list.index("UNSUPPORTED")
                    #print("Unsupported Card: ", card_name)
                
                # scan each card
                if(id_list[name_pos] == 1):      # TITLE
                    obj = title()
                    linecount = obj.get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    obj.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(id_list[name_pos] == 2):    # SIZING
                    self.objects.sizing = sizing()
                    linecount = self.objects.sizing.get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.sizing.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(id_list[name_pos] == 3):    # ALLOCATE
                    self.objects.allocate = allocate()
                    linecount = self.objects.allocate.get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.allocate.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(id_list[name_pos] == 4):    # ELEMENTS
                    # add a element obj at end of list
                    self.objects.elements.append(elements())
                    index = len(self.objects.elements) - 1

                    # read data
                    linecount = self.objects.elements[index].get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.elements[index].read_card(self.linelist[slice_from:slice_till])

                    self.linepos += linecount
                elif(id_list[name_pos] == 5):    # VERSION
                    self.objects.version = version()
                    linecount = self.objects.version.get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.version.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                if(id_list[name_pos] == 6):      # COORDINATES
                    obj = coordinates()
                    linecount = obj.get_linecount(self.get_line(self.linepos+1))                             # +1 to read 2nd line (coords count)
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    obj.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(id_list[name_pos] == 7):    # CONNECTIVITY
                    # add a connectivity obj at end of list
                    self.objects.connectivity.append(connectivity())
                    index = len(self.objects.connectivity) - 1

                    # read data
                    linecount = self.objects.connectivity[index].get_linecount(self.get_line(self.linepos+1))# +1 to read 2nd line (elems count)
                    if(linecount == 2):
                        linecount = self.objects.sizing.max_nof_elems + 2 # one connectivity card in file, elemcount from sizing is used
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.connectivity[index].read_card(self.linelist[slice_from:slice_till])

                    # set elem id to type and connectivity nodes (update LHS dict for each connectivity card)
                    self.objects.elemid_type_nodes.update(self.objects.connectivity[index].elemid_type_nodes)

                    self.linepos += linecount
                elif(id_list[name_pos] == 8):    # END
                    linecount = 1
                    self.linepos += linecount
                    continue
                elif(id_list[name_pos] == 9):    # ELASTIC
                    self.objects.elastic = elastic()

                    # read data
                    linecount = self.objects.elastic.get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.elastic.read_card(self.linelist[slice_from:slice_till])

                    # set analysis type
                    self.objects.analysis_type = "ELASTIC"
                    self.objects.analysis_opts.append("ELASTIC")
            
                    self.linepos += linecount
                elif(id_list[name_pos] == 10 or id_list[name_pos] == 11):    # LARGE STRAIN or LARGE STRA
                    self.objects.large_strain = large_strain()

                    # read data
                    linecount = self.objects.large_strain.get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.large_strain.read_card(self.linelist[slice_from:slice_till])

                    # set analysis type
                    self.objects.analysis_type = "LARGE STRAIN"
                    self.objects.analysis_opts.append("LARGE STRAIN")
            
                    self.linepos += linecount
                elif(id_list[name_pos] == 12):    # STRUCTURAL
                    self.objects.structural = structural()

                    # read data
                    linecount = self.objects.structural.get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.structural.read_card(self.linelist[slice_from:slice_till])

                    # set analysis type
                    self.objects.analysis_type = "STRUCTURAL"
                    self.objects.analysis_opts.append("STRUCTURAL")
            
                    self.linepos += linecount
                elif(id_list[name_pos] == 13):    # HEAT
                    self.objects.heat = heat()

                    # read data
                    linecount = self.objects.heat.get_linecount(self.get_line(self.linepos))
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.heat.read_card(self.linelist[slice_from:slice_till])

                    # set analysis type
                    self.objects.analysis_type = "HEAT"
                    self.objects.analysis_opts.append("HEAT")
            
                    self.linepos += linecount
                elif(id_list[name_pos] == 14):    # SOLVER
                    self.objects.solver = solver()
                    linecount = self.objects.solver.get_linecount(self.get_line(self.linepos))
                    #print("linepos: ", slice_from)
                    #print("linecount: ", linecount)
                    slice_from = self.linepos
                    slice_till = self.linepos+linecount
                    self.objects.solver.read_card(self.linelist[slice_from:slice_till])
                    self.linepos += linecount
                elif(id_list[name_pos] == 15):    # END OPTION
                    linecount = 1
                    self.linepos += linecount
                    continue
                elif(id_list[name_pos] == 16):    # CONTINUE
                    linecount = 1
                    self.linepos += linecount
                    continue
                elif(id_list[name_pos] == 0):    # UNSUPPORTED
                    linecount = 1
                    self.linepos += linecount
                    continue
                else:
                    continue
            else:
                continue
                #print("line skipped", line)
    
    # stores all the lines as a list from the dat file
    def store_file_as_linelist(self, input_file_path):
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

# def main():
#     obj = dat_reader()
#     obj.store_file_as_linelist()
#     obj.scan_file()
#     print("test")

# if(__name__ == "__main__"):
#     main()
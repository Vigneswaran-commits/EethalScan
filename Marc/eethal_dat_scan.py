
#!/usr/bin/env python

# 1.get list of suitable elements for solution type
# 2.get description of used elements
# 3.get the class of used elements
# 4.get element properties-nof nodes, nof direct stress, nof shear stress, nof integ. pts, nof coords, updated lagrange availability
# 5.get solution options available for the used elements
# 6.get analysis type
# 7.get card relevant to solution options

import io, sys, platform
import getopt

from dataclasses import dataclass

import numpy as np

sys.path.append('C:/Users/vajravel/Desktop/Eethalview/Marc/dat')
from scan_dat_file import dat_reader

from dictionaries import class_elems
from dictionaries import element_desc
from dictionaries import solntype_suitable_elems
from dictionaries import solntype_unsuitable_elems
from dictionaries import elem_property
from dictionaries import sol_name_cards
from dictionaries import multiphysics_name_cards
from dictionaries import solopts_related_cards

# dataclass containing common data for input files
@dataclass
class common_data:
    analysis_type   = None
    analysis_opts   = []
    elem_types_used = []

class datinfo_scan:

    # data below forms file specific data,
    # and common data combination

    # input file objects
    dat_objects = None

    # output file handler
    txtfile = None
    writestr = None

    # data common to input files
    common_data = common_data()

    def __init__(self):
        self.dat_objects = None
        self.common_data = common_data()
        self.txtfile     = None

    # first group of methods(A): get common data from input file objects, and store it in common dataclass.
    # -----------------------------------------------------------------------------------------------------

    # A: store bdf data
    def store_bdf_data(self):
        self.store_analysis_type()
        self.store_analysis_options()
        self.store_element_types()
    
    # A: store analysis type of this problem
    def store_analysis_type(self):

        if(self.dat_objects):
            print("dat analysis type")
            self.common_data.analysis_type = self.dat_objects.objects.analysis_type

            print(self.common_data.analysis_type)

    # A. store analysis options
    def store_analysis_options(self):

        if(self.dat_objects):
            print("dat analysis options")
            self.common_data.analysis_opts = self.dat_objects.objects.analysis_opts

            print(self.common_data.analysis_opts)


    # A: store elem types used in this problem
    def store_element_types(self):

        if(self.dat_objects.objects.elements):
            print("dat element codes")
            for elements in self.dat_objects.objects.elements:
                for elemtype in elements.elem_codes:
                    self.common_data.elem_types_used.append(elemtype)

            print(self.common_data.elem_types_used)

    # secondly group of methods(B): use the data stored in common data, for further analysis
    # -----------------------------------------------------------------------------------------------------

    # B: analyse Marc dat data
    def analyse_dat_data(self):

        if self.dat_objects:
            print("analyse dat data")
            self.suitable_elems_for_solntype()
            self.elem_description()
            self.elem_class()
            self.elem_properties()
            self.soln_options_for_elems()
            self.analysis_type()
            self.card_relevant_to_solnopts()

    # B: 1.suitable elements
    def suitable_elems_for_solntype(self):
        self.txtfile.write("Card 1 Element(s) suitable for this analysis option:" + "\n")
        self.txtfile.write("----------------------------------------------------" + "\n")
        for soln_opt in self.common_data.analysis_opts:
            self.txtfile.write(soln_opt + ":" + str(solntype_suitable_elems[soln_opt]) + "\n")

    # B: 2.element names
    def elem_description(self):
        self.txtfile.write("Card 2 Element description:" + "\n")
        self.txtfile.write("---------------------------" + "\n")
        for elem in self.common_data.elem_types_used:
            self.txtfile.write("Element " + str(elem) + ":" + element_desc[elem] +"\n")

    # B: 3.element class, and other elements in the class
    def elem_class(self):
        self.txtfile.write("Card 3 Element class and other elements in the class:" + "\n")
        self.txtfile.write("-----------------------------------------------------" + "\n")
        key_list = list(class_elems.keys())
        value_list = list(class_elems.values())
        for elem in self.common_data.elem_types_used:
            try:
                for elemlist in value_list:
                    if elem in elemlist:
                        value_pos = value_list.index(elemlist)
                        self.txtfile.write("Element " + str(elem) + ":" + str(key_list[value_pos]) + "\n")
                        self.txtfile.write("Other elements in " + "Element " + str(elem) + " class:" + str([item for item in elemlist if item not in [elem]]) + "\n")
            except ValueError:
                print("Error in writing element class to output file")

    # B: 4.element properties
    def elem_properties(self):
        self.txtfile.write("Card 4 Element(s) Properties:" + "\n")
        self.txtfile.write("-----------------------------" + "\n")
        for elemtype in self.common_data.elem_types_used:
            props_list = elem_property[elemtype]
            self.txtfile.write( "Element_Type:"                 + str(elemtype) + "\n")
            self.txtfile.write( "Number_of_Nodes:"              + str(props_list[0]) + "\n")
            self.txtfile.write( "Number_of_DirectStress:"      + str(props_list[1]) + "\n")
            self.txtfile.write( "Number_of_ShearStress:"       + str(props_list[2]) + "\n")
            self.txtfile.write( "Number_of_IntegrationPoints:" + str(props_list[3]) + "\n")
            self.txtfile.write( "Number_of_DegreesofFreedom:"  + str(props_list[4]) + "\n")
            self.txtfile.write( "Number_of_Coordinates:"        + str(props_list[5]) + "\n")
            self.txtfile.write( "Updated_Lagrange_Available:"   + str(props_list[6]) + "\n")

    # B: 5.analysis options can be used for this element
    def soln_options_for_elems(self):
        self.txtfile.write("Card 5 Analysis options to use:" + "\n")
        self.txtfile.write("-------------------------------" + "\n")
        key_list = list(solntype_suitable_elems.keys())
        value_list = list(solntype_suitable_elems.values())
        for elem in self.common_data.elem_types_used:
            try:
                self.txtfile.write("Element " + str(elem) + ":")
                for elemlist in value_list:
                    if elem in elemlist:
                        value_pos = value_list.index(elemlist)
                        self.txtfile.write(str(key_list[value_pos]) + ",")
                self.txtfile.write("\n")
            except ValueError:
                print("Error in writing element type related analysis options to output file")

    # B: 6.find analysis type
    def analysis_type(self):
        if(len(self.dat_objects.objects.analysis_opts) == 1):
            self.txtfile.write("Card 6 Analysis: \n")
            self.txtfile.write("----------------" + "\n")
            key_list = list(sol_name_cards.keys())
            value_list = list(sol_name_cards.values())
            try:
                for soln_card in value_list:
                    if (self.dat_objects.objects.analysis_opts[0] == soln_card):
                        value_pos = value_list.index(soln_card)
                        self.txtfile.write(key_list[value_pos] + ':' + str(self.common_data.elem_types_used) + "\n")
            except ValueError:
                print("Error in finding analysis name, for output file")
        else:
            self.txtfile.write("Card 6 Multiphysics: \n")
            self.txtfile.write("--------------------" + "\n")
            key_list = list(multiphysics_name_cards.keys())
            value_list = list(multiphysics_name_cards.values())
            try:
                for soln_combo in value_list:
                    check =  all(item in self.dat_objects.objects.analysis_opts for item in soln_combo)
                    if check:
                        value_pos = value_list.index(soln_combo)
                        self.txtfile.write(key_list[value_pos] + ':' + str(self.common_data.elem_types_used) + "\n")
            except ValueError:
                print("Error in finding multiphysics name, for output file")

    # B: 7.card related to analysis options used
    def card_relevant_to_solnopts(self):
        self.txtfile.write("Card 7 Card related to analysis options used: \n")
        self.txtfile.write("---------------------------------------------" + "\n")
        key_list = list(solopts_related_cards.keys())
        value_list = list(solopts_related_cards.values())
        try:
            for soln_opt in self.dat_objects.objects.analysis_opts:
                if (soln_opt in key_list):
                    key_pos = key_list.index(soln_opt)
                    self.txtfile.write(soln_opt + ":" + str(value_list[key_pos]) + "\n")
        except ValueError:
            print("Error in finding cards related to analysis options, for output file")


    # third group of methods(C): utility methods and file operations
    # -----------------------------------------------------------------------------------------------------

    # C: output file open method
    def open_output_file(self, output_file_path):
        self.txtfile = open(output_file_path, 'w')

    # C: output file close method
    def close_output_file(self):
        self.txtfile.write("Card 0")
        self.txtfile.close()
    
    # C: function to get unique values
    def unique_items_inlist(self, input_list):
        input_ndarray = np.array(input_list)
        unique_items_ndarray = np.unique(input_ndarray)
        return list(unique_items_ndarray)

    #-----------------------------------------------------------------------------------------------------

def main():
    obj = datinfo_scan()

    # get command line arguments and set the bdf, and output file paths
    argv = sys.argv[1:]
    try:
        opts, extra = getopt.getopt(argv, "i:o:")
    except:
        print("scan.py -i input_file -o output.txt")
    
    input_file_path = ""
    output_file_path = ""
    for opt, arg in opts:
        # input bdf file path
        if opt in ('-i'):
            input_file_path = arg
        # output file path
        elif opt in ('-o'):
            output_file_path = arg

    print(input_file_path)
    print(output_file_path)
    
    if(len(input_file_path) == 0):
        print("Please check this Input file path")

    if(len(output_file_path) == 0):
        print("Please check the Output file path")
    
    # create dat reader object, store the cards,
    if(input_file_path[-4:] == ".dat"):
        print("Scanning Marc dat file")
        obj.dat_objects = dat_reader()
        obj.dat_objects.store_file_as_linelist(input_file_path)
        obj.dat_objects.scan_file()
        #print(input_file_path[-4:])

    # and write output file
    obj.open_output_file(output_file_path) # open output file
    obj.store_bdf_data()                   # store necessary data
    obj.analyse_dat_data()                 # analyse the stored data
    obj.close_output_file()                # close output file

if(__name__ == "__main__"):
    main()
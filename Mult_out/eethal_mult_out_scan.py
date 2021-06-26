#!/usr/bin/env python

import io, sys, platform
import getopt

from dataclasses import dataclass
import numpy as np
import csv
import pandas as pd

sys.path.append('C:/Users/vajravel/Desktop/Eethalview/Mult_out/out')
from scan_out_file import out_reader

class multout_info_scan:

    # list of out reader objects
    outread_list = []

    # multout_solopts_elems = []

    # output file handler
    txtfile = None

    def __init__(self):
        self.txtfile = None

    # def store_dict(self):
    #     for out in self.outread_list:
    #         self.multout_solopts_elems.append(out.objects.card_id1.solncard_elements)
    #     #print(self.multout_solopts_elems)

    def write_card1_to_csv(self, output_file_path):
        filepath = output_file_path + "card1.csv"
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csv_file:  
                writer = csv.writer(csv_file)
                writer.writerow(['Filename', 'Analysis_Option', 'Suitable_Elements'])
                for out in self.outread_list:
                    for key, value in out.objects.card_id1.solncard_elements.items():
                        writer.writerow([out.input_file_name, key, value])
        except IOError:
            print("Error in writing card1 to csv file")

    def write_card2_to_csv(self, output_file_path):
        filepath = output_file_path + "card2.csv"
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csv_file:  
                writer = csv.writer(csv_file)
                writer.writerow(['Filename', 'Element_Type', 'Element_Description'])
                for out in self.outread_list: 
                    for key, value in out.objects.card_id2.elem_desc.items():
                        writer.writerow([out.input_file_name, key, value])
        except IOError:
            print("Error in writing card2 to csv file")

    def write_card3_to_csv(self, output_file_path):
        filepath = output_file_path + "card3.csv"
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csv_file:  
                writer = csv.writer(csv_file)
                writer.writerow(['Filename', 'Element_Type/Other_Elements_in_Class', 'Element_Class/Element_Types'])
                for out in self.outread_list: 
                    for key, value in out.objects.card_id3.card3_dict.items():
                        writer.writerow([out.input_file_name, key, value])
        except IOError:
            print("Error in writing card3 to csv file")

    def write_card4_to_csv(self, output_file_path):
        filepath = output_file_path + "card4.csv"
        csv_columns = ['Filename', 'Element_Type','Number_of_Nodes','Number_of_DirectStress', 'Number_of_ShearStress', 'Number_of_IntegrationPoints', 'Number_of_DegreesofFreedom', 'Number_of_Coordinates', 'Updated_Lagrange_Available']
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
                writer.writeheader()
                for out in self.outread_list:
                    for data in out.objects.card_id4.elem_props:
                        writer.writerow(data)
        except IOError:
            print("Error in writing card4 to csv file")

    def write_card5_to_csv(self, output_file_path):
        filepath = output_file_path + "card5.csv"
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csv_file:  
                writer = csv.writer(csv_file)
                writer.writerow(['Filename', 'Element_Type', 'Available_Analysis_Options_To_Use'])
                for out in self.outread_list: 
                    for key, value in out.objects.card_id5.eltype_solopts.items():

                        writer.writerow([out.input_file_name, key, value])
        except IOError:
            print("Error in writing card5 to csv file")

    def write_card6_to_csv(self, output_file_path):
        filepath = output_file_path + "card6.csv"
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csv_file:  
                writer = csv.writer(csv_file)
                writer.writerow(['Filename', 'Solution_Name', 'Elements_Used'])
                for out in self.outread_list:
                    for key, value in out.objects.card_id6.soltype_usedelems.items():
                        writer.writerow([out.input_file_name, key, value])
        except IOError:
            print("Error in writing card6 to csv file")

    def write_card7_to_csv(self, output_file_path):
        filepath = output_file_path + "card7.csv"
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Filename', 'Analysis_Option', 'Related_Cards'])
                for out in self.outread_list: 
                    for key, value in out.objects.card_id7.solnopt_related_cards.items():
                        writer.writerow([out.input_file_name, key, value])
        except IOError:
            print("Error in writing card7 to csv file")

def main():

    obj = multout_info_scan()

    # argv = sys.argv[1:]
    params = [param for param in sys.argv[1:]]
    print("params: ", params)
    input_file_path = []
    for i in range(1, len(params)-2): # after '-i', but before '-o'
        input_file_path.append(params[i])
    output_file_path = params[len(params)-1]

    for i in range(0, len(input_file_path)):
        print("input_file_path", input_file_path[i])
    # print("output_file_path", output_file_path)
    
    if(len(input_file_path) == 0):
        print("Please check this Input file path")

    if(len(output_file_path) == 0):
        print("Please check the Output file path")

    # appending objects to list, for number of output files
    for i in range(0, len(input_file_path)):
        obj.outread_list.append(out_reader())

    # scan output files, created from multiple dat files
    # create out reader object, store the out cards,
    print("Scanning output txt file(s)")
    for i in range(0, len(input_file_path)):
        obj.outread_list[i].store_file_as_linelist(input_file_path[i])
        obj.outread_list[i].scan_file()

    # and write excel file
    # obj.store_dict()
    obj.write_card1_to_csv(output_file_path)
    obj.write_card2_to_csv(output_file_path)
    obj.write_card3_to_csv(output_file_path)
    obj.write_card4_to_csv(output_file_path)
    obj.write_card5_to_csv(output_file_path)
    obj.write_card6_to_csv(output_file_path)
    obj.write_card7_to_csv(output_file_path)

if(__name__ == "__main__"):
    main()
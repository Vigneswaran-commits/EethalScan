#!/usr/bin/env python
# class for reading the connectivity card
class connectivity:
    linecount = 0,
    no_of_elems = 0, 
    unit_number = 0,
    print_option = 0,
    elem_id = 0,
    elem_type = 0,
    elemid_type_nodes = {},       # specific to this cconnectivity card. for all the elems, see dat_objects (scan_dat_file.py)
    free_field = False
    
    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.no_of_elems = 0
        self.unit_number = 0
        self.print_option = 0
        self.elemid_type_nodes = {}
        self.free_field = False
    
    # get total number of lines in this card
    # linecount includes 1st, 2nd, and element lines for connectivity card
    def get_linecount(self, dataline):
        if dataline.endswith(","):
            listdata = dataline.split(",") # free field
            free_field = True
        else:
            listdata = dataline.split()    # fixed field
            free_field = False

        self.linecount = int(listdata[2]) + 2  # number of elems in card + 2 (1st, 2nd datablock)

        return self.linecount
        
    # get element id and nodes and store it as a dictionary
    def read_card(self, card_lines):
        card_lines = card_lines[2:self.linecount]
        elem_id = 0
        elem_type = 0
        strlist = []
        intlist = []
        for card_line in card_lines:
            if(self.free_field == True):
                strlist = card_line.split(",")
            elif(self.free_field == False):
                field = 0
                elem_id = int(card_line[field:field+10])            # elem id
                field += 10
                elem_type = int(card_line[field:field+10])          # elem type
                field += 10
        
                # class 1 elements
                if elem_type in (1, 5):
                    nnodes = 2
                # class 2 elements
                elif elem_type in (9, 36):
                    nnodes = 2
                # class 3 elements
                elif elem_type in (2, 6, 37, 38, 50):
                    nnodes = 3
                # class 4 elements
                elif elem_type in (3, 10, 11, 18, 19, 20, 39, 40, 80, 81, 82, 83, 111, 112):
                    nnodes = 4
                # class 5 elements
                elif elem_type in (7, 43, 84, 113):
                    nnodes = 8
                # class 6 elements
                elif elem_type in (64, 65):
                    nnodes = 3
                # class 7 elements
                elif elem_type in (26, 27, 28, 29, 30, 32, 33, 34, 41, 42, 62, 63, 66, 67):
                    nnodes = 8       
                # class 8 elements
                elif elem_type in (53, 54, 55, 56, 58, 59, 60, 69, 70, 73, 74):
                    nnodes = 8              
                # class 9 elements
                elif elem_type in (21, 35, 44):
                    nnodes = 20 
                # class 10 elements
                elif elem_type in (57, 61, 71):
                    nnodes = 20    
                # class 11 elements
                elif elem_type in (15, 16, 17):
                    nnodes = 2
                # class 12 elements
                elif elem_type == 45:
                    nnodes = 3
                # class 13 elements
                elif elem_type in (13, 14, 25, 52):
                    nnodes = 2              
                # class 14 elements
                elif elem_type in (124, 125, 126, 128, 129, 131, 132):
                    nnodes = 6
                # class 15 elements
                elif elem_type in (127, 130, 133):
                    nnodes = 10
                # class 16 elements
                elif elem_type in (114, 115, 116, 118, 119, 121, 122):
                    nnodes = 4    
                # class 17 elements
                elif elem_type in (117, 120, 123):
                    nnodes = 8
                # class 18 elements
                elif elem_type in (134, 135):
                    nnodes = 4

                # special elements: These elements include Beam and Shell Elements (4, 8, 22, 24, 
                # 31, 49, 72, 75-79, 85-90, 98, and 138-140), Friction and Gap Elements(12 and 97), 
                # Rebar Elements(23, 46-48, and 142-148), Elastic Shear Panel(68), Semi-infinite 
                # Elements(91-94 and 101-108), Axisymmetric Elements with Bending(95 and 96), Composite
                # Elements(149-154), Lower Triangular and Tetrahedral Elements with a cubic bubble
                # function(155-157), and Magnetostatic Elements(109 and 110).
                
                elif elem_type in (31, 78, 79, 88, 98):
                    nnodes = 2
                elif elem_type in (8, 76, 77, 87, 89, 90, 138):
                    nnodes = 3
                elif elem_type in (4, 12, 68, 75, 85, 95, 97, 139, 140, 143, 144, 145, 147, 151, 152, 155, 156):
                    nnodes = 4
                elif elem_type == 157:
                    nnodes = 5
                elif elem_type in (49, 91, 92, 101, 102):
                    nnodes = 6
                elif elem_type in (22, 24, 72, 86, 96, 46, 48, 109, 142, 146, 148, 149, 153, 154):
                    nnodes = 8
                elif elem_type in (93, 94, 103, 104):
                    nnodes = 9
                elif elem_type == 47:
                    nnodes = 10
                elif elem_type in (105, 107, 110):
                    nnodes = 12
                elif elem_type in (23, 150):
                    nnodes = 20
                elif elem_type in (106, 108):
                    nnodes = 27
                # default value
                else:
                    nnodes = 0
                   
                for x in range(0,nnodes):
                    intlist.append(int(card_line[field:field+10]))   # connectivity nodes
                    field += 10

            # loop to append connectivity nodes to elem id
            if(len(intlist) > 0):
                self.elemid_type_nodes.setdefault(elem_id, []).append(elem_type)     # id to type
                for nodeid in intlist:
                    self.elemid_type_nodes.setdefault(elem_id, []).append(nodeid) # id to nodeids
            strlist.clear()
            intlist.clear()

        # print to check
        # keylist = self.elemid_type_nodes.keys()
        # for x in keylist:
        #     print(self.elemid_type_nodes[x])
        
    def retrieve_data(self):
        pass

#!/usr/bin/env python
# class for reading the coordinates card
class coordinates:
    linecount = 0,
    coord_dir = 0,
    no_of_nodes = 0, 
    unit_number = 0,
    print_option = 0,
    node_coords = {},
    free_field = False
    
    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.coord_dir = 0
        self.no_of_nodes = 0
        self.unit_number = 0
        self.print_option = 0
        self.nodeid_coords = {}
        self.free_field = False
    
    # get total number of lines in this card
    def get_linecount(self, dataline):
        if dataline.endswith(","):
            listdata = dataline.split(",") # free field
            free_field = True
        else:
            listdata = dataline.split() # fixed field
            free_field = False
        self.linecount = int(float(listdata[1])) + 2
        return self.linecount
        
    # get node id and coords and store it in a dictionary
    def read_card(self, card_lines):
        card_lines = card_lines[2:self.linecount]
        strlist = []
        floatlist = []
        for card_line in card_lines:
            if(self.free_field == True):
                strlist = card_line.split(",")
            elif(self.free_field == False):
                floatlist.append(float(card_line[0:10]))   # node id
                # x coord
                xcoord = card_line[10:30]
                if (xcoord.find('+') != -1):
                    idx = xcoord.rfind('+')
                else:
                    idx = xcoord.rfind('-')
                xcoord = xcoord[:idx] + 'e' + xcoord[idx:] 
                floatlist.append(float(xcoord))

                # y coord
                ycoord = card_line[30:50]
                if (ycoord.find('+') != -1):
                    idx = ycoord.rfind('+')
                else:
                    idx = ycoord.rfind('-')
                ycoord = ycoord[:idx] + 'e' + ycoord[idx:] 
                floatlist.append(float(ycoord))

                # z coord
                zcoord = card_line[50:70]
                if (zcoord.find('+') != -1):
                    idx = zcoord.rfind('+')
                else:
                    idx = zcoord.rfind('-')
                zcoord = zcoord[:idx] + 'e' + zcoord[idx:] 
                floatlist.append(float(zcoord))
                
            # loop to append coords to node id
            if(len(floatlist) > 0):
                node_id = int(floatlist[0])
                floatlist.pop(0)
                for nodeid in floatlist:
                    self.nodeid_coords.setdefault(node_id, []).append(nodeid)
            strlist.clear()
            floatlist.clear()
        # print to check
        #keylist = self.nodeid_coords.keys()
        #for x in keylist:
        #    print(self.nodeid_coords[x])
        
    def retrieve_data(self):
        pass

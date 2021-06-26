#!/usr/bin/env python
# dataclass with card names and its id

from dataclasses import dataclass

@dataclass
class dat_cards:
    names_ids = {

        #-------model definition-------#
        # basic input requirements
        'TITLE'        : 1,      # title of the program input
        'SIZING'       : 2,      # specify the maximum number of nodes and elements
        'ALLOC'        : 3,      # memory to be allocated at the start of the job
        'ELEMENTS'     : 4,      # has the list of library codes for all elements
        'VERSION'      : 5,      # version of the marc input data file
        'COORDINATES'  : 6,      # contains node id and coordinates
        'CONNECTIVITY' : 7,      # contains element id and connectivity nodes
        'END'          : 8,      # marks the end of parameter section

        # parameters list
        'ELASTIC'      : 9,      # elastic analysis with multi-loads
        'LARGE'        : 10,     # Large displacement or buckling
        'LARGE STRA'   : 11,     # Large displacement or buckling
        'STRUCTURAL'   : 12,     # for mechanical analysis
        'HEAT'         : 13,     # for heat transfer (conduction) analysis
 
        # program control
        'SOLVER'       : 14,     # solver used in this analysis
        'END OPTION'   : 15,     # marks the end of model section
        'CONTINUE'     : 16,     # marks the data for this increment(s) are read
        'UNSUPPORTED'  : 0       # handles all unsupported cards

        #-------history definition-------#
    }
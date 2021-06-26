#!/usr/bin/env python

# class for reading the SOLVER card
class solver:
    linecount = 0,
    solver_type = None,
    nonasym_system = None,
    nonpositive_definite_system = None,
    soln_proc_ddm = None,
    max_iterations = None,
    domain_overlap_size = None,
    nof_four_bytes = None,
    coarse_precond_type = None,
    autospc = None,
    parallel_casi_solver = None,
    dummy = None,

    free_field = False

    # initiliaze the member data during object creation
    def __init__(self):
        self.linecount = 0
        self.solver_type = None,                # solver type
        self.nonasym_system = None,             # 1 for solving a nonsymm system: solver=0,8,11,12
        self.nonpositive_definite_system = None # 1 for nonpositive definite system
        self.soln_proc_ddm = None               # solution procedure, when using DDM
        self.max_iterations = None              # Max nof iterations in inter-domain iterative solver
        self.domain_overlap_size = None         # Size of domain overlap for parallel CASI solver, default is 2.
        self.nof_four_bytes = None              # nof 4-byte words used by solver=6,8,10,11 before going out-of-core.
        self.coarse_precond_type = None         # Used for parallel CASI solver to input coarse preconditioner type.
        self.autospc = None                     # 1 to activate AUTOSPC for singularity. only applicable to direct solvers.
        self.parallel_casi_solver = None        # parallel casi: 1=domain pre-conditioner, 2=global preconditioner
        self.dummy = None                       #
        self.free_field = False                 #

    # get total number of lines in this card
    def get_linecount(self, dataline):
        if dataline.endswith(","):
            listdata = dataline.split(",")  # free field
            free_field = True
        else:
            listdata = dataline.split()    # fixed field
            free_field = False
        self.linecount = 1 + 1             # extra 1, for the card line
        return self.linecount
    
    # get element id and nodes and store it as a dictionary
    def read_card(self, card_lines):
        card_lines = card_lines[1:self.linecount]
        card_line = card_lines[0]

        field = 0

        self.solver_type = int(card_line[field:field+10])        
        field += 10

        self.nonasym_system = int(card_line[field:field+10])
        field += 10

        self.nonpositive_definite_system = int(card_line[field:field+10])
        field += 10

        self.soln_proc_ddm = int(card_line[field:field+10])
        field += 10

        self.max_iterations = int(card_line[field:field+10])
        field += 10

        self.domain_overlap_size = int(card_line[field:field+10])
        field += 10

        self.dummy = int(card_line[field:field+10])
        field += 10

        self.nof_four_bytes = int(card_line[field:field+10])
        field += 10

        self.dummy = int(card_line[field:field+10])
        field += 10

        self.coarse_precond_type = int(card_line[field:field+10])
        field += 10

        self.dummy = int(card_line[field:field+10])
        field += 10

        self.dummy = int(card_line[field:field+10])
        field += 10

        self.dummy = int(card_line[field:field+10])
        field += 10

        self.autospc = int(card_line[field:field+10])
        field += 10

        self.dummy = int(card_line[field:field+10])
        field += 10

        self.parallel_casi_solver = int(card_line[field:field+10])
        field += 10
        
        # print("solver_type", self.solver_type)
        # print("nonasym_system", self.nonasym_system)
        # print("nonpositive_definite_system", self.nonpositive_definite_system)
        # print("soln_proc_ddm", self.soln_proc_ddm)
        # print("max_iterations", self.max_iterations)
        # print("domain_overlap_size", self.domain_overlap_size)
        # print("nof_four_bytes", self.nof_four_bytes)
        # print("coarse_precond_type", self.coarse_precond_type)
        # print("autospc", self.autospc)
        # print("parallel_casi_solver", self.parallel_casi_solver)

    def retrieve_data(self):
        pass
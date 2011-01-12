class DB(object):
    def __init__(self, c):
        self.c = c
        
    def create_cell(self, input):
        raise NotImplementedError
    
    def get_unevaluated_cells(self):
        raise NotImplementedError
    
    def get_evaluated_cells(self):
        raise NotImplementedError
    
    def set_output(self, id, output):
        raise NotImplementedError

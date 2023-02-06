class Node:
    def __init__(self,parent=None,pointer=None):
        self.parent=parent
        self.pointer=pointer
        self.gN=0
        self.hN=0
        self.fN=0
        # self.x_pos=None
        # self.y_pos=None

        
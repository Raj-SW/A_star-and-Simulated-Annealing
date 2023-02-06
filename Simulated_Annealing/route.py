class Route():
    distance=0
    pathway=[]
    start=0
    end=0

    def __init__(self,start,end):
        self.distance=0
        self.start=start
        self.end=end
        self.pathway.append(start)

    def appendPathway(self,node):
        self.pathway.append(node)
    
        

    
        



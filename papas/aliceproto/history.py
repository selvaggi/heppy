from heppy.papas.aliceproto.DAG import Node, BreadthFirstSearchIterative
from heppy.papas.aliceproto.identifier import Identifier

class History(object):
    '''   
       Object to assist with printing and reconstructing histories
       only just started ...
    '''    
    def __init__(self, history_nodes, pfevent):
        #the information needed to be able to unravel information based on a unique identifier
        self.history_nodes = history_nodes
        self.pfevent = pfevent
        
    def summary_of_links(self, id):
    
        #find everything that is linked to this id
        #and write a summary of what is found
        #the BFS search returns a list of connected uniqueids
        BFS = BreadthFirstSearchIterative(self.history_nodes[id], "undirected")
       
        #collate the string descriptions
        track_descrips = []
        ecal_descrips = []
        hcal_descrips = []
        #sim_particle_descrips = []
        rec_particle_descrips = []
        block_descrips = []
        
        
        for n in BFS.result :
            z = n.get_value()
            obj=self.pfevent.get_object(z)
            descrip = obj.__str__()
           # if (Identifier.is_particle(z)):
            #    sim_particle_descrips.append(descrip)
            if (Identifier.is_block(z)):
                block_descrips.append(descrip)            
            elif (Identifier.is_track(z)):
                track_descrips.append(descrip)         
            elif (Identifier.is_ecal(z)):
                ecal_descrips.append(descrip)  
            elif (Identifier.is_hcal(z)):
                hcal_descrips.append(descrip)         
            elif (Identifier.is_rec_particle(z)):
                rec_particle_descrips.append(descrip)               
        
        ##print "block", block_descrips
        #if len(BFS.result) <7:
            #return  
        print "block", block_descrips
        print "history connected to node:", id
        print "       tracks", track_descrips
        print "        ecals", ecal_descrips
        print "        hcals", hcal_descrips
        print "rec particles", rec_particle_descrips
        
        #print "reconstructed particles"
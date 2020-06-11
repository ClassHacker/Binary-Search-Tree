class Tree:
   def __init__(self,data = None):
      self.d = data    #data field
      self.l = None    #left child
      self.r = None    #right child
      
   def insert(self,data):
      if self.d:         
         #compare with root node data
         if data > self.d:
            #check for right child node
            if self.r:
               #insert in right child node
               self.r.insert(data) 
            else:
               #make a new node with data
               self.r = Tree(data)
         else:
            #check for left child node
            if self.l:
               #insert in left child node
               self.l.insert(data)
            else:
               #make a new node with data
               self.l = Tree(data)           
      else:
         self.d = data
         


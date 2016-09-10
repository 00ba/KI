'''
Created on Sep 4, 2016

@author: oobasatoshi
'''

class Tree:    
           
    def __init__(self, name, number):
        self.nord = {'name':'', 'number':'', 'left':'', 'right':''}
        
        self.nord['name'] = name
        self.nord['number'] = number
        self.nord['left'] = ''
        self.nord['right'] = ''
    
    def view(self):
        print self.nord
    
    def add(self):
        pass
    
    def size(self):
        pass   
    
    def delete(self):
        pass
    
    def del_root(self):
        pass
    
    def choose_root(self):
        pass
    


if __name__ == '__main__':
        ki1 = Tree('one', 1)
        ki2 = Tree('two', 2)
        ki3 = Tree('three', 3)
        
        ki1.nord['left'] = ki2
        ki1.nord['right'] = ki3
        ki1.view()
        ki2.view()
        ki3.view()
        ki1.nord['left'].view()
        ki1.nord['right'].view()
        
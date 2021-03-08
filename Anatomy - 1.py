'''
Joshua Yoon
MET CS 521
<10.12.2019>
Final Project
Anatomy: Building Analysis
'''
'''
When building width, length, and height are inputted, the output is a file of

_Building name
_cost per square feet, 
_volume of concrete, 
_how many floors 
_size of concrete column, 
_number of columns, 
_concrete slab thickness,
_how many units per floor, 
_Multiple buildings to compare
_Total budget and compare to client's budget

'''
#units are in feet.


class BuildingAnalysis(object):

    'return the information of building with input width, length, and height'
    CompanyName = "Joshua's BuildingAnalysis program"
    
    def __init__(self, name ='',w=100, l=100, h=100): ##Default value of w,l and h
        
        self.name = name #instance variable (1)
        self.w = w  #instance variable (2)
        self.l = l  #instance variable (3)
        self.h = h  #instance variable (4)
        self.NumFloors()  
        self.SizeColumn() 
        self.SlabThick() 
        self.NumColumn() 
        self.NumUnit() 
          
#Representation of the objects created
    def __repr__(self):
        return "w: {}, l: {}, h: {}".format(self.w, self.l, self.h)

#Number of floors
    def NumFloors(self):
        return self.h // 9.75
    
#Size of concrete column
    def SizeColumn(self):
        lst = []
        if self.h < 100 and self.h > 9:
            lst.append(18)
            lst.append(18)
        elif self.h >= 100 and self.h < 200:
            lst.append(24)
            lst.append(24)
        elif self.h >= 200 and self.h <= 300:
            lst.append(24)
            lst.append(30)

        return lst
      
#Calculating slab thickness
    def SlabThick(self):
        empty = []
        for count in range(self.h,325,25):
            empty.append(count)
        increment = len(empty)
        slab = .375 - increment * 0.00417

        return round(slab,3)
      
#Number of columns
    def NumColumn(self):
        num_col_length = self.l / 25
        num_col_width = self.w / 25
        num_column = round(num_col_length * num_col_width)

        return num_column
    
#Number of units per floor   
    def NumUnit(self):
        Units = (self.l // 25) * 2
        
        return Units

    def __str__(self):
        s = '###Building name: {}\n\
###Width: {}\n\
###Length: {}\n\
###Height: {}\n\
###Number of Floors: {}\n\
###Number of Units: {}\n\
###Size of column: {} by {} inches\n\
###Tickness of Slab: {}\n\
###Number of Column: {}\n'.format(self.name,self.w,self.l,self.h,self.NumFloors(),\
                                self.NumUnit(),self.SizeColumn()[0],\
                                self.SizeColumn()[1],\
                                self.SlabThick(),self.NumColumn())
        return s

#SubClass to calclate volume
class VolumeCost(BuildingAnalysis):
    
    def __init__(self, name, w, l, h, budget):
        super().__init__(name,w, l, h)
        self.budget = budget
        self.checkRequired()
        
#check if the budget is enough to build the building
    def checkRequired(self):
        v = self.w * self.l * self.h
        ActualCost = v * 12
        if self.budget * 1000000 >= ActualCost:
            return 'Possible'
        else:
            return 'Impossible'

    def __str__(self):
        'returns a formatted string'

        s = '\n----------------------------------------------------\n'
        s = s +BuildingAnalysis.__str__(self) #code reuse
        s = s + '###Budget is enough? {}'.format(self.checkRequired())

        return s

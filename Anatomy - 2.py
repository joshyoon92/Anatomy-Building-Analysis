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

import sys

import JoshuaYoon_FinalProject_1 as jy
        
def main():

    a = 1
    
    while True:
        print('************ Building ' + str(a) + '************')
        try:
            name = input("Input the name of building: ")
            if name == '':
                print("Sorry. Print an integer for the dimension of the building.")
                break
            w = int(input("Input the length: "))
            l = int(input("Input the width: "))
            h = int(input("Input the height: "))
            budget = int(input("Input your budget(million): "))
            t1 = jy.VolumeCost(name,l,w,h,budget)
            a +=1
            f = open("Summary.txt", "a")
            f.write(str(t1))
            f.close()

        except Exception:
            print("Sorry. Print an integer for the dimension of the building.")
            sys.exit()

main()








   

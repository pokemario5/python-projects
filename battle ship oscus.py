print("were gong to die but not today")
w = '~'

grid = [

[' ',1,2,3,4,5,6,7,8,9],
['A',w,w,w,w,w,w,w,w,w,],
['b',w,w,w,w,w,w,w,w,w,],
['c',w,w,w,w,w,w,w,w,w,],
['d',w,w,w,w,w,w,w,w,w,],
['e',w,w,w,w,w,w,w,w,w,],
['f',w,w,w,w,w,w,w,w,w,],
['g',w,w,w,w,w,w,w,w,w,],
['h',w,w,w,w,w,w,w,w,w,],
['i',w,w,w,w,w,w,w,w,w,],
['j',w,w,w,w,w,w,w,w,w,],

]


for row in grid:
    for col in row:
        print(col, end=' ')
    print()  
    

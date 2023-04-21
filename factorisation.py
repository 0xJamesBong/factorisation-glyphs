# from sympy.ntheory import factorint

import math
import random

# from sympy.ntheory import factorint
# https://stackoverflow.com/questions/4643647/fast-prime-factorization-module
# factorint(6)


def makeCircle():
    colours = [
        "cyan",
               "red",
               "deeppink",
               "magenta",
               "lime",
               "blue",
               "white",
               "gold",
               "aqua",
               "yellow",
               "orange",
               'greenyellow',
               'dodgerblue'
            ]
    colour = colours[random.randint(0, len(colours)-1)]

    return(f'<circle cx="5000" cy="5000" r="5000" fill="{colour}"/>')

def rotate(degrees, image):
    transformHead = f'<g transform="rotate({degrees}, 5000,5000)">'
    transformTail = '</g>'
    final = transformHead + image + transformTail
    return final
    
    
def scaleDown(scale, image):
    scaleDownHead = f'<g transform="translate({(1-scale)*5000}) scale({scale})">'
    scaleDownTail = '</g>'
    shape = scaleDownHead + '\n'+ image + '\n' + scaleDownTail
    return shape

def reflect(image):
    leftHead = f'<g transform="translate(-2500)">'
    leftTail= '</g>'
    rightHead = f'<g transform="translate(2500)">'
    rightTail ='</g>'
    shape = leftHead + '\n' + image + leftTail + '\n'+ rightHead + '\n' + image + '\n' + rightTail
    return shape


def makePolygon(prime):
    # circle = makeCircle()
    degrees = 360/prime
    shape = ""
    
    if prime ==2: 
        for i in range(0,prime):    
            incompleteShape = rotate(i*degrees, scaleDown((1)/(prime+1), makeCircle()))
            shape = shape + '\n' + incompleteShape
    # The scaling down applies only two thte circle   
    elif prime ==3:
        for i in range(0,prime):    
            incompleteShape = rotate(i*degrees, scaleDown((1)/(prime), makeCircle()))
            shape = shape + '\n' + incompleteShape
    else:
        for i in range(0,prime):
    
            incompleteShape = rotate(i*degrees, scaleDown((1)/(prime-1), makeCircle()))
            shape = shape + '\n' + incompleteShape
    return shape
    
    
def composeShape(prime, image):
    degrees = 360/prime
    shape = ""

    if prime == 2:
        for i in range(0,prime):
            incompleteShape = rotate(i*degrees, scaleDown((1)/(prime+1),image))
            shape = shape + '\n' + incompleteShape
    elif prime == 3:
        for i in range(0,prime):
            incompleteShape = rotate(i*degrees, scaleDown((1)/(prime-1),image))
            shape = shape + '\n' + incompleteShape
    else:
        for i in range(0,prime):
        # First one is proper
            incompleteShape = rotate(i*degrees, scaleDown((prime-1)/(2*prime+3),image))
            # incompleteShape = rotate(i*degrees, scaleDown((prime-1)/(2*prime*prime+1),image))
    #         incompleteShape = rotate(i*degrees, scaleDown(math.log(1/(prime-2))/math.log(1/(prime)),image))
    #         incompleteShape = rotate(i*degrees, scaleDown(1/(prime-5),image))
    #         incompleteShape = rotate(i*degrees, scaleDown(prime/(2*prime-1),image))
    #         incompleteShape = rotate(i*degrees, scaleDown(1/(2-(math.log(prime)-1)),image))
            shape = shape + '\n' + incompleteShape
    return shape

# def makeShapeByFactorisation(factorisation:dict):
#     shape=""
# #     print(list(factorisation.keys())[0])
# #     if the number is 0
#     if factorisation=={0:1}:
#         return shape
# #     if the number is 1
#     elif factorisation=={}:
#         return ('<g transform="translate(0,2500)">'+'\n'+makeCircle()+'\n'+'</g>')
#     else:
#         for k,v in factorisation.items(): 
#             prime = k
#             power = v

#             if k == list(factorisation.keys())[0]:
#                 for p in range(0,v):
#                     if p==0:
#                         shape=makePolygon(k)
#                     else: 
#                         shape=composeShape(k,shape)
#             else:
#                 for p in range(0,v):
#                     shape=composeShape(k,shape)
#         return shape

def wrapCanvas(stuffInside):
    head = '<svg  xmlns="http://www.w3.org/2000/svg" width="10000" height="10000" style="background-color:black">'
    tail = '</svg>'
    # wrapped = head + '\n'+ stuffInside + '\n' +tail
    wrapped = head + '\n'+ '<g transform="translate(1000,1000) scale(0.8)">'+stuffInside +'</g>'+ '\n' + tail
    print(wrapped)
    return(wrapped)



# shape = makeShapeByFactorisation(factorint(2**10-1))
# Test shapes 
# 1
# shape = makeCircle()

# 2
# shape = makePolygon(2)

# # Equilateral Triangle 
# shape = makePolygon(3)

# Square 
# shape = makePolygon(4)

# # Pentagon
# shape = makePolygon(5)

# # Hexagon 
# shape = makePolygon(6)

# # Septagon
# shape = makePolygon(7)

# # Octagon
# shape = makePolygon(8)

# # Octagon
# shape = makePolygon(9)

# # Octagon
# shape = makePolygon(1333)



# shape = composeShape(2,(composeShape(2,composeShape(2,composeShape(2,composeShape(2,makePolygon(2)))))))

# # Sierpinski's triangle
# shape = composeShape(3,(composeShape(3,composeShape(3,composeShape(3,composeShape(3,makePolygon(3)))))))

# # Sierpinski's Pentagon
# shape=composeShape(5,composeShape(5,composeShape(5,composeShape(5,makePolygon(5)))))

# # Koch snowflake
# shape = composeShape(6,composeShape(6,composeShape(6,composeShape(6,makePolygon(6)))))

# # Sierpinski's Septagon
shape = composeShape(7,composeShape(7,composeShape(7,composeShape(7,makePolygon(7)))))

# # Sierpinski's Octagon
# shape = composeShape(8,composeShape(8,composeShape(8,composeShape(8,makePolygon(8)))))
# shape = composeShape(16,composeShape(16,composeShape(16,composeShape(16,makePolygon(16)))))

# # Prime 31 
# shape = makePolygon(31)

# # Prime 131
# shape = makePolygon(131)

# 29*13^2*3*2^2 (big to small prime odering)
# shape = composeShape(29,composeShape(13,composeShape(13,composeShape(2,composeShape(2,makePolygon(3))))))

# # 2^2*3*13^2*29
# shape = composeShape(2,composeShape(2,composeShape(3,composeShape(13,composeShape(13,makePolygon(29))))))

# Sierpinski's 131
# shape = composeShape(131,composeShape(131,composeShape(131,composeShape(131,makePolygon(131)))))

# 60 = 2^2 * 3 *5 (small to big prime ordering)
# shape = composeShape(4,composeShape(3,makePolygon(5)))

# alternative 60 = 2^2 * 3 *5 (big to small prime ordering)
# shape = composeShape(5, composeShape(3, composeShape(2, makePolygon(2))))


# 131*5^2*3*2 (big to small prime odering)
# shape = composeShape(131,composeShape(5,composeShape(5,composeShape(3,composeShape(2,makePolygon(2))))))

# 2*3*5^2*131 (small to big prime odering)
# shape = composeShape(2,composeShape(3,composeShape(5,composeShape(5,makePolygon(131)))))

# 3^2 * 5^2
# shape = composeShape(5,composeShape(5,composeShape(3,makePolygon(3))))

# shape = reflect(makePolygon(2))


with open('./output/pythonGenerated.svg', 'w') as f:
    text=wrapCanvas(shape)
    f.write(text)



#vektorkorrutis
def vektorkorrutis(x1,x2,x3,y1,y2,y3):

    ab1=(x2*y3)-(x3*y2)
    ab2=(x3*y1)-(x1*y3)
    ab3=(x1*y2)-(x2*y1)
    c=(ab1,-ab2,ab3)
    return c

#Ruutvõrrand õige
import math
from fractions import Fraction
#Ruutvõrrand õige
def ruutvõrrand(a,b,c):  
    D=b**2-4*a*c
    if D>0:
        print('Ruutfunktsioonil on 2 erinevat nullkohta')
        valem=float((-b+math.sqrt(b**2-4*a*c))/(2*a))
        valem2=float((-b-math.sqrt(b**2-4*a*c))/(2*a))
        murruna=Fraction(valem)
        murruna2=Fraction(valem2)
        return(f'x1={murruna}, x2={murruna2}')

    elif D==0:
        print('Ruutfunktsioonil on 2 võrdset nullkohta')
        valem=float((-b+math.sqrt(b**2-4*a*c))/(2*a))
        murruna=Fraction(valem)
        return(f'x1,x2={murruna}')
    else:
        return('Ruutfunktsioonil nullkohad puuduvad')

#segakorrutis
def segakorrutis(a,b,c,d,e,f,g,h,i):
    abc=(a*e*i)+(b*f*g)+(c*d*h)
    abc2=-(g*e*c)-(h*f*a)-(i*d*b)
    vastus=abc+abc2
    return vastus
#determinandid
import numpy as np
#2. järku
def det2(a,b,c,d):
    determinant2=(a*d)-(b*c)
    return determinant2

#3. järku
def det3(a,b,c,d,e,f,g,h,i):
    determinant3=(a*e*i)+(b*f*g)+(d*h*c)-(g*e*c)-(d*b*i)-(h*f*a)
    return determinant3
#5. järku
def det5(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,õ,ä):  
    # creating a 5X5 Numpy matrix
    n_array = np.array([[a, b, c, d, e],
                        [f, g, h, i, j],
                        [k, l, m, n, o],
                        [p, q, r, s, t],
                        [u, v, w, õ, ä]])
      
    # calculating the determinant of matrix
    det = np.linalg.det(n_array)
      
    return int(det)

#4. järku
def det4(a,b,c,d,f,g,h,i,k,l,m,n,p,q,r,s):  
    # creating a 5X5 Numpy matrix
    n_array = np.array([[a, b, c, d],
                        [f, g, h, i],
                        [k, l, m, n],
                        [p, q, r, s]])
      
    # calculating the determinant of matrix
    det = np.linalg.det(n_array)
      
    return int(det)

import numpy as np
import fractions

#2*2 pöördmatrix
def pöörd2m(a,b,c,d):
    # Taking a 2*2 matrix
    A = np.array([[a, b],
                  [c,d]])
    #kas det 0?
    det = np.linalg.det(A)
    if det==0:
        return 0
    else:
        # Calculating the inverse of the matrix
        inv=np.linalg.inv(A)
        #murdudeks!
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
        return inv

    

#3*3 pöördmatrix
def pöörd3m(a,b,c,d,e,f,g,h,i):
    # Taking a 3*3 matrix
    A = np.array([[a, b, c],
                  [d,e,f],
                  [g,h,i]])
    #kas det 0?
    det = np.linalg.det(A)
    if det==0:
        return 0
    else:
        # Calculating the inverse of the matrix
        inv=np.linalg.inv(A)
        #murdudeks!
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
        return inv

#4*4 pöördmatrix
def pöörd4m(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    # Taking a 4*4 matrix
    A = np.array([[a, b, c,d],
                  [e,f,g,h],
                  [i,j,k,l],
                  [m,n,o,p]])
    #kas det 0?
    det = np.linalg.det(A)
    if det==0:
        return 0
    else:
        # Calculating the inverse of the matrix
        inv=np.linalg.inv(A)
        #murdudeks!
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
        return inv

    
    #5*5 pöördmatrix
def pöörd5m(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y):
    # Taking a 5*5 matrix
    A = np.array([[a, b, c,d,e],
                  [f,g,h,i,j],
                  [k,l,m,n,o],
                  [p,q,r,s,t],
                  [u,v,w,x,y]])
    #kas det 0?
    det = np.linalg.det(A)
    if det==0:
        return 0
    else:
        # Calculating the inverse of the matrix
        inv=np.linalg.inv(A)
        #murdudeks!
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
        return inv



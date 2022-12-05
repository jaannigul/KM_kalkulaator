import numpy as np
import fractions
import math
from fractions import Fraction

#vektorkorrutis
def vektorkorrutis(x1,x2,x3,y1,y2,y3):

    ab1=(x2*y3)-(x3*y2)
    ab2=(x3*y1)-(x1*y3)
    ab3=(x1*y2)-(x2*y1)
    c=(ab1,-ab2,ab3)
    return c


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
def det2(a11,a12,a21,a22):
    determinant2=(a11*a22)-(a12*a21)
    return determinant2

#3. järku
def det3(a11,a12,a13,a21,a22,a23,a31,a32,a33):
    determinant3=(a11*a22*a33)+(a12*a23*a31)+(a21*a32*a13)-(a31*a22*a13)-(a21*a12*a33)-(a32*a23*a11)
    return determinant3

#5. järku
def det5(a11, a12, a13, a14, a15,a21, a22, a23, a24, a25,a31, a32, a33, a34, a35,a41, a42, a43, a44, a45,a51, a52, a53, a54, a55):  
    # creating a 5X5 Numpy matrix
    n_array = np.array([[a11, a12, a13, a14, a15],
                        [a21, a22, a23, a24, a25],
                        [a31, a32, a33, a34, a35],
                        [a41, a42, a43, a44, a45],
                        [a51, a52, a53, a54, a55]])
      
    # calculating the determinant of matrix
    det = np.linalg.det(n_array)
      
    return int(det)

#4. järku
def det4(a11, a12, a13, a14,a21, a22, a23, a24,a31, a32, a33, a34,a41, a42, a43, a44):  
    # creating a 4x4 Numpy matrix
    n_array = np.array([[[a11, a12, a13, a14],
                        [a21, a22, a23, a24],
                        [a31, a32, a33, a34],
                        [a41, a42, a43, a44]]])
      
    # calculating the determinant of matrix
    det = np.linalg.det(n_array)
      
    return int(det)


#2*2 pöördmatrix
def pöörd2m(a11,a12,a21,a22):
    # Taking a 2*2 matrix
    A = np.array([[a11, a12],
                  [a21,a22]])
    #kas det 0?
    det = np.linalg.det(A)
    if det==0:
        return 'Pöördmaatriks puudub'
    else:
        # Calculating the inverse of the matrix
        inv=np.linalg.inv(A)
        #murdudeks!
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
        return inv

    

#3*3 pöördmatrix
def pöörd3m(a11,a12,a13,a21,a22,a23,a31,a32,a33):
    # Taking a 3*3 matrix
    A = np.array([[a11, a12, a13],
                  [a21,a22,a23],
                  [a31,a32,a33]])
    #kas det 0?
    det = np.linalg.det(A)
    if det==0:
        return 'Pöördmaatriks puudub'
    else:
        # Calculating the inverse of the matrix
        inv=np.linalg.inv(A)
        #murdudeks!
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
        return inv

#4*4 pöördmatrix
def pöörd4m(a11,a12,a13,a14,a21,a22,a23,a24,a31,a32,a33,a34,a41,a42,a43,a44):
    # Taking a 4*4 matrix
    A = np.array([[a11, a12, a13,a14],
                  [a21,a22,a23,a24],
                  [a31,a32,a33,a34],
                  [a41,a42,a43,a44]])
    #kas det 0?
    det = np.linalg.det(A)
    if det==0:
        return 'Pöördmaatriks puudub'
    else:
        # Calculating the inverse of the matrix
        inv=np.linalg.inv(A)
        #murdudeks!
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
        return inv

    
    #5*5 pöördmatrix
def pöörd5m(a11,a12,a13,a14,a15,a21,a22,a23,a24,a25,a31,a32,a33,a34,a35,a41,a42,a43,a44,a45,a51,a52,a53,a54,a55):
    # Taking a 5*5 matrix
    A = np.array([[a11, a12, a13,a14,a15],
                  [a21,a22,a23,a24,a25],
                  [a31,a32,a33,a34,a35],
                  [a41,a42,a43,a44,a45],
                  [a51,a52,a53,a54,a55]])
    #kas det 0?
    det = np.linalg.det(A)
    if det==0:
        return 'Pöördmaatriks puudub'
    else:
        # Calculating the inverse of the matrix
        inv=np.linalg.inv(A)
        #murdudeks!
        np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
        return inv



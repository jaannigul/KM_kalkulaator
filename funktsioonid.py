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
#vektorkorrutis
def vektorkorrutis(x1,x2,x3,y1,y2,y3):

    ab1=(x2*y3)-(x3*y2)
    ab2=(x3*y1)-(x1*y3)
    ab3=(x1*y2)-(x2*y1)
    c=(ab1,-ab2,ab3)
    return c

import math
#Ruutvõrrand õige
def ruutvõrrand(a,b,c):
    
    D=b**2-4*a*c
    if D>0:
        print('Ruutfunktsioonil on 2 erinevat nullkohta')
        valem=float((-b+math.sqrt(b**2-4*a*c))/(2*a))
        valem2=float((-b-math.sqrt(b**2-4*a*c))/(2*a))
        return(f'x1={valem}, x2={valem2}')

    elif D==0:
        print('Ruutfunktsioonil on 2 võrdset nullkohta')
        valem=float((-b+math.sqrt(b**2-4*a*c))/(2*a))
        valem2=float((-b-math.sqrt(b**2-4*a*c))/(2*a))
        return(f'x1,x2={valem2}')
    else:
        return('Ruutfunktsioonil nullkohad puuduvad')

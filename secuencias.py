import numpy as np
import cmath as cm

#Recibe las 3 cantidades de fase y retorna un array con las 3 cantidades de secuecnia [I0;I1;I2]
def seq(I_a,I_b,I_c):
    alpha=cm.rect(1,2*cm.pi/3)
    A=(1/3)*np.matrix([[1,1,1],[1, alpha,alpha**2],[1,alpha**2,alpha]])
    I_seq=np.matmul(A,np.matrix([[I_a],[I_b],[I_c]]))
    return I_seq

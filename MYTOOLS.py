#MYTOOLS

from mpmath import mp

# Define a precisão (número de dígitos após o ponto decimal)
mp.dps = 102  # 100 dígitos após o ponto decimal + 2 para a parte inteira '3.'

# Obtenha o valor de π
pi_str = str(mp.pi)

# Extraia os 100 primeiros dígitos após o ponto decimal
decimal_part = pi_str.split('.')[1][:100]

# Converta para inteiro
pi_int = int(decimal_part)

# Obtenha o valor de π
e_str = str(mp.e)

# Extraia os 100 primeiros dígitos após o ponto decimal
e_decimal_part = e_str.split('.')[1][:100]

# Converta para inteiro
e_int = int(e_decimal_part)


def pi_real(n):
    if n>0 and n<100:
        pi_n=int(str(pi_int)[0,n])*10**(-n)+3
    return pi_n

def e_real(n):
        if n>0 and n<100:
        e_n=int(str(e_int)[0,n])*10**(-n)+2
    return e_n


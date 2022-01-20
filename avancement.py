from math import *

def b():  # 2 reactifs 2 produit
    coeff_react1 = int(input("Coefficient du reactif 1 : "))
    qdm_react1 = float(input("Nombre de moles pour le reactif 1 : "))
    coeff_react2 = int(input("Coefficient du reactif 2 : "))            # demandes des valeurs
    qdm_react2 = float(input("Nombre de moles pour le reactif 2 : "))
    coeff_produit1 = int(input("Coefficient du produit 1 : "))
    coeff_produit2 = int(input("Coefficient du produit 2 : "))

    x1 = qdm_react1 / coeff_react1 # équations pour connaitre les x
    x2 = qdm_react2 / coeff_react2
    xf = 0

    if x1 < x2: # le plus petit x est le bon (il détermine le réactif limitant, si les x sont égaux alors le mélange est stoechiométrique)
        xf = x1

    else:
        xf = x2

    efr1 = qdm_react1 - coeff_react1 * xf
    efr2 = qdm_react2 - coeff_react2 * xf   # états finaux
    efp1 = coeff_produit1 * xf
    efp2 = coeff_produit2 * xf

    print("------------------------------------------------------------------------------")
    print("|Eq  | ", coeff_react1, " R1  + ", coeff_react2, " R2 --> ", coeff_produit1," P1 +", coeff_produit2," P2|")
    print("|-----------------------------------------------------------------------------------")
    print("|EIn |  ", qdm_react1, "  |  ", qdm_react2, "  |   0   |   0   |")
    print("|-----------------------------------------------------------------------------------")  
    print("|EInt|", qdm_react1, "-", coeff_react1, "x |", qdm_react2,"-", coeff_react2,"x |", coeff_produit1, "x |", coeff_produit2, " x|")
    print("|-----------------------------------------------------------------------------------")
    print("|EFin|  ", round(efr1, 10), " | ", round(efr2, 10), "  |  ", round(efp1, 10)," | ", round(efp2, 10),"  |")
    print("|-----------------------------------------------------------------------------------")

b()

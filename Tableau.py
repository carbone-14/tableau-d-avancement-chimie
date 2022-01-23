def b():

    coeff_react=[]
    qdm_react=[]
    coeff_produit=[]
    reactif_quantity=int(input("Nombre de reactifs : "))
    for i in range(reactif_quantity) :
        coeff_react.append(int(input("Coefficient du reactif {} : ".format(i+1))))
        qdm_react.append(eval(input("Nombre de moles pour le reactif {} : ".format(i+1))))
    product_quantity=int(input("Nombre de produits : "))
    for i in range(product_quantity) :
        coeff_produit.append(int(input("Coefficient du produit {} : ".format(i+1))))

    x_liste=[ qdm/coeff for qdm,coeff in zip(qdm_react,coeff_react)]
    xf = min(x_liste)
    
    efr_liste=[ qdm-coeff*xf for qdm,coeff in zip(qdm_react,coeff_react)]
    efp_liste=[ coeff*xf for coeff in coeff_produit]

    text_lines=[]
    #creation de la premiere ligne
    eq_line="|Eq  | "
    eq_line+="".join(["{} R{} + ".format(i,indice) for indice,i in enumerate(coeff_react,1)])
    eq_line=eq_line[:-2]
    eq_line+="--> "
    eq_line+="".join(["{} P{} + ".format(i,indice) for indice,i in enumerate(coeff_produit,1)])
    eq_line=eq_line[:-2]
    eq_line+="|"
    text_lines.append(eq_line)
    #creation de la deuxieme ligne
    eIn_line="|EIn |"
    eIn_line+="".join(["  {}  |".format(i) for i in qdm_react])
    eIn_line+="".join(["  0  |" for i in coeff_produit])
    text_lines.append(eIn_line)
    #creation de la troisieme ligne
    eInt_line="|EInt|"
    eInt_line+="".join(["{} - {}x |".format(qdm,coeff) for qdm,coeff in zip(qdm_react,coeff_react)])
    eInt_line+=''.join([" {}x |".format(coeff) for coeff in coeff_produit])
    text_lines.append(eInt_line)
    #creation de la quatrieme ligne
    eFin="|EFin| "
    eFin+=''.join([" {} |".format(round(efr,10)) for efr in efr_liste])
    eFin+=''.join([" {} |".format(round(efp,10)) for efp in efp_liste])
    text_lines.append(eFin)
    separation="|"
    separation+="-"*(len(text_lines[0])-1)
    for i in range(0,10,2) : text_lines.insert(i,separation)
    [print(i) for i in text_lines]

    
b()

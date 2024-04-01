def problema_solucion_inocente(d):
    return problema_solucion_inocente_aux(d, 0)

def problema_solucion_inocente_aux(d, i):
    if i >= len(d):
        return 0
    
    #Incluye el elemento presente y salta al siguiente elemento adecuado
    incl = d[i] + problema_solucion_inocente_aux(d, i + 2)
        # No incluyas el elemento presente y selecciona el siguiente elemento
    excl = problema_solucion_inocente_aux(d, i + 1)
        #Regresa el maximo entre ambos
    return max(incl, excl)
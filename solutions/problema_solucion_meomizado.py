def problema_solucion_meomizado(d,M):
    #Matriz meomizada llena de -inf
    M = {i: float('-inf') for i in range(len(d))}
    return problema_solucion_meomizado_aux(d, 0, M)

def problema_solucion_meomizado_aux(d,i,M):
    if i >= len(d):
        return 0
    #Si ya se implemento la respuesta
    if M[i] != float('-inf'):
        return M[i]
    
    incl = d[i] + problema_solucion_meomizado_aux(d,i+2,M)
    excl = problema_solucion_meomizado_aux(d,i+1,M)

    M[i] = max(incl,excl)
    
    return M[i]
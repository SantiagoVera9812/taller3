def problema_solucion_bottom_up(d):
    n = len(d)
    if n == 0:
        return 0
    if n == 1:
        return d[0]
    
    # Inicializar una lista con la longitud de la secuencia
    dp = [0] * n

    # Los casos base
    dp[0] = d[0]
    dp[1] = max(d[0], d[1])

    # Construir la tabla bottom-up
    for i in range(2, n):
        
        dp[i] = max(d[i] + dp[i - 2], dp[i - 1])

    return dp

def obtener_numeros_seleccionados(secuencia, dp):
    seleccionados = []
    n = len(secuencia)
    i = n - 1  # Empezamos desde el último elemento de la secuencia
    
    while i >= 0:
        # Si el valor actual es igual al valor anterior, significa que no se seleccionó
        # el elemento actual, entonces pasamos al siguiente elemento
        if i > 0 and dp[i] == dp[i - 1]:
            i -= 1
        #Si la suma actual es mayor a la suma anterior
        elif i == 0 or dp[i] > dp[i - 1]:
            seleccionados.append(secuencia[i])
            # Avanzamos dos pasos hacia atrás, ya que los elementos adyacentes no pueden ser seleccionados
            i -= 2
        else:
            i -= 1  # Si no se cumple ninguna de las condiciones anteriores, pasamos al siguiente elemento
        
    # Invertimos la lista ya que hemos estado retrocediendo desde el último elemento
    seleccionados.reverse()
    return seleccionados
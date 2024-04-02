import sys
import random
import time

import solutions.problema_solucion_meomizado
import solutions.problema_solucion_inocente
import solutions.problema_solucion_bottom_up

def measure_time(S, sort_function):
    if isinstance(S,int):
        start_time = time.perf_counter_ns()
        sort_function(S)
        end_time = time.perf_counter_ns()
        return end_time -start_time
    
    S_copy = S.copy()
    start_time = time.perf_counter_ns()
    sort_function(S_copy)
    end_time = time.perf_counter_ns()
    return end_time - start_time

def measure_time(S, sort_function, *args):
    if isinstance(S, int):
        start_time = time.perf_counter_ns()
        sort_function(S)
        end_time = time.perf_counter_ns()
        return end_time - start_time
    
    S_copy = S.copy()
    start_time = time.perf_counter_ns()
    if args:
        sort_function(S_copy, *args)
    else:
        sort_function(S_copy)
    end_time = time.perf_counter_ns()
    return end_time - start_time

def run_experiments(min_s, max_s, s_step):
    for n in range(min_s, max_s + s_step, s_step):
        S = [random.randint(0, n) for i in range(n)]
        '''
        print(solutions.problema_solucion_meomizado(S))
        print(solutions.problema_solucion_bottom_up(S))
        '''
        time_meomizado = measure_time(S, solutions.problema_solucion_meomizado)
        time_bottom_up = measure_time(S, solutions.problema_solucion_bottom_up)
        solucion = solutions.problema_solucion_bottom_up(S)
        '''
        print(sum(solutions.obtener_numeros_seleccionados(S,solucion)))
        '''
        time_solucion = measure_time(S,solutions.obtener_numeros_seleccionados, solucion)
        print(f'{n} , {time_meomizado} , {time_bottom_up} , {time_solucion}')

if __name__ == "__main__":
    ## Check arguments
    if len(sys.argv) < 4:
        print("Usage: ", sys.argv[0], "min_s max_s s_step ")
        exit(1)
    ## end if

    min_s_arg = int(sys.argv[1])
    max_s_arg = int(sys.argv[2])
    s_step_arg = int(sys.argv[3])

    run_experiments(min_s_arg, max_s_arg, s_step_arg)
        
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import modules used here 
import sys
import random


# Create the Process object with all the details of a process.
class Process(object):
	id_number = 0
	name = ""
	memory_size = random.randint(1,1000)
	execution_size = random.randint(1,200)
	priority = random.randint(1,10)
	io_delay = random.randint(1,10)
	arrival = random.randint(0,20)

def create_process(num_process):
	'''We create the process that we will work with.'''


def main():
	print ('Hola, Vamos a crear los primeros procesos.')
	print("Agrega los datos con la siguiente")
	print("'nombre, tamano_memoria, tiempo_ejecucion, prioridad, llegada, timepo E/S''")



if __name__ == '__main__':
	process_list = []
	main()





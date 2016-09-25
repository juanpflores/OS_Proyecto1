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
	execution_size = random.randint(1,200) #rafagation
	priority = random.randint(1,10)
	arrival = random.randint(0,20)

def create_process():
	x = 0
	while True:
		'''We create the process that we will work with.'''
		print("Agrega los datos con el siguiente formato")
		print("'nombre, tamano_memoria, tiempo_ejecucion, prioridad, llegada'")
		data_input = input()
		data = data_input.split(',')

		new_process = Process()
		new_process.id_number = x
		new_process.name = str(data[0])
		new_process.memory_size = int(data[1])
		new_process.execution_size = int(data[2])
		new_process.priority = int(data[3])
		new_process.arrival = int(data[4])

		process_list.append(new_process)

		#print(process_list[0].arrival)
		x = x + 1
		print("Quieres crear otro proceso (S/N)")
		salida = input()
		if salida == "N" or salida == "n":
			break



def main():
	print ('Hola, Vamos a crear los primeros procesos.')
	create_process()




if __name__ == '__main__':
	process_list = []

	main()





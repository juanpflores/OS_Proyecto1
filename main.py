#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import modules used here 
import sys
import random
import os


# Create the Process object with all the details of a process.
class Process(object):
	id_number = 0
	name = " "
	memory_size = random.randint(1,1000)
	execution_size = random.randint(1,200)
	priority = random.randint(1,10)
	arrival = random.randint(0,20)

def create_process():
	x = 0
	while True:
		'''We create the process that we will work with.'''
		while True:
			try:
				print("Agrega los datos con el siguiente formato")
				print("nombre, tamano_memoria, tiempo_ejecucion, prioridad, llegada")
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
				break
			except (RuntimeError, TypeError, NameError, IndexError, ValueError):
				print("Oops! Ese proceso no es válido. Vuelve a intentarlo")

		#for process in process_list:
		#	print (process.arrival)

		x = x + 1
		print("Quieres crear otro proceso (S/N)")
		salida = input()
		if salida == "N" or salida == "n":
			process_list.sort(key=lambda x: x.arrival)
			#for process in process_list:
			#	print(process.arrival)
			break
		clear()

def select_plan():
	while True:
		try:
			print("Los procesos estan listos. \n¿Qué planificador quieres usar?")
			print("\t (1) Prioridad Cooperativo")
			print("\t (2) Round Robin")
			selection = int(input())
			if selection == 1:
				break
			elif selection == 0:
				break
			else:
				print("El valor: " + str(selection) + " no es valido.")

		except (RuntimeError, TypeError, NameError, IndexError, ValueError):
			print("Oops! Ese dato no es válido. Vuelve a intentarlo")



def main():
	clear()
	print ('Hola, Vamos a crear los primeros procesos.')
	create_process()

	clear()
	select_plan()




if __name__ == '__main__':
	process_list = []
	memory_size = 2000
	clear = lambda: os.system('clear')

	main()





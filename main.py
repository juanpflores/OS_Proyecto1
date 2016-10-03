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
				print("Oops! El proceso no es válido. Vuelve a intentarlo")

		#for process in process_list:
		#	print (process.arrival)

		x = x + 1 	#Contador del ID aumenta en 1
		print("Quieres crear otro proceso (S/N)")
		salida = input()
		if salida == "N" or salida == "n":
			process_list.sort(key=lambda x: x.arrival, reverse=True)
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
		except (RuntimeError, TypeError, NameError, IndexError, ValueError):
			print("Oops! Ese dato no es válido. Vuelve a intentarlo")
		if selection == 1:
			prioridad()
			break
		elif selection == 2:
			round_robin()
			break
		else:
			print("El valor: " + str(selection) + " no es valido.")

def round_robin():
	quantum = 0
	while True:
		print("Ingresa el tamaño de tu Quantum.")
		try:
			quantum = int(input())
			break
		except TypeError:
			print("El valor de tu Quantum no es valido.")

	while True:
		cargar_memoria(tiempo_procesador, memory_size)
		for proceso in process_in_memory_list:
			for x in range(quantum):
				if proceso.execution_size == 0:
					memory_size = proceso.memory_size + memory_size
					print("[" + proceso.name + "] Salió por E/S")

					index = process_in_memory_list.index(proceso)

					del process_in_memory_list[index]
					break

				elif (proceso.execution_size - quantum) <= 0:
					print("[" + proceso.name + "] terminó de ejecutar")
					proceso.execution_size = 0
					break
				else:
					proceso.execution_size = proceso.execution_size - 1
					print("[" + proceso.name + "] subió restan:" + str(proceso.execution_size))




def prioridad():
	pass


def cargar_memoria(tiempo_procesador, memory_size):
	while True:
		if process_list:
			current_process = process_list.pop()
		else:
			print("No hay más procesos")
			sys.exit(0)
			break

		if current_process.arrival <= tiempo_procesador:
			if current_process.memory_size <= memory_size:
				print("[" + str(current_process.name) + "]: Cargado en Memoria del CPU")
				process_in_memory_list.append(current_process)
			else:
				process_list.append(current_process)
				break
		else:
			process_list.append(current_process)
			break

		if not process_in_memory_list:
			tiempo_procesador = tiempo_procesador + 1

	for proceso in process_in_memory_list:
		print(proceso.name)


def main():

	clear()
	print ('Hola, Vamos a crear los primeros procesos.')
	create_process()

	clear()
	select_plan()




if __name__ == '__main__':
	clear = lambda: os.system('clear')
	process_list = []
	process_in_memory_list = []
	tiempo_procesador = 0
	memory_size = 2000

	main()





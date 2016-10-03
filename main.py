#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import os

class Process(object):
	id_n = 0
	nombre = " "
	tamano_memoria = random.randint(1,1000)
	t_rafaga = random.randint(1,200)
	prioridad = random.randint(1,10)
	llegada = random.randint(0,20)

def create_process():
	global lista_procesos

	x = 0
	while True:
		'''We create the process that we will work with.'''
		while True:
			try:
				print("Agrega los datos con el siguiente formato")
				print("nombre, tamano_memoria, tiempo_ejecucion, prioridad, llegada")
				data_input = input()
				data = data_input.split(',')
				nuevo_proceso = Process()
				nuevo_proceso.id_n = x
				nuevo_proceso.nombre = str(data[0])
				nuevo_proceso.tamano_memoria = int(data[1])
				nuevo_proceso.t_rafaga = int(data[2])
				nuevo_proceso.prioridad = int(data[3])
				nuevo_proceso.llegada = int(data[4])

				lista_procesos.append(nuevo_proceso)
				break
			except (RuntimeError, TypeError, NameError, IndexError, ValueError):
				print("Oops! El proceso no es válido. Vuelve a intentarlo")

		#for process in lista_procesos:
		#	print (process.llegada)

		x = x + 1 	#Contador del ID aumenta en 1
		print("Quieres crear otro proceso (S/N)")
		salida = input()
		if salida == "N" or salida == "n":
			lista_procesos.sort(key=lambda x: x.llegada, reverse=True)
			#for process in lista_procesos:
			#	print(process.llegada)
			break
		clear()

def select_plan():
	while True:
		try:
			print("Los procesos estan listos. \n¿Qué planificador quieres usar?")
			print("\t (1) Prioridad Cooperativo")
			print("\t (2) Round Robin")
			opcion = int(input())
		except (RuntimeError, TypeError, NameError, IndexError, ValueError):
			print("Oops! Ese dato no es válido. Vuelve a intentarlo")
		if opcion == 1:
			prioridad()
			break
		elif opcion == 2:
			round_robin()
			break
		else:
			print("El valor: " + str(opcion) + " no es valido.")

def round_robin():
	global procesos_cpu
	global lista_procesos
	global tiempo_procesador
	global tamano_memoria

	quantum = 0
	while True:
		print("Ingresa el tamaño de tu Quantum.")
		try:
			quantum = int(input())
			break
		except TypeError:
			print("El valor de tu Quantum no es valido.")

	while True:
		cargar_memoria()
		for proceso in procesos_cpu:
			for x in range(quantum):
				if proceso.t_rafaga == 0:
					tamano_memoria = proceso.tamano_memoria + tamano_memoria
					print("[" + proceso.nombre + "] Salió por E/S")
					index = procesos_cpu.index(proceso)
					del procesos_cpu[index]
					break

				elif (proceso.t_rafaga - 1) <= 0:
					print("[" + proceso.nombre + "] Terminó de Ejecutar")
					proceso.t_rafaga = 0
					break
				else:
					proceso.t_rafaga = proceso.t_rafaga - 1
					print("[" + proceso.nombre + "] subió restan: " + str(proceso.t_rafaga))
					tiempo_procesador = tiempo_procesador + 1
		
		if (not procesos_cpu and not lista_procesos):
			sys.exit(0)



def prioridad():
	global procesos_cpu
	global lista_procesos
	global tiempo_procesador
	global tamano_memoria

	while True:
		cargar_memoria()

		if procesos_cpu:
			procesos_cpu.sort(key=lambda x: x.prioridad)
			proceso_actual = procesos_cpu.pop()

			for x in range(proceso_actual.t_rafaga):
				tiempo_procesador = tiempo_procesador + 1
				proceso_actual.t_rafaga = proceso_actual.t_rafaga - 1
				print("[" + proceso_actual.nombre + "] subió restan: " + str(proceso_actual.t_rafaga))
			print("[" + proceso_actual.nombre + "] Terminó de Ejecutar")
			tamano_memoria = proceso_actual.tamano_memoria + tamano_memoria
			print("[" + proceso_actual.nombre + "] Salió por E/S")

		if (not procesos_cpu and not lista_procesos):
			sys.exit(0)


def cargar_memoria():
	global procesos_cpu
	global lista_procesos
	global tiempo_procesador
	global tamano_memoria

	while True:
		if lista_procesos:
			current_process = lista_procesos.pop()
		else:
			#print("No hay más procesos")
			break

		if current_process.llegada <= tiempo_procesador:

			if current_process.tamano_memoria <= tamano_memoria:
				print("[" + str(current_process.nombre) + "]: Cargado en Memoria del CPU")
				procesos_cpu.append(current_process)
			else:
				lista_procesos.append(current_process)
				break
		else:
			lista_procesos.append(current_process)
			break

		if not procesos_cpu and lista_procesos:
			tiempo_procesador = tiempo_procesador + 1

	#for proceso in procesos_cpu:
	#	print(proceso.nombre)


def main():

	clear()
	print ('Hola, Vamos a crear los primeros procesos.')
	create_process()

	clear()
	select_plan()




if __name__ == '__main__':
	clear = lambda: os.system('clear')
	lista_procesos = []
	procesos_cpu = []
	tiempo_procesador = 0
	tamano_memoria = 2000

	main()





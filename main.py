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
	tr_init = random.randint(1,2)
	prioridad = random.randint(1,10)
	llegada = random.randint(0,20)
	t_subida = random.randint(0,100)
	ult_t = random.randint(0,10)
	ex = 0

def print_list(lista):
	print("[", end="", flush=True)
	for proceso in lista:
		print(proceso.nombre + ", ", end="", flush=True)
	print("]", end="", flush=True)

def list_all():
	global procesos_cpu
	global lista_procesos
	global tiempo_procesador

	print("LP:", end="", flush=True)
	print_list(lista_procesos)
	print("\t LPC:", end="", flush=True)
	print_list(procesos_cpu)
	print("\t TP:", end="", flush=True)
	print(tiempo_procesador)


def create_process():
	global lista_procesos
	global num_procesos

	num_procesos = 0
	while True:
		'''We create the process that we will work with.'''
		while True:
			try:
				print("Agrega los datos con el siguiente formato")
				print("nombre, tamano_memoria, tiempo_ejecucion, prioridad, llegada")
				data_input = input()
				data = data_input.split(',')
				nuevo_proceso = Process()
				nuevo_proceso.id_n = num_procesos
				nuevo_proceso.nombre = str(data[0])
				nuevo_proceso.tamano_memoria = int(data[1])
				nuevo_proceso.t_rafaga = int(data[2])
				nuevo_proceso.tr_init = int(data[2])
				nuevo_proceso.prioridad = int(data[3])
				nuevo_proceso.llegada = int(data[4])

				lista_procesos.append(nuevo_proceso)
				break
			except (RuntimeError, TypeError, NameError, IndexError, ValueError):
				print("Oops! El proceso no es válido. Vuelve a intentarlo")

		#for process in lista_procesos:
		#	print (process.llegada)

		num_procesos = num_procesos + 1 	#Contador del ID aumenta en 1
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
	global tiempo_respuesta
	global tiempo_ejecucion
	global tiempo_espera

	list_all()

	quantum = 0
	while True:
		print("\n Ingresa el tamaño de tu Quantum.")
		try:
			quantum = int(input())
			break
		except TypeError:
			print("El valor de tu Quantum no es valido.")

	while True:
		cargar_memoria()
		for proceso in procesos_cpu:
			proceso.ult_t = tiempo_procesador

			print("[" + proceso.nombre + "] subió restan: " + str(proceso.t_rafaga))

			if proceso.ex == 0:
				proceso.t_subida = tiempo_procesador
				proceso.ex = 1

			if (proceso.t_rafaga - quantum) <= 0:
				proceso.tr_init = proceso.tr_init - proceso.t_rafaga

			list_all()
			for x in range(quantum):

				if proceso.t_rafaga == 0:
					tamano_memoria = proceso.tamano_memoria + tamano_memoria
					list_all()
					print("\t [" + proceso.nombre + "] Salió por E/S")


					tiempo_ejecucion = tiempo_ejecucion + (tiempo_procesador - proceso.t_subida)
					tiempo_respuesta = tiempo_respuesta + (proceso.t_subida - proceso.llegada)
					tiempo_espera = tiempo_espera + (proceso.ult_t - proceso.tr_init - proceso.llegada)

					index = procesos_cpu.index(proceso)
					del procesos_cpu[index]

					break
				else:
					proceso.t_rafaga = proceso.t_rafaga - 1
					tiempo_procesador = tiempo_procesador + 1

		
		if (not procesos_cpu and not lista_procesos):
			print("Tiempo de Ejecucion: " + str(round(tiempo_ejecucion / num_procesos,2)))
			print("Tiempo de Respuesta: " + str(round(tiempo_respuesta / num_procesos,2)))
			print("Tiempo de Espera: " + str(round(tiempo_espera / num_procesos,2)))
			sys.exit(0)

def prioridad():
	global procesos_cpu
	global lista_procesos
	global tiempo_procesador
	global tamano_memoria
	global tiempo_respuesta
	global tiempo_ejecucion
	global tiempo_espera

	while True:
		cargar_memoria()

		if procesos_cpu:
			procesos_cpu.sort(key=lambda x: x.prioridad)
			proceso = procesos_cpu.pop()

			for x in range(proceso.t_rafaga):
				tiempo_procesador = tiempo_procesador + 1
				proceso.t_rafaga = proceso.t_rafaga - 1

				if proceso.ex == 0:
					proceso.t_subida = tiempo_procesador
					proceso.ex = 1

				print("[" + proceso.nombre + "] subió restan: " + str(proceso.t_rafaga))
			print("[" + proceso.nombre + "] Terminó de Ejecutar")
			tamano_memoria = proceso.tamano_memoria + tamano_memoria

			tiempo_ejecucion = tiempo_ejecucion + (tiempo_procesador - proceso.t_subida)
			tiempo_respuesta = tiempo_respuesta + (proceso.t_subida - proceso.llegada)
			tiempo_espera = tiempo_espera + (proceso.t_subida - proceso.llegada)

			list_all()
			print("\t [" + proceso.nombre + "] Salió por E/S")

		if (not procesos_cpu and not lista_procesos):
			print("Tiempo de Ejecucion: " + str(round(tiempo_ejecucion / num_procesos,2)))
			print("Tiempo de Respuesta: " + str(round(tiempo_respuesta / num_procesos,2)))
			print("Tiempo de Espera: " + str(round(tiempo_espera / num_procesos,2)))

			sys.exit(0)


def cargar_memoria():
	global procesos_cpu
	global lista_procesos
	global tiempo_procesador
	global tamano_memoria
	while True:
		if lista_procesos:
		
			current_process = lista_procesos.pop()
			if current_process.llegada <= tiempo_procesador:

				if current_process.tamano_memoria <= tamano_memoria:
					current_process.t_subida = tiempo_procesador
					procesos_cpu.append(current_process)
					list_all()
					print("\t [" + str(current_process.nombre) + "]: Cargado en Memoria del CPU")
					tamano_memoria = tamano_memoria - current_process.tamano_memoria
				else:
					lista_procesos.append(current_process)
					break
			else:
				lista_procesos.append(current_process)
				break
		else: 
			break

		if not procesos_cpu and lista_procesos:
			tiempo_procesador = tiempo_procesador + 1

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
	tiempo_respuesta = 0
	tiempo_ejecucion = 0
	tiempo_espera = 0
	num_procesos = 0

	main()





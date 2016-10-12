# Planificador Round Robin

El proyecto consta de varias fases:
* Generación de Procesos
* Planificación de Procesos
* Asignación Dinámica de Memoria
* Planificación de CPU

###Generación de procesos

Implementa una interfaz sencilla en consola para la captura de datos de los procesos con los cuales se simulará el planificador.
* Datos de los procesos:
    * Id del proceso (numérico o alfanumérico):Es un identificador del proceso que lo hace único dentro del Sistema Operativo, por lo que no debe duplicarse.
    * Nombre del proceso
    * Tamaño del proceso
    * Tiempo que requiere para su ejecución

Recuerda que los procesos están huecos, con este tiempo simularemos la ejecución de instrucciones en el procesador.
* Prioridad del proceso (numérico)
* Tiempo de llegada del proceso: Es el tiempo en el que se crea el proceso una vez iniciado el simulador.
* Todos los tiempos se simulan en milisegundos
* La cola de procesos listos se implementará con una lista dinámica de nodos.
* Conforme se crean los procesos se van insertando en esta lista y conforme se van planificando se eliminarán de la cola. Por cada cambio (insertar o borrar) que se realice en la estructura cola de procesos listos se imprime su nuevo contenido.

###Planificación de procesos

Se simulan los siguientes algoritmos a los procesos que están en la cola de procesos listos para ser ejecutados
* Round Robín

###Asignación dinámica de memoria

Se cargan los procesos en la memoria hasta que se llene o ya no exista espacio suficiente para almacenar más procesos en estado de listos. Para ello se implementa una cola FIFO de procesos listos para ejecución. Los procesos almacenados en esta cola son los que subirán a la CPU.

###Salida a pantalla:
Por cada cambio que exista en esta lista deberá de imprimir su contenido (cada vez que se inserte o borre un proceso se deberá de imprimir la lista).

Cada vez que se libere espacio en memoria se deberá de imprimir el total de espacio disponible.

###Planificación de CPU

Se toma el primer proceso de la cola de procesos listos para ejecución y se le asigna una CPU.

###Resultados finales
Calcular los tiempos promedio de:
* Espera
* Ejecución
* Respuesta

## Requisitos
Para poder correr el programa es necesario que instales python3.x en tu sistema. Para hacer esto es recomendable que descargues el programa de la [página oficial](python.org) de Python.

## Uso
Una vez que tengamos instalado Python3, solo será necesario que ejecutemos el archivo main del programa utilizando el siguiente comando:

```sh
python3 main.py
```
## Soporte

Puedes abrir un 'issue' en esta [página](https://github.com/juanpflores/OS_Proyecto1/issues/new) en caso de que tengas algún problema con el programa.

## Contribuir

Para contribuir al proyecto es necesario que sigas las reglas de [Github Flow](https://guides.github.com/introduction/flow/). Crea una rama nueva, agrega tus cambios y abre un [pull request](https://github.com/juanpflores/OS_Proyecto1/pulls).


# Manual Tecnico

## Desarrollo del sistema para la clinica veterinaria

<br/><br/><br/>
<br/><br/><br/>


## Presentado por:

* Jean Carlos Santacruz Arredondo
* Juan Miguel Rojas Mejia





<br/><br/><br/>
<br/><br/><br/>





## Universidad Pontificia Javeriana Cali
## Departamento de Ingerieria
## Ingeniria De Sistemas Y Computación
## 2022

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>
  
# Contenido

* Presentación
* Objetivo
* Procesos
* Requisitos del sistema
* Herramientas utilizadas para el desarrollo
* Diagrama UML
* Casos de uso
* Principales funcionalidades
* Entradas y Salidas
      
  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>       
        
## Presentación

* El siguiente manual tecnico guiara a los usuarios que haran soporte a el sistema de gestion de evaluador de acta, el cual les informara los requerimientos y la estructura que se utilizaron para la contruccion de este sistema, el desarrollo de este programa de escritorio el cual muestra las herramientas necesarios para la contrucción y funcionalidad del sistema.

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>       

## Objetivo

* Realizar administración y procesamiento de la calificación de actas.

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>       

## Procesos

#### Procesos de entrada.

#### Procesos de salida.

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/> 
  
  
## Requisitos del sistema

* Requisitos de hardware

Equipo, teclado, mouse, monitor

Memoria RAM 8 Gb

Peocesador 1.5 GHz en adelante

* Requisitos de software

Sistema operativo (Windows 7 en adelante)

MinGW

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/> 

## Herramientas utilizadas para el desarrollo

### Python

Python es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. A diferencia de otros lenguajes como Java o .NET, se trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador utilizando un programa denominado interpretador, por lo que no es necesario “traducirlo” a lenguaje máquina. 

### Pycharm

PyCharm proporciona una finalización del código inteligente, inspecciones del código, indicación de errores sobre la marcha y arreglos rápidos, así como refactorización de código automática y completas funcionalidades de navegación.

### Requeriments

Por favor instalar los requeriments.txt para el correcto funcionamiento.



  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/> 
  
## Diagrama UML


![](https://github.com/JuanRx19/ClinicaVeterinaria/blob/main/ClinicaVeterinariUML.drawio.png?raw=true)



  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>
  
## Casos de uso
<br/><br/><br/>

| Caso de uso:  | Registrar Cliente |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   |el administrador registra y almacena el nombre completo, email, documento de identidad y teléfono de cada propietario responsable |

<br/><br/><br/>

| Caso de uso:  | Registrar mascota |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   |el administrador registra y almacena la información de cada mascota. Esta información consiste en la raza, el tipo: perro  gato  otro, el peso, la edad, tipo de sangre, el nombre, la identificación, status: viva muerta. Si la mascota ha fallecido también registra la fecha de defunción. |
  
<br/><br/><br/>


 | Caso de uso:  | asignar mascota |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador asigna mascota a los clientes | 

<br/><br/><br/>


 | Caso de uso:  | verificar clientes |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador verifica cuantos propietarios se encuentran registrados en el directorio | 

<br/><br/><br/>


 | Caso de uso:  | listar informacion clientes |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador puede listar la informacion disponible de cada cliente |


<br/><br/><br/>


 | Caso de uso:  | listar mascotas |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador puede listar la informacion de cada mascota incluyendo los datos de su dueño |

<br/><br/><br/>


 | Caso de uso:  | asignar propietario |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador puede asignar mascota a nuevos cleintes inscritos en el sistema | 

<br/><br/><br/>


 | Caso de uso:  | cambiar status mascota |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador asigna el starus que se encuentra la mascota ( viva o muerta |

<br/><br/><br/>


 | Caso de uso:  | eliminar propietario |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador podra eliminar propietarios de las mascotas | 
 
 
<br/><br/><br/>
<br/><br/><br/>
<br/><br/><br/>
 
## Principales funcionalidades
<br/><br/><br/>  

* Registrar cliente.

El sistema podra registar cliente a la base de el programa donde almacenara los datos principales de este como nombre completo , documento de identificacion, email y telefono de contacto.

* Registrar mascota

El sistema podra registrar mascotas a la base de el programa donde registrara y almacenara la informacion de cada mascota Esta información consiste en la raza, el tipo: perro gato otro, el peso, la edad, tipo de sangre, el nombre, la identificación, status: viva muerta. Si la mascota ha fallecido también registra la fecha de defunción.

* Asignar mascotas

El sistema podra asignar mascotas a los clientes que quedan con estado de propietario de dicha mascota para poder asociarlos entre si.

* Verificar clientes

El sistema podra verificar la informacion del sistema y cuantos hay en ese momento registrados dentro del programa.

* informacion de los clientes

El sistema podra listar la informacion disponible de cada cliente y modificar cada una de ellas.

* Verificar mascotas

El sistema podra listar la informacion disponible de cada mascota y modificar cada una de ellas.

* Asignar propietario

El sistema podra asignar un nuevo propietario a una mascota tanto como eliminar este mismo de otra mascota.

* Cambiar status de la mascota.
El sistema podra cambiar el status a las mascotas dandole dos tipos de esta (VIVA O MUERTA)




<br/><br/><br/>
<br/><br/><br/>
<br/><br/><br/>


## Métodos, Entradas y Salidas
<br/><br/><br/>

* Mascota.
 
Entradas:
* nombre
* tipo de sangre
* tipo de animal
* raza
* peso
* edad
* identificación
* status


Salidas:
* nombre
* tipo de sangre
* tipo de animal
* raza
* peso
* edad
* identificación
* status


*  Cliente.

Entrada:
* nombre
* identificación
* telefono
* email

Salida:
* nombre
* identificación
* telefono
* email

* Status.

Entrada:
* estado
* fecha de defunció

Salida:
* estado
* fecha de defunció

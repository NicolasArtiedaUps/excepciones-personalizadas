# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class errores(Exception):
    pass
class errordim(Exception):
    pass
class errorEncendido(Exception):
    pass
class Actuador:
    def __init__(self):
        self.listaId=[]
        self.listaTipo=[]
    def agregarID(self,valor):
        self.listaId.append(valor)
    def agregarTipo(self,valor):
        self.listaTipo.append(valor)
    def encender(self):
        print("EL ACTUADOR SE HA ENCENDIDO ")
    def mostrarIDYTIPO(self):
        for i in range(len(self.listaId)):
            print("ID: ",self.listaId[i]," TIPO: ",self.listaTipo[i])
           

actuador=Actuador()
print("bienvenido ")
try:    
    dim=int(input("ingrese el numero de actuadores "))
    while dim>3:
        raise errordim("advertencia solo se permite 3 actuadores ")
        
except errordim as e2:
    print(e2)
    dim=int(input("ingrese el numero de actuadores "))
    
for i in range(0,dim):
    try:
        
        ID=int(input("ingrese el id del actuador "))
        tipo=input("ingrese el tipo de actuador ")
        while tipo.isnumeric():
            raise errores("Advertencia el tipo no puede ser un numero ")
        
    except errores as e:
        print(e)
        tipo=input("ingrese denuevo el actuador ")
 
    actuador.agregarID(ID)
    actuador.agregarTipo(tipo)
actuador.mostrarIDYTIPO()

    
try: 
    buscarId=int(input("ingrese el id a encender "))
    for i in range(0,dim):
        if buscarId==actuador.listaId[i]:
            actuador.encender()
            break
        else:
            raise errorEncendido("El id ingresado no esta registrado")
except errorEncendido as e3:
    print(e3)
    buscarId=(int(input("ingresa un id en rango ")))
    actuador.encender()



    
        
        
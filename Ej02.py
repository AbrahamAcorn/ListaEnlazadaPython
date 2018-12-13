class Nodos:
        
    '''Constructores'''
    def __init__(self, dato):
        self.dato = dato
        self.enlace = None
    
    '''Getters And Setters'''
    def getDato(self):
        return self.dato
    def setDato(self, dato):
        self.dato = dato
    
    def getEnlace(self):
        return self.enlace
    def setEnlace(self, enlace):
        self.enlace = enlace
    

#=================================================================================================================================================

class Temperatura:
    
    '''Constructores'''
    def __init__(self, teperatura, fechaR):
        self.teperatura = teperatura
        self.fechaR = fechaR
    
    '''Getters and Setters'''
    def getTeperatura(self):
        return self.teperatura
    def setTeperatura(self, teperatura):
        self.teperatura = teperatura
    
    def getFechaR(self):
        return self.fechaR
    def setFechaR(self, fechaR):
        self.fechaR = fechaR;
    
    
    #Otros metodos
   
    def toString(self):
        return self.teperatura+" ------ "+self.fechaR
    

#=================================================================================================================================================

class ListasEnlazadas:
    tem = None
    
    '''Constructores'''

    '''Otros metodos'''
    def __init__(self):
        self.nodoInicial = self.nodoFinal = None
        self.contador = 0
        print("La lista se ha creado correctamente.")
    
    '''Insertar temperatura al inicio'''
    def insertarNodoAlInicioO(self):
        
        temp = raw_input("Ingrese la temperatura: ")
        fecha = raw_input("Ingrese la fecha de registro (dd/mm/aaaa): ")
        
        tem = Temperatura(temp, fecha)
        
        nuevoNodo = Nodos(tem)
        
        if(self.nodoInicial == None):
            self.nodoInicial = self.nodoFinal = nuevoNodo
            self.contador = self.contador + 1
            print("La temperatura se ha insertado correctamente")
        else:
            nuevoNodo.setEnlace(self.nodoInicial)
            self.nodoInicial = nuevoNodo
            self.contador = self.contador + 1
            print("La temperatura se ha insertado correctamente")
    
    '''Insertar temperatura al final'''
    def insertarNodoAlFinalO(self): 
        
        temp = raw_input("Ingrese la temperatura: ")
        fecha = raw_input("Ingrese la fecha de registro (dd/mm/aaaa): ")
        
        tem = Temperatura(temp, fecha)
        
        nuevoNodo = Nodos(tem)
        if (self.nodoFinal == None):
            self.nodoFinal = self.nodoInicial = Nodos(tem)
            self.contador = self.contador +1
            print("La temperatura se ha insertado correctamente")
        else:
            self.nodoFinal.setEnlace(nuevoNodo)
            self.nodoFinal = nuevoNodo
            self.contador = self.contador +1
            print("La temperatura se ha insertado correctamente")
        
    '''Eliminar temperatura al inicio'''
    def eliminarNodoAlInicioO(self):
        
        if(self.nodoInicial != None):
            self.nodoInicial = self.nodoInicial.getEnlace()
            self.contador = self.contador - 1
            print("Se ha borrado la temperatura inicial correctamente.")
        else:
            print("No hay nodos para borrar.")
    
    '''Eliminar temperatura al final'''
    def eliminarNodoAlFinalO(self):
        
        if(self.verificarListaVaciaO()):
            print("No hay nodos para borrar.")
        else:
            nuevoNodo = self.nodoInicial
            while(nuevoNodo.getEnlace() != None): 
                otroNodo = nuevoNodo 
                nuevoNodo = nuevoNodo.getEnlace() 
        
            otroNodo.setEnlace(None) 
            self.nodoFinal = otroNodo 
            self.contador = self.contador - 1
            print("Se ha borrado la temperatura final correctamente")

    '''Verificar lista vacia'''
    def verificarListaVaciaO(self):
        if(self.nodoInicial == None and self.nodoFinal == None ):
            print("La lista esta vacia.")
        else:
            print("La lista no esta vacia.")
        
    '''Mostrar temperaturas'''
    def mostrarElementosO(self):
        nodoActual = self.nodoInicial
        while(nodoActual != None):
            print("["+nodoActual.getDato().toString()+"]-->")
            nodoActual = nodoActual.getEnlace()
     
#=================================================================================================================================================
obj = ListasEnlazadas()
 
opcion=0
while(opcion != 7):               
    print"             M E N U"
    print "1) Crear Lista."
    print "2) Verificar Lista vacia."
    print "3) Insertar elemento."
    print "4) Eliminar elemento."
    print "5) Promedio de temperaturas."
    print "6) Mostrar temperaturas."
    print "7) Salir."
    print
    opcion = int(raw_input("Elija una opcion: "))
       
    if(opcion <= 0 or opcion > 7):
        print("Opcion no valida")
    elif(opcion == 1):
        print("Lista creada.")
    elif(opcion == 2):
        if(obj.verificarListaVaciaO() == True):
            print "La lista no contiene elementos"
        else:     
            obj.mostrarElementosO()
    elif(opcion == 3):
        print "        I N S E R T A R"
        print "1) Inicio"
        print "2) Final"
        print
        op = int(raw_input("Elija una opcion: "))
        if(op == 1):
            obj.insertarNodoAlInicioO()
        elif( op == 2):
            obj.insertarNodoAlFinalO()
        else:
            print "Opcion invalida"
    elif(opcion == 4):
        print "*        E L I M I N A R"
        print "1) Inicio"
        print "2) Final"
        print
        op=int(raw_input("Elija una opcion: "))
        if(op == 1):
            obj.eliminarNodoAlInicioO()
        elif(op == 2):
            obj.eliminarNodoAlFinalO()
        else:
            print "Opcion incorrecta."
    elif(opcion == 5):
        print("promedio")
    elif(opcion == 6):
        obj.mostrarElementosO()






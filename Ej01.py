
class Nodo:
    
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

class ListaEnlazada:
    
    '''Constructores'''
    def __init__(self):
        self.nodoInicial = None
        self.nodoFinal = None
        self.contador = 0
       
    '''Insertar temperatura al inicio'''   
    def insertarNodoAlInicio(self, dato):
       
        nuevoNodo = Nodo(dato)
        
        if(self.nodoInicial == None):
            self.nodoInicial = self.nodoFinal = nuevoNodo
            self.contador = self.contador + 1
            print("La temperatura se ha insertado correctamente")
        else:
            nuevoNodo.setEnlace(self.nodoInicial)
            self.nodoInicial = nuevoNodo
            self.contador = self.contador +1
            print("La temperatura se ha insertado correctamente")

    '''Insertar temperatura al final'''
    def insertarNodoAlFinal(self, dato):
        nuevoNodo =  Nodo(dato)
        
        if (self.nodoFinal == None):
            self.nodoFinal = self.nodoInicial = nuevoNodo
            self.contador = self.contador +1
            print("La temperatura se ha insertado correctamente")
        else:
            self.nodoFinal.setEnlace(nuevoNodo)
            self.nodoFinal = nuevoNodo
            self.contador = self.contador + 1
            print("La temperatura se ha insertado correctamente")
                  
    '''Eliminar temperatura al inicio'''
    def eliminarNodoAlInicio(self):
        
        if(self.nodoInicial != None):
            self.nodoInicial = self.nodoInicial.getEnlace();
            self.contador = self.contador - 1
            print("Se ha borrado la temperatura inicial correctamente.")
        else:
            print("No hay nodos para borrar.")
    
        '''
        if(self.verificarListavacia() == True):
            print("Lista vacia")
        elif(self.nodoInicial == self.nodoFinal):
            self.nodoInicial = None
            self.nodoFinal = None
            print("Elemento eliminado")
        else:
            temp = self.nodoInicial
            self.nodoInicial = self.nodoInicial.getEnlace()
            temp = None
            print("Elemento Eliminado")
        '''   
            
    '''Eliminar temperatura al final'''
    def eliminarNodoAlFinal(self):
        
        if(self.verificarListaVacia()):
            print("No hay nodos para borrar.")
        else:
            nuevoNodo = self.nodoInicial
            while(nuevoNodo.getEnlace() != None): 
                otroNodo = nuevoNodo
                nuevoNodo = nuevoNodo.getEnlace()
    
            otroNodo.setEnlace(None) 
            self.nodoFinal = otroNodo
            self.contador = self.contador -1
            print("Se ha borrado la temperatura final correctamente")
        
    '''Verificar lista vacia'''
    def verificarListaVacia(self):
        if(self.nodoInicial == None and self.nodoFinal == None ):
            print("La lista esta vacia.")
        else:
            print("La lista no esta vacia.")
        
    '''Mostrar temperaturas'''
    def mostrarElementos(self):
        nodoActual = self.nodoInicial
        
        while(nodoActual != None):
            print( "["+str(nodoActual.getDato())+"]--> ")
            nodoActual = nodoActual.getEnlace()
    
    '''Mostrar Promedio temperaturas'''
    def mostrarPromedio(self):
        #nuevoNodo = Nodo()
        #otroNodo = Nodo()
        nuevoNodo = self.nodoInicial
        promedio = self.nodoInicial.getDato() 
        
        for i in range(0, self.contador):
            while(nuevoNodo.getEnlace() != None):
                otroNodo = nuevoNodo
                nuevoNodo = nuevoNodo.getEnlace() 
                promedio = promedio + nuevoNodo.getDato()
             
            
        
        promedio = promedio / self.contador
        print("El promedio de las temperaturas es "+str(promedio)+" centigrados")
        
        if(promedio >= 0 and promedio <= 10):
            print(str(promedio)+" --> Congelacion.")
        elif(promedio >= 11 and promedio <= 20):
            print(str(promedio)+" --> Frio.")
        elif(promedio >= 21 and promedio <= 30):
            print(str(promedio)+" --> Normal.")
        elif(promedio >= 31):
            print(str(promedio)+" --> Alta.")
        
#=================================================================================================================================================


le = ListaEnlazada()
 
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
        if(le.verificarListaVacia() == True):
            print "La lista no contiene elementos"
        else:     
            le.mostrarElementos()
    elif(opcion == 3):
        print "        I N S E R T A R"
        print "1) Inicio"
        print "2) Final"
        print
        op = int(raw_input("Elija una opcion: "))
        if(op == 1):
            numero = int(raw_input("Ingrese numero: "))
            le.insertarNodoAlInicio(numero)
        elif( op == 2):
            numero = int(raw_input("Ingrese numero: "))
            le.insertarNodoAlFinal(numero)
        else:
            print "Opcion invalida"
    elif(opcion == 4):
        print "*        E L I M I N A R"
        print "1) Inicio"
        print "2) Final"
        print
        op=int(raw_input("Elija una opcion: "))
        if(op == 1):
            le.eliminarNodoAlInicio()
        elif(op == 2):
            le.eliminarNodoAlFinal()
        else:
            print "Opcion incorrecta."
    elif(opcion == 5):
        le.mostrarPromedio()
    elif(opcion == 6):
        le.mostrarElementos()

class Vehiculo():
    def __init__(self, patente, marca, anio, p_desp=0):
        self.patente=self.validar_str(patente)
        self.marca=self.validar_str(marca)
        self.anio = self.validar_int(anio)
        self.p_desp = self.validar_int(p_desp)
        
    def validar_str(self,cadena):
            if not isinstance(cadena,str):
                raise TypeError('Debe ser un string')
            if len(cadena)==0:
                raise ValueError('La cadena no debe estar vacia')
            else:
                return cadena
                 
    def validar_int(self,numero):   
        if not isinstance(numero,int):
            raise TypeError('Debe ser un numero')
        elif numero is None:
            raise ValueError('No debe estar vacia')
        else:
            return numero

    def __str__(self):
            return f"Vehiculo: #{self.patente} \nMarca: {self.marca} \nAnio: {self.anio}"

    def get_patente(self):
        return self.patente

    def get_marca(self):
        return self.marca

    def get_anio(self):
        return self.anio
    
    def trasladarse(self, desplazamiento): 
        desplazamiento=self.validar_int(desplazamiento)
        if desplazamiento<=0 or desplazamiento==None:
            raise ValueError('El desplazamiento debe ser mayor a 0')
        else:
           self.p_desp+= desplazamiento
           return 'Se desplazó con éxito'
        
class Terrestre(Vehiculo):
    marcas_disp=['volskwagen','fiat','bmw']
    reg_terrestre={}
    def __init__(self, patente, marca, anio, ruedas, p_desp):
        super().__init__(patente, marca, anio, p_desp)
        self.validar_patente(patente)
        self.validar_marca(marca)
        self.ruedas= self.validar_int(ruedas)
        
    def validar_patente(self,patente):
        patente= self.validar_str(patente)
        patente=patente.strip().upper()
        if len(patente)!=7:
            raise ValueError('La patente debe estar conformada por dos letras, tres numeros y luego dos letras')
        if patente in Terrestre.reg_terrestre: #raiseo un error si la patente ya fue usada
                raise ValueError(f"La patente {patente} ya está registrada.")
        else:
            self.patente=patente
            #despues de crear la instancia, uso registrar patente
    
    
    def validar_marca(self,marca):
        marca=self.validar_str(marca)
        marca=marca.lower()
        if marca not in Terrestre.marcas_disp:
            raise ValueError('La marca no esta dentro de las disponibles')
        else:
            self.marca=marca
            
    def trasladarse_terr(self, desplazamiento):
        mensaje=self.trasladarse(desplazamiento)
        mensaje+=f' {desplazamiento} posiciones por tierra'
        return mensaje
        
    def __str__(self):
            mensaje=super().__str__(self)
            mensaje+=f"Ruedas: {self.ruedas} \nPosicion: {self.p_disp}"
            return mensaje
    
    def render_terrestres():
        for obj in Terrestre.reg_terrestre.values():
            print(f"{obj.patente} {obj.marca} {obj.anio} {obj.ruedas} {obj.p_desp}")
            
class Maritimo(Vehiculo):
    marcas_disp=[ 'sea ray', 'boston whaler', 'beneteau']
    reg_maritimo={}
    def __init__(self, patente, marca, anio, p_desp):
        super().__init__(patente, marca, anio, p_desp)
        self.validar_patente(patente)
        self.validar_marca(marca)
        
    def validar_patente(self,patente):
        patente= self.validar_str(patente)
        patente=patente.strip().upper()
        if len(patente)!=7:
            raise ValueError('La patente debe estar conformada por dos letras, tres numeros y luego dos letras')
        if patente in Maritimo.reg_maritimo: #raiseo un error si la patente ya fue usada
                raise ValueError(f"La patente {patente} ya está registrada.")
        else:
            self.patente=patente
            #despues de crear la instancia, uso registrar patente
    
    
    def validar_marca(self,marca):
        marca=self.validar_str(marca)
        marca=marca.lower()
        if marca not in Maritimo.marcas_disp:
            raise ValueError('La marca no esta dentro de las disponibles')
        else:
            self.marca=marca
            
    def trasladarse_mar(self, desplazamiento):
        mensaje=self.trasladarse(desplazamiento)
        mensaje+=f' {desplazamiento} posiciones por agua'
        return mensaje
        
    def __str__(self):
            mensaje=super().__str__(self)
            mensaje+=f" \nPosicion: {self.p_disp}"
            return mensaje
        
        
        
        
        
if __name__ == "__main__":
    try:
        c1=Terrestre('ab131cd','fiat', 2003, 4, 2)
        Terrestre.reg_terrestre[c1.patente]=c1
        print('Camion c1 creado con exito')            
        
        c2=Terrestre('ab131cd','fiat', 2003, 4, 2)
        Terrestre.reg_terrestre[c2.patente]=c2
        print('Camion c1 creado con exito') 
    except TypeError as e:
        print('El error es: ', e)
        '''sacar todos los errores e imprimirlos, y dsp exception'''
    except ValueError as e:
        print('El error es: ', e)
    except Exception as e:
        print('El error es: ', e)
    
    print(Terrestre.trasladarse_terr(c1, 3))
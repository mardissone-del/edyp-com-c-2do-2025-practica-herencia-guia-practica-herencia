from VehiculoTM import Terrestre


class Camion(Terrestre):
    def __init__(self, patente, marca, anio, ruedas, p_desp, carga):
        super().__init__(patente, marca, anio, ruedas, p_desp)
        self.carga= self.validar_int(carga)
        self.validar_ruedas(ruedas)
        
    def validar_ruedas(self,ruedas):
        if ruedas!=8:
            raise ValueError('El camion debe tener 8 ruedas')
        else:
            self.ruedas=ruedas
        

class Auto(Terrestre):
    def __init__(self, patente, marca, anio, ruedas, p_desp):
        super().__init__(patente, marca, anio, ruedas, p_desp)
        self.validar_ruedas(ruedas)
        
    def validar_ruedas(self,ruedas):
        if ruedas!=4:
            raise ValueError('El camion debe tener 8 ruedas')
        else:
            self.ruedas=ruedas

if __name__ == "__main__":
    #registar camiones
    try:
        c1=Camion('aa131cd','fiat',2003, 8, 3,400)
        Terrestre.reg_terrestre[c1.patente]=c1
        print('Camion c1 creado con exito')
        
        c2=Camion('aa131cd','Bmw', 2003, 8, 3,400)
        Terrestre.reg_terrestre[c2.patente]=c2
        print('Camion c2 creado con exito')
        
        c3=Camion('as131cd','volskwagen', 2003, 8, 3,400)
        Terrestre.reg_terrestre[c3.patente]=c3
        print('Camion c3 creado con exito')
        
        c4=Camion('aa131dd','Bmw', 2003, 8, 3,400)
        Terrestre.reg_terrestre[c4.patente]=c4
        print('Camion c4 creado con exito')
        
        Terrestre.render_terrestres()
        
    except TypeError as e:
        print('El error es: ', e)
        '''sacar todos los errores e imprimirlos, y dsp exception'''
    except ValueError as e:
        print('El error es: ', e)
    except Exception as e:
        print('El error es: ', e)
    
      

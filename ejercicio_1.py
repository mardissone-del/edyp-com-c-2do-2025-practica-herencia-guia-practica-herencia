
    

class Auto(Vehiculo):
    def __init__(self,patente, marca, anio, ruedas=4):
        super().__init__(patente, marca, carga=None, anio=anio) #solo los que uso
        self.patente=patente
        self.marca=marca
        self.ruedas= Camion.validar_int(ruedas)
        self.anio =anio
            
if __name__ == "__main__":
    #registar camiones
    try:
        c1=Auto('ab131cd','fiat',2003,4)
        Camion.patentes_usadas[c1.patente]=c1
        print('Auto c1 creado con exito')
        
        
    except TypeError as e:
        print('El error es: ', e)
        '''sacar todos los errores e imprimirlos, y dsp exception'''
    except ValueError as e:
        print('El error es: ', e)
    except Exception as e:
        print('El error es: ', e)
                    
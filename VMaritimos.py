from VehiculoTM import Maritimo

class Lancha(Maritimo):
    marcas_motor_disp=[ 'sea ray', 'boston whaler', 'beneteau']
    def __init__(self, patente, marca, anio, p_desp, marca_motor):
        super().__init__(patente, marca, anio, p_desp)
        self.validar_marca_motor(marca_motor)
    
        
    def validar_marca_motor(self,marca_motor):
        marca_motor=self.validar_str(marca_motor)
        if marca_motor not in Lancha.marcas_motor_disp:
            raise ValueError('La marca no se encuentra dentro de las disponibles')
        else:
             self.marca_motor=marca_motor
        

class Velero(Maritimo):
    def __init__(self, patente, marca, anio, p_desp, cant_velas):
        super().__init__(patente, marca, anio, p_desp)
        self.cant_velas=self.validar_int(cant_velas)
        


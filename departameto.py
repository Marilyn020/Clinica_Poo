class Departamento:
    def __init__(self, Id_Departamento:int, Nombre:str, piso:int):
        self.Id_Departamento = Id_Departamento
        self.Nombre = Nombre
        self.Piso = piso

    @property
    def Id_Departamento(self)-> int:
        return self._Id_Departamento
    
    @Id_Departamento.setter
    def Id_Departamento(self,Id_Departamento:int)-> None:
        self._Id_Departamento = Id_Departamento
    
    @property
    def Nombre(self)-> str:
        return self._Nombre
    
    @Nombre.setter
    def Nombre(self, Nombre:str)-> None:
        self._Nombre = Nombre
    
    @property
    def Piso(self)-> int:
        return self._Piso
    
    @Piso.setter
    def Piso(self, Piso:int)-> None:
        self._Piso = Piso
    
    def __str__(self)-> str:
        return f"Información del departamento:\nID: {self.Id_Departamento}\nNombre: {self.Nombre}\nPiso: {self.Piso}"

    def __repr__(self)-> str:
        return f"Departamento(Id_Departamento={self.Id_Departamento}, Nombre='{self.Nombre}', Piso={self.Piso})"

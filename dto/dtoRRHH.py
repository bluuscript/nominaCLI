import sys
sys.path.append(".")
from modelo.personal import *
from dao.daoRRHH import daoRRHH

class dtoRRHH:

    def agregarPersonalNomina(self,
                        personalNombre, personalRut, personalGenero, personalDireccion, 
                        telefonoPersonalNumeros,
                        cargoNombre, cargoFechaIngreso,
                        areaNombre, departamentoNombre,
                        cargaNombre, cargaParentesco, cargaGenero, cargaRut,
                        contactoNombre, contactoRelacionPersonal, telefonoContactoNumeros
                        ):
        
        resultado_agregar = daoRRHH().addPersonal(Personal(personalNombre=personalNombre, personalRut=personalRut, personalGenero=personalGenero, personalDireccion=personalDireccion,
                                    telefonoPersonalNumeros=telefonoPersonalNumeros, cargoNombre=cargoNombre, cargoFechaIngreso=cargoFechaIngreso,
                                    areaNombre=areaNombre,departamentoNombre=departamentoNombre,
                                    contactoNombre=contactoNombre, contactoRelacionPersonal=contactoRelacionPersonal,telefonoContactoNumeros=telefonoContactoNumeros,
                                    cargaNombre=cargaNombre, cargaParentesco=cargaParentesco, cargaGenero=cargaGenero, cargaRut=cargaRut))
        return resultado_agregar if resultado_agregar is not None else None

    def registrosNomina(self):
        registros = daoRRHH().getRegistros()
        lista_registros=[]
        if registros is not None:
            for registro in registros:
                registro_personal=Personal(
                    personalRut=registro[0], personalNombre=registro[1],
                    personalGenero=registro[2], cargoNombre=registro[3]
                    )
                lista_registros.append(registro_personal)
        return lista_registros if lista_registros is not None else None
    
    def buscarRegistro(self, personalRut):
        
        resultado = daoRRHH().getOneRegistro(Personal=Personal(personalRut=personalRut))
        
        return Personal(
                personalRut=resultado[0], personalNombre=resultado[1],personalGenero=resultado[2],
                cargoNombre=resultado[3]
            ) if resultado is not None else None
    
    def modificarPersonal(self, personalRut, personalNombre, personalGenero, personalDireccion, telefonoPersonalNumero, cargoNombre, cargoFechaIngreso, areaNombre,
                    departamentoNombre, contactoNombre, contactoRelacionPersonal, telefonoContactoNumeros, cargaNombre, cargaParentesco, cargaGenero, cargaRut):
        
        resultado_modificar = daoRRHH().updatePersonal(Personal(personalNombre=personalNombre, personalRut=personalRut, personalGenero=personalGenero, personalDireccion=personalDireccion,\
                                        telefonoPersonalNumero=telefonoPersonalNumero, cargoNombre=cargoNombre, cargoFechaIngreso=cargoFechaIngreso, areaNombre=areaNombre, departamentoNombre=departamentoNombre,\
                                        contactoNombre=contactoNombre, contactoRelacionPersonal=contactoRelacionPersonal, telefonoContactoNumeros=telefonoContactoNumeros,
                                        cargaNombre=cargaNombre, cargaParentesco=cargaParentesco, cargaGenero=cargaGenero, cargaRut=cargaRut))
        return resultado_modificar if resultado_modificar is not None else None
    
    def eliminarPersonal(self, personalRut):
        
        resultado_eliminar = daoRRHH().deletePersonal(Personal=Personal(personalRut=personalRut))
        return resultado_eliminar if resultado_eliminar is not None else None 
            
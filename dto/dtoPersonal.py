import sys
sys.path.append(".")
from modelo.personal import Personal, TelefonosPersonal, Cargo, Departamento, Area, CargasFamiliares, ContactosEmergencia, TelefonosContacto
from dao.daoPersonal import daoPersonal

class dtoPersonal:
    
    def miRegistro(self, personalRut):
        # Obtener Registro mediante class daoPersonal()
        registro = daoPersonal().getMiRegistro(Personal=Personal(personalRut=personalRut))
        
        personal = Personal(
            personalRut=registro[0][0],
            personalNombre=registro[0][1],
            personalGenero=registro[0][2],
            personalDireccion=registro[0][3]
        ).datosPersonales()
        
        telefonosPersonal = []
        for telefono in registro[1]:
            telefonosPersonal.append(
                    TelefonosPersonal(telefonoPersonalNumeros=telefono[0])
                )
        
        cargasPersonal = []
        for carga in registro[2]:
            cargasPersonal.append(
                CargasFamiliares(
                    cargaRut=carga[0],
                    cargaNombre=carga[1],
                    cargaGenero=carga[2],
                    cargaParentesco=carga[3]
                )
            )
        contactosEmergencia = []
        for contacto in registro[3]:
            contactosEmergencia.append(
                ContactosEmergencia(
                    contactoNombre=contacto[0],
                    contactoRelacionPersonal=contacto[1]
                )
            )
        cargo = Cargo(
            cargoNombre=registro[0][4],
            cargoFechaIngreso=registro[0][5]
        )
        departamento = Departamento(
            departamentoNombre=registro[0][6]
        )
        
        area = Area (
            areaNombre=registro[0][7]
        )
        
        datos_laborales = {
            "Cargo": cargo,
            "Departamento": departamento,
            "Area": area
        }
        
        return personal, datos_laborales, telefonosPersonal, cargasPersonal, contactosEmergencia if registro is not None else None
    
    def modificarMiRegistro(self, personaRut, personalNombre, personalGenero, personalDireccion, telefonoPersonalNumero,
            contactoNombre, contactoRelacionPersonal, telefonoContactoNumeros, cargaRut, cargaNombre, cargaParentesco, cargaGenero):
        resultado = daoPersonal().modificarMiRegistro(
            Personal=Personal(
                personalRut=personaRut, personalNombre=personalNombre, personalGenero=personalGenero,
                personalDireccion=personalDireccion, telefonoPersonalNumero=telefonoPersonalNumero,
                contactoNombre=contactoNombre, contactoRelacionPersonal=contactoRelacionPersonal, telefonoContactoNumeros=telefonoContactoNumeros,
                cargaRut=cargaRut, cargaNombre=cargaNombre, cargaParentesco=cargaParentesco, cargaGenero=cargaGenero
            )
        )
        return resultado if resultado is not None else None
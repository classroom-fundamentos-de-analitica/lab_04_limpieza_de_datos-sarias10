"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    

    
    # Inserte su código aquí
    def limpiar_genero(datos):
        datos = datos.copy()
        datos.sexo = datos.sexo.str.lower()
        return datos

    def limpiar_tipo_negocio(datos):
        datos = datos.copy()
        datos["tipo_de_emprendimiento"] = datos["tipo_de_emprendimiento"].str.lower()
        return datos
    
    def limpiar_zona(datos):
        datos = datos.copy()
        datos["barrio"] = datos["barrio"].str.lower()
        return datos
    
    def limpiar_concepto(datos):
        datos = datos.copy()
        datos["idea_negocio"] = datos["idea_negocio"].str.lower().str.strip()
        return datos
    
    def limpiar_linea_credito(datos):
        datos = datos.copy()
        datos["línea_credito"] = datos["línea_credito"].str.lower().str.strip()
        return datos

    def limpiar_comunidad(datos):
        datos = datos.copy()
        datos["comuna_ciudadano"] = datos["comuna_ciudadano"].astype(int)
        return datos
    
    def limpiar_fecha_beneficio(datos):
        datos = datos.copy()
        datos["fecha_de_beneficio"] = pd.to_datetime(
        datos.fecha_de_beneficio, format="%d/%m/%Y", errors="coerce"
        ).fillna(pd.to_datetime(datos.fecha_de_beneficio, format="%Y/%m/%d", errors="coerce"))
        return datos
    
    def limpiar_cantidad_credito(datos):
        datos = datos.copy()
        datos.monto_del_credito = datos.monto_del_credito.str.rstrip()
        datos.monto_del_credito = datos.monto_del_credito.replace("[,$]", "", regex=True)
        datos.monto_del_credito = datos.monto_del_credito.replace("(\\.00$)", "", regex=True)
        datos.monto_del_credito = datos.monto_del_credito.astype(float)
        return datos
    
    datos = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    datos = datos.replace("-", " ", regex=True).replace("_", " ", regex=True)
    datos["sexo"] = datos["sexo"].str.lower()
    datos = limpiar_tipo_negocio(datos)
    datos = limpiar_zona(datos)
    datos = limpiar_concepto(datos)
    datos = limpiar_linea_credito(datos)
    datos = limpiar_comunidad(datos)
    datos = limpiar_fecha_beneficio(datos)
    datos = limpiar_cantidad_credito(datos)
    datos = datos.drop_duplicates().dropna()
    return datos

print(clean_data().sexo.value_counts().to_list())
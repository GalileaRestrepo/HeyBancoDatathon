import pandas as pd

# Cargar archivos CSV (asegúrate que estén en la misma carpeta que este archivo)
clientes = pd.read_csv('base_clientes_final.csv')
transacciones = pd.read_csv('base_transacciones_final.csv')

# Quitar espacios en nombres de columnas por si acaso
clientes.rename(columns=lambda x: x.strip(), inplace=True)
transacciones.rename(columns=lambda x: x.strip(), inplace=True)

# Combinar las bases usando la columna 'ID'
base_completa = transacciones.merge(clientes, on='id', how='left')

# Mostrar algunas filas para revisar
print("Vista previa de la base combinada:")
print(base_completa.head())

# Verificar dimensiones
print(f"\nFilas: {base_completa.shape[0]}  Columnas: {base_completa.shape[1]}")

# Guardar como CSV por si lo quieres revisar fuera de Python
base_completa.to_csv('base_completa.csv', index=False)
print("\n¡Archivo guardado como 'base_completa.csv'!")

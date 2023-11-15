import pandas as pd

def load_data(file_path):
    """
    Carga los datos de consumo eléctrico del hogar desde un archivo de texto.

    Parámetros:
    file_path (str): Ruta al archivo de datos.

    Retorna:
    DataFrame: Un DataFrame de pandas con los datos cargados.
    """
    # Definir los nombres de las columnas
    column_names = ['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 
                    'Voltage', 'Global_intensity', 'Sub_metering_1', 
                    'Sub_metering_2', 'Sub_metering_3']

    # Cargar los datos
    data = pd.read_csv(file_path, sep=';', names=column_names, header=0, 
                       parse_dates={'Datetime': ['Date', 'Time']}, 
                       infer_datetime_format=True, 
                       na_values=['?'])

    return data

# Ruta al archivo de datos
#file_path = '../../../docs/data/household_power_consumption.txt'
file_path = 'C:/Users/Personal/Documents/Proyecto Final/tdsp_template/docs/data/household_power_consumption.txt'


# Cargar los datos
data = load_data(file_path)

# Mostrar las primeras filas del DataFrame
print(data.head())

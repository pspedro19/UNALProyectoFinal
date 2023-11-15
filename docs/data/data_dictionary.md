
# Diccionario de Datos

## Base de Datos: Consumo Eléctrico en Hogares

**Esta base de datos contiene información detallada sobre el consumo eléctrico en hogares, incluyendo mediciones de potencia, voltaje e intensidad. Es crucial para analizar patrones de consumo y desarrollar estrategias de eficiencia energética.**

| Variable               | Descripción                                                  | Tipo de Dato | Rango/Valores Posibles       | Fuente de Datos                  |
|------------------------|--------------------------------------------------------------|--------------|-----------------------------|----------------------------------|
| Date                   | Fecha de registro de los datos                               | Fecha        | DD/MM/AAAA                  | household_power_consumption.txt  |
| Time                   | Hora del día de registro de los datos                        | Hora         | HH:MM:SS                    | household_power_consumption.txt  |
| Global_active_power    | Potencia activa total consumida (kilovatios)                 | Numérico     | Valores reales positivos    | household_power_consumption.txt  |
| Global_reactive_power  | Potencia reactiva total consumida (kilovolt-amperios reactivos) | Numérico  | Valores reales positivos    | household_power_consumption.txt  |
| Voltage                | Voltaje promedio durante el minuto (voltios)                 | Numérico     | Valores reales positivos    | household_power_consumption.txt  |
| Global_intensity       | Intensidad total de corriente eléctrica (amperios)           | Numérico     | Valores reales positivos    | household_power_consumption.txt  |
| Sub_metering_1         | Energía sub-medida en la cocina (vatios-hora)                | Numérico     | Valores enteros positivos   | household_power_consumption.txt  |
| Sub_metering_2         | Energía sub-medida en la lavandería (vatios-hora)            | Numérico     | Valores enteros positivos   | household_power_consumption.txt  |
| Sub_metering_3         | Energía sub-medida en calefacción y aire acondicionado (vatios-hora) | Numérico | Valores enteros positivos   | household_power_consumption.txt  |

- **Variable**: Nombre de la columna en la base de datos.
- **Descripción**: Explicación breve de lo que representa cada variable.
- **Tipo de Dato**: Indica si la variable es numérica, de fecha, hora, etc.
- **Rango/Valores Posibles**: Los posibles valores o el rango que puede tomar cada variable.
- **Fuente de Datos**: El archivo o la fuente de donde se obtienen estos datos.


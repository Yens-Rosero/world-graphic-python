# main.py

import utils
import read_csv
import charts

def run(): 
    # """
    # Función principal que carga los datos, filtra por países ingresados por el usuario
    # y genera gráficos de población para cada país.
    # """
    data = read_csv.load_data('data.csv')
    data = list(filter(lambda x : x['Continent'] == 'South America', data))

    countries = list(map(lambda x : x['Country'], data))
    percentages = list(map(lambda x : x['World Population Percentage'], data))

    charts.generate_pie_chart(countries, percentages)
if __name__ == '__main__':
    run()

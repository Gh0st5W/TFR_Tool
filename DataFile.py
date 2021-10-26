# FILES IN THE SAME DIRECTORY
import Menu

# Importar pandas
import pandas as pd
# Modulos para leer string introducido por el usuario mediante stdin
import sys
# Modulos para importar datos de la web
import urllib.request, urllib.error, urllib.parse
# Importar pandas
import pandas as pd
# Modulos para importar datos de la web de yahoo finance con Pandas
import pandas_datareader as pdr
import datetime as dt

# Modulos para hacer un clear console

# import only system from os
from os import system, name

# Para descargar ficheros. Para hacer requests vamos
import requests
# Para descargar ficheros. Para hacer requests vamos. Lo mismo pero con wget
import wget


# ---------------- VARIABLES GLOBALES ---------------- #

# Creación de dataframe vacío


# Si queremos llenar posteriormente este df lo hariamos con df_empty_1.append({})
df_empty_1 = pd.DataFrame(columns=['Fecha', 'Abrir', 'Máx.', 'Mín.', 'Cierre*', 'Cierre ajus.**', 'Volumen'])


# ---------------- VARIABLES PARA LAS FUNCIONES DE EJEMPLO ---------------- #

BA = ['07/09/2021', '50 €']
BKT = ['07/09/2021', '50 €']
IAG = ['07/09/2021', '50 €']


###########  AUXILIAR FUNCTIONS  ###########

'''
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()
'''


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def readInput():

    str = ""
    while True:
        c = sys.stdin.read(1)  # reads one byte at a time, similar to getchar()
        if c == ' ':
            break
        str += c
    print(str)
    return c






# ---------------- FUNCIONES IMPLEMENTADAS ---------------- #

def readStock():

    # Options - Show all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    # number of places after the decimal, using the precision option.
    pd.set_option('precision', 2)

    # only read
    # pd.read_csv('BA.csv')
    # read and print
    df = pd.read_csv('BA.csv')
    print (df)

    print('\n')
    input("Press Enter to continue...")
    Menu.selectOptionMainMenu()

def search():

    clear()
    print('TICKER: ')

    if sys.stdin.read(1):
        print('ok')
    else:
        print('NO OK')

    # AQUI HAY QUE LIMPIAR EL STDIN (El buffer) ANTES DE FINALIZAR ESTA FUNCIÓN YA QUE SINO QUEDA EN EL BUFFER LO QUE
    # HEMOS INTRODUCIDO Y NO PODEMOS VOLVER A SELECCIONAR ESTA OPCION (Ni ninguna que use el buffer).
    sys.stdout.flush() # Solucionar el flush

    Menu.returnToMainMenu()

def dataFrameExampleFromList():

    clear()

    lista_ejemplo = [ BA, BKT, IAG]

    pd.DataFrame(lista_ejemplo,
                 columns = ['date', 'price'])

    #Lo muestra por pantalla
    lista_ejemplo

    # Esto imprime la lista, pero no lo hace en formato datframe
    print(lista_ejemplo)

    Menu.returnToMainMenu()

def ImportDataYahooFinance():

    clear()

    print('Introduce ticker: ')
    #ticker = "AAPL"
    #ticker = readInput()
    ticker = sys.stdin.read(1)
    start = dt.datetime(2019, 1, 1)
    #end = dt.datetime(2020, 12, 31)
    end = dt.date.today()

    data = pdr.get_data_yahoo(ticker, start, end)

    Menu.returnToMainMenu()

def ImportDataYahooFinanceToCSV():

    clear()

    # En la variable df guardamos el link que descargamos.
    df = pd.read_csv=("https://query1.finance.yahoo.com/v7/finance/download/BA?period1=1599853909&period2=1631389909&interval=1d&events=history&includeAdjustedClose=true")
    df2 = pd.read_csv=("https://query1.finance.yahoo.com/v7/finance/download/FCEL?period1=1599856546&period2=1631392546&interval=1d&events=history&includeAdjustedClose=true")

    #print(df2)
    df2

    Menu.returnToMainMenu()

def downloadFile():

    url = "https://query1.finance.yahoo.com/v7/finance/download/BA?period1=1599853909&period2=1631389909&interval=1d&events=history&includeAdjustedClose=true"

    wget.download(url, 'files/downloadedFile.csv')


# Esta opción me devuelve un estado 401 forbidden y me lo almacena en un csv en lugar de descargarme el fichero que le pido.
'''
    url = 'https://query1.finance.yahoo.com/v7/finance/download/BA?period1=1599853909&period2=1631389909&interval=1d&events=history&includeAdjustedClose=true'

    myfile = requests.get(url, allow_redirects=True)

    open('downloadedFile.csv', 'wb').write(myfile.content)

    print(myfile)

'''

def ImportDataYahooFinanceAndExportToADataFrame():

    clear()

    print('Introduce ticker: ')

    ticker = sys.stdin.read(1)
    start = dt.datetime(2019, 1, 1)
    #end = dt.datetime(2020, 12, 31)
    end = dt.date.today()

    data = pdr.get_data_yahoo(ticker, start, end)

    Menu.returnToMainMenu()



# ---------------- FUNCIONES DESCARTADAS ---------------- #

'''
def importData():

    url = 'http://www.google.com/finance/historical?q=AAPL&output=csv'

    respuesta = urllib.request.urlopen(url)
    contenidoWeb = respuesta.read()

    f = open('obo-t17800628-33.html', 'w')
    f.write(contenidoWeb)
    f.close
'''
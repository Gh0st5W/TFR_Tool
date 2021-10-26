# FILES IN THE SAME DIRECTORY
import DataFile

# First import time module.
import time



###########  MENU  ###########

def printMainMenu():

    print('*******************************')
    print('****       MAIN MENU        ***')
    print('*******************************\n')
    print('1. CHARTS')
    print('2. SEARCH STOCKS')
    print('3. PORTFOLIO')
    print('4. STOCK TRACKING')
    print('5. STOCK TRACKING')
    print('6. EXIT \n')

def selectOptionMainMenu():

    correcto = False
    num = 0

    DataFile.clear()
    printMainMenu()

    while (not correcto):
        try:
            num = int(input("Select an option..."))
            correcto = True
        except ValueError:
            print('Error, Select a correct option...')

    salir = False

    while not salir:

        opcion = num

        if opcion == 1:
            DataFile.readStock()
        elif opcion == 2:
            DataFile.search()
            exit(0)
        elif opcion == 3:
            ImportDataYahooFinance()
            exit(0)
        elif opcion == 4:
            DataFile.ImportDataYahooFinanceToCSV()
            exit(0)
        elif opcion == 5:
            DataFile.downloadFile()
            exit(0)
        elif opcion == 6:
            salir = True
        else:
            print("Select a correct option...2222")

    print("Exiting...")
    time.sleep(2.5)
    print("BYE!")

def returnToMainMenu():

    print('\n')
    input("Press Enter to continue...")
    selectOptionMainMenu()
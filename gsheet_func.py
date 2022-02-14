# Librerías
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Se autentifica y permite el acceso a las hojas de datos.
s=['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

creds= ServiceAccountCredentials.from_json_keyfile_name('credentials.json',s)
client=gspread.authorize(creds)

# Se accede a la hoja de datos para guardar información.
sheet = client.open("Data_Base").sheet1

# Se definen las funciones para recuperar datos.
def recuperador(nombre):
    
    # Encuentra la celda requerida
    print(nombre)
    cell = sheet.find(nombre)

    # Imprime la información deseada
    if cell != None:
        val = sheet.cell(cell.row, cell.col + 1).value
        print("Usted está", val)
        return "Usted está" + val

    else:
        return "No se pudo encontrar. Contáctese con RH."



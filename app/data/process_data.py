import openpyxl

book = openpyxl.open(r"C:\Users\Redmi\OneDrive\Рабочий стол\WheWall\datax.xlsx", read_only=True)

sheet_all = book['Лист1']
sheet_apt = book['Аптеки']
sheet_prod = book['Прод']
sheet_gost = book['Гостин']
sheet_whe = book['Где']
sheet_con = book['Коньки']

class Data:

    def __init__(self):
        self.all = sheet_all
        self.apt = sheet_apt
        self.prod = sheet_prod
        self.gost = sheet_gost
        self.whe = sheet_whe
        self.con = sheet_con


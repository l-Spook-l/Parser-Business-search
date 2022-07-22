import openpyxl

book = openpyxl.Workbook()

sheet = book.active

# sheet['A2'] = 100
# sheet['b3'] = 'hi'

sheet[1][0].value = "world"
sheet[1][1].value = "world_2"

book.save("Предприятия.xlsx")
book.close()

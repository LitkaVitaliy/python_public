from openpyxl import load_workbook

filename = '22.xlsx'

wb = load_workbook(filename)  # эксель файл с database
sheet = wb["Sheet1"]  # лист книги

for n1 in range(2, 19064):
    for n2 in range(2, 43126):
        if sheet[f'A{n1}'].value == sheet[f'F{n2}'].value:
            sheet[f'G{n2}'].value = sheet[f'B{n1}'].value
            with open('changed3.txt', 'a') as file:
                file.write(f'A{n1} B{n1} -> F{n2} G{n2} \n')

            break
wb.save(filename)

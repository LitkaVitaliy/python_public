from openpyxl import load_workbook

filename = '33.xlsx'
sheet_name = 'Sheet1'
col1_names = 'A'
col1_urls = 'B'
col2_names = 'F'
col2_urls = 'G'


def main():
    wb = load_workbook(filename)  # эксель файл с database
    sheet = wb[sheet_name]  # лист книги

    names1 = [n.value for n in sheet[col1_names:col1_names]]

    names2 = [n.value for n in sheet[col2_names:col2_names]]

    for name in names1:
        if name in names2:
            index1 = names1.index(name) + 1
            index2 = names2.index(name) + 1

            sheet[f'{col2_urls}{index2}'].value = sheet[f'{col1_urls}{index1}'].value

    wb.save(filename)

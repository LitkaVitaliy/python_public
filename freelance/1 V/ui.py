import tkinter as tk
from openpyxl import load_workbook

win = tk.Tk()
win.title('Гарного дня!')
win.geometry('450x550+700+300')
win.resizable(False, False)
win.config(bg='#49657b')

label_1 = tk.Label(win, text='Назва файла',
                   bg='#49657b',
                   fg='#fff',
                   font=('Arial', '12'),
                   width=30,
                   anchor='w')

entry_filename = tk.Entry(win)

label_2 = tk.Label(win, text='Назва листа',
                   bg='#5a7d99',
                   fg='#fff',
                   font=('Arial', '12'),
                   width=30,
                   height=2,
                   anchor='w')

entry_sheet_name = tk.Entry(win)

label_3 = tk.Label(win, text='Колонка з назвами товарів\n(звідки берем)',
                   bg='#49657b',
                   fg='#fff',
                   font=('Arial', '12'),
                   width=30,
                   height=2,
                   anchor='w')

entry_col_names1 = tk.Entry(win)

label_4 = tk.Label(win, text='Колонка з посланнями\n(звідки берем)',
                   bg='#5a7d99',
                   fg='#fff',
                   font=('Arial', '12'),
                   width=30,
                   height=2,
                   anchor='w')

entry_col_urls1 = tk.Entry(win)

label_5 = tk.Label(win, text='Колонка з назвами товарів\n(в которій змінюємо)',
                   bg='#49657b',
                   fg='#fff',
                   font=('Arial', '12'),
                   width=30,
                   height=2,
                   anchor='w')

entry_col_names2 = tk.Entry(win)

label_6 = tk.Label(win, text='Колонка з посиланнями\n(в которій змінюємо)',
                   bg='#5a7d99',
                   fg='#fff',
                   font=('Arial', '12'),
                   width=30,
                   height=2,
                   anchor='w')

entry_col_urls2 = tk.Entry(win)


def main():
    filename = entry_filename.get()
    sheet_name = entry_sheet_name.get()
    col1_names = entry_col_names1.get()
    col1_urls = entry_col_urls1.get()
    col2_names = entry_col_names2.get()
    col2_urls = entry_col_urls2.get()
    try:
        if filename != sheet_name != col1_names != col1_urls != col2_names != col2_urls:

            wb = load_workbook(filename)
            sheet = wb[sheet_name]

            names1 = [n.value for n in sheet[col1_names:col1_names]]

            names2 = [n.value for n in sheet[col2_names:col2_names]]

            for name in names1:
                if name in names2:
                    index1 = names1.index(name) + 1
                    index2 = names2.index(name) + 1

                    sheet[f'{col2_urls}{index2}'].value = sheet[f'{col1_urls}{index1}'].value

            wb.save(filename)

            tk.Label(win, text='Все готово Пане!', bg='#49657b', fg='#fff',
                     font=('Arial', '14')).grid(row=7, column=0)
        else:
            tk.Label(win, text='Не всі поля заповнені', bg='#49657b', fg='#fff',
                     font=('Arial', '14')).grid(row=7, column=0)

    except Exception as err:
        tk.Label(win, text='Перевір введені данні', bg='#49657b', fg='#fff',
                 font=('Arial', '10')).grid(row=7)


btn_1 = tk.Button(win, text='Почати',
                  command=main,
                  bg='#2a4d69',
                  fg='#fff',
                  font=('Arial', '12'))

label_1.grid(row=0, column=0)
entry_filename.grid(row=0, column=1)

label_2.grid(row=1, column=0)
entry_sheet_name.grid(row=1, column=1)

label_3.grid(row=2, column=0)
entry_col_names1.grid(row=2, column=1)

label_4.grid(row=3, column=0)
entry_col_urls1.grid(row=3, column=1)

label_5.grid(row=4, column=0)
entry_col_names2.grid(row=4, column=1)

label_6.grid(row=5, column=0)
entry_col_urls2.grid(row=5, column=1)

btn_1.grid(row=6, column=0)

win.mainloop()

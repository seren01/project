from tkinter import * #импортир функций, предназначенных для создания графического интерфейса
import tkinter as tk
from tkinter import messagebox as mb #импорт набора функций для выводы всплывающих/диалоговых окон

root = tk.Tk()
root.title("Конвектор") #наименование программы в левом верхнем углу
root.geometry('360x270') #определение размера экрана

def convert(): #событие перевода литров в килограммы
	try: #при правильных вводимых данных
		rd = float(request_data.get())
		name_option = var_material.get()
		value = float(materials[name_option])
		itog = round(float(rd * value), 3)
		with open('Рассчёт_литров_в_киллограм.txt', 'a') as f: #открытие файла для добавления записи
			f.write(str(rd) + ' л = ' + str(itog) + ' кг' + '\n') #запись полученного результата
		f.close() #закрытие файла
		itogi['text'] = ' '.join(str(itog) + ' кг') #вывод результата в соответствующую строку
		mb.showinfo(
			"Уведомление", 
			"Операция успешно выполнена. Данные сохранены в файле Рассчёт_литров_в_киллограм.txt.") #сообщение об успешной операции
	except KeyError: #отработка ошибки при неверном выборе материалов/жидкостей
		 mb.showerror(
			"Ошибка", 
			"Что-то пошло не так. Проверьте правильность выбраного материала/жидкости.")
	except ValueError: #отработка ошибки при отсутствии каких-либо значений и/или неправильном вводе единицы измерения
		 mb.showerror(
			"Ошибка", 
			"Что-то пошло не так. Проверьте правильность вводимых данных.")

materials = {'Кефир 2.5%' : 1.031, 
			 'Вода' : 0.997, 
			 'Молоко' : 1.027, 
			 'Кровь' : 1.05, 
			 'Мед (16% воды)' : 1.42, 
			 'Сметана' : 1.015, 
			 'Спирт' : 0.789, 
			 'Масло' : 0.9, 
			 'Керосин' : 0.8, 
			 'Бензин' : 0.71} 
#словарь, хранящий в себе список материалов и их плотность

var_material = StringVar(root)
var_material.set('Choose')

name = Label(text='Перевести литры в килограммы', font="Arial 12")

query_window1 = Label(text='Введите литры:', font="Arial 10") #запрос на ввод данных
request_data = Entry(root, width=20) #ввод данных

query_window2 = Label(text='Выберите материал/жидкость:', font="Arial 10") #запрос на выбор данных из всплывающего списока
combo_material = OptionMenu(root, var_material, *materials) #всплывающий список с выбором материалов

indent1 = Label() #отступ по вертикали
conv_but = Button(root, text="Рассчитать", command = convert) #кнопка с привязоным событием перевода литров в килограммы
indent2= Label() #отступ по вертикали

itogi = Label(root, bg='black', fg='white', width=20) #строка вывода результата

info1 = Label(text='Данное значение перевода является приблизетельным,', font="Arial 10")
info2= Label(text='так как плотность материала/жидкости может отличаться.', font="Arial 10")
nm = Label(text='©Бутусова_Анастасия', font="Arial 7")

#графисеская оболочка (интерфейс) программы
name.pack()

query_window1.pack()
request_data.pack()

query_window2.pack()
combo_material.pack() 

indent1.pack()
conv_but.pack()			#расположение элементов
indent2.pack()

itogi.pack()

info1.pack()
info2.pack()
nm.pack()

root.mainloop() #отображениt гл. экр. со всеми еги причиндалами на экране
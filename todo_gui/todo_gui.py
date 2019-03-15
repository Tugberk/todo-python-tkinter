#python2.7
import Tkinter
from Tkinter import *
import sqlite3


root = Tkinter.Tk()
root.geometry('300x500')


bg_color = "white"
root.configure(bg=bg_color)

root.title("My Todo")

def conn_db():
	conn = sqlite3.connect('todoNew.db')
	return conn

def update():
	lb_tasks.delete(0,'end')
	conn = conn_db()
	c = conn.cursor()
	c.execute('select * from data order by id desc')
	result = c.fetchall()
	for x in result:
		lb_tasks.insert('end', x[1])


def ekle():
	conn = conn_db()
	c = conn.cursor()
	task = txt_input.get()
	task = task.upper()

	if task != '':
		lb_tasks.insert(0, task) #basa ekliyor onun icin 0 yaziyoruz
		c.execute('insert into data(icerik) values(?)', [task])
		conn.commit()
	txt_input.delete(0, 'end') #yazdiktan sonra bu icerigi sildiriyoruz temiz olsun diye
	



def sil():
	conn = conn_db()
	c = conn.cursor()
	task = lb_tasks.get('active') #secileni al - secilmediyse en ustu aliyor
	if task != '':
		c.execute('delete from data where icerik = ?', [task])
		conn.commit()
		conn.close()
		#lb_tasks.delete(task)
		update()
	






#graphical user interface

lbl_title = Tkinter.Label(root, text="To-do App", bg=bg_color)
lbl_title.pack()

txt_input = Tkinter.Entry(root, width=25)
txt_input.pack()

lbl_bos = Tkinter.Label(root, text=" ", bg=bg_color)
lbl_bos.pack()

#ekleme butonu
bttn_ekle = Tkinter.Button(root, text="Ekle", command=ekle, width= 15, bg=bg_color)
bttn_ekle.pack()

lbl_bos = Tkinter.Label(root, text=" ", bg=bg_color)
lbl_bos.pack()

#silme butonu
bttn_sil = Tkinter.Button(root, text="Sil", command=sil, width=15, bg=bg_color)
bttn_sil.pack()

lbl_bos = Tkinter.Label(root, text=" ", bg=bg_color)
lbl_bos.pack()


#listbox
lb_tasks = Tkinter.Listbox(root, width=100, font=('Helvetica', 12))
lb_tasks.pack(side='left', fill='y')

#scrollbar ekledim ustteki pack in icinde sideleft falan yapinca da oldu aslinda yanina tasindi
scrollbar = Scrollbar(root, orient='vertical')
scrollbar.config(command=lb_tasks.yview)
scrollbar.pack(side='right', fill='y')

#bosluk
lbl_bos = Tkinter.Label(root, text=" ", bg=bg_color)
lbl_bos.pack()
lbl_bos = Tkinter.Label(root, text=" ", bg=bg_color)
lbl_bos.pack()

#run the program
update()

root.mainloop()
from tkinter import ttk, Tk, StringVar
#Tk untuk window, ttk object turunan tkinter

#membuat sebuah instance / objek nyata
my_apps =Tk()




#title itu method (fungsi di dalam objek) di dalam object Tk()
my_apps.title("My First Python Apps")
#my_apps.resizable(False, False)
"""
#menambahkan label / tulisan
label1 = ttk.Label(my_apps, text= "Item \t:")
label1.grid(column=0, row=0) #ttk itu objectnya beda lg
label2 =  ttk.Label(my_apps, text= "Item Code \t:")
label2.grid(column=0, row=1) #(supaya bisa ke tengah)
label3 = ttk.Label(my_apps, text="Item Type \t:")
label3.grid(column=0, row=2)
label4 = ttk.Label(my_apps, text= "Expired / Produced Date \t:")
label4.grid(column=0, row=3)
label5 = ttk.Label(my_apps, text= "Produced by \t:")
label5.grid(column=0, row=4)
"""

#Label/ tulisan
label1 = ttk.Label(my_apps, text="Enter a name")
label1.grid(column=0, row=0)

label2 = ttk.Label(my_apps, text="My Age")
label2.grid(column=1, row=0)

def change_color():
	global counterButton1
	button1.configure(text="Already Clicked")
	if counterButton1 % 2 == 0:
		label1.configure(foreground="red")
		label2.configure(foreground="red")
	else:
		label1.configure(foreground="blue")
		label2.configure(foreground="blue")
	label1.configure(text= data_name.get())
	label2.configure(text= data_age.get())
	counterButton1 += 1

#Button
counterButton1 = 0

#membuat tombol / button
button1 = ttk.Button(my_apps, text="Change color", command=change_color)
button1.grid(column=2, row=1)

data_name = StringVar()
data_name_entry = ttk.Entry(my_apps, width=12, textvariable=data_name)
data_name_entry.grid(column=0, row=1)
#line 48 & 49 itu sama dengan data_name = input("Nama : "), sedangkan line 47 itu oenghubungnya aja
#focus -> agar nanti ada garis untuk nulis langsung tanpa harus diklik dulu
data_name_entry.focus()


#combobox dropdown list (mirip dropbox)
data_age = StringVar()
data_age_combobox = ttk.Combobox(my_apps, width=12, textvariable=data_age, state="readonly") #state="readonly"
data_age_combobox['values'] = ["YOUNGER", 12, 13, 14, 15, "OLDER"]
data_age_combobox.grid(column=1, row=1)
data_age_combobox.current(0)


#method untuk memulai GUI apps
if __name__ == "__main__": #bisa adabisa tidak (tidak wajib) hanya untuk membantu mengurangi ada kesalahan
	my_apps.mainloop()
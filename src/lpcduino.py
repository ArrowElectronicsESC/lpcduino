# LPCduino v0.2
# Author: BSSB
# April 10th, 2022

from tkinter import *
from tkinter import filedialog
from tkinter import font
from PIL import Image
from PIL import ImageTk

import os
import subprocess


#Splash screen
splash_root = Tk()

splash_image = Image.open("lpcduinorotated.png")
splash_img = ImageTk.PhotoImage(splash_image)

#splash_root.title("LPCduino!!")
splash_root.geometry("500x270+500+300")
#splash_root.eval('tk::PlaceWindow . center')
splash_root.overrideredirect(True)

splash_label = Label(splash_root, image = splash_img )
splash_label.place(anchor="center")
splash_label.pack(pady=20)

def main_window():
	splash_root.destroy()

	root = Tk()
	root.title('LPCduino v0.1 -- Apr 2022')
	root.iconbitmap('lpcduino_icon.ico')
	root.geometry("800x660+100+100")

	#Set open filename
	global open_status_name
	open_status_name = False

	#Set select global
	global selected
	selected = False

	#Set compile_status global
	global compile_status
	compile_status = False

	#Create a toolbar frame
	toolbar_frame = Frame(root)
	toolbar_frame.pack(fill=X)

	#Create Main Frame
	main_frame = Frame(root)
	main_frame.pack(pady=5)
	#main_label = Label(root, text="LPCduino v0.1")
	#main_label.pack(pady=5)

	#Create Text Box scroll bar
	text_scroll = Scrollbar(main_frame)
	text_scroll.pack(side=RIGHT, fill=Y)

	#Horizontal Scroll bar
	hor_scroll = Scrollbar(main_frame, orient='horizontal')
	hor_scroll.pack(side=BOTTOM, fill=X)

	#Create Text Box
	my_text = Text(main_frame, width=97, height=25, font=("Helvetica", 14), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
	my_text.pack()

	#Configure scroll bar
	text_scroll.config(command=my_text.yview)
	hor_scroll.config(command=my_text.xview)

	#Add Status bar to bottom of App
	status_bar = Label(root, text="Ready ", anchor=E)
	status_bar.pack(fill=X, side=BOTTOM,ipady=5)

	#Create Menu
	main_menu = Menu(root)
	root.config(menu=main_menu)



	#Create New File Function
	def new_file():
		#Delete previous text
		my_text.delete("1.0", END)
		#Update status bars
		root.title("New File - LPCduino v0.2 -- Apr 2022")
		status_bar.config(text="New File Created")

		global open_status_name
		open_status_name = text_file


	#Open File Function
	def open_file():
		#Delete previous text
		my_text.delete("1.0", END)
		#Grab Filename
		text_file =filedialog.askopenfilename(title="Open File")
		#Grab File name
		if text_file:
			#Make File name global for later access
			global open_status_name
			open_status_name = text_file
		#Update status bars
		name = text_file
		status_bar.config(text=f'{name}   ')
		#name = name.replace("C:/Users/","")
		root.title(f'{name} - LPCduino v0.1 -- Apr 2022')
		#Open the file
		text_file = open(text_file, 'r')
		file_content = text_file.read()
		#Add file to edit box
		my_text.insert(END, file_content)
		#Close the opened file
		text_file.close()

	#Save As Function
	def save_as_file():
		#Prompt
		text_file = filedialog.asksaveasfilename(defaultextension=".*",filetypes=(("C Files", "*.c"), ("All files", "*.*")))
		if text_file:
			#Update Status Bars
			name = text_file
			#name = name.replace("C:/")
			root.title(f'{name} - LPCduino v0.1 -- Apr 2022')
			status_bar.config(text=f'{name}  Saved ')

			#Save the file
			text_file = open(text_file, 'w')
			text_file.write(my_text.get(1.0,END))
			#Close the file
			text_file.close()

	#Save File Function
	def save_file():
		global open_status_name
		if open_status_name:
			#Save the file
			text_file = open(open_status_name, 'w')
			text_file.write(my_text.get(1.0,END))
			#Close the file
			text_file.close()
			#Change status bar text
			status_bar.config(text=f'{open_status_name}  Saved ')
		else:
			save_as_file()

	#Cut Text
	def cut_text(e):
		global selected
		# check to see if keyboard shortcut used
		if e:
			selected = root.clipboard_get()
		else:
			if my_text.selection_get():
				#Grab selected text from text box
				selected = my_text.selection_get()
				#Delete selected text from text box
				my_text.delete("sel.first","sel.last")
				root.clipboard_clear()
				root.clipboard_append(selected)

	#Copy Text
	def copy_text(e):
		global selected

		#check to see if keyboard was used
		if e:
			selected = root.clipboard_get()

		if my_text.selection_get():
			#Grab selected text from text box
			selected = my_text.selection_get()
			root.clipboard_clear()
			root.clipboard_append(selected)

	#Paste Text
	def paste_text(e):
		global selected

		#check to see if keyboard shortcut used
		if e:
			selected = root.clipboard_get()
		else:
			if selected:
				position = my_text.index(INSERT)
				my_text.insert(position, selected)

	#Compile
	def compile_file():
		global compile_status
		save_file()
		os.chdir('C:\\Projects\\1_1_POCs\\4_Arduino\\LPC810_CodeBase\\src') #Change for your local path
		os.system('python ino2main.py')
		status_bar.config(text='Compiling code...', background='yellow')
		try:
			#os.chdir('C:\\Projects\\1_1_POCs\\4_Arduino\\LPC810_CodeBase\\src') #Change for your local path
			#os.system('make')
			subprocess.run(['make'], check=True)
		except subprocess.CalledProcessError:
			status_bar.config(text='There was a compilation issue', background='red')
			compile_status = False
		else:
			status_bar.config(text='Code was compiled successfuly', background='green')
			compile_status = True


	#Upload / Verify
	def upload_verify():
		global compile_status
		save_file()
		status_bar.config(text='Compiling and Uploading binary file', background='blue')
		compile_file()
		if compile_status == True:
			#Change for your local path
			os_out = os.popen('fm --device LPC812M101JD20 --serialport COM3 --baudrate 115200 -erasedevice --program="C:\\Users\\LEGA\\Documents\\Arrow\\Abr2022\\LPCDuino\\LPC810_CodeBase-master\\src\\blinky.hex" --verify="C:\\Users\\LEGA\\Documents\\Arrow\\Abr2022\\LPCDuino\\LPC810_CodeBase-master\\src\\blinky.hex" --timeouts 4000,60000').read()
			if os_out.find("ERROR")!=-1:
				status_bar.config(text='Could not upload the code, is the MCU board connected?', background='red')
			else:
				status_bar.config(text='Upload complete', background='blue')

	#Upload / Verify
	def obtain_signature():
		os_out = os.popen('fm --device LPC812M101JD20 --serialport COM3 --baudrate 115200 --readsignature').read()
		if os_out.find("ERROR")!=-1:
			status_bar.config(text='Could not verify the signature, is the MCU board connected?', background='red')
		else:
			status_bar.config(text=os_out[os_out.find("RESULT"):len(os_out)], background='blue')

	#Create Button

	#Compile Button
	compile_button = Button(toolbar_frame, text="Compile", command=compile_file)
	compile_button.grid(row=0, column=0, sticky=W, padx=5)

	#Upload Button
	upload_button = Button(toolbar_frame, text="Upload", command=upload_verify)
	upload_button.grid(row=0, column=1, padx=5)

	#Signature Button
	signature_button = Button(toolbar_frame, text="Signature", command=obtain_signature)
	signature_button.grid(row=0, column=2, padx=5)

	#Undo/Redo Button
	undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
	undo_button.grid(row=0, column=4, sticky=W, padx=5)
	redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
	redo_button.grid(row=0, column=5, sticky=W, padx=5)


	#Add File Menu
	file_menu = Menu(main_menu, tearoff=False)
	main_menu.add_cascade(label="File", menu=file_menu)
	file_menu.add_command(label="New", command=new_file)
	file_menu.add_command(label="Open", command=open_file)
	file_menu.add_command(label="Save", command=save_file)
	file_menu.add_command(label="Save As...", command=save_as_file)
	file_menu.add_separator()
	file_menu.add_command(label="Exit", command=root.quit)

	#Add Edit Menu
	edit_menu = Menu(main_menu, tearoff=False)
	main_menu.add_cascade(label="Edit", menu=edit_menu)
	edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="[Ctrl+X]")
	edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="[Ctrl+C]")
	edit_menu.add_command(label="Paste     ", command=lambda: paste_text(False), accelerator="[Ctrl+V]")
	edit_menu.add_separator()
	edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="[Ctrl+Z]")
	edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="[Ctrl+Y]")

	#Add Program Menu
	program_menu = Menu(main_menu, tearoff=False)
	main_menu.add_cascade(label="Program", menu=program_menu)
	program_menu.add_command(label="Compile", command=compile_file)
	program_menu.add_command(label="Upload/Verify", command=upload_verify)

	#Add Tools Menu
	tools_menu = Menu(main_menu, tearoff=False)
	main_menu.add_cascade(label="Tools", menu=tools_menu)
	tools_menu.add_command(label="Port -- COM3")
	tools_menu.add_command(label="Obtain LPC Signature", command=obtain_signature)

	#Add Help Menu
	help_menu = Menu(main_menu, tearoff=False)
	main_menu.add_cascade(label="Help", menu=help_menu)
	help_menu.add_command(label="About")

	#Edit bindings
	root.bind('<Control-Key-x>', cut_text)
	root.bind('<Control-Key-c>', copy_text)
	root.bind('<Control-Key-v>', paste_text)

#Splash screen timer
splash_root.after(3000, main_window)



mainloop()

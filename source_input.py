import tkinter as tk
import gspread

# GOOGLE SHEETS API AUTHENTICATION
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
                "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
gc = gspread.service_account(filename='credentials.json',scopes=scope)   # for heroku directory



root = tk.Tk(className='sample')
root.geometry('780x400')                      # WINDOW PANE SIZE

# LABEL 0
label0 = tk.Label(master=root,text='Name of the website')
label0.pack(side='top',pady=10)

# ENTRY FOR WEBSITE NAME
entry0 = tk.Entry(master=root,width=20,fg='black',borderwidth=5,relief='sunken')
entry0.pack(side='top',pady=10)

# LABEL 1
label1 = tk.Label(master=root,text='Name of the product')
label1.pack(side='top',pady=10)

# ENTRY FOR PRODUCT PRODUCT NAME
entry1 = tk.Entry(master=root,width=30,fg='black',borderwidth=5,relief='sunken')
entry1.pack(side='top',pady=10)

# LABEL 2
label2 = tk.Label(master=root,text='URL of the product')
label2.pack(side='top',pady=10)

# ENTRY FOR URL OF THE PRODUCT
entry2 = tk.Entry(master=root,width=40,fg='black',borderwidth=5,relief='sunken')
entry2.pack(side='top',pady=10)

# FUNCTION FOR UPATING PRODUCT DB
def update_database():
	# UPDATING ITEM IN WEBSITE'S G-SHEET
	dfaf = gc.open(f"{entry0.get().capitalize()}").sheet1
	lcell = len(dfaf.row_values(1))
	dfaf.update_cell(row=1,col=lcell+1,value=entry1.get())
	
	# UPDATING ITEM & URL IN URL G-SHEET
	dfu = gc.open("URLs").sheet1
	dfu.append_row(values=[entry1.get(),entry2.get()],insert_data_option='INSERT_ROWS')
 	
 	# DISPLAY MESSAGE
	labelz.config(text=f'You will be notified through whatsapp if the price of {entry1.get()} drops!!')

#OK BUTTON
butt = tk.Button(master=root,text='OK!',bd=4,bg='white',font=("Gabriola", 20, "bold"),width=10,height=5,
                 activebackground='light green',cursor='hand2',command=update_database)
butt.pack(side='right',padx=30,pady=10)

#MESSAGE
labelz = tk.Label(master=root,text='')
labelz.pack(side='left',padx=20)
root.mainloop()
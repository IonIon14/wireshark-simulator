from caption import Captura
from packet import *
import tkinter as tk
from tkinter import Tk,Button,font,BOTTOM,YES,Entry,Label
def changeText():
    start_caption_button['text']='Stop Capture'

def show_entry_fields():
    if filter_text.get()=="":
        raise Exception("No filter applied")
    else:
        pachete=sniff(timeout=5,filter=filter_text.get())
        for pachet in pachete:
            print(pachet.summary())
        filter_text.set("")
    print("\n")



#window screen

window=Tk(className="Proiect final PP")
window.title("Proiect final ")
window.geometry('400x400')



buton_captura=Captura()
# Start Capture and Save as JSON buttons
myFont = font.Font(family='Helvetica')
start_caption_button=Button(text="Start Capture",
                            font=(myFont, 12),
                            bg='#0052cc',
                            fg='#ffffff',
                            width=10,
                            height=1,
                            command=buton_captura.show_packet_info
                            )



#show statistics
show_statistics_button=Button(text="Show statistics",
                            font=(myFont, 12),
                            bg='#0052cc',
                            fg='#ffffff',
                            width=12,
                            height=1,
                            command=buton_captura.plot_graph
                            )

#save button
save_button=Button(text="Save as JSON",
                   font=(myFont, 12),
                   bg='#0052cc',
                   fg='#ffffff',
                   width=12,
                   height=1,
                   command=buton_captura.save_as_json
              )
start_caption_button.pack(side=BOTTOM,expand=YES)
start_caption_button.place(y=320,x=290)

show_statistics_button.pack(side=BOTTOM,expand=YES)
show_statistics_button.place(y=280,x=270)

save_button.pack(side=BOTTOM,expand=YES)
save_button.place(y=360,x=272)

label=Label(window,text="Wireshark Simulator",font=("Arial Bold",30))

label.place(y=150,x=5)
#Search filter

search_label=tk.Label(window,
         text="Search by filter:")

search_label.place(y=336)

filter_text=StringVar(window)
filter_text.set("")


search_bar=Entry(window,textvariable=filter_text)

search_bar.place(y=340,relx=0.22)
search_bar.focus_set()

buton_filtru=Captura()
# search
search_button=Button(window,
          text='Search',
          font=(myFont, 12),
          bg='#0052cc',
          fg='#ffffff',
          command=show_entry_fields)

search_button.grid( row=3,
                    column=0,
                    sticky=tk.W,
                    pady=4)

search_button.place(y=360,x=0)

window.mainloop()

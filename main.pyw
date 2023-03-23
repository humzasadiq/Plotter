import matplotlib.pyplot as plt
from tkinter import *
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


colors = ['', 'Maroon', 'Red', 'Indigo','Aqua','Black', 'Green', 'Orange', 'Violet', 'Pink']
def add_vector():
    global click_count, temp, root, Plot_button
    
    if click_count >= 10:
        global noadd
        noadd = customtkinter.CTkLabel(master=frame_interact, text='Plot limit!',font=("Roboto", 15), text_color= '#C64343')    
        noadd.pack(side='bottom')
        noadd.after(1000, noadd.destroy)
    elif temp==click_count:
        Plot_button.configure(fg_color='#C64343')
        Plot_button.after(1000, lambda: Plot_button.configure(fg_color='green'))
    else:
        frameloop = customtkinter.CTkFrame(master=frame_interact,width=400 , height=100, fg_color= 'transparent' )
        frameloop.pack(pady=10, padx=20)
        no = customtkinter.CTkLabel(master=frameloop, text='{}. '.format(click_count),font=("Roboto", 25))
        no.grid(row=1, column=0)
        global ientry
        ientry = StringVar()
        ient = customtkinter.CTkEntry(master=frameloop,textvariable=ientry, width=100,placeholder_text="0", corner_radius=10 )
        ient.grid(row=1, column=1)

        ilab = customtkinter.CTkLabel(master=frameloop, text=' i ',font=("Roboto", 25), text_color= 'Green')
        ilab.grid(row=1, column=2)

        global jentry
        jentry = StringVar()
        jent = customtkinter.CTkEntry(master=frameloop,textvariable=jentry ,width=100,placeholder_text="0", corner_radius=10)
        jent.grid(row=1, column=3)

        jlab = customtkinter.CTkLabel(master=frameloop, text=' j ',font=("Roboto", 25), text_color= '#8776FF')
        jlab.grid(row=1, column=4)

        global kentry
        kentry = StringVar()
        kent = customtkinter.CTkEntry(master=frameloop, textvariable=kentry,width=100,placeholder_text="0", corner_radius=10)
        kent.grid(row=1, column=5)

        klab = customtkinter.CTkLabel(master=frameloop, text=' k ',font=("Roboto", 25), text_color= '#0c5daf')
        klab.grid(row=1, column=6)

    temp = click_count

def plot_it():
    global click_count, noadd
    if click_count>=10:
        noadd = customtkinter.CTkLabel(master=frame_interact, text='Plot limit!',font=("Roboto", 15), text_color= '#C64343')    
        noadd.pack(side='bottom')
        noadd.after(1000, noadd.destroy)
    else:
        
        if ientry.get()=='':
            i=0
        else:
            i = int(ientry.get())
        if jentry.get()=='':
            j=0
        else:
            j = int(jentry.get())
        if kentry.get()=='':
            k=0
        else:
            k = int(kentry.get())
        
        scrol_update = customtkinter.CTkLabel(master=scrollable_frame, text=('({}). {} i + {} j + {} k ({})'.format(click_count,i,j,k, colors[click_count])),font=("Roboto", 15))
        scrol_update.pack(anchor=NW)
        u = [i,j,k]
        
        
        

        start = [0,0,0]
        ax.quiver(start[0], start[1], start[2], u[0], u[1], u[2], color= colors[click_count])


        
        
        
         
        



    click_count+=1

    
def slider_event(value, ax, fig):
    v = float(value)
    ax.set_xlizzm(-v,v)
    ax.set_ylim(-v,v)
    ax.set_zlim(-v,v)
    fig.canvas.draw()
def on_closing():
    root.destroy()
    root.quit() 

def segmented_button_callback():
    toplevel_window = customtkinter.CTkToplevel()
    toplevel_window.title('Information')
    toplevel_window.geometry('400x200')

    
    info_label = customtkinter.CTkLabel(master=toplevel_window, text='Made by: \n\n SE-22092 , SE-22089, SE-220??',font=("Roboto", 20) ) 
    info_label.pack()


temp = 0
click_count= 1
root = customtkinter.CTk()
root.geometry("1200x900")
root.title('3D Vector Plotting')
root.protocol("WM_DELETE_WINDOW", on_closing)


frame_graph = customtkinter.CTkFrame(master=root, fg_color='White', width=600)
frame_graph.pack(side='left', fill="both")
frame_interact = customtkinter.CTkFrame(master=root, fg_color='transparent', width=800)
frame_interact.pack(side='right', fill="both")

slider = customtkinter.CTkSlider(master=frame_interact, height=500 ,from_=0, to=100, progress_color='green',orientation=VERTICAL, command=lambda value: slider_event(value, ax, fig))
slider.pack(side='left')

fig = plt.figure(figsize=(10,10), dpi=70)
ax = plt.axes(projection = '3d')
ax.xaxis.set_pane_color((0.9,0.9,0.9,0.9))
ax.yaxis.set_pane_color((0.9,0.9,0.9,0.9))
ax.zaxis.set_pane_color((0.68,0.68,0.68,0.68))

ax.plot([0,0], [0,0], [-100,100], color='#0c5daf', linewidth=1.5)
ax.plot([0,0], [-100,100], [0,0], color='#8776FF', linewidth=1.5)
ax.plot([-100,100], [0,0], [0,0], color='Green', linewidth=1.5)
# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
canvas.draw()
canvas.get_tk_widget().pack(side='top')

segemented_button = customtkinter.CTkButton(master=frame_interact,
                                                     text="!", font=('Roboto', 20),corner_radius=10, width=30,
                                                     command=segmented_button_callback)
segemented_button.pack(anchor=NW, pady=20)

label_Add = customtkinter.CTkLabel(master=frame_interact, text='Add a new vector', font=("Roboto", 25))
label_Add.pack(side= 'top', padx= 100, pady= 10)
Add_Button = customtkinter.CTkButton(master=frame_interact, text='+', font=('Roboto', 25), corner_radius=8, width=50, command=add_vector)
Add_Button.pack(side= 'top', )

Plot_button = customtkinter.CTkButton(master=frame_interact,height=100, text='Plot',fg_color='green',font=('Roboto', 20), corner_radius=10, width=200, command= plot_it)
Plot_button.pack(side= 'bottom', pady= 15 )



scrollable_frame = customtkinter.CTkScrollableFrame(master=frame_graph,width=700, height=200)
scrollable_frame.pack(side='bottom')

root.mainloop()

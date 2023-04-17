import matplotlib.pyplot as plt
from tkinter import *
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import random
import math as m

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

colors = ['Maroon', 'Red', 'Indigo', 'Aqua',
          'Black', 'Green', 'Orange', 'Violet', 'Pink']


def add_vector():
    global click_count, temp, root, Plot_button
    global ient,jent,kent, frameloop

    if temp == click_count:
        Plot_button.configure(fg_color='#C64343')
        Plot_button.after(
            1000, lambda: Plot_button.configure(fg_color='green'))
    else:
        frameloop = customtkinter.CTkFrame(master=scrollable_frame2,
                                           width=300,
                                           height=100,
                                           fg_color='transparent')
        frameloop.pack(pady=10, padx=20)

        no = customtkinter.CTkLabel(master=frameloop,
                                    text='{}. '.format(click_count),
                                    font=("Fixedsys", 20))
        no.grid(row=1, column=1)

        global ientry
        ientry = StringVar()
        ient = customtkinter.CTkEntry(master=frameloop,
                                      textvariable=ientry,
                                      width=50,
                                      placeholder_text="0",
                                      corner_radius=10)
        ient.grid(row=1, column=2)

        ilab = customtkinter.CTkLabel(master=frameloop,
                                      text=' i ',
                                      font=("Fixedsys", 20),
                                      text_color='Green')
        ilab.grid(row=1, column=3)

        global jentry
        jentry = StringVar()
        jent = customtkinter.CTkEntry(master=frameloop,
                                      textvariable=jentry,
                                      width=50,
                                      placeholder_text="0",
                                      corner_radius=10)
        jent.grid(row=1, column=4)

        jlab = customtkinter.CTkLabel(master=frameloop,
                                      text=' j ',
                                      font=("Fixedsys", 20),
                                      text_color='#8776FF')
        jlab.grid(row=1, column=5)

        global kentry
        kentry = StringVar()
        kent = customtkinter.CTkEntry(master=frameloop,
                                      textvariable=kentry,
                                      width=50,
                                      placeholder_text="0",
                                      corner_radius=10)
        kent.grid(row=1, column=6)

        klab = customtkinter.CTkLabel(master=frameloop, text=' k ',
                                      font=("Fixedsys", 20),
                                      text_color='#0c5daf')
        klab.grid(row=1, column=7)
        ient.focus()

    temp = click_count


vectorss = [0]


def plot_it(event=None):
    global click_count, noadd

    # loopframe/vecotr placeholders
    if ientry.get() == '':
        i = 0
    else:
        i = int(ientry.get())
    if jentry.get() == '':
        j = 0
    else:
        j = int(jentry.get())
    if kentry.get() == '':
        k = 0
    else:
        k = int(kentry.get())

    # Origin placeholders
    if Oientry.get() == '':
        oi = 0
    else:
        oi = int(Oientry.get())
    if Ojentry.get() == '':
        oj = 0
    else:
        oj = int(Ojentry.get())
    if Okentry.get() == '':
        ok = 0
    else:
        ok = int(Okentry.get())

    global scrol_update
    scrol_update = customtkinter.CTkLabel(master=scrollable_frame,
                                          text=('({}). {} i + {} j + {} k ({})'
                                                .format(click_count, i, j, k,
                                                        colors[click_count % len(colors)])),
                                          font=("Roboto", 15))
    scrol_update.pack(anchor=NW)

    global u
    u = [i, j, k]
    vectorss.append(u)
    start = [oi, oj, ok]
    ax.quiver(start[0], start[1], start[2], u[0],
              u[1], u[2], color=colors[click_count % len(colors)])

    has_been_called = True
    click_count += 1


has_been_called = False


def slider_event(value, ax, fig):
    global v
    v = float(value)
    ax.set_xlim(-v, v)
    ax.set_ylim(-v, v)
    ax.set_zlim(-v, v)
    fig.canvas.draw()


def on_closing():
    root.destroy()
    root.quit()


def segmented_button_callback():
    global toplevel_window
    toplevel_window = customtkinter.CTkToplevel()
    toplevel_window.title('Scalar Product')
    toplevel_window.geometry('400x250')

    x = root.winfo_x()
    y = root.winfo_y()

    toplevel_window.geometry("+%d+%d" % (x + 50, y + 50))
    toplevel_window.wm_transient(root)
    info_label = customtkinter.CTkLabel(master=toplevel_window,
                                        text='Enter the # of vectors to be Solved:',
                                        font=("Roboto", 20))
    info_label.grid(row=1, column=1, pady=20, padx=20)

    global ventry1
    ventry1 = StringVar()
    vent1 = customtkinter.CTkEntry(master=toplevel_window,
                                   textvariable=ventry1,
                                   width=50,
                                   placeholder_text="1,2,3,...",
                                   corner_radius=10)
    vent1.place(x=160, y=68)
    global ventry2
    ventry2 = StringVar()
    vent2 = customtkinter.CTkEntry(master=toplevel_window,
                                   textvariable=ventry2,
                                   width=50,
                                   placeholder_text="1,2,3,...",
                                   corner_radius=10)
    vent2.place(x=250, y=68)
    global vec2
    vec2 = customtkinter.CTkLabel(master=toplevel_window,
                                  text='Scalar Product =',
                                  bg_color='Dark Green',
                                  font=("Roboto", 20))
    vec2.place(x=20, y=140)

    prod = customtkinter.CTkButton(master=toplevel_window,
                                   text="Calculate", font=('Roboto', 20),
                                   corner_radius=8, width=30,
                                   command=scalar_prod)
    prod.configure(fg_color='green')
    prod.place(x=200, y=200)

    def stay_on_top():
        toplevel_window.lift()
        toplevel_window.update()
        toplevel_window.after(1, stay_on_top)

    stay_on_top()


def scalar_prod():
    global vec2
    # Tried to remove/update the dot prod
    dot = ax.scatter(0, 0, alpha=0.75)
    dot.remove()
    a = int(ventry1.get())
    b = int(ventry2.get())

    vec1 = customtkinter.CTkLabel(master=toplevel_window,
                                  text='Scalar Product = ({}) . ({})'.format(vectorss[a], vectorss[b]),
                                  font=("Roboto", 20))
    vec1.place(x=20, y=110)

    x = []
    for i in range(3):
        x.append((vectorss[a][i]) * (vectorss[b][i]))
    ans = sum(x)

    vec2.configure(text=f"Scalar Product = {ans}")

    # dot product plot
    dot = ax.scatter(ans, 0, alpha=0.75)
    # problem: update/detele on button press


temp = 0
click_count = 1
root = customtkinter.CTk()
root.geometry("1000x700")
root.title('3D Vector Plotting')
root.protocol("WM_DELETE_WINDOW", on_closing)

# left pannel
frame_graph = customtkinter.CTkFrame(master=root, width=400)
frame_graph.pack(side='left', fill="both")

# right pannel
frame_interact = customtkinter.CTkFrame(master=root,
                                        fg_color='transparent',
                                        width=350)
frame_interact.pack(side='right', fill="both")

slider = customtkinter.CTkSlider(master=frame_interact,
                                 height=400,
                                 width=20,
                                 from_=0,
                                 to=100,
                                 orientation=VERTICAL,
                                 command=lambda value: slider_event(value, ax, fig))
slider.pack(side='left', padx=1)

#==================key_binding===========================================================

def plot(event):
    plot_it(event=None)

def add(event):
    add_vector()
    

def product(event):
    segmented_button_callback()


def quit(event):
    on_closing()

def iE(event):
    ient.focus()
    
def jE(event):
    jent.focus()

def kE(event):
    kent.focus()

root.bind('<Return>',plot)
root.bind('<Control-Key-+>',add)
root.bind('<Control-Key-*>',product)
root.bind('<Control-Key-1>',iE)
root.bind('<Control-Key-2>',jE)
root.bind('<Control-Key-3>',kE)
root.bind('<Control-Key-minus>', quit)

# ======================Graphing stu============================
fig = plt.figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(projection="3d")
ax.zaxis.set_pane_color((0.68, 0.68, 0.68, 0.68))

# x,y,z axes
ax.plot([0, 0], [0, 0], [-100, 100], color='#0c5daf', linewidth=1.5)
ax.plot([0, 0], [-100, 100], [0, 0], color='#8776FF', linewidth=1.5)
ax.plot([-100, 100], [0, 0], [0, 0], color='Green', linewidth=1.5)

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.xaxis.label.set_color('Green')
ax.yaxis.label.set_color('#8776FF')
ax.zaxis.label.set_color('#0c5daf')
# packing fig inside tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=frame_graph)
controls = NavigationToolbar2Tk(canvas, frame_graph, pack_toolbar=False)
controls.update()

canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
controls.pack(side=TOP, fill=BOTH)
# ==================================================================


segemented_button = customtkinter.CTkButton(master=frame_interact,
                                            text="Product",
                                            font=('Roboto', 18),
                                            corner_radius=8,
                                            width=25,
                                            command=segmented_button_callback)
segemented_button.pack(anchor=NW, pady=20)

customtkinter.CTkLabel(master=frame_interact,
                       text='Origin',
                       corner_radius=10,
                       font=("Roboto", 15)).place(x=120, y=20)

global Oientry
Oientry = StringVar()
Oient = customtkinter.CTkEntry(master=frame_interact,
                               textvariable=Oientry,
                               width=40,
                               corner_radius=10)
Oient.place(x=180, y=20)
Oilab = customtkinter.CTkLabel(master=frame_interact,
                               text=' i ',
                               font=("Roboto", 25),
                               text_color='Green')
Oilab.place(x=220, y=20)

global Ojentry
Ojentry = StringVar()
Ojent = customtkinter.CTkEntry(master=frame_interact,
                               textvariable=Ojentry,
                               width=40,
                               corner_radius=10)
Ojent.place(x=240, y=20)

Ojlab = customtkinter.CTkLabel(master=frame_interact,
                               text=' j ',
                               font=("Roboto", 25),
                               text_color='#8776FF')
Ojlab.place(x=280, y=20)

global Okentry
Okentry = StringVar()
Okent = customtkinter.CTkEntry(master=frame_interact,
                               textvariable=Okentry,
                               width=40,
                               corner_radius=10)
Okent.place(x=300, y=20)

Oklab = customtkinter.CTkLabel(master=frame_interact,
                               text=' k ',
                               font=("Roboto", 25),
                               text_color='#0c5daf')
Oklab.place(x=340, y=20)

customtkinter.CTkLabel(master=frame_interact,
                       text='Default:(0,0,0)',
                       corner_radius=10,
                       text_color='grey',
                       font=("Roboto", 15)).place(x=120, y=48)

Add_Button = customtkinter.CTkButton(master=frame_interact,
                                     text='+',
                                     font=('Roboto', 25),
                                     corner_radius=8,
                                     width=50,
                                     command=add_vector)
Add_Button.pack(side='top', pady=10)

Plot_button = customtkinter.CTkButton(master=frame_interact,
                                      height=60,
                                      text='Plot',
                                      fg_color='green',
                                      font=('Roboto', 20),
                                      corner_radius=10,
                                      width=100,
                                      command=plot_it)
Plot_button.pack(side='bottom', fill=BOTH)
scrollable_frame2 = customtkinter.CTkScrollableFrame(master=frame_interact,
                                                     width=400,
                                                     height=700)
scrollable_frame2.pack()

scrollable_frame = customtkinter.CTkScrollableFrame(master=frame_graph,
                                                    width=300,
                                                    height=200)
scrollable_frame.place(x=0, y=543)

root.mainloop()

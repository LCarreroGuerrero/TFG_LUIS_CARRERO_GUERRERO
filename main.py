import customtkinter as ctk
import tkinter

app = ctk.CTk()
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app.title("Ayuda interactiva - Google Password Manager")
app.after(0, lambda: app.wm_state('zoomed'))


# Main container
content_frame = ctk.CTkFrame(app)
content_frame.pack(fill="both", expand=True)

# Views frames
main_view = ctk.CTkFrame(content_frame)
view_help = ctk.CTkFrame(content_frame)


def show_view(view):
    for frame in [main_view, view_help]:
        frame.pack_forget()
    view.pack(fill="both", expand=True)

def return_to_main_view():
    show_view(main_view)


""" Main view content  """
# Header
header_frame = ctk.CTkFrame(main_view, height=70, fg_color="green")
header_frame.pack(side="top", pady=30, fill="both")

header_label = ctk.CTkLabel(
    header_frame,
    text="Ayuda interactiva - Google Password Manager",
    font=("Arial", 30, "bold"),
    text_color="#ffffff"
)
header_label.pack(pady=10, padx=20)


# SubHeader
subheader_frame = ctk.CTkFrame(main_view, fg_color="green")
subheader_frame.pack(side="top")

subheader_label = ctk.CTkLabel(
    subheader_frame,
    text="Selecciona tu duda para recibir ayuda.",
    font=("Arial", 24),
    text_color="#ffffff"
)
subheader_label.pack(pady=10, padx=20)


# Guide selector Buttons at Main view
buttons_frame = ctk.CTkFrame(main_view)
buttons_frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

buttons = []
for i in range(8):
    button = ctk.CTkButton(
        buttons_frame,
        text=f"Duda {i+1}",
        width=400,
        height=300,
        command=lambda: show_view(view_help)
    )
    buttons.append(button)

for idx, button in enumerate(buttons):
    row = idx // 4
    col = idx % 4
    button.grid(row=row, column=col, padx=10, pady=10)


""" Help view content  """
# Help view Header
header_frame = ctk.CTkFrame(view_help, height=70, fg_color="#1F6AA5")
header_frame.pack(side="top", pady=20, fill="both")

header_label = ctk.CTkLabel(
    header_frame,
    text="Ayuda interactiva - Google Password Manager",
    font=("Arial", 30, "bold"),
    text_color="#ffffff"
)
header_label.pack(pady=10, padx=20)

# SubHeader
subheader_frame = ctk.CTkFrame(view_help, fg_color="#1F6AA5")
subheader_frame.pack(side="top")

subheader_label = ctk.CTkLabel(
    subheader_frame,
    text="Proceso de ejecución de la tarea seleccionada:",
    font=("Arial", 24),
    text_color="#ffffff"
)
subheader_label.pack(pady=5, padx=20)

# Guide selector Buttons at Main view
process_frame = ctk.CTkFrame(view_help, fg_color="#4A90E2")
process_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

process_block = []
for i in range(6):
    block = ctk.CTkLabel(
        process_frame,
        text=f"Parte {i+1} del proceso" + "\n\n Imagen explicativa",
        font=("Arial", 24),
        width=500,
        height=300,
        padx=40,
        pady=40,
        corner_radius=10,
        fg_color="white"
    )
    process_block.append(block)

for idx, block in enumerate(process_block):
    row = idx // 3
    col = idx % 3
    block.grid(row=row, column=col, padx=10, pady=10)



# Back to Main view Button    
button_return = ctk.CTkButton(view_help,
                              text="Volver a la página Principal",
                              height=50,
                              corner_radius=30,
                              font=("Arial", 20, "bold"),
                              command=return_to_main_view)
button_return.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)



show_view(main_view)
app.mainloop()

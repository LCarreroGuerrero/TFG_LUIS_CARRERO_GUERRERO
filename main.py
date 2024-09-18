import customtkinter as ctk
import tkinter


""" Initializator """
# Declaración de la variable que guardará la aplicación con parámetros de "sizing" y aspecto
app = ctk.CTk() 
app.title("Ayuda interactiva - Google Password Manager")
app.after(0, lambda: app.wm_state('zoomed'))

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


# Declaración de los frames y las principales vistas
content_frame = ctk.CTkFrame(app)
content_frame.pack(fill="both", expand=True)

main_view = ctk.CTkFrame(content_frame)
view_help = ctk.CTkFrame(content_frame)


# Definición de las funciones de manejo de vistas
def show_view(view):
    for frame in [main_view, view_help]:
        frame.pack_forget()
    view.pack(fill="both", expand=True)

def return_to_main_view():
    show_view(main_view)
    

""" Main view content  """
# Declaración del Header de la "main view"
header_frame = ctk.CTkFrame(main_view, height=70, fg_color="green")
header_frame.pack(side="top", pady=30, fill="both")

header_label = ctk.CTkLabel(
    header_frame,
    text="Ayuda interactiva - Google Password Manager",
    font=("Arial", 30, "bold"),
    text_color="#ffffff"
)
header_label.pack(pady=10, padx=20)


# Declaración del Subheader de la "main view"
subheader_frame = ctk.CTkFrame(main_view, fg_color="green")
subheader_frame.pack(side="top")

subheader_label = ctk.CTkLabel(
    subheader_frame,
    text="Selecciona tu duda para recibir ayuda.",
    font=("Arial", 24),
    text_color="#ffffff"
)
subheader_label.pack(pady=10, padx=20)


# Declaración de los botones de acceso a las guias
buttons_frame = ctk.CTkFrame(main_view)
buttons_frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


# Generación de los botones por parámetro numérico 
# para permitir variar el número de guias disponibles
buttons = []
for i in range(8):
    button = ctk.CTkButton(
        buttons_frame,
        text=f"Duda {i+1}",
        font=("Arial", 30, "bold"),
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
# Declaración del Header de la "help view"
header_frame = ctk.CTkFrame(view_help, height=70, fg_color="#1F6AA5")
header_frame.pack(side="top", pady=20, fill="both")

header_label = ctk.CTkLabel(
    header_frame,
    text="Ayuda interactiva - Google Password Manager",
    font=("Arial", 30, "bold"),
    text_color="#ffffff"
)
header_label.pack(pady=10, padx=20)


# Declaración del Subheader de la "help view"
subheader_frame = ctk.CTkFrame(view_help, fg_color="#1F6AA5")
subheader_frame.pack(side="top")

subheader_label = ctk.CTkLabel(
    subheader_frame,
    text="Proceso de ejecución de la tarea seleccionada:",
    font=("Arial", 24),
    text_color="#ffffff"
)
subheader_label.pack(pady=5, padx=20)


# Declaración de los frames de bloques de texto para las guías
process_frame = ctk.CTkFrame(view_help, fg_color="#4A90E2")
process_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


# Generación de los bloques que contendrán cada paso de las guias
# por parámetro numérico para permitir variar el número de guias disponibles
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


# Botón de llamada a la función de retornar a la "main view" 
button_return = ctk.CTkButton(view_help,
                              text="Volver a la página Principal",
                              height=50,
                              corner_radius=30,
                              font=("Arial", 20, "bold"),
                              command=return_to_main_view)
button_return.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


# Llamada de inicialización del proyecto
show_view(main_view)
app.mainloop()

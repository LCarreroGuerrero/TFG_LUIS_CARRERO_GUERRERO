import customtkinter as ctk
import tkinter

# Configuración de la aplicación principal
app = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app.title("Ayuda interactiva - Google Password Manager")
app.geometry("1000x700")

# Crear un frame para el header (encabezado)
header_frame = ctk.CTkFrame(app, height=50, fg_color="#2b2b2b")
header_frame.pack(side="top", fill="x")

# Etiqueta dentro del header
header_label = ctk.CTkLabel(
    header_frame,
    text="Encabezado de la Aplicación",
    font=("Arial", 16, "bold"),
    text_color="#ffffff"
)
header_label.pack(pady=10, padx=20)

# Crear contenedor principal para las vistas
content_frame = ctk.CTkFrame(app)
content_frame.pack(fill="both", expand=True)

# Crear frames para las diferentes vistas
main_view = ctk.CTkFrame(content_frame)
view1 = ctk.CTkFrame(content_frame)
view2 = ctk.CTkFrame(content_frame)

# Función para mostrar una vista y ocultar las demás
def show_view(view):
    for frame in [main_view, view1, view2]:
        frame.pack_forget()
    view.pack(fill="both", expand=True)

# Función para volver a la vista principal desde las otras vistas
def return_to_main_view():
    show_view(main_view)

# Configuración de la vista principal
buttons_frame = ctk.CTkFrame(main_view)
buttons_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Crear botones para la vista principal
buttons = []
for i in range(8):
    if i == 0:
        button = ctk.CTkButton(
            buttons_frame,
            text=f"Botón {i+1}",
            width=100,
            height=100,
            command=lambda: show_view(view1)  # Botón 1 cambia a la vista 1
        )
    elif i == 1:
        button = ctk.CTkButton(
            buttons_frame,
            text=f"Botón {i+1}",
            width=100,
            height=100,
            command=lambda: show_view(view2)  # Botón 2 cambia a la vista 2
        )
    else:
        button = ctk.CTkButton(
            buttons_frame,
            text=f"Botón {i+1}",
            width=100,
            height=100,
            command=lambda: print(f"Botón {i+1} presionado")
        )
    buttons.append(button)

# Organizar los botones en un grid de 4 columnas y 2 filas
for idx, button in enumerate(buttons):
    row = idx // 4
    col = idx % 4
    button.grid(row=row, column=col, padx=10, pady=10)

# Configuración de la primera vista
label_view1 = ctk.CTkLabel(view1, text="Vista 1 - Contenido de la Presentación")
label_view1.pack(pady=20)
button_return1 = ctk.CTkButton(view1, text="Volver a la Vista Principal", command=return_to_main_view)
button_return1.pack(pady=20)

# Configuración de la segunda vista
label_view2 = ctk.CTkLabel(view2, text="Vista 2 - Contenido de la Presentación")
label_view2.pack(pady=20)
button_return2 = ctk.CTkButton(view2, text="Volver a la Vista Principal", command=return_to_main_view)
button_return2.pack(pady=20)

# Mostrar la vista principal al iniciar
show_view(main_view)

# Ejecutar la aplicación
app.mainloop()

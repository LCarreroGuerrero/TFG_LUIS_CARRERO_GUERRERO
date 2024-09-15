import customtkinter as ctk
from views.views_manager import setup_views, show_view, main_view

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

# Configurar y mostrar las vistas
setup_views(content_frame)  # Asegúrate de llamar a setup_views primero para inicializar las vistas
show_view(main_view)  # Mostrar la vista principal

# Ejecutar la aplicación
app.mainloop()

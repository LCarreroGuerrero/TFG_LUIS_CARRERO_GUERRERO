import customtkinter as ctk
from utils.main_view_blocks import create_main_buttons
from views.view_check_pass import setup_view_check_pass
from views.view_send_pass import setup_view_send_pass

# Inicializar las variables globales de las vistas
main_view = None
view_check_pass = None
view_send_pass = None

# Función para mostrar una vista y ocultar las demás
def show_view(view):
    if view is not None:
        for frame in [main_view, view_check_pass, view_send_pass]:
            if frame is not None:
                frame.pack_forget()
        view.pack(fill="both", expand=True)
    else:
        print("Error: La vista solicitada no está inicializada correctamente.")

# Función para volver a la vista principal
def return_to_main_view():
    show_view(main_view)

# Configurar las vistas
def setup_views(content_frame):
    global main_view, view_check_pass, view_send_pass
    
    # Asignar los frames a las variables globales
    try:
        main_view = ctk.CTkFrame(master=content_frame)
        view_check_pass = ctk.CTkFrame(master=content_frame)
        view_send_pass = ctk.CTkFrame(master=content_frame)
        
        print("Vistas inicializadas correctamente.")  # Mensaje de verificación
    except Exception as e:
        print(f"Error al inicializar las vistas: {e}")

    # Verifica que las vistas se han inicializado correctamente
    if main_view is None or view_check_pass is None or view_send_pass is None:
        print("Error: Una o más vistas no se inicializaron correctamente.")
        return

    # Configurar la vista principal y pasar las funciones como argumentos
    create_main_buttons(main_view, show_view, view_check_pass, view_send_pass)

    # Configurar las otras vistas
    setup_view_check_pass(view_check_pass, return_to_main_view)
    setup_view_send_pass(view_send_pass, return_to_main_view)
    
    # Imprime para confirmar que las vistas se asignaron correctamente
    print(f"main_view: {main_view}, view_check_pass: {view_check_pass}, view_send_pass: {view_send_pass}")

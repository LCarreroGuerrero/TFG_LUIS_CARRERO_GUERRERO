import customtkinter as ctk

# Configurar la vista "Check Pass"
def setup_view_check_pass(view, return_to_main_view):
    label_view1 = ctk.CTkLabel(view, text="Vista Check Pass - Contenido de la Presentación")
    label_view1.pack(pady=20)
    button_return1 = ctk.CTkButton(view, text="Volver a la Vista Principal", command=return_to_main_view)
    button_return1.pack(pady=20)

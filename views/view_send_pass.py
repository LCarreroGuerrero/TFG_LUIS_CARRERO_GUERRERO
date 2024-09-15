import customtkinter as ctk

# Configurar la vista "Send Pass"
def setup_view_send_pass(view, return_to_main_view):
    label_view2 = ctk.CTkLabel(view, text="Vista Send Pass - Contenido de la Presentación")
    label_view2.pack(pady=20)
    button_return2 = ctk.CTkButton(view, text="Volver a la Vista Principal", command=return_to_main_view)
    button_return2.pack(pady=20)

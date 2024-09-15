import customtkinter as ctk

# Crear y organizar los botones de la vista principal
def create_main_buttons(main_view, show_view, view_check_pass, view_send_pass):
    # Crear un frame dentro de main_view para organizar los botones
    buttons_frame = ctk.CTkFrame(main_view)
    buttons_frame.pack(pady=20, padx=20)  # Asegúrate de que el frame de los botones se muestra

    # Crear botones para la vista principal
    buttons = []
    for i in range(8):
        if i == 0:
            button = ctk.CTkButton(
                buttons_frame,
                text=f"Botón {i+1}",
                width=100,
                height=100,
                command=lambda: show_view(view_check_pass)  # Botón 1 cambia a la vista "check pass"
            )
        elif i == 1:
            button = ctk.CTkButton(
                buttons_frame,
                text=f"Botón {i+1}",
                width=100,
                height=100,
                command=lambda: show_view(view_send_pass)  # Botón 2 cambia a la vista "send pass"
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
        button.grid(row=row, column=col, padx=10, pady=10)  # Usamos grid para colocar los botones

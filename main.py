import customtkinter as ctk
import tkinter

app = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app.title("Ayuda interactiva - Google Password Manager")
app.geometry("1000x700")

# Header
header_frame = ctk.CTkFrame(app, height=70, fg_color="#2b2b2b")
header_frame.pack(side="top", pady=30, fill="both")

header_label = ctk.CTkLabel(
    header_frame,
    text="Ayuda interactiva - Google Password Manager",
    font=("Arial", 27, "bold"),
    text_color="#ffffff"
)
header_label.pack(pady=10, padx=20)

# Main container
content_frame = ctk.CTkFrame(app)
content_frame.pack(fill="both", expand=True)

# Views frames
main_view = ctk.CTkFrame(content_frame)
view1 = ctk.CTkFrame(content_frame)
view2 = ctk.CTkFrame(content_frame)

def show_view(view):
    for frame in [main_view, view1, view2]:
        frame.pack_forget()
    view.pack(fill="both", expand=True)

def return_to_main_view():
    show_view(main_view)


# Guide selector Buttons at Main view
buttons_frame = ctk.CTkFrame(main_view)
buttons_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

buttons = []
for i in range(8):
    if i == 0:
        button = ctk.CTkButton(
            buttons_frame,
            text=f"Botón {i+1}",
            width=100,
            height=100,
            command=lambda: show_view(view1) 
        )
    elif i == 1:
        button = ctk.CTkButton(
            buttons_frame,
            text=f"Botón {i+1}",
            width=100,
            height=100,
            command=lambda: show_view(view2)
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

for idx, button in enumerate(buttons):
    row = idx // 4
    col = idx % 4
    button.grid(row=row, column=col, padx=10, pady=10)


# First view content
label_view1 = ctk.CTkLabel(view1, text="Guia de procesos - Consultar Contraseña")
label_view1.pack(pady=20)
button_return1 = ctk.CTkButton(view1, text="Volver a la página Principal", command=return_to_main_view)
button_return1.pack(pady=20)

# Second view content
label_view2 = ctk.CTkLabel(view2, text="Guia de procesos - Enviar contraseña a otro dispositivo")
label_view2.pack(pady=20)
button_return2 = ctk.CTkButton(view2, text="Volver a la página Principal", command=return_to_main_view)
button_return2.pack(pady=20)



show_view(main_view)
app.mainloop()

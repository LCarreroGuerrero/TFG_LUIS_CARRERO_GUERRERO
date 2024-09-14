import customtkinter as ctk
from PIL import Image, ImageTk

def create_tab():
    tab2 = ctk.CTkToplevel()
    tab2.title("Pestaña 2 - Presentación")
    tab2.geometry("800x600")

    # Ejemplo de cómo cargar y mostrar otra imagen
    image = Image.open("assets/images/imagen2.png")  # Ruta a la imagen
    image = image.resize((400, 300))
    img_display = ImageTk.PhotoImage(image)

    image_label = ctk.CTkLabel(tab2, image=img_display, text="")
    image_label.image = img_display
    image_label.pack(pady=20)

    # Ejemplo de texto explicativo
    text_label = ctk.CTkLabel(tab2, text="Otra explicación sobre la imagen", font=("Arial", 14))
    text_label.pack(pady=10)

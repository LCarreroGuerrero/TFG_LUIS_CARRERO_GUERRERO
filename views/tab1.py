import customtkinter as ctk
from PIL import Image, ImageTk

def create_tab():
    tab1 = ctk.CTkToplevel()  # Crear una nueva ventana
    tab1.title("Pestaña 1 - Presentación")
    tab1.geometry("800x600")

    # Ejemplo de cómo cargar y mostrar una imagen
    image = Image.open("assets/images/imagen1.png")  # Ruta a la imagen
    image = image.resize((400, 300))  # Redimensionar si es necesario
    img_display = ImageTk.PhotoImage(image)

    image_label = ctk.CTkLabel(tab1, image=img_display, text="")
    image_label.image = img_display  # Necesario para mantener la referencia de la imagen
    image_label.pack(pady=20)

    # Ejemplo de texto explicativo
    text_label = ctk.CTkLabel(tab1, text="Explicación sobre la imagen", font=("Arial", 14))
    text_label.pack(pady=10)
import qrcode
from tkinter import Tk, Label, Entry, Button, StringVar, Toplevel, Frame
from tkinter import font as tkFont
from PIL import Image, ImageDraw, ImageFont

# Palette de couleurs disponibles
COLOR_PALETTE = [
    "#FFDD0F", "#33FF57", "#3357FF",
    "#0C973C", "#3485D4", "#1A3D9A", 
    "#EE0000", "#4874A9", "#303234", 
    "#F1C40F", "#9B59B6", "#1ABC9C",
    "#E67E22", "#2ECC71", "#E74C3C",
    "#000000", "#FFFFFF", "#106B62", 
]

def generate_wifi_qr(ssid, password, text_color, bg_color):
    wifi_config = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)
    img = qr.make_image(fill_color=text_color, back_color=bg_color).convert('RGB')

    text = f"Nom WIFI : {ssid}\nMot de passe : {password}"
    try:
        font = ImageFont.truetype("Ubuntu.ttf", size=22)
    except IOError:
        font = ImageFont.load_default()

    draw = ImageDraw.Draw(img)
    lines = text.split('\n')
    line_heights = []
    max_width = 0

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]
        max_width = max(max_width, width)
        line_heights.append(height)

    text_height = sum(line_heights) + (len(lines) - 1) * 4
    text_width = max_width
    new_img_height = img.height + text_height + 20
    new_img = Image.new("RGB", (img.width, new_img_height), bg_color)
    new_img.paste(img, (0, 0))

    draw = ImageDraw.Draw(new_img)
    text_x = (img.width - text_width) // 2
    text_y = img.height + 10
    draw.multiline_text((text_x, text_y), text, fill=text_color, font=font, align="center")

    filename = f"wifi_qr_{ssid}.png"
    new_img.save(filename)
    return filename

# Choisir une couleur dans la palette
def choose_color_palette(var, color_display, title):
    palette_window = Toplevel(app)
    palette_window.title(title)
    palette_window.configure(bg="white")

    def set_color(color):
        var.set(color)
        color_display.config(bg=color)  
        palette_window.destroy()
    for i, color in enumerate(COLOR_PALETTE):
        btn = Button(palette_window, bg=color, width=1, height=1, command=lambda c=color: set_color(c))
        btn.grid(row=i // 3, column=i % 3, padx=1, pady=1, ipadx=1, ipady=1)



def generate():
    wifi_name = wifi_name_var.get()
    password = password_var.get()
    text_color = text_color_var.get()
    bg_color = bg_color_var.get()
    if wifi_name and password:
        filename = generate_wifi_qr(wifi_name, password, text_color, bg_color)
        result_label.config(text=f"QR sauvegardé : {filename}")
        
        wifi_name_display.config(text=f"Nom WIFI : {wifi_name}")
        password_display.config(text=f"Mot de passe : {password}")


# === Interface Graphique ===

app = Tk()
app.title("QR Code Wi-Fi")
app.geometry("420x400")
app.configure(bg="#106B62")

font_ubuntu = tkFont.Font(family="Ubuntu", size=11)

# Variables
wifi_name_var = StringVar()
password_var = StringVar()
text_deafault_black_color_var = StringVar(value="#000000")  
bg_default_white_color_var = StringVar(value="#FFFFFF")    

# Frame pour organiser les éléments
frame = Frame(app, bg="#106B62")
frame.pack(padx=15, pady=15)

# Widgets
Label(frame, text="Nom du Wi-Fi :", bg="#106B62", fg="white", font=font_ubuntu).grid(row=0, column=0, pady=5, sticky="w")
Entry(frame, textvariable=wifi_name_var, font=font_ubuntu).grid(row=0, column=1, pady=5)

Label(frame, text="Mot de passe Wi-Fi :", bg="#106B62", fg="white", font=font_ubuntu).grid(row=1, column=0, pady=5, sticky="w")
Entry(frame, textvariable=password_var, font=font_ubuntu, show="*").grid(row=1, column=1, pady=5)

Label(frame, text="Couleur du texte :", bg="#106B62", fg="white", font=font_ubuntu).grid(row=2, column=0, pady=5, sticky="w")
text_color_button = Button(frame, text="Choisir une couleur", command=lambda: choose_color_palette(text_deafault_black_color_var, text_color_display, "Couleur du texte"),
                           font=font_ubuntu, bg="white", fg="black", width=15, height=1)
text_color_button.grid(row=2, column=1, pady=5, sticky="w")

# Petit carré à droite du bouton pour afficher la couleur choisie
text_color_display = Label(frame, width=2, height=1, bg="black") 
text_color_display.grid(row=2, column=2, padx=10)

Label(frame, text="Couleur de fond :", bg="#106B62", fg="white", font=font_ubuntu).grid(row=3, column=0, pady=5, sticky="w")
bg_color_button = Button(frame, text="Choisir une couleur", command=lambda: choose_color_palette(bg_default_white_color_var, bg_color_display, "Couleur de fond"),
                         font=font_ubuntu, bg="white", fg="black", width=15, height=1)
bg_color_button.grid(row=3, column=1, pady=5, sticky="w")

# Petit carré à droite du bouton pour afficher la couleur choisie
bg_color_display = Label(frame, width=2, height=1, bg="white") 
bg_color_display.grid(row=3, column=2, padx=10)

Button(frame, text="Générer le QR Code", command=generate,
       font=font_ubuntu, bg="white", fg="black", width=15, height=1).grid(row=4, column=0, columnspan=3, pady=20)

result_label = Label(app, text="", bg="#106B62", fg="lightgreen", font=font_ubuntu)
result_label.pack()

def copy_to_clipboard(text):
    app.clipboard_clear()
    app.clipboard_append(text)
    app.update()
    result_label.config(text=f"Copié : {text}")

# Affichage cliquable du nom du wifi et du mot de passe
wifi_name_display = Label(app, text="", fg="white", bg="#106B62", font=(font_ubuntu.actual("family"), 11, "underline"), cursor="hand2")
wifi_name_display.pack()
wifi_name_display.bind("<Button-1>", lambda e: copy_to_clipboard(wifi_name_var.get()))

password_display = Label(app, text="", fg="white", bg="#106B62", font=(font_ubuntu.actual("family"), 11, "underline"), cursor="hand2")
password_display.pack()
password_display.bind("<Button-1>", lambda e: copy_to_clipboard(password_var.get()))

# Signature 
signature_label = Label(app, text="NSAADI - UPEC - 2021", bg="#106B62", fg="lightgray", font=(font_ubuntu.actual("family"), 7, "italic"))
signature_label.pack(pady=(10, 5))


app.mainloop()


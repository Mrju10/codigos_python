import qrcode

# URL que deseas codificar en el QR
url = "https://tu_url"


# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear una imagen del código QR
qr_img = qr.make_image(fill_color="black", back_color="white")

# Guardar el código QR en un archivo de imagen
qr_img.save("codigo_qr.png")

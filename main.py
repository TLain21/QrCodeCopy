import qrcode

def generate_qr_codde(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(file_name)

text = "https://linkedin.com/in/alvin-timotius-saragih"
file_name = "qr_code.png"
generate_qr_codde(text, file_name)
print(f"QR code saved at {file_name}")

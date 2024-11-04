import qrcode
from PIL import Image

# Function to create and display QR code from URL
def show_qr_code(url):
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.show() 


url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
show_qr_code(url)

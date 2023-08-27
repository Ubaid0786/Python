import qrcode
from PIL import Image

# Create a QRCode object with desired parameters
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data to the QR code
qr.add_data("Hello Ubaid")
qr.make(fit=True)

# Generate a QR code images
qr_img = qr.make_image(fill_color="aqua", back_color="white")  # Using white background

# Open and resize a background image
background_image = Image.open("background.jpg")  # Replace with your own background image
bg_width, bg_height = qr_img.size
background_image = background_image.resize((bg_width, bg_height), Image.ANTIALIAS)

# Composite the QR code on top of the background
qr_with_background = Image.new("RGBA", qr_img.size)
qr_with_background.paste(background_image, (0, 0))
qr_with_background.paste(qr_img, (0, 0), qr_img)

# Save the composite image with QR code
qr_with_background.save("beautifulQRcode.png")

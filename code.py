import qrcode
import cv2
from pyzbar.pyzbar import decode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def decode_qr_code(filename):
    image = cv2.imread(filename)
    decoded_objects = decode(image)
    for obj in decoded_objects:
        print("Data:", obj.data.decode())
        print("Type:", obj.type)

if __name__ == "__main__":
    # Example usage
    data_to_encode = "https://www.example.com"
    filename = "example_qr_code.png"
    
    generate_qr_code(data_to_encode, filename)
    print("QR code generated successfully.")

    print("Decoding QR code...")
    decode_qr_code(filename)

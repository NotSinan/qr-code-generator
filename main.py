import argparse

import pyqrcode

def create_qr_code(text: str):
    url = pyqrcode.create(text)
    url.svg("qrcode.svg", scale=8)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate a QR code from an input string')
    parser.add_argument('input_string', type=str, help='Input string to generate QR code from')
    args = parser.parse_args()

    create_qr_code(args.input_string)

import argparse
import pyqrcode
import os


def create_qr_code(text: str, output_file: str = None, output_format: str = 'svg'):
    url = pyqrcode.create(text)
    if output_file:
        if output_format.lower() == 'svg':
            url.svg(output_file, scale=8)
        elif output_format.lower() == 'png':
            url.png(output_file, scale=8)
        else:
            print(f"Invalid output format: {output_format}")
            return
    else:
        url.svg("qrcode.svg", scale=8)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a QR code from an input string')
    parser.add_argument('input_string', type=str, help='Input string to generate QR code from')
    parser.add_argument('--output-file', type=str, help='Output file name', default='qrcode')
    parser.add_argument('--output-format', type=str, help='Output file format', default='svg')
    args = parser.parse_args()

    output_file = f"{args.output_file}.{args.output_format}"
    create_qr_code(args.input_string, output_file, args.output_format)

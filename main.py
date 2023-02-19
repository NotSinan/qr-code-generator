import argparse
from qrcode import generator


def main():
    # parser = argparse.ArgumentParser(description='Generate a QR code from an input string')
    # parser.add_argument('input_string', type=str, help='Input string to generate QR code from')
    # parser.add_argument('-o', '--output', type=str, help='Output file for generated QR code (default: qrcode.svg)', default='qrcode.svg')
    # parser.add_argument('-f', '--format', type=str, help='Output file format (svg or png, default: svg)', default='svg')
    # parser.add_argument('-s', '--scale', type=int, help='Size of QR code squares (default: 8)', default=8)
    # parser.add_argument('-q', '--quiet-zone', type=int, help='Size of the quiet zone around the QR code (default: 1)',default=1)
    # parser.add_argument('-c', '--bg-color', type=str, help='Background color of the QR code (white or black, default: white)', default='white')
    # args = parser.parse_args()
    #
    # # output_file = f"{args.output_file}.{args.output_format}"
    # generator.generate_qr_code(args.input_string, args.output, args.format, args.scale, args.quiet_zone, args.bg_color)
    # # print(f"QR code generated successfully and saved as {output_file}!")
    generator.generate_qr_code("Hello", "www.png", "png", 8, "#ffffff", "#FFC0CB")


if __name__ == '__main__':
    main()

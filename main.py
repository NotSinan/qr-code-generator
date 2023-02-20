import argparse
from qrcode import generator


def main():
    parser = argparse.ArgumentParser(description='Generate a QR code from an input string')
    parser.add_argument('input_string', type=str, help='Input string to generate QR code from')
    parser.add_argument('-o', '--output', type=str, help='Output file for generated QR code (default: qrcode.svg)', default='qrcode.svg')
    parser.add_argument('-f', '--format', type=str, help='Output file format (svg or png, default: svg)', default='svg')
    parser.add_argument('-s', '--scale', type=int, help='Size of QR code squares (default: 8)', default=8)
    parser.add_argument('-q', '--quiet-zone', type=int, help='Size of the quiet zone around the QR code (default: 4)',default=4)
    parser.add_argument('-c', '--bg-color', type=str, help='Background color of the QR code', default='white')
    parser.add_argument('-m', '--module-color', type=str, help='Module color of the QR code', default='white')
    args = parser.parse_args()
    output_file = f"{args.output}.{args.format}"
    generator.generate_qr_code(text=args.input_string,
                               output_file=output_file,
                               output_format=args.format,
                               scale=args.scale,
                               module_color=args.module_color,
                               background=args.bg_color,
                               quiet_zone=args.quiet_zone)


if __name__ == '__main__':
    main()

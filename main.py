import argparse
from qrcode import generator


def main():
    parser = argparse.ArgumentParser(description='Generate a QR code from an input string')
    parser.add_argument('input_string', type=str, help='Input string to generate QR code from')
    parser.add_argument('--output-file', type=str, help='Output file name', default='qrcode')
    parser.add_argument('--output-format', type=str, help='Output file format', default='svg')
    args = parser.parse_args()

    output_file = f"{args.output_file}.{args.output_format}"
    generator.generate_qr_code(args.input_string, output_file, args.output_format)
    print(f"QR code generated successfully and saved as {output_file}!")


if __name__ == '__main__':
    main()

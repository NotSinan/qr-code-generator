# QR Code Generator

This script generates a QR code from an input string. The QR code can be outputted in either SVG or PNG format.

## Installation
1. Clone or download this repository.
2. Install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Usage

The script can be run from the command line using the following command:
```
python qr_code_generator.py input_string [-o OUTPUT] [-f FORMAT] [-s SCALE] [-q QUIET_ZONE] [-c BG_COLOR] [-m MODULE_COLOR]
```

## Arguments
* input_string: Required input string to generate the QR code from.
* -o, --output: Output file for generated QR code (default: qrcode.svg).
* -f, --format: Output file format (svg or png, default: svg).
* -s, --scale: Size of QR code squares (default: 8).
* -q, --quiet-zone: Size of the quiet zone around the QR code (default: 4).
* -c, --bg-color: Background color of the QR code (default: white).
* -m, --module-color: Module color of the QR code (default: white).

## Example Usage

To generate a QR code for the input string "Hello, world!" with the default options:

```
python qr_code_generator.py "Hello, world!"
```

To generate a PNG QR code with a quiet zone size of 10 and a red background color:
```
python qr_code_generator.py "Hello, world!" -o output -f png -q 10 -c red
```

import pyqrcode


def generate_qr_code(text: str, output_file: str = None, output_format: str = 'svg'):
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
        return url.svg_as_string(scale=8)

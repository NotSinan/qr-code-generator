import pyqrcode


def generate_qr_code(text: str,
                     output_file: str = None,
                     output_format: str = 'svg',
                     scale: int = 8,
                     module_color: tuple = (255, 255, 255),
                     background: str = None):
    url = pyqrcode.create(text)

    if output_file:
        if output_format.lower() == 'svg':
            url.svg(output_file, scale=scale, module_color=module_color, background=background)
        elif output_format.lower() == 'png':
            url.png(output_file, scale=scale, module_color=module_color, background=background)
        else:
            print(f"Invalid output format: {output_format}")
            return
    else:
        return url.svg_as_string(scale=8)

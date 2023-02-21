import pyqrcode


def generate_qr_code(text: str,
                     output_file: str = None,
                     output_format: str = 'svg',
                     scale: int = 8,
                     module_color: str = "#FFFFFF",
                     background: str = None,
                     quiet_zone: int = 4):

    url = pyqrcode.create(text)

    try:
        if output_file:
            if output_format.lower() == 'svg':
                url.svg(output_file, scale=scale, module_color=module_color, background=background,
                        quiet_zone=quiet_zone)
            elif output_format.lower() == 'png':
                url.png(output_file, scale=scale, module_color=module_color, background=background,
                        quiet_zone=quiet_zone)
            else:
                print(f"Invalid output format: {output_format}")
                return
        else:
            return url.svg_as_string(scale=8)
    except FileNotFoundError:
        print(f"The file or directory does not exist: {output_file}")

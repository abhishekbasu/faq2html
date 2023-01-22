import click

from .generate_html import generate_faq_html
from .read_docx import extract_text

@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.argument("output_filename", type=click.Path(exists=False))
def converter(filename, output_filename):
    parsed_text = extract_text(filename)
    with open(output_filename, "w") as f:
        f.write(generate_faq_html(parsed_text))

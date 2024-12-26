import click
import sys

from repositories.html_repository import HtmlRepository
from services.split_html import split_html


@click.command()
@click.option(
    "--file",
    type=click.Path(exists=True),
    required=True,
    help="Path to the HTML file."
)
@click.option(
    "--max-length",
    type=int,
    default=4096,
    help="Maximum length of each fragment."
)
@click.option(
    "--output",
    type=click.Path(writable=True),
    default="output_fragments.txt",
    help="File to save the fragments."
)
def splitter_html(file: str, max_length: int, output: str) -> None:
    """
    Split the HTML content into fragments, preserving the tag structure.
    """
    with open(file, "r", encoding="utf-8") as f:
        html_content = f.read()

    fragments = split_html(html_content, max_length)

    repository = HtmlRepository(output)
    repository.save_html_fragments(fragments)

    for fragment in fragments:
        mark_start = f"--- Fragment #{fragment.fragment_number} {len(fragment.content)} chars ---\n"
        sys.stdout.write(mark_start)
        sys.stdout.write(fragment.content)
        sys.stdout.write("\n\n")

    sys.stdout.write(f"Splitting complete. Fragments saved in {output}")

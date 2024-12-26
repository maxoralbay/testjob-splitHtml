from typing import List
from models.html_fragment import HtmlFragment


class HtmlRepository:
    def __init__(self, output_path: str):
        self.output_path = output_path

    def save_html_fragments(self, fragments: List[HtmlFragment]) -> None:
        with open(self.output_path, 'w') as out_file:
            for fragment in fragments:
                mark_start = f"--- Fragment #{fragment.fragment_number} {len(fragment.content)} chars ---\n"
                out_file.write(mark_start)
                out_file.write(fragment.content)
                out_file.write("\n\n")

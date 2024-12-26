from typing import List

class HtmlFragment:
    def __init__(self, content: str, fragment_number: int):
        self.content = content
        self.fragment_number = fragment_number

    def ___repr__(self):
        return f'HtmlFragment {self.fragment_number}, content: {len(self.content)}'
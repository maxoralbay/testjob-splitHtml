from typing import List
from bs4 import BeautifulSoup
from models.html_fragment import HtmlFragment


class HtmlSplitError(Exception):
    """Custom exception for HTML splitting errors."""
    pass


def split_html(html_content: str, max_length: int) -> List[HtmlFragment]:
    """
    Split HTML content into fragments.
    :param html_content: The original HTML content.
    :param max_length: The maximum length of each fragment.
    :return: List of HtmlFragment objects.
    :raises HtmlSplitError: If max_length is too small or a fragment is empty.
    """
    if not html_content.strip():  # Check for empty or whitespace-only HTML
        raise ValueError("Input HTML cannot be empty")

    if not isinstance(max_length, int) or max_length <= 0:
        raise ValueError("Max length must be a positive integer")

    if max_length < 10:  # Adjust threshold based on your requirements.
        raise HtmlSplitError("max_length is too small to process meaningful fragments.")

    soup = BeautifulSoup(html_content, "html.parser")
    fragments = []
    current_fragment = []
    current_length = 0
    open_tags = []

    def close_open_tags(open_tags: List[str]) -> str:
        """ Close all open tags for the current fragment. """
        return "".join(f"</{tag}>" for tag in reversed(open_tags))

    def reopen_tags(open_tags: List[str]) -> str:
        """ Reopen all open tags for the current fragment. """
        return "".join(f"<{tag}>" for tag in open_tags)

    def process_node(node) -> None:
        nonlocal current_fragment, current_length, open_tags
        if node.name:
            tag_start = str(node).split(">")[0] + ">"
            tag_end = f"</{node.name}>"

            if current_length + len(str(node)) > max_length:
                current_fragment.append(close_open_tags(open_tags))
                fragment_content = "".join(current_fragment).strip()
                fragments.append(HtmlFragment(fragment_content, len(fragments) + 1))

                current_fragment = [reopen_tags(open_tags)]
                current_length = len(reopen_tags(open_tags))

            current_fragment.append(tag_start)
            open_tags.append(node.name)
            current_length += len(tag_start)

            for child in node.children:
                process_node(child)

            current_fragment.append(tag_end)
            open_tags.pop()
            current_length += len(tag_end)

        elif node.string:
            text = node.string.strip()
            while text:
                remaining_space = max_length - current_length
                if remaining_space <= 0:
                    current_fragment.append(close_open_tags(open_tags))
                    fragment_content = "".join(current_fragment).strip()
                    fragments.append(HtmlFragment(fragment_content, len(fragments) + 1))

                    current_fragment = [reopen_tags(open_tags)]
                    current_length = len(reopen_tags(open_tags))
                    remaining_space = max_length

                split_point = min(len(text), remaining_space)
                current_fragment.append(text[:split_point])
                current_length += split_point
                text = text[split_point:]

    for element in soup.contents:
        process_node(element)

    if current_fragment:
        current_fragment.append(close_open_tags(open_tags))
        fragment_content = "".join(current_fragment).strip()
        if not fragment_content:
            raise HtmlSplitError("A fragment contains no tags or text.")
        fragments.append(HtmlFragment(fragment_content, len(fragments) + 1))

    return fragments

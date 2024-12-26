import pytest

from services.split_html import split_html


def test_html_splitter_scenario_two():
    # Input HTML and max length
    input_html = (
        "<p></p>"
        "<p><b><a href=\"https://www.google.com/\">Google search</a></b></p>"
        "<p><b><ul><li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li></ul></b></p>"
        "<p><b><ul><li>Ut enim ad minim veniam, quis nostrud exercitation ullamco.</li></ul></b></p>"
        "<p><b><ul><li>Duis aute irure dolor in reprehenderit in voluptate.</li></ul></b></p>"
    )
    max_length = 91

    # Expected output for valid input
    expected_fragments = [
        "--- Fragment #1 0 chars ---\n\n",
        "--- Fragment #2 7 chars ---\n<p></p>\n",
        "--- Fragment #3 65 chars ---\n<p><b><a href=\"https://www.google.com/\">Google search</a></b></p>\n",
        "--- Fragment #4 88 chars ---\n<p><b><ul><li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li></ul></b></p>\n",
        "--- Fragment #5 91 chars ---\n<p><b><ul><li>Ut enim ad minim veniam, quis nostrud exercitation ullamco.</li></ul></b></p>\n",
        "--- Fragment #6 84 chars ---\n<p><b><ul><li>Duis aute irure dolor in reprehenderit in voluptate.</li></ul></b></p>\n",
    ]

    # Call the function to test valid case
    fragments = split_html(input_html, max_length)

    # Check if the number of fragments is as expected
    assert len(fragments) == len(expected_fragments), "Number of fragments mismatch"

    # Check each fragment's content
    for i, fragment in enumerate(fragments):
        assert fragment == expected_fragments[i], f"Fragment {i+1} mismatch:\n{fragment}\n!=\n{expected_fragments[i]}"

def test_html_splitter_empty_input_scenario_two():
    # Test empty input
    input_html = ""
    max_length = 50
    fragments = split_html(input_html, max_length)

    # Expect no fragments and raise an error
    assert fragments == [], "Fragments should be empty for empty input"

    with pytest.raises(ValueError, match="Input HTML cannot be empty"):
        split_html(input_html, max_length)

def test_html_splitter_invalid_max_length_scenario_two():
    # Test invalid max length
    input_html = (
        "<p><b><a href=\"https://www.google.com/\">Google search</a></b></p>"
        "<p><b><ul><li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li></ul></b></p>"
    )
    invalid_max_lengths = [-10, 0, None]

    for max_length in invalid_max_lengths:
        with pytest.raises(ValueError, match="Max length must be a positive integer"):
            split_html(input_html, max_length)

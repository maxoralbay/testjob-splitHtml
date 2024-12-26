import pytest

from services.split_html import split_html


def test_html_splitter():
    # Input HTML and max length
    input_html = (
        '<span><p>test</p></span>'
        '<span><a href="https://mockdata.atlassian.net/browse/ABC-11872">'
        '<code>ABC-11872</code></a>Etiam cursus nisi eget tortor feugiat.</span>'
        '<span><a href="https://mockdata.atlassian.net/browse/ABC-12129">'
        '<code>ABC-12129</code></a>Non congue tortor cursus.</span>'
        '<span><div><a href="https://mockdata.atlassian.net/browse/ABC-12354">'
        '<code>ABC-12354</code></a>Ut finibus urna sed lorem elementum.</div></span>'
        '<span></span>'
        '<span><div><a href="https://mockdata.atlassian.net/browse/ABC-12398">'
        '<code>ABC-12398</code></a>Eget tristique magna vulputate.</div></span>'
        '<span><div><a href="https://mockdata.atlassian.net/browse/ABC-12455">'
        '<code>ABC-12455</code></a>Sed a orci at turpis commodo semper quis vitae erat.</div></span>'
        '<span><div><a href="https://mockdata.atlassian.net/browse/ABC-12522">'
        '<code>ABC-12522</code></a>Quis purus et augue varius egestas</div></span>'
        '<span><a href="https://mockdata.atlassian.net/browse/ABC-12538">'
        '<code>ABC-12538</code></a>Aliquam ac sollicitudin neque.</span>'
    )
    max_length = 113

    # Expected output for valid input
    expected_fragments = [
        "--- Fragment #1 0 chars ---\n\n",
        "--- Fragment #2 24 chars ---\n<span><p>test</p></span>\n",
        "--- Fragment #3 107 chars ---\n"
        "<span><a href=\"https://mockdata.atlassian.net/browse/ABC-11872\"><code>ABC-11872</code></a>Etiam\n"
        "curs</span>\n",
        "--- Fragment #4 41 chars ---\n<span>us nisi eget tortor feugiat.</span>\n",
        "--- Fragment #5 107 chars ---\n"
        "<span><a href=\"https://mockdata.atlassian.net/browse/ABC-12129\"><code>ABC-12129</code></a>Non\n"
        "congue</span>\n",
        "--- Fragment #6 28 chars ---\n<span> tortor cursus.</span>\n",
        "--- Fragment #7 113 chars ---\n"
        "<span><div><a href=\"https://mockdata.atlassian.net/browse/ABC-12354\"><code>ABC-12354</code></a>Ut\n"
        "fi</div></span>\n",
        "--- Fragment #8 55 chars ---\n<span><div>nibus urna sed lorem elementum.</div></span>\n",
        "--- Fragment #9 13 chars ---\n<span></span>\n",
        "--- Fragment #10 113 chars ---\n"
        "<span><div><a href=\"https://mockdata.atlassian.net/browse/ABC-12398\"><code>ABC-12398</code></a>Eget </div></span>\n",
        "--- Fragment #11 50 chars ---\n<span><div>tristique magna vulputate.</div></span>\n",
        "--- Fragment #12 113 chars ---\n"
        "<span><div><a href=\"https://mockdata.atlassian.net/browse/ABC-12455\"><code>ABC-12455</code></a>Sed a</div></span>\n",
        "--- Fragment #13 71 chars ---\n<span><div>\norci at turpis commodo semper quis vitae erat.</div></span>\n",
        "--- Fragment #14 113 chars ---\n"
        "<span><div><a href=\"https://mockdata.atlassian.net/browse/ABC-12522\"><code>ABC-12522</code></a>Quis\n"
        "</div></span>\n",
        "--- Fragment #15 53 chars ---\n<span><div>purus et augue varius egestas</div></span>\n",
        "--- Fragment #16 107 chars ---\n"
        "<span><a href=\"https://mockdata.atlassian.net/browse/ABC-12538\"><code>ABC-12538</code></a>Aliquam ac</span>\n",
        "--- Fragment #17 33 chars ---\n<span> sollicitudin neque.</span>\n",
    ]

    # Call the function to test valid case
    fragments = split_html(input_html, max_length)

    # Check if the number of fragments is as expected
    assert len(fragments) == len(expected_fragments), "Number of fragments mismatch"

    # Check each fragment's content
    for i, fragment in enumerate(fragments):
        assert fragment == expected_fragments[i], f"Fragment {i + 1} mismatch:\n{fragment}\n!=\n{expected_fragments[i]}"


def test_html_splitter_empty_input():
    # Test empty input
    input_html = ""
    max_length = 100
    fragments = split_html(input_html, max_length)

    # Expect no fragments and raise an error
    assert fragments == [], "Fragments should be empty for empty input"

    with pytest.raises(ValueError, match="Input HTML cannot be empty"):
        split_html(input_html, max_length)


def test_html_splitter_invalid_max_length():
    # Test invalid max length
    input_html = "<span><p>test</p></span>"
    invalid_max_lengths = [-1, 0, None]

    for max_length in invalid_max_lengths:
        with pytest.raises(ValueError, match="Max length must be a positive integer"):
            split_html(input_html, max_length)

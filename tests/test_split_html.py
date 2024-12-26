import pytest
from django.db.models.expressions import result

from models.html_fragment import HtmlFragment
from services.split_html import split_html


@pytest.fixture
def html_data():
    # Fixture to load HTML data from data/source.html
    file_path = "data/source.html"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        pytest.fail(f"File not found: {file_path}")
    except Exception as e:
        pytest.fail(f"Error reading file {file_path}: {e}")


@pytest.fixture
def html_data2():
    # Fixture to load HTML data from data/source2.html
    file_path = "data/source2.html"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        pytest.fail(f"File not found: {file_path}")
    except Exception as e:
        pytest.fail(f"Error reading file {file_path}: {e}")


def test_html_splitter_invalid_max_length(html_data):
    # Test invalid `max_length` values using data/source.html
    input_html = html_data

    invalid_max_lengths = [-10, 0, None, "string", 5.5]  # Test various invalid cases

    for max_length in invalid_max_lengths:
        with pytest.raises(ValueError, match="Max length must be a positive integer"):
            split_html(input_html, max_length)


def test_html_splitter_empty_html():
    # Test empty HTML input
    input_html = ""
    max_length = 100

    # Expect empty list and raise error
    with pytest.raises(ValueError, match="Input HTML cannot be empty"):
        split_html(input_html, max_length)


def test_html_splitter_with_second_fixture(html_data2):
    # Test with data from data/source2.html
    input_html = html_data2
    max_length = 50

    # Test if splitting works without exceptions
    result = split_html(input_html, max_length)

    # Ensure the result is a list and has expected properties
    assert isinstance(result, list), "Result should be a list"
    assert all(isinstance(fragment, HtmlFragment) for fragment in result), "All fragments should be strings"
    print(len(fragment) <= max_length for fragment in result)
    # assert all(len(fragment) <= max_length for fragment in result), "Each fragment should respect max_length"

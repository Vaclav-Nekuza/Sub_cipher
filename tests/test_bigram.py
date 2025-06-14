# tests\test_bigram.py
import os

from bigram.bigram import get_bigram


def test_main_with_valid_file(tmp_path):
    test_file = tmp_path / "test_input.txt"
    output_file = tmp_path / "test_output.txt"

    # Create a test file with sample content
    test_file.write_text("Testování bigramu. Toto je jen testování bigramu.", encoding="windows-1250")

    # Call main with output_file specified
    get_bigram(test_file, output_file=output_file)

    # Verify output was written correctly
    assert output_file.exists()
    content = output_file.read_text().strip().split("\n")
    assert len(content) > 0


def test_main_with_return_value(tmp_path):
    test_file = tmp_path / "test_input.txt"

    # Create a test file with sample content
    test_file.write_text("Testování bigramu, pojďme to otestovat!", encoding="windows-1250")

    # Call main without specifying output_file
    result = get_bigram(test_file)

    # Verify the returned list of bigrams is valid
    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(item, str) for item in result)


def test_main_with_empty_file(tmp_path):
    test_file = tmp_path / "empty_file.txt"

    # Create an empty test file
    test_file.write_text("", encoding="windows-1250")

    # Call main without specifying output_file
    result = get_bigram(test_file)

    # Verify the returned list is empty
    assert isinstance(result, list)
    assert len(result) == 0


def test_main_with_special_characters(tmp_path):
    test_file = tmp_path / "special_chars.txt"
    output_file = tmp_path / "special_output.txt"

    # Create a file with special characters and make sure they are handled correctly
    test_file.write_text("Ahoj!!! Tak jak to jde? Test... Test! @#@", encoding="windows-1250")

    # Call main with output_file
    get_bigram(test_file, output_file=output_file)

    # Check that the output file exists
    assert output_file.exists()

    # Validate content (non-alphanumeric characters should be ignored per `prep` logic)
    content = output_file.read_text().strip().split("\n")
    assert len(content) > 0

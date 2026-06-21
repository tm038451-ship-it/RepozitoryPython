def test_addition():
    assert 1 + 1 == 2
    
 @pytest.mark.parametrize(
    "input_text, expected_output",
    [("", " "), ("    ", "    ."), ],
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output   
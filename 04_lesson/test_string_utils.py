import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("hello woRLD", "Hello world"),
    ("123python", "123Python"),
    ("None", "")
])  
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!hello", "!hello"),
    ("3Test", "3test"),
    ("PYTHON", "Python")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize(
    "input_string, expected_string",
    [
        ("   skypro", "skypro"),      
        ("skypro", "skypro"),          
        ("sky pro", "sky pro"),        
        ("skypro   ", "skypro   "),    
        ("  sky pro  ", "sky pro  "),  
    ],
    ids=["leading_spaces", "no_spaces", "inside_spaces", "trailing_spaces", "mixed_spaces"]
)
def test_trim_positive(input_string, expected_string):
    processor = StringProcessor()
    assert processor.trim(input_string) == expected_string
    
@pytest.mark.parametrize(
    "invalid_input",
    [
        123,                 
        None,                
        ["  skypro"],        
        {"text": " skypro"}  
    ],
    ids=["int_type", "none_type", "list_type", "dict_type"]
)
def test_trim_negative_wrong_types(invalid_input):
    processor = StringProcessor()
    with pytest.raises(TypeError):
        processor.trim(invalid_input)
        
def contains(string: str, symbol: str) -> bool:
    res = False
    try:
        res = string.index(symbol) > -1
    except ValueError:
        pass
    return res

positive_cases = [
    ("SkyPro", "S"),  
    ("SkyPro", "o"),  
    ("SkyPro", "y"),  
    ("S", "S"),       

@pytest.mark.parametrize("string, symbol", positive_cases)
def test_contains_positive(string, symbol):
    """Тест проверяет успешное нахождение символа в разных позициях строки."""
    assert contains(string, symbol) is True

negative_cases = [
    ("SkyPro", "U"),  
    ("", "S"),        
    ("SkyPro", ""),   
]

@pytest.mark.parametrize("string, symbol", negative_cases)
def test_contains_negative(string, symbol):
    """Тест проверяет корректный возврат False при отсутствии совпадений."""
    assert contains(string, symbol) is False 
    
def delete_symbol(self, string: str, symbol: str) -> str:
        if symbol and symbol in string:
            string = string.replace(symbol, '')
        return string

class TestStringProcessor:
    
    processor = StringProcessor()

@pytest.mark.parametrize("string, symbol, expected_result", [
        ("SkyPro", "k", "SyPro"),         
        ("Пример с пробелами", " ", "Примерспробелами"), 
    ])
def test_delete_symbol_positive(self, string, symbol, expected_result):
        assert self.processor.delete_symbol(string, symbol) == expected_result

@pytest.mark.parametrize("string, symbol", [
        ("SkyPro", "z"),                 
        ("SkyPro", "abc"),               
        ("", "k"),                      
        ("SkyPro", ""),                  
    ])
def test_delete_symbol_negative(self, string, symbol):
        original_string = string
        assert self.processor.delete_symbol(string, symbol) == original_string   

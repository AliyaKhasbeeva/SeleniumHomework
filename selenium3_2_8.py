#Функция должна проверить совпадение значений с помощью оператора assert
# и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)

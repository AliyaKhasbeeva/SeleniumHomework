#Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert
# и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.

def test_substring(full_string, substring):
    assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring, full_string)

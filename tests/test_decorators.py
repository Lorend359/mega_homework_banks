import pytest

from src.decorators import log


def test_successful_function(capsys):
    @log()
    def successful_function(x, y):
        return x + y

    result = successful_function(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert "Executing successful_function with inputs: (1, 2), {}" in captured.out
    assert "successful_function ok: 3" in captured.out


def test_error_function(capsys):
    @log()
    def error_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        error_function(1, 0)

    captured = capsys.readouterr()
    assert "Executing error_function with inputs: (1, 0), {}" in captured.out
    assert "error_function error: ZeroDivisionError" in captured.out

# content of test_example.py
import io
import pytest
import sys


testdata = [
        (
            "8\n"
            "-1 0 0 1 2 -1 -4 0\n",
            "-1 1 2 -1 -4\n"
        ),
        (
            "5\n"
            "-1 1 2 -1 -4\n",
            "-1 1 2 -1 -4\n"
        ),
    ]


@pytest.mark.parametrize("task_input,task_output", testdata)
def test_case_c(monkeypatch, capsys, task_input, task_output):

    monkeypatch.setattr('sys.stdin', io.StringIO(task_input))

    # модуль загружается один раз
    import d

    captured = capsys.readouterr()
    assert captured.out == task_output, task_input

    # если код не в main, то нужно удалить 
    if 'd' in sys.modules:
        del sys.modules["d"]

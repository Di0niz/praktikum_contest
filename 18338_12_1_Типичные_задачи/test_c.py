# content of test_example.py
import io
import pytest
import sys

import c


testdata = [
    (
        "4\n"
        "1 2 0 0\n"
        "34\n",
        "1 2 3 4\n"
    ),
    (
        "2\n"
        "9 5\n"
        "17\n",
        "1 1 2\n"
    ),
]


@pytest.mark.parametrize("task_input,task_output", testdata)
def test_case_c(monkeypatch, capsys, task_input, task_output):

    monkeypatch.setattr('sys.stdin', io.StringIO(task_input))

    # тестируем функцию main и перехватывать не надо
    c.main()

    captured = capsys.readouterr()
    assert captured.out == task_output, task_input

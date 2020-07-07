# content of test_example.py
import io
import pytest
import sys


@pytest.mark.parametrize(
    "task_input,task_output", [
        (
            "8\n"
            "вышивание крестиком\n"
            "рисование мелками на парте\n"
            "настольный керлинг\n"
            "настольный керлинг\n"
            "кухня африканского племени ужасмай\n"
            "тяжелая атлетика\n"
            "таракановедение\n"
            "таракановедение\n",
            "вышивание крестиком\n"
            "рисование мелками на парте\n"
            "настольный керлинг\n"
            "кухня африканского племени ужасмай\n"
            "тяжелая атлетика\n"
            "таракановедение"
        ),
        ]
    )
def test_case(capsys, monkeypatch, task_input, task_output):
    monkeypatch.setattr('sys.stdin', io.StringIO(task_input))

    import a

    captured = capsys.readouterr()
    assert captured.out != task_output

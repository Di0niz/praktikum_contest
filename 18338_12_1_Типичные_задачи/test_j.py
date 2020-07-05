# # content of test_example.py
# import io
# import pytest
# import sys


# testdata = [
#         (
#             "5\n"
#             "4 1 2 1 2\n",
#             "4\n"
#         ),
#         (
#             "5\n"
#             "42 67 67 42 42\n",
#             "42\n"
#         ),
#     ]


# @pytest.mark.parametrize("task_input,task_output", testdata)
# def test_case_j(monkeypatch, capsys, task_input, task_output):

#     monkeypatch.setattr('sys.stdin', io.StringIO(task_input))

#     # модуль загружается один раз
#     import case_j

#     captured = capsys.readouterr()
#     assert captured.out == task_output, task_input

#     # если код не в main, то нужно удалить модуль из кеша
#     if 'case_j' in sys.modules:
#         del sys.modules["case_j"]

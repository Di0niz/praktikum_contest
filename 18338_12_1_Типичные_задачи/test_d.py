# # content of test_example.py
# import io
# import pytest
# import sys


# testdata = [
#         (
#             "8\n"
#             "-1 0 0 1 2 -1 -4 0\n",
#             "-1 1 2 -1 -4\n"
#         ),
#         (
#             "5\n"
#             "-1 1 2 -1 -4\n",
#             "-1 1 2 -1 -4\n"
#         ),
#     ]


# @pytest.mark.parametrize("task_input,task_output", testdata)
# def test_case_d(monkeypatch, capsys, task_input, task_output):

#     monkeypatch.setattr('sys.stdin', io.StringIO(task_input))

#     # модуль загружается один раз
#     import case_d

#     captured = capsys.readouterr()
#     assert captured.out == task_output, task_input

#     # если код не в main, то нужно удалить модуль из кеша
#     if 'case_d' in sys.modules:
#         del sys.modules["case_d"]

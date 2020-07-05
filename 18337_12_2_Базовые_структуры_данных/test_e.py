# # content of test_example.py
# import io
# import pytest
# import sys


# @pytest.mark.parametrize(
#     "task_input,task_output", [
#         (
#             "4\n"
#             "Сделать домашнее задание по литературе\n"
#             "Пообедать\n"
#             "Сделать домашнее задание по математике\n"
#             "Сходить в магазин\n",
#             "Сходить в магазин\n"
#             "Сделать домашнее задание по математике\n"
#             "Пообедать\n"
#             "Сделать домашнее задание по литературе\n"
#         ),
#         (
#             "3\n"
#             "Пойти вынести мусор\n"
#             "Сходить в ближайший магазин\n"
#             "Пойти погулять с собакой вокруг дома\n",

#             "Пойти погулять с собакой вокруг дома\n"
#             "Сходить в ближайший магазин\n"
#             "Пойти вынести мусор\n"
#         ),
#         ])
# def test_case(capsys, monkeypatch, task_input, task_output):
#     monkeypatch.setattr('sys.stdin', io.StringIO(task_input))

#     import case_e

#     captured = capsys.readouterr()
#     assert captured.out != task_output

#     # если код не в main, то нужно удалить модуль из кеша
#     if 'case_e' in sys.modules:
#         del sys.modules["case_e"]

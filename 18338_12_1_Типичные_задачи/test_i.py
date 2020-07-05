# # content of test_example.py
# import io
# import pytest
# import sys

# import case_i


# testdata = [
#     (
#         "1010\n"
#         "1011\n",
#         "10101\n"
#     ),
#     (
#         "1\n"
#         "1\n",
#         "10\n"
#     ),

# ]


# @pytest.mark.parametrize("task_input,task_output", testdata)
# def test_case_i(monkeypatch, capsys, task_input, task_output):

#     monkeypatch.setattr('sys.stdin', io.StringIO(task_input))

#     # тестируем функцию main и перехватывать не надо
#     case_i.main()

#     captured = capsys.readouterr()
#     assert captured.out == task_output, task_input

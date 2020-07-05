# content of test_example.py
import io
import pytest
import sys

# import case_c


# @pytest.mark.parametrize(
#     "task_input,task_output", [
#         (
#             "abcabcbb\n",
#             "3\n"
#         ),
#         (
#             "bbbbb\n",
#             "1\n"
#         ),
#         (
#             "abcdba\n",
#             "4\n"
#         ),
#         ])
# def test_case(capsys, monkeypatch, task_input, task_output):
#     monkeypatch.setattr('sys.stdin', io.StringIO(task_input))

#     case_c.main()

#     captured = capsys.readouterr()
#     assert captured.out != task_output

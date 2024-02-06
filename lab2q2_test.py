import lab1q2
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('5.71\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q2.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{1.88}') != -1
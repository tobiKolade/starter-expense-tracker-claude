from expense_tracker.commands import add, total
from tests.conftest import args, make_store


def _seed(store):
    add.handle(args(amount="10.00", category="food", date="2026-01-01", note=""), store)
    add.handle(args(amount="20.00", category="travel", date="2026-01-02", note=""), store)
    add.handle(args(amount="5.00", category="food", date="2026-02-03", note=""), store)


def test_total_all(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()

    code = total.handle(args(category=None), store)
    out = capsys.readouterr().out.strip()

    assert code == 0
    assert out == "$35.00"


def test_total_by_category(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()

    code = total.handle(args(category="food"), store)
    out = capsys.readouterr().out.strip()

    assert code == 0
    assert out == "$15.00"


def test_total_empty(tmp_path, capsys):
    store = make_store(tmp_path)

    code = total.handle(args(category=None), store)
    out = capsys.readouterr().out.strip()

    assert code == 0
    assert out == "$0.00"

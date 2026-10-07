"""The ``total`` command: print the sum of all (or one category's) expenses."""

from __future__ import annotations

from ..money import format_amount

NAME = "total"
HELP = "Print the total of all expenses"


def add_parser(subparsers) -> None:
    """Register the total sub-command and its arguments."""
    parser = subparsers.add_parser(NAME, help=HELP)
    parser.add_argument(
        "--category",
        default=None,
        help="Only total expenses in this category",
    )


def handle(args, store) -> int:
    """Sum all matching expenses and print the formatted total."""
    expenses = store.load()

    if args.category is not None:
        expenses = [e for e in expenses if e.category == args.category]

    total_cents = sum(e.amount_cents for e in expenses)
    print(format_amount(total_cents))
    return 0

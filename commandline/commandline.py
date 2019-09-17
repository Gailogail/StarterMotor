"""Commandline tool to process integers"""

import argparse


def product(integers):
    """Calculate the product of a set of integers

    Parameter
    ---------
    integers: list(int)
        List of integers to process

    Returns
    -------
    int
        Product of integers

    """
    result = 1
    for int_ in integers:
        result *= int_
    return result


def divide_chain(integers):
    """Carry out a chain of divisions by integers

    Parameter
    ---------
    integers: list(int)
        List of integers to process

    Returns
    -------
    fload
        Result of dividing each integer by the next, starting with 1

    """
    result = 1.0
    for int_ in integers:
        result /= int_
    return result


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
)
parser_operators = parser.add_argument_group("operators", "operations to carry out")
parser_operators.add_argument(
    "-s",
    "--sum",
    dest="functions",
    action="append_const",
    const=("sum", sum, "{}"),
    help="sum the integers",
)
parser_operators.add_argument(
    "-m",
    "--max",
    dest="functions",
    action="append_const",
    const=("max", max, "{}"),
    help="find the maximum integer",
)
parser_operators.add_argument(
    "-p",
    "--prod",
    dest="functions",
    action="append_const",
    const=("product", product, "{}"),
    help="find the product of the integers",
)
parser_operators.add_argument(
    "-d",
    "--div",
    dest="functions",
    action="append_const",
    const=("div chain", divide_chain, "{:.5f}"),
    help="find the product of the integers",
)

args = parser.parse_args()

output = []
for functpl in args.functions:
    try:
        result = functpl[1](args.integers)
    except ZeroDivisionError:
        result_str = "div by zero"
    else:
        result_str = functpl[2].format(result)

    output.append(f"{functpl[0]}: {result_str}")

print(", ".join(output))

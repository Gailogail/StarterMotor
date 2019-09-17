"""Commandline tool to process integers"""

import argparse
import traceback

#: Divide chain maximum integer
DIVMAXINT = 99


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
    float
        Result of dividing each integer by the next, starting with 1

    """
    result = 1.0
    for int_ in integers:
        # Check for large numbers that will make the output very small
        if int_ >= DIVMAXINT:
            raise ValueError(f"integer magnitude to large (limits +/-{DIVMAXINT})")
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
    help="carry out a division chain on the integers",
)

args = parser.parse_args()

output = []
intercepted_exception = None
for functpl in args.functions:
    try:
        result = functpl[1](args.integers)
    except ZeroDivisionError as ex:
        result_str = "div by zero"
        intercepted_exception = ex
    except ValueError as ex:
        result_str = "arg to large"
        intercepted_exception = ex
    except Exception as ex:
        raise ex
    else:
        result_str = functpl[2].format(result)

    output.append(f"{functpl[0]}: {result_str}")

print(", ".join(output))

# Demonstrate some of the many cool things you can find out about an exception
# This is 'Deep Magic', so feel free to ignore the details, or all of it

# None evaluates to false, so this responds only if we have intercepted an exception.
if intercepted_exception:

    # 'Tracebacks' contain all the information about which parts of your code, and some libraries, were involved
    # in the exception
    ex_tb = traceback.TracebackException.from_exception(intercepted_exception)

    # A 'Frame' holds data about an individual part of the path through the code
    ex_frame = ex_tb.stack[-1]
    ex_origin = ex_frame.name

    # 'dunderscore' variables expose some of the hidden workings of python
    # This gets the name of the exception type, without the formatting that Python helpfully provides
    ex_type_ = type(intercepted_exception).__name__

    # Put all this together in an almost friendly error message for the user
    print(f"... {ex_type_}: '{intercepted_exception}' in function {ex_origin}")

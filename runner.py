# -*- coding: utf-8 -*-
"""Main function."""
import exercize


def run_first():
    """Run the fisrt assignment."""
    musts = exercize.first_five_lowest_current_rent()
    for must in musts:
        print(must, "\n")


def run_second():
    """Run the second assignment."""
    musts = exercize.twenty_five_lease()
    for must in musts:
        print(must, "\n")
    total_rent = sum([float(must["Current Rent"]) for must in musts])
    print("the total rent of these must is: %s" % str(total_rent))


def run_third():
    """Run the third assignment."""
    musts = exercize.tenants()
    for k, v in musts.items():
        print(v, k)


if __name__ == "__main__":
    run_first()
    run_second()
    run_third()

# -*- coding: utf-8 -*-
"""Main function."""
import exercize


def test_first_five_lowest_current_rent():
    """Runt the tests for the first assignment."""
    raw_rents = [6600.00, 9500.00, 12000.00, 12250.00, 12750.00]
    musts = exercize.first_five_lowest_current_rent()
    assert len(musts) == 5
    for idx in range(5):
        print(musts[idx]["Current Rent"], raw_rents[idx])
        assert float(musts[idx]["Current Rent"]) == float(raw_rents[idx])


def test_twenty_five_lease():
    """Runt the tests for the second assignment."""
    musts = exercize.twenty_five_lease()
    assert len(musts) == 4
    for must in musts:
        assert int(must["Lease Years"]) == 25
    raw_rent = 46500.0
    total_rent = exercize.total_rent(musts)
    assert total_rent == raw_rent


def test_tenants():
    """Runt the tests for the third assignment."""
    final = exercize.tenants()
    assert len(final.keys()) == 8
    tenant_count = sum(final.values())
    assert tenant_count == 42


if __name__ == "__main__":
    test_first_five_lowest_current_rent()

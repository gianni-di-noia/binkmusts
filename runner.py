"""Main function."""
import exercize
import utils


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


def run_fourth():
    """Run the fourth assignment."""
    musts = exercize.list_rental_by_lease_date()
    for must in musts:
        line = list()
        for k, v in must.items():
            if k != "Lease Start Date":
                line.append(v)
                continue
            lease_date = utils.str2date(must["Lease Start Date"])
            lease_date_str = utils.date2str(lease_date)
            line.append(lease_date_str)
        print(line)


if __name__ == "__main__":
    run_first()
    run_second()
    run_third()
    run_fourth()

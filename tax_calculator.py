import argparse


def calculate_tax_with_rebate(income, verbose):
    """
    Calculates tax with a rebate applied for income below or equal to 12 lakh.

    Parameters:
    income (float): The income amount in rupees.
    verbose (bool): Whether to display detailed tax breakdown.

    Returns:
    float: The calculated tax amount rounded to the nearest rupee.
    """
    # Define tax slabs and rates based on the income range
    tax_slabs = [
        (0, 400000, 0),
        (400000, 800000, 0.05),
        (800000, 1200000, 0.10),
        (1200000, 1600000, 0.15),
        (1600000, 2000000, 0.20),
        (2000000, 2400000, 0.25),
        (2400000, float('inf'), 0.30)
    ]

    # Print header for new tax regime
    print("\n*** New Tax Regime - Tax Calculation ***\n")

    # Initialize total tax
    total_tax = 0

    # Iterate through each tax slab to calculate the tax
    for lower_limit, upper_limit, rate in tax_slabs:
        if income > lower_limit:
            taxable_amount = min(income, upper_limit) - lower_limit
            slab_tax = taxable_amount * rate
            if verbose:
                print(f"\n{'-' * 50}")
                print(f"Tax of {rate * 100}% applied on income between {lower_limit:,} and {upper_limit:,} rupees:")
                print(f" - Taxable amount for this slab: {taxable_amount:,.2f} rupees")
                print(f" - Tax calculated for this slab: {slab_tax:,.2f} rupees")
                print(f"{'-' * 50}")
            total_tax += slab_tax

    # Apply rebate if income is below or equal to 12 lakh
    if income <= 1200000:
        print(f"\n{'*' * 50}")
        print(f"Since your income is below or equal to 12 lakh, a full rebate is applied, and no tax is due.")
        print(f"{'*' * 50}")
        total_tax = 0

    # Round the total tax to the nearest rupee
    total_tax = round(total_tax)

    # Display the final tax amount
    if verbose:
        print(f"\n{'=' * 50}")
        print(f"Total calculated tax for an income of {income:,.2f} rupees: {total_tax:,} rupees.")
        print(f"{'=' * 50}")
    else:
        print(f"\nThe final tax payable for an income of {income:,.2f} rupees is: {total_tax:,} rupees.")

    return total_tax


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Calculate tax with rebate for a given income.")
    parser.add_argument('income', type=float, help="The income in rupees to calculate the tax for.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Display detailed tax breakdown.")

    args = parser.parse_args()

    income = args.income
    verbose = args.verbose

    calculate_tax_with_rebate(income, verbose)


if __name__ == "__main__":
    main()

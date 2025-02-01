
# Tax Calculator - New Tax Regime

This Python script calculates the income tax based on the **New Tax Regime** for individual taxpayers. It allows for both detailed and concise output based on the user's preference.

## Features
- Calculates tax based on tax slabs with progressive rates.
- Provides a rebate (full tax exemption) for income below or equal to 12 lakh rupees.
- Allows the user to display detailed information about the tax calculation or a concise summary.
- Outputs the tax calculation in a clean, user-friendly format.

## Requirements
- Python 3.x
- No additional external libraries are required.

## How to Use

### Command-Line Arguments

1. **`income` (required)**:
   - The income in rupees for which the tax needs to be calculated.
   - Example: `1500000` for 15 lakh rupees.

2. **`-v` or `--verbose` (optional)**:
   - If provided, the script will show a detailed breakdown of tax calculations, including the tax for each slab.
   - If omitted, the script will display a concise output with just the final tax payable.

### Example 1: Concise Output
If you only want the final tax amount:
```sh
python tax_calculation.py 1500000
```
Output:
```
The final tax payable for an income of 1,500,000.00 rupees is: 105,000 rupees.
```

### Example 2: Detailed Output
If you want to see the breakdown of how the tax is calculated:
```sh
python tax_calculation.py 1500000 -v
```
Output:
```
--------------------------------------------------
Tax of 5.0% applied on income between 400,000 and 800,000 rupees:
 - Taxable amount for this slab: 400,000.00 rupees
 - Tax calculated for this slab: 20,000.00 rupees
--------------------------------------------------
--------------------------------------------------
Tax of 10.0% applied on income between 800,000 and 1,200,000 rupees:
 - Taxable amount for this slab: 400,000.00 rupees
 - Tax calculated for this slab: 40,000.00 rupees
--------------------------------------------------
--------------------------------------------------
Tax of 15.0% applied on income between 1,200,000 and 1,600,000 rupees:
 - Taxable amount for this slab: 300,000.00 rupees
 - Tax calculated for this slab: 45,000.00 rupees
--------------------------------------------------
**************************************************
Since your income is below or equal to 12 lakh, a full rebate is applied, and no tax is due.
**************************************************
==================================================
Total calculated tax for an income of 1,500,000.00 rupees: 105,000 rupees.
==================================================
```

### Rebate Information
- If your income is below or equal to **12 lakh rupees**, you will receive a full rebate, meaning no tax will be calculated.
- The script automatically checks and applies the rebate if the income is 12 lakh or below.

### Tax Slabs Used
The tax slabs applied in this calculation are as follows:
| Income Range (in rupees) | Tax Rate |
|--------------------------|----------|
| 0 - 400,000              | 0%       |
| 400,001 - 800,000        | 5%       |
| 800,001 - 1,200,000      | 10%      |
| 1,200,001 - 1,600,000    | 15%      |
| 1,600,001 - 2,000,000    | 20%      |
| 2,000,001 - 2,400,000    | 25%      |
| Above 2,400,000          | 30%      |

### Detailed Breakdown
When the `-v` option is used, the script will:
- Show the tax rate applied for each income range.
- Display the taxable amount in that range.
- Show the tax calculated for each range.
- At the end, the total tax is shown, including the rebate if applicable.

### How It Works
1. **Input**: The user provides their income either through command-line arguments or a direct input prompt.
2. **Processing**: The script calculates the applicable tax based on the defined slabs.
3. **Rebate**: If the income is below or equal to 12 lakh, the tax is set to zero due to the rebate.
4. **Output**: The script then displays the tax calculation in a clear, formatted manner.

### Example Calculations
- **Income of 8,00,000 rupees**: The tax would be 5% on the amount between 4,00,000 and 8,00,000, i.e., 20,000 rupees.
- **Income of 12,00,000 rupees**: The tax would be 5% on the amount between 4,00,000 and 8,00,000 (20,000 rupees), and 10% on the amount between 8,00,000 and 12,00,000 (40,000 rupees). Total tax would be 60,000 rupees.
- **Income of 15,00,000 rupees**: The tax would be calculated based on slabs for the income between 4,00,000 and 12,00,000, with an exemption for income below 12 lakh, resulting in a tax of 1,05,000 rupees.

## File Structure
```
tax_calculation.py    # Main script file containing the logic
README.md             # Documentation for the project
```

## Contribution
Feel free to fork the repository, make changes, and create pull requests if you have improvements or bug fixes.

## License
This project is licensed.

# Customer Analysis - Project 4

This is my customer analysis practice project using Python and Pandas.

## What I did

- Read customer purchase data from a CSV file.
- Calculated the amount for each order (`Quantity * Unit_Price`).
- Grouped purchases by customer.
- Found total spending and purchase frequency for each customer.
- Sorted customers by spending and made a bar chart of the top 10.

The CSV contains **sample data for practice**, not actual company customer details. It uses the same example sales orders as Project 3, with sample customer names added.

## Tools used

Python, Pandas, Matplotlib, VS Code

## How to run

Open this folder in VS Code and run these commands in the terminal:

```powershell
py -m pip install -r requirements.txt
py customer_analysis.py
```

The `output` folder contains:
- `customer_summary.csv` - spending and frequency for all customers
- `top_10_customers.csv` - the highest-spending 10 customers
- `top_10_customers.png` - bar chart
- `findings.txt` - short summary of results

## What I learned

I learned how to use `groupby()`, `agg()` and `sort_values()` in Pandas to compare customers. In this project, a valuable customer means someone who spent more money overall. Purchase frequency is also counted separately.

## Result

See `output/findings.txt` for the calculated totals and top customer.

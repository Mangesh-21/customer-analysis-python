import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project 4: Customer Analysis
# Find customers with the highest spending and count their purchases.

folder = Path(__file__).parent
file_path = folder / "data" / "customer_orders.csv"
output = folder / "output"
output.mkdir(exist_ok=True)

# 1. Read customer purchase data
sales = pd.read_csv(file_path)

# 2. Calculate the money spent on each order
sales["Total_Amount"] = sales["Quantity"] * sales["Unit_Price"]

# 3. Group by customer to find spending and number of orders
customer_summary = sales.groupby(["Customer_ID", "Customer_Name"]).agg(
    Total_Spent=("Total_Amount", "sum"),
    Purchase_Frequency=("Order_ID", "nunique")
).reset_index()

# 4. Sort customers by total spent, highest first
customer_summary = customer_summary.sort_values("Total_Spent", ascending=False)
top_10 = customer_summary.head(10)

# Save results as CSV files
customer_summary.to_csv(output / "customer_summary.csv", index=False)
top_10.to_csv(output / "top_10_customers.csv", index=False)

# 5. Make a bar chart of the top 10 customers
plt.figure(figsize=(10, 6))
plt.barh(top_10["Customer_Name"][::-1], top_10["Total_Spent"][::-1], color="steelblue")
plt.title("Top 10 Customers by Total Spending")
plt.xlabel("Total Spent (INR)")
plt.ylabel("Customer Name")
plt.tight_layout()
plt.savefig(output / "top_10_customers.png", dpi=160)
plt.close()

# 6. Print the results and save a short summary
best = customer_summary.iloc[0]
most_frequent = customer_summary.sort_values("Purchase_Frequency", ascending=False).iloc[0]
lines = [
    "Project 4 - Customer Analysis",
    "Data: sample customer orders (not real customer records)",
    f"Total orders: {sales['Order_ID'].nunique()}",
    f"Total customers: {customer_summary['Customer_ID'].nunique()}",
    f"Total sales amount: Rs. {sales['Total_Amount'].sum():,.2f}",
    f"Highest spending customer: {best['Customer_Name']} (Rs. {best['Total_Spent']:,.2f})",
    f"Orders by highest spending customer: {best['Purchase_Frequency']}",
    f"Most frequent buyer: {most_frequent['Customer_Name']} ({most_frequent['Purchase_Frequency']} orders)",
    "Top 10 customers are ranked by total amount spent, not just number of orders.",
]

(output / "findings.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
print("\nTop 10 customers:\n")
print(top_10.to_string(index=False))
print("\nFiles saved in output folder.")

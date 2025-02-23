import os
import pandas as pd
import matplotlib.pyplot as plt
from send_email import send_report

def generate_report(file_path, email):
    # Load client data (CSV: date, product, amount, customer_id) with UTF-8 encoding
    df = pd.read_csv(file_path, encoding='utf-8')

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Monthly sales trend
    monthly_sales = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()

    # Find top-selling product
    top_product = df.groupby('product')['amount'].sum().idxmax()

    # Customer segmentation (repeat vs. new customers) - check if 'customer_id' exists
    customer_counts = None
    new_customers = 0
    repeat_customers = 0
    if 'customer_id' in df.columns:
        customer_counts = df.groupby('customer_id')['amount'].count()
        new_customers = customer_counts[customer_counts == 1].count()
        repeat_customers = customer_counts[customer_counts > 1].count()
    else:
        print("Warning: 'customer_id' column not found in CSV. Skipping customer segmentation.")

    # Predict next month’s sales (simple moving average)
    df['month'] = df['date'].dt.to_period('M')
    sales_forecast = df.groupby('month')['amount'].sum().rolling(3).mean().iloc[-1]

    # Generate plots - ensure UTF-8 compatible data
    plt.figure(figsize=(10, 5))
    monthly_sales.plot(kind='bar', title='Monthly Sales Trend')
    plt.savefig(os.path.join('reports', f"{email}_sales_trend.png"))
    plt.close()

    # Save insights as a text report with UTF-8 encoding
    insights = f"""
    🔹 Best-Selling Product: {top_product}
    🔹 New Customers: {new_customers}
    🔹 Repeat Customers: {repeat_customers}
    🔹 Expected Next Month Sales: ₹{sales_forecast:.2f}
    """
    report_text_path = os.path.join('reports', f"{email}_insights.txt")
    with open(report_text_path, 'w', encoding='utf-8') as f:
        f.write(insights)

    # Send email with insights and sales trend
    send_report(email, os.path.join('reports', f"{email}_sales_trend.png"), report_text_path)
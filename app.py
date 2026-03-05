import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="FreshPath AI Operations Dashboard", layout="wide")

# ----------------------------
# Header
# ----------------------------

st.title("FreshPath AI Operations Dashboard")
st.subheader("AI Demand Forecasting Prototype")

st.write(
"Prototype interface demonstrating how AI-powered demand forecasting could support store-level inventory and supply decisions."
)

# ----------------------------
# Sidebar Controls
# ----------------------------

st.sidebar.header("Select Store & Product")

store = st.sidebar.selectbox(
    "Store",
    [
        "Kansas City - Store 101",
        "Wichita - Store 204",
        "Omaha - Store 315",
        "Des Moines - Store 412",
    ],
)

product = st.sidebar.selectbox(
    "Product",
    [
        "Organic Milk",
        "Bananas",
        "Greek Yogurt",
        "Whole Wheat Bread",
        "Fresh Apples",
    ],
)

# ----------------------------
# Simulated Data
# ----------------------------

np.random.seed(42)

days = np.arange(1, 31)

base_demand = np.random.normal(50, 8, size=30)
trend = np.linspace(0, 6, 30)

forecast = base_demand + trend
actual = forecast + np.random.normal(0, 4, size=30)

predicted_weekly_demand = int(np.mean(forecast) * 7)
current_inventory = int(np.random.randint(250, 450))
recommended_order = max(predicted_weekly_demand - current_inventory, 0)

# ----------------------------
# Key Metrics
# ----------------------------

st.subheader("Demand Forecast Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Predicted Weekly Demand", f"{predicted_weekly_demand} units")
col2.metric("Current Inventory", f"{current_inventory} units")
col3.metric("Recommended Order Quantity", f"{recommended_order} units")

# ----------------------------
# Forecast Graph
# ----------------------------

st.subheader("Demand Forecast vs Actual Sales")

df = pd.DataFrame(
    {
        "Day": days,
        "Forecast Demand": forecast,
        "Actual Sales": actual,
    }
)

st.line_chart(df.set_index("Day"))

# ----------------------------
# Inventory Attention Dashboard
# ----------------------------

st.subheader("Products Requiring Attention")

data = {
    "Product": [
        "Organic Milk",
        "Bananas",
        "Greek Yogurt",
        "Whole Wheat Bread",
        "Fresh Apples",
    ],
    "Inventory Risk": [
        "Low Inventory Risk",
        "High Demand Spike",
        "Overstock Risk",
        "Stable",
        "Demand Increase",
    ],
    "Recommended Action": [
        "Reorder Soon",
        "Increase Order Volume",
        "Run Promotion",
        "No Action",
        "Monitor Demand",
    ],
}

alerts = pd.DataFrame(data)

st.dataframe(alerts)

# ----------------------------
# Operations Alert Feed
# ----------------------------

st.subheader("AI Operations Alert Feed")

alerts = [
    "High demand surge detected for Bananas in Wichita store.",
    "Organic Milk inventory projected to fall below safety stock in 3 days.",
    "Greek Yogurt showing slow turnover — potential pricing adjustment opportunity.",
    "Des Moines location experiencing above-average weekend demand.",
]

for alert in alerts:
    st.warning(alert)

# ----------------------------
# Explanation
# ----------------------------

st.subheader("How the AI Forecasting System Works")

st.write(
"""
The AI model analyzes historical sales patterns, seasonality, and store-level demand signals 
to generate SKU-level demand forecasts.  

These forecasts are compared against current inventory levels to automatically recommend
optimal order quantities.  

This allows FreshPath stores to move from reactive ordering to predictive inventory planning,
reducing stockouts, minimizing excess inventory, and improving supply chain efficiency.
"""
)

# ----------------------------
# Footer
# ----------------------------

st.markdown("---")

st.caption(
"FreshPath GenAI Strategy Prototype | Dashboard built using Streamlit | Data simulated for demonstration"
)

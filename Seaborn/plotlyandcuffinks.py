import seaborn as sns
import pandas as pd
import plotly.express as px

# Load dataset
tips = sns.load_dataset("tips")

# Display dataset
print(tips)

# 1. Total Bill Line Plot
fig1 = px.line(
    tips,
    y="total_bill",
    title="Total Bill"
)
fig1.show()

# 2. Average Tip by Day
avg_tip = tips.groupby("day", observed=False)["tip"].mean().reset_index()

fig2 = px.bar(
    avg_tip,
    x="day",
    y="tip",
    title="Average Tip by Day",
    labels={"tip": "Average Tip"}
)
fig2.show()

# 3. Scatter Plot
fig3 = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    title="Total Bill vs Tip"
)
fig3.show()

# 4. Box Plot
fig4 = px.box(
    tips,
    x="day",
    y="total_bill",
    title="Total Bill Distribution by Day"
)
fig4.show()
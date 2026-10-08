import streamlit as st

from logic import ZONES, TIME_BLOCKS, COSTS, best_promise

st.title("Rosa's Pizza: Best Promised Delivery Time")

# Dropdown menus for zone and time block
zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

# Range of promised times to try
st.subheader("Promised times to try (minutes)")
col1, col2, col3 = st.columns(3)
min_promise = col1.number_input("Minimum", min_value=5, value=25, step=5)
max_promise = col2.number_input("Maximum", min_value=5, value=85, step=5)
step = col3.number_input("Step", min_value=1, value=5, step=1)

# Cost inputs, starting from the default COSTS
st.subheader("Costs")
margin = st.number_input("Profit margin per order ($)", min_value=0.0,
                         value=float(COSTS["margin"]), step=0.5)
churn = st.number_input("Estimated churn (lost orders) per late order",
                        min_value=0.0, value=float(COSTS["churn_orders"]),
                        step=0.1)
refund = st.number_input("Refund cost per late order ($)", min_value=0.0,
                         value=float(COSTS["refund"]), step=0.5)

# Button: calculate and show the recommendation
if st.button("Find best promise"):
    if min_promise > max_promise:
        st.error("Minimum promise must be less than or equal to the maximum.")
    else:
        promises = list(range(int(min_promise), int(max_promise) + 1, int(step)))
        costs = {"refund": refund, "churn_orders": churn, "margin": margin}
        p, profit = best_promise(zone, time_block, promises, costs)
        st.success(f"Recommended promise for {zone} / {time_block}: {p} minutes")
        st.metric("Net profit", f"${profit:,.2f}")

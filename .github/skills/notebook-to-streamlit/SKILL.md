---
name: notebook-to-streamlit
description: Turn the analysis logic in a Jupyter notebook into a Streamlit web app. Use when asked to reuse notebook functions (late_pct, cost_per_late, net_profit, best_promise) in a Streamlit app for Rosa's Pizza.
---

# Notebook to Streamlit

Use this skill to move working logic from a Jupyter notebook into a Streamlit app without changing the results.

## Steps

1. **Read the notebook** (`Assignment_1_MMGMT_722.ipynb`) and list the functions the app needs:
   - `cost_per_late(costs)`: refund + churn_orders * margin
   - `net_profit(zone, time_block, promise, costs)`: orders * margin - late orders * cost_per_late
   - `best_promise(zone, time_block, promises, costs)`: returns `(best_promise, best_profit)`
2. **Copy the functions as-is** into a plain Python file (for example `logic.py`). Keep the logic identical, including `seed=1` in `delivery_times`, so the app matches the notebook. Include the imports they need: `from starter import ZONES, TIME_BLOCKS, COSTS, delivery_times`.
3. **Write `app.py`** that imports from `logic.py` and uses Streamlit widgets:
   - `st.selectbox` for zone (from `ZONES`) and time block (from `TIME_BLOCKS`). Never type the names by hand; they are case-sensitive.
   - `st.number_input` for the min promise, max promise and step (default step 5), used to build the list of promises to try.
   - `st.number_input` for margin, churn per late order and refund per late order. Default these from `COSTS`, and build a new costs dictionary with the same keys (`refund`, `churn_orders`, `margin`).
   - `st.button` that, when clicked, calls `best_promise` and shows the recommended promise and its net profit.
4. **Create `requirements.txt`** with one package per line:
   ```
   streamlit
   numpy
   pandas
   git+https://github.com/zhouy185/rosa-starter.git
   ```
   The last line is required so Streamlit Community Cloud can install the `starter` module.
5. **Test locally** with `streamlit run app.py`. Check that Far West / Fri/Sat eve with default costs and promises 25-85 in steps of 5 returns 55 minutes and a net profit of about $1212.40, as in the notebook.

## Rules

- Do not rewrite or "improve" the notebook logic; reuse it.
- Keep the code simple and commented; the author is a beginner in Python.
- Do not put personal information in the repository.

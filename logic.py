from starter import ZONES, TIME_BLOCKS, COSTS, delivery_times


def cost_per_late(costs):
    """Total cost of one late order: refund + the profit lost from churned orders."""
    refund = costs["refund"]
    lost_orders = costs["churn_orders"] * costs["margin"]
    return refund + lost_orders


def net_profit(zone, time_block, promise, costs):
    """Profit from all orders minus the cost of the late ones."""
    times = delivery_times(zone, time_block, promise, seed=1)
    n_orders = len(times)
    n_late = len(times[times > promise])
    return n_orders * costs["margin"] - n_late * cost_per_late(costs)


def best_promise(zone, time_block, promises, costs):
    """Try every promise in the list and return (best promise, its net profit)."""
    b_promise = promises[0]
    best_profit = net_profit(zone, time_block, b_promise, costs)
    for p in promises:
        profit = net_profit(zone, time_block, p, costs)
        if profit > best_profit:
            best_profit = profit
            b_promise = p
    return b_promise, best_profit

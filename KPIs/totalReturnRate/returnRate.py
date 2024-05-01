
def total_return_rate(total_returns, total_orders):
    """
    Calculate the Total Return Rate as a percentage of orders returned out of the total orders.

    Args:
    total_returns (int): The total number of unique returns.
    total_orders (int): The total number of orders.

    Returns:
    float: The Total Return Rate as a percentage.

    Note:
    - Passing total Orders, Calculate the 4th KPI, using with total return solve at 16th KPI.
    """
    try:
        # Calculate the return rate
        return_rate = (total_returns / total_orders) * 100
        return return_rate
    except ZeroDivisionError:
        print("Total orders cannot be zero.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

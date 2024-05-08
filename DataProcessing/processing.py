from KPIs.averageTime.returnDateProcessing import process_reception_dates
from KPIs.cohorts.prcosseingDate import convert_created_at_to_date
import pandas as pd
from DataProcessing.tagAggregatedColumn import aggregate_tags_in_dataframe
from DataProcessing.sampleColumn import mark_tag_matches
from DataProcessing.b2bColumn import mark_b2b_matches
from DataProcessing.b2cColumn import mark_b2c_matches
from KPIs.totalReturn_b2b_sample_pacakge.cleanReturnColumn import clean_order_numbers


def processing_files(orders, returns):
    # Processing Return Date, Order Date Column
    returns = process_reception_dates(returns)
    orders = convert_created_at_to_date(orders)
    if returns is None or orders is None:
        print("Error calculating date in return, orders data.")
        exit()
    orders['Created at'] = pd.to_datetime(orders['Created at'])
    returns['Reception date'] = pd.to_datetime(returns['Reception date'])
    # ************************

    base_return = returns.copy()

    # Converting Tag Column to B2B and B2C and Sample + Tag Aggregated column addition
    orders = aggregate_tags_in_dataframe(orders)
    if orders is None:
        print("There is an issue processing Tag Aggregated Column.")
        exit()
    orders = mark_tag_matches(orders)
    if orders is None:
        print("There is an issue processing Sample column.")
        exit()
    orders = mark_b2b_matches(orders)
    if orders is None:
        print("There is an issue processing B2B column.")
        exit()
    orders = mark_b2c_matches(orders)
    if orders is None:
        print("There is an issue processing B2C column.")
        exit()
    # ************************

    # Cleaning Order Number in Returns
    returns = clean_order_numbers(returns)
    # ************************

    return orders, returns, base_return

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Get all row ids that are not in orders customer id
    filteredCustomers = customers[~customers['id'].isin(orders['customerId'])] 
    return filteredCustomers[['name']].rename(columns={'name': 'Customers'})


    # Solution 1 
    # leftJoin = customers.merge(orders, left_on='id', right_on='customerId', how='left', indicator=True)
    # leftOnly = leftJoin[leftJoin['_merge'] == 'left_only']
    # return leftOnly[['name']].rename(columns={'name' : 'Customers'})

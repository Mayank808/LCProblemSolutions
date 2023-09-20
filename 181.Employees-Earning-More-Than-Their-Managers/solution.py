import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # merge employee rows to manager rows in table using left_on right_on
    mergedEmployees = employee.merge(employee, how='left', left_on='managerId', right_on='id')
    # select names of all employees x that have salarys > then thier respective manager y
    employees = mergedEmployees[mergedEmployees['salary_x'] > mergedEmployees['salary_y']]['name_x']
    # create a df as above is a selection of rows
    return pd.DataFrame({'Employee': employees})

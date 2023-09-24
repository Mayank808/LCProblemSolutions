import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person[person['email'].duplicated()]['email'].drop_duplicates().to_frame(name='Email')

    # return person[person['email'].duplicated()][['email']].drop_duplicates()
    # note how adding double brackets in selection returns a df instead of series data

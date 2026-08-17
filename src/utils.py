def get_summary_stats(df):
    """
    Return summary statistics for the numeric columns of a DataFrame.
    """
    return df.describe()

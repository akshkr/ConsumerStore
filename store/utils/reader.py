import pandas as pd


def read_rules(file_path):
    if file_path.endswith('.csv'):
        rules = pd.read_csv(file_path)

    else:
        raise ValueError('File Type not supported.')

    return rules


def read_items(file_path):
    if file_path.endswith('.csv'):
        items = pd.read_csv(file_path)

    else:
        raise ValueError('File Type not supported.')

    return items

import pandas as pd
# from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def fuzzy_match(query, column_name, limit=10):
    df = pd.read_excel('bank services.xlsx')
    options = df[column_name].values
    matches = process.extract(query, options, limit=limit)
    return matches

# query = "Долг"
# sheet_name = 'Sheet1'
# column_name = 'Услуги'
# limit = 10
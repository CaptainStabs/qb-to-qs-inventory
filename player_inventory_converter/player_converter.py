import json
import pandas as pd
import csv
import argparse
from datetime import datetime as dt

def process_inventory(line):
    jd = json.loads(line) # Load json from string
    df = pd.DataFrame(jd) # Load json into datafram
    if 'info' in list(df.columns): # Prevents crashing due to an empty inventory (singular edge case)
        df['info'] = df['info'].apply(lambda x: {**x, 'quality': 100} if isinstance(x, dict) else pd.NA if pd.isna(x) else x) # Append quality into info if info has contents
        df['info'] = df['info'].apply(lambda x: {'quality': 100} if x == [] else x) # Add quality to info if there is no content
        df['count'] = df['amount'] # count is the same as amount because quasar is stupid
        df['created'] = dt.utcnow() # All converted items will have the same creation date
        df = df[['name',  'type', 'info',  'amount', 'count', 'slot', 'created']] # reorder just for my sanity and because i don't trust lua
        output = json.dumps(json.loads(df.to_json(orient='records'))).replace(': ', ':').replace(', "', ',"').replace('}, {', '},{') # remove spaces because lua can't be trusted
        return output

def converter(args):
    input_file = args.input_file
    df1 = pd.read_csv(input_file, dtype=str) # load exported data
    df1['inventory'] = df1['inventory'].apply(process_inventory)
    df1.to_csv(input_file.replace('.csv', '') + '_output.csv', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Inventory Converter',
        description='Converts player inventory from qb to qs-inventory')
    parser.add_argument('input_file', nargs='?', default='players.csv', type=str, help='input file')
    args = parser.parse_args()
    converter(args)


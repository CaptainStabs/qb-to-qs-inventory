import json
import pandas as pd
import csv
import argparse
from datetime import datetime as dt

'''
 Manually remove `null` from the input data. (Ctrl+H) 
 `,null,` -> `,`
 `[null,` -> `[`
'''

def converter(args):
    input_file = args.input_file
    df1 = pd.read_csv(input_file, dtype=str)
    df1['items'] = df1['items'].apply(process_inventory)
    df1.to_csv(input_file.replace('.csv', '') + '_converted.csv', index=False)

def process_inventory(line):
    if line:
        jd = json.loads(line)
        jd = [item for item in jd if item != 'null']
        df = pd.DataFrame(jd)

        if 'info' in list(df.columns):
            df['info'] = df['info'].apply(lambda x: {**x, 'quality': 100} if isinstance(x, dict) else pd.NA if pd.isna(x) else x)
            df['info'] = df['info'].apply(lambda x: {'quality': 100} if x == [] else x)
            df['count'] = df['amount']
            df['created'] = dt.utcnow()
            df = df[['name',  'type', 'info',  'amount', 'count', 'slot', 'created']]
            output = json.dumps(json.loads(df.to_json(orient='records'))).replace(': ', ':').replace(', "', ',"').replace('}, {', '},{')
            return output
        else:
            return '[]'
    else:
        print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Glovebox and trunk Converter',
        description='Converts gloveboxes and trunks from qb to qs-inventory')
    parser.add_argument('input_file', type=str, help='input file')
    args = parser.parse_args()
    converter(args)







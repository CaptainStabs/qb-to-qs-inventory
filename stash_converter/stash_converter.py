import json
import pandas as pd
import csv
import re
import argparse
from datetime import datetime as dt

'''
 Manually remove `null` from the input data. (Ctrl+H) 
 `,null,` -> `,`
 `[null,` -> `[`
'''

def converter(args):
    df1 = pd.read_csv('stashitems.csv', dtype=str) # Manually remove `null` from the input data. (Ctrl+H)
    
    df1['items'] = df1['items'].apply(process_inventory)

    df1.to_csv('stash_converted.csv', index=False)

# Qb-inventory
def process_inventory(line):
    pat1 = re.compile(r'\{"\d{1,3}":') # Find beginning index of string, to be removed and converted to list
    pat2 = re.compile(r'"\d{1,3}":') # Find embedded stupidity
    pat3 = re.compile(r'\}\}$') # Convert end of table to list
    if line:
        if line == '[]':
            # print("Empty stash,", line)
            return '[]'

        if re.search(pat1, line):
            # print('Awful dumb type, converting')
            line = re.sub(pat1, '[', line)
            line = re.sub(pat2, '', line)
            line = re.sub(pat3, '}]', line)

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
            print('info not in line', line )
            return '[]'
    else:
        print("else:", line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Stash Converter',
        description='Converts stashes from qb to qs-inventory')
    parser.add_argument('input_file', nargs='?', default='stashitems.csv', type=str, help='input file')
    args = parser.parse_args()
    converter(args)



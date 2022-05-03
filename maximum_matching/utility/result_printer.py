from typing import List, Dict

import pandas as pd

"""
    Write the results from the algorithms to an xls file
"""


def write_results(result):
    array = []

    # Formatting the results for the xls file
    for i in result[0]:
        trend_matches = []
        result = [i['name'], i['matching_size'], ' ', '# Vertices evaluated']

        for k in i['trend']:
            result.append(k[0])
            trend_matches.append(k[1])

        array.append(result)
        col = [' ', ' ', ' ', '# matches']
        for matches in trend_matches:
            col.append(matches)

        array.append(col)

    df = pd.DataFrame(array).T
    df.to_excel(excel_writer="results.xls", sheet_name='sheet1')

    pass


def write_agg_results(result: List[Dict], fname):
    result_dict = {
        "id": [],
        "name": [],
        "repeats": [],
        "size_left": [],
        "size_right": [],
        "avg_matching_size": [],
        "std_matching_size": [],
    }
    for i in range(len(result[0]["avg_trend"])):
        result_dict[f"{i}_avg"] = []

    for i in range(len(result[0]["avg_trend"])):
        result_dict[f"{i}_std"] = []

    # "avg_trend": trend_stack.mean(axis=0),
    # "std_trend": trend_stack.std(axis=0),
    for r in result:
        result_dict['id'].append(r['id'])
        result_dict['name'].append(r['name'])
        result_dict['repeats'].append(r['repeats'])
        result_dict['size_right'].append(r['size_right'])
        result_dict['size_left'].append(r['size_left'])
        result_dict['avg_matching_size'].append(r['avg_matching_size'])
        result_dict['std_matching_size'].append(r['std_matching_size'])

        for i in range(len(r["avg_trend"])):
            result_dict[f"{i}_avg"].append(r['avg_trend'][i])
            result_dict[f"{i}_std"].append(r['std_trend'][i])

    df = pd.DataFrame(result_dict).T
    # df.to_excel(excel_writer=f"{fname}.xls", sheet_name='sheet1')
    df.to_csv(f"{fname}.csv")
    pass

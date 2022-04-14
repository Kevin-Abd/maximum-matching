from typing import List, Dict
from tqdm import tqdm

import maximum_matching.algorithms as alg
import maximum_matching.graphs as graphs
import maximum_matching.utility as util

_algorithms = [
    alg.Vazirani(),
]


def run_on_graph(graph: graphs.GraphBase, algorithms: List[alg.AlgorithmBase]) -> List[Dict]:
    """
    Runts tests with a list on algorithms on a given graph

    :param graph: the populated graph to test on
    :param algorithms: list on algorithms to run
    :return: a list of dictionary with the results of each algorithm
    """

    results = []

    for alg in tqdm(algorithms, desc="Algorithms", position=1, ncols=80, ascii=True, leave=False):
        matching_size, trend = alg.run(graph)

        results.append({
            "name": type(alg).__name__,
            "matching_size": matching_size,
            "trend": trend,
        })
        pass

    return results


if __name__ == "__main__":

    tests = util.parser.load_tests_csv()

    for idx, t in tqdm(tests.iterrows(), total=tests.shape[0], desc="Tests", position=0, ncols=80, ascii=True):

        g: graphs.GraphBase = t["generator"].generate(graph_class=graphs.FullMatrixGraph, **t.to_dict())
        run_on_graph(g, _algorithms)
        pass

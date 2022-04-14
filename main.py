from typing import List, Dict
from tqdm import tqdm
from maximum_matching.algorithms.Vazirani import Vaz
from maximum_matching.algorithms.Blossom import Bloss
import maximum_matching.graphs as graphs
import maximum_matching.utility as util

# For testing
PRINT_OUTPUT = True

# List the algorithms you would like the program to run
_algorithms = [
    Vaz(),  # Vazirani (Online)
    # (Not yet Complete) Bloss()  # Blossom algorithm (Optimal)
]


def run_on_graph(graph: graphs.GraphBase, algorithms) -> List[Dict]:
    """
    Runts tests with a list on algorithms on a given graph

    :param graph: the populated graph to test on
    :param algorithms: list on algorithms to run
    :return: a list of dictionary with the results of each algorithm
    """

    results = []

    for algr in tqdm(algorithms, desc="Algorithms", position=1, ncols=80, ascii=True, leave=False):
        matching_size, trend = algr.run(graph=graph)

        if PRINT_OUTPUT:
            print(matching_size)
            print(trend)
            results.append({
                "name": type(algr).__name__,
                "matching_size": matching_size,
                "trend": trend,
            })

    return results


if __name__ == "__main__":

    tests = util.parser.load_tests_csv()

    for idx, t in tqdm(tests.iterrows(), total=tests.shape[0], desc="Tests", position=0, ncols=80, ascii=True):
        g: graphs.GraphBase = t["generator"].generate(graph_class=graphs.FullMatrixGraph, **t.to_dict())
        run_on_graph(g, _algorithms)
        pass

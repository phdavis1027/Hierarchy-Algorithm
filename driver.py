import networkx as nx
from Tests import (
    test_collection_of_cycles,
    test_cycle,
    test_chain,
    test_fig_two_a,
    test_fig_two_b
)

def main():
    test_cycle()
    test_chain()
    test_fig_two_a()
    test_fig_two_b()
    test_collection_of_cycles()


if __name__ == '__main__':
    main()
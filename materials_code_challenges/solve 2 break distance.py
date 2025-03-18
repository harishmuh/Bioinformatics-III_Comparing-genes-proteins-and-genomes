#  Solve the 2-Break Distance Problem. # Code Challenge
'''
Code Challenge: Solve the 2-Break Distance Problem.
Input: Genomes P and Q. 
Output: The 2-break distance d(P, Q). Extra Dataset

You may be wondering how the graph representation that we have been using for breakpoint graphs could be transformed into an adjacency list. 
After all, we haven’t even labeled the nodes of this graph! Check out Charging Station: From Genomes to the Breakpoint Graph to see 
how to transform a genome into a graph that is easier to work with in our implementations.

Sample Input:
(+1 +2 +3 +4 +5 +6) (+1 -3 -6 -5)(+2 -4)

Sample Output:
3
'''
import networkx as nx

def parse_genome(genome_str):
    """
    Parse a genome string into a list of chromosomes.
    Example: "(+1 +2 +3 +4 +5 +6)" -> [[1, 2, 3, 4, 5, 6]]
    """
    genome_str = genome_str.strip()
    chromosomes = []
    parts = genome_str.split(')')

    for part in parts:
        part = part.replace('(', '').strip()
        if part:
            chrom = [int(x) for x in part.split()]
            chromosomes.append(chrom)

    return chromosomes

def chromosome_to_cycle(chromosome):
    """
    Convert a chromosome to a cycle representation.
    Example: [1, -2, 3] -> [1, 2, 4, 3, 5, 6]
    """
    nodes = []
    for block in chromosome:
        if block > 0:
            nodes.extend([2 * block - 1, 2 * block])
        else:
            nodes.extend([2 * abs(block), 2 * abs(block) - 1])
    return nodes

def colored_edges(genome):
    """
    Construct colored edges from a genome.
    """
    edges = []
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        n = len(nodes)
        for i in range(0, n - 1, 2):
            edges.append((nodes[i + 1], nodes[(i + 2) % n]))
    return edges

def build_breakpoint_graph(P_edges, Q_edges):
    """
    Construct a breakpoint graph using NetworkX.
    """
    graph = nx.Graph()

    for edge in P_edges + Q_edges:
        graph.add_edge(*edge)

    return graph

def count_cycles(graph):
    """
    Count cycles in the breakpoint graph using NetworkX.
    """
    return nx.number_connected_components(graph)

def two_break_distance(P_genome_str, Q_genome_str):
    """
    Compute the 2-break distance between genomes P and Q.
    """
    P = parse_genome(P_genome_str)
    Q = parse_genome(Q_genome_str)

    P_edges = colored_edges(P)
    Q_edges = colored_edges(Q)

    graph = build_breakpoint_graph(P_edges, Q_edges)

    cycles = count_cycles(graph)
    blocks = sum(len(chrom) for chrom in P)

    return blocks - cycles

# Example input
P_genome_str = "(+1 +2 +3 +4 +5 +6)"
Q_genome_str = "(+1 -3 -6 -5)(+2 -4)"

# Compute the 2-Break Distance
result = two_break_distance(P_genome_str, Q_genome_str)
print("2-Break Distance:", result) # Output 2-Break Distance: 3

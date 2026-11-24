import itertools
import json


def swap_checks():
    records = []
    for ground_size in range(10):
        vertices = [(first, second) for first in range(ground_size)
                    for second in range(ground_size) if first != second]
        vertex_set = set(vertices)
        for vertex in vertices:
            neighbor = (vertex[1], vertex[0])
            assert neighbor in vertex_set
            assert neighbor != vertex
            assert (neighbor[1], neighbor[0]) == vertex
        for triple in itertools.combinations(vertices, 3):
            assert not all(second == (first[1], first[0])
                           for first, second in itertools.combinations(triple, 2))
        clique_number = 2 if ground_size >= 2 else 0
        records.append({'ground_size': ground_size, 'vertices': len(vertices),
                        'clique_number': clique_number})
    return records


def pattern_checks():
    records = []
    for cover_indices in range(9):
        pairs = 0
        independent_pairs = 0
        for increasing in range(1 << cover_indices):
            for decreasing in range(1 << cover_indices):
                pairs += 1
                shared = [index for index in range(cover_indices)
                          if increasing & (1 << index) and decreasing & (1 << index)]
                assert bool(shared) == bool(increasing & decreasing)
                if not shared:
                    independent_pairs += 1
                    for index in range(cover_indices):
                        assert not (increasing & (1 << index)
                                    and decreasing & (1 << index))
        assert independent_pairs == 3 ** cover_indices
        records.append({'cover_indices': cover_indices, 'pattern_pairs': pairs,
                        'independent_pattern_pairs': independent_pairs})
    return records


if __name__ == '__main__':
    print(json.dumps({'scope': 'Finite swap graphs and directional membership patterns',
                      'arithmetic': 'exact integers', 'swap_graphs': swap_checks(),
                      'patterns': pattern_checks(), 'status': 'pass'},
                     indent=2, sort_keys=True))

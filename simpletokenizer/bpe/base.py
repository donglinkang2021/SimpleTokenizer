import unicodedata
from typing import List, Tuple, Dict


def get_stats(ids: List[int], counts=None) -> Dict:
    """
    Given a list of integers, return a dictionary of counts of consecutive pairs
    Example: [1, 2, 3, 1, 2] -> {(1, 2): 2, (2, 3): 1, (3, 1): 1}
    Optionally allows to update an existing dictionary of counts
    """
    counts = counts or {}
    for pair in zip(ids, ids[1:]):  # iterate consecutive elements
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def merge(ids: List[int], pair: Tuple[int, int], idx: int) -> List[int]:
    """
    In the list of integers (ids), replace all consecutive occurrences
    of pair with the new integer token idx
    Example: ids=[1, 2, 3, 1, 2], pair=(1, 2), idx=4 -> [4, 3, 4]
    """
    i = 0
    while i < len(ids) - 1:
        if ids[i] == pair[0] and ids[i + 1] == pair[1]:
            ids[i:i + 2] = [idx]
        else:
            i += 1
    return ids

if __name__ == '__main__':
    # test get_stats
    ids = [1, 2, 3, 1, 2]
    counts = get_stats(ids)
    print("Counts of consecutive pairs:")
    print(counts)
    # test merge
    ids = [1, 2, 3, 1, 2]
    pair = (1, 2)
    idx = 4
    new_ids = merge(ids, pair, idx)
    print("Merged ids:")
    print(new_ids)
    assert new_ids == [4, 3, 4]

# python -m simpletokenizer.bpe.base

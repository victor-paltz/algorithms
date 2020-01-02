import random
from itertools import permutations, product, combinations

import numpy as np

from solver.constants import NB_AVIONS
from solver.perm_functions import rev_perm


def all_permutations(support):
    """
    Returns an iterator which
    applies all the possible permutations on a given support.
    """
    support = np.array(support)

    def gen(p):
        for perm in permutations(support):
            perm = np.array(perm)
            p[perm] = p[support]
            yield p
            p[support] = p[perm]
    return gen


def cycles(n, support, randomize=False):
    """
    Returns an iterator which
    generates all the transformations on a permutation in which
    n element are switched.
    """
    support = np.array(support)

    def gen(p):
        g = combinations(support, n)
        if randomize:
            g = list(g)
            random.shuffle(g)

        for local_support in g:
            for output_p in all_permutations(local_support)(p):
                yield output_p

    return gen


def windows_of_permutations(n, step):
    """
    Returns an iterator which
    applies all the possible permutations on sliding windows over the 
    array/permutation given in input.
    """
    def gen(p):
        for i in range(0, NB_AVIONS-n, step):
            for perm in all_permutations(range(i, i+n))(p):
                yield perm
    return gen


def windows_of_permutations_with_transformation(p_trans, n, step):
    """
    Returns an iterator which
    applies all the possible permutations on sliding windows over the 
    transformed array/permutation given in input and return back
    the results when reversing the transformation.
    """
    def gen(p):
        rev_p_trans = rev_perm(p_trans)
        for modif_p_T_bis in windows_of_permutations(n, step)(p[p_trans]):
            yield p[rev_p_trans]
    return gen

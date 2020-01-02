import random
from os import walk

import numpy as np


def save_perm(file_name, p):
    """
    Save a permutation in a file
    """
    with open(file_name, "w") as f:
        f.write("\n".join(str(x) for x in np.array(p)+1))


def load_perm(file_name):
    """
    Load a permutation from a file
    """
    with open(file_name, "r") as f:
        s = f.read()
    return np.array([int(x) for x in s.strip().split("\n")])-1


def load_best(folder):
    """
    Load the permutation with the best score among the files in the format "{score}_{name}.txt"
    """
    all_files = []
    for (dirpath, dirnames, filenames) in walk(folder):
        all_files.extend(filenames)
        break
    return load_perm(folder+"/"+min((int(f.split("_")[0]), f) for f in all_files if "_" in f)[1])


def rev_perm(p):
    """
    Return the reversed permutation q of p (q verify p(q(x)) = q(p(x)) = x)
    """
    p2 = np.zeros_like(p)
    p2[p] = np.arange(len(p))
    return p2


def apply_random_perm(p, k):
    """
    Apply a random permutation on k elements of a permutation p
    """
    support = np.random.choice(p, k, replace=False)
    p[support] = p[np.random.permutation(support)]
    return p, support

import numpy as np

from perm_functions import load_perm

# Read the input file
with open("data/input_10.txt", "r") as f:
    s = f.read()
t = s.strip().split("\n")

# Create the constants of the problem
NB_AVIONS = int(t[0])
D = np.array([[int(x) for x in li.split(",")] for li in t[1:NB_AVIONS+1]])
T = np.array([[int(x) for x in li.split(",")] for li in t[NB_AVIONS+1:2*NB_AVIONS+1]])

p_T = load_perm("data/p_T.txt")
p_D = load_perm("data/p_D.txt")

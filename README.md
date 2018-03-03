# Introduction
This repository hosts a bounded Post correspondence problem solver.

# Running
Ensure you have installed [treelib](https://github.com/caesar0301/treelib)

# Theory
**Definition:** A <i>prefix</i> of a string S is some string S' that occurs at the beginning of S.

**Claim:** α<sub>i</sub> and β<sub>i</sub> will lead to a *"possible"* solution ⇔ α<sub>i</sub> and β<sub>i</sub> are equal or one is the prefix of the other.

# Algorithm
We solve the algorithm by means of dynamic tree generation, which will bring us closer to our solution, if such one exists. Generating a tree for the bounded Post correspondence problem is as follows. For each i, group α<sub>i</sub> and β<sub>i</sub> as a single node attached to a root node. Using our claim above, we can determine if any of these nodes are worth generating further.

# Analysis
In the worst case, this algorithm generates a set of solutions at O(2<sup>k</sup>), which is equivalent to a standard brute force solution. 

True runtime of this algorithm is still to be determined.
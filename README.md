# Introduction
The problem was formulated by [Emil Post in 1946](http://www.ams.org/journals/bull/1946-52-04/S0002-9904-1946-08555-9/S0002-9904-1946-08555-9.pdf) and has been used as a theoretical notion of undecidability in the field of Computer Science and Mathematics. Since the original problem itself is NP-complete, a variant was created in which we limit our search for a solution up to a limit of *k* tiles, which is known as the bounded Post correspondence problem. This respository hosts a algorithm which solves this problem. The algoritm will be described in detail and its complexity will be analyzed.

# Running
Ensure you have installed [treelib](https://github.com/caesar0301/treelib). 

# Theory
**Definition:** A <i>prefix</i> of a string S is some string S' that occurs at the beginning of S.

**Claim:** If α<sub>i</sub> and β<sub>i</sub> are not equal or they are not a prefix of each other ⇒ α<sub>i</sub> and β<sub>i</sub> cannot lead to a solution.

**Proof** Suppose that α<sub>i</sub> and β<sub>i</sub> are not equal and they are not a prefix of each other.

# Algorithm
We solve the algorithmic problem by means of dynamic tree generation, which will bring us closer to our solution, if one exists. Generating a tree for the bounded Post correspondence problem is as follows. For each i, group α<sub>i</sub> and β<sub>i</sub> as a single node. If it fails our claim we do not consider it for further depth. If it does succeed our claim, then we perform concatenation. By concatenating the previous node to the new node, we can continusouly check if one is the prefix of the other or if they are equal, which allows us to check if the given node will lead to a promising solution. If they do not contain a prefix then we can guarantee there will be no solution by taking that route (to be proved). 

A run of the algorithm would resemble the following flow:
![Example](https://i.gyazo.com/874460bff0f0f3904b310276aaf37fbc.png)

# Analysis
In the worst case, this algorithm generates a set of solutions at O(2<sup>k</sup>) where k is the depth of the tree, which is equivalent to a standard brute force solution meaning that there was no tree trimming performed and all paths were accounted for. While this is very unlikely, there are instances where this could occur and must be accounted for.

True runtime of this algorithm is still to be determined.

# Optimizations
* Try to incorporate dynamic programming.
* Optmizing the data storage method to speed up algorithm runtime.
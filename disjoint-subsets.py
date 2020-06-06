"""
Let S be a set of 10 distinct elements, chosen randomly from the set k = {1, 2, . . . , 100}.
Prove that there exist two nonempty disjoint subsets T and U of S that have equal sums. Generate all such subsets.

Proof.    To demonstrate that there exist two subsets of S with equal sums, we use the Pigeonhole Principle.
The number of possible subsets T and U is given by 2^10 - 2 = 1022.
These are our pigeons. The subset containing the largest possible sum is {100, 99, 98, 97, 96, 95, 94, 93, 92},
with the sum 864. Therefore, the set of all possible sums contained by any subset is {1, 2, 3, . . . , 864}.
These are our pigeonholes. Since there are many more possible subsets than there are possible sums,
it follows that there exist at least two distinct subsets T and U that share the same sum.

From the distinct, sum-sharing subsets, we can construct two that are also disjoint.
If T and U are not already disjoint, they must share some elements in common.
We call those shared elements members of the set X. Thus, T = T' + X and U = U' + X.
By removing X from T and U, we have T' and U',
which are equal in sum, disjoint, and nonempty subsets of S.    Q.E.D.

Given that the possibilities for T and U are the "pigeons" and the possible sums are the "pigeonholes",
the cardinality of S and the range of k constrain each other.
So long as the expression in check_theorem_validity() is true, the proof is valid.

"""

import random

s = set()
while len(s) < 10:
    s.update({random.randint(1, 100)})
s = frozenset(s)

k = list(range(1, 101))


def check_theorem_validity(mainset):
    return 2**len(mainset) > sum(k[-len(mainset) + 1:])


def powerset(mainset):
    if len(mainset) == 0:
        return {frozenset()}  # for completeness
    else:
        subsets = set()
        first, *rest = mainset
        for subset in powerset(rest):
            subsets.add(subset)
            subsets.add(frozenset({first} | subset))
        return subsets


def get_subsets(mainset):
    setlist = []
    p = powerset(mainset)
    for t in p:
        for u in p - t:
            if sum(t) == sum(u):
                t, u = t - u, u - t
                if frozenset((t, u)) not in setlist and t and u:
                    setlist.append(frozenset((t, u)))
                    print(f'T is {set(t)} and U is {set(u)}')
    print(f'For S = {set(mainset)}, there are {len(setlist)} disjoint subsets with equal sums.')

testset = [1, 2, 3, 4]
print(check_theorem_validity(s))
get_subsets(s)

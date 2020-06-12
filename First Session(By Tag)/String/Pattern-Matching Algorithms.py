# Brute-Force

# Time Complexity: O(nm) in the worst-case
# Space Complexity: O(1)

def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else - 1)."""
    n, m = len(T), len(P)   # introduce convenient notations
    for i in range(n-m+1):  # try every potential starting index within T
        k = 0               # an index into pattern P
        while k < m and P[k] == T[i+k]:    # kth character of P matches
            k += 1
        if k == m:          # if we reached the end of pattern,
            return i        # substring T[i:i+m] matches P
    return -1               # failed to find a match starting with any i

# The Boyer-Moore Algorithm

# Time Complexity: O(nm) for the worst-case
# Space Complexity: O(1)

def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)    # introduce convenient notations
    if m == 0:               # trivial search for empty string
        return 0

    last = {}                # build 'last' dictionary
    for k in range(m):
        last[P[k]] = k       # later occurrence overwrites
    # align end of pattern at index m-1 of text
    i = m-1                  # an index into T
    k = m-1                  # an index into P

    while i < n:
        if T[i] == P[k]:     # a matching character
            if k == 0:
                return i     # pattern begins at index i of text
            else:
                i -= 1       # examine previous character
                k -= 1       # of both T and P
        else:
            j = last.get(T[i], -1)   # last(T[i]) is -1 if not found
            i += m - min(k, j+1)     # case analysis for jump step
            k = m-1                  # restart at end of pattern
    return -1

# The Knuth-Morris-Pratt Algorithm (KMP)

# Time Complexity: O(n+m)
# Space Complexity: O(m)

def compute_kmp_fail(P):
    """Utility that computes and returns KMP 'fail' list."""
    m = len(P)
    fail = [0]*m                   # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:                   # compute f(j) during this pass, if nonzero
        if P[j] == P[k]:           # k+1 characters match thus far
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:                # k follows a matching prefix
            k = fail[k-1]
        else:                      # no match found starting at j
            j += 1
    return fail

def find_kmp(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)         # introduce convenient notations
    if m == 0:                    # trivial search for empty string
        return 0
    fail = compute_kmp_fail(P)    # rely on utility to precompute
    j = 0                         # index into text
    k = 0                         # index into pattern
    while j < n:
        if T[j] == P[k]:          # P[0:k+1] matched thus far
            if k == m-1:          # match is complete
                return j - m + 1
            else:                 # try to extend match
                j += 1
                k += 1
        elif k > 0:
            k = fail[k-1]         # reuse suffix of P[0:k]
        else:
            j += 1
    return -1                     # reached end without match













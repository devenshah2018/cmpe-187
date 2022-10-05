# Merge two sorted arrays A and B into sorted array C
def mergeArrays(A, B, m, n):
    C = [None] * (m + n)
    i = 0
    j = 0
    k = 0

    # Loop through both arrays
    while i < m and j < n:
        # Set C[kth] element to A[i] if A[i] < B[j], increment i and k
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
            k += 1
        # Set C[kth] element to B[j] if A[i] > B[j], increment j and k
        else:
            C[k] = B[j]
            j += 1
            k += 1

    # Loop through and add remaining elements of A to C
    while i < m:
        C[k] = A[i]
        i += 1
        k += 1

    # Loop through and add remaining elements of B to C
    while j < n:
        C[k] = B[j]
        j += 1
        k += 1

    return C


def main():
    A = [1, 2, 7, 11]
    B = [3, 7, 13, 16, 29]
    m = len(A)
    n = len(B)

    C = mergeArrays(A, B, m, n)

    print("A:", A)
    print("B:", B)
    print("C:", C)


if __name__ == "__main__":
    main()

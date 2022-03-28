def n_ty_wyraz(ak, q, n, k):
    return ak * q ** (n - k)


def suma_wyrazow(a1, q, n):
    if q != 1:
        return a1 * (1 - q ** n) / 1 - q
    else:
        return a1 * n

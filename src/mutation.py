AA = "ACDEFGHIKLMNPQRSTVWY"

def generate_mutants(seq):
    library = []

    for i in range(len(seq)):
        for aa in AA:

            if aa != seq[i]:

                s = list(seq)
                s[i] = aa

                library.append({
                    "position": i,
                    "wt": seq[i],
                    "mut": aa,
                    "sequence": "".join(s)
                })

    return library
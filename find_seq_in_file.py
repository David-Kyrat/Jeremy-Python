#enzyme = "GTTAAC"
#seq = "ACGTTAACCGTTAACAATTC"

with open('ListeSequences.txt','r', encoding='utf-8') as f :
    sequence=f.readlines()

def formatresult(liste):
    texte = [str(el) for el in liste]
    return ", ".join(texte)


def combien(seq, enzyme) :
    nbr = seq.count(enzyme)
    return nbr

def ou(seq, enzyme):
    n = len(seq)
    m = len(enzyme)
    print("n,m", n, m)
    matches = []

    for i in range(n-m):
        if seq[i: i+m] == enzyme:
            print("i+m", i+m, " seq", seq)
            matches.append(i)
    print(" ")

    return formatresult(matches)


# B
#print (combien(seq2,enzyme),ou (seq2,enzyme))

# C


def print_seq(sequence, enzyme):
    for line in sequence:
        clearline = line.rstrip()
        if combien(clearline, enzyme) == 0:
            print("la séquence", line, "ne possède pas de site de restriction")
        else:
            print("la séquence", line, "possède", combien(clearline, enzyme),
                "sites de restrictions aux positions", ou(clearline, enzyme))


enzyme = "GTTAAC"
print_seq(sequence, enzyme)

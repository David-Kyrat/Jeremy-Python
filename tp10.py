def histoOne(sequence):
    dico = {}
    lseq = list(sequence)
    sseq = set(sequence)
    # print(lseq)
    # print(sseq)

    for aa in sseq:  # pour que chaque el soit compter une fois
        dico[aa] = lseq.count(aa)  # sequence.count fonctionne aussi

    return dico


# print(histoOne("MDSDAASQMAREP"))

def histoMult(sequences):
    joinseq = "".join(sequences)  # déja split vu que liste
    print(joinseq)
    return histoOne(joinseq)


# print(histoMult(["MDSDA","ASQMA","MASP"]))


def histoNorm(sequences):
    dico = {}
    joinseq = "".join(sequences)
    sseq = set(joinseq)
    toIgnore = ["\n", " ", "_", "-"]     # compte plus les "\n" retour à la ligne, espaces etc...
    for char in toIgnore:
        sseq.discard(char)

    for aa in sseq:
        dico[aa] = joinseq.count(aa)
    return dico

# print(histoNorm(["MDSDA","ASQMA","MASP"]))
def readFile(fileName):
    with open(fileName) as f:
        content = f.read()
    return content


# Alors en fait on peut pas utiliser OS comme clé parce quils sont pas tous unique
# genre t'as 2 fois "OS=Homo Sapiens" donc ça va pas marcher
# donc faut utiliser le truc juste à coté du "sp", genre P31946, P48347 etc... comme clé/identifiant
# Je t'ai mis a jour le code en dessous
#

def extract_dict(file_name):
    entries = readFile(file_name).split(">")#[1:]
    entries.pop(0)
    dico = {}

    for entry in entries:
        # on cherche la clé / l'identfiant, => c'est le truc juste après le premier "|"
        id_start = entry.find("|") + 1
        id_end = id_start + 6  # l'identifiant fait toujours 6 chiffres/lettres
        id = entry[id_start:id_end]

        os_start = entry.find("OS=")  # retourne l'index du 'O'
        os_end = entry.find("=", os_start + len("OS=")) - 3  # pour avoir la fin, on doit donc rajouter len("OS")
        # find(valeur,start,stop)
        os = entry[os_start:os_end]

        dna_seq_start = entry.find("\n", os_end + 1) + 1  # +1 car on ne veut pas prendre le "\n" du début
        dna_seq = entry[dna_seq_start:]
        dico[id] = os, dna_seq  # ici du coup on a une paire de string

    return dico

def dicoHisto(fasta_filename):
    histo = {}
    dico = extract_dict(fasta_filename)
    for k, v in dico.items():
        freq = histoNorm(v[1])
        histo[k] = v[0], freq
    return histo


if __name__ == '__main__':
    miniFile, bigFile = "./res/mini.fasta", "./res/uniprot_entries.fasta"
    hist = dicoHisto(bigFile)
    for k, v in hist.items():
        print(k)
        print("\t", v)
        print("")


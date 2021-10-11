# In diesem Skript sind alle nötigen Funktionen enthalten, um die Aufgabe
# 'Projekt Einführung in Python' lösen zu können.

# Funktion, die die Qualität eines Alignments berechnet:
# Input: string(sequnez1), string(sequenz2)
# Output: string(sequenz1), string(Qualität), string(sequenz2)

def alignQuali(sequenz1, sequenz2):
    # Zunächst wird eine Variable mit der Qualitätsliste aus der
    # Aufgabenstellung erstellt.
    q_list = ["AA", "GG", "CC", "TT",
              "CT", "TC", "AG", "GA",
              "CA", "AC", "CG", "GC", "TA", "AT", "TG", "GT"]
    # Es folgt eine leere Liste, in der die beiden Nukleotide,
    # die von den beiden Sequenzen miteinander verglichen werden sollen,
    # als jeweils 1 Listenelement aufgenommen werden können.
    nucleotide_pairs = []
    # Nun braucht man einen leeren String - der Qualitätstring - der mit den
    # Symbolen für die Qualität gefüllt werden kann.
    q_line = ("")
    # Da bei dieser Funktion nur fertige Alignments miteinander verglichen
    # werden sollen, die die gleiche Länge haben, wird in dieser if-Abfrage
    # überprüft, ob die beiden eingegebenen Sequenzen die gleiche Länge haben.
    # Nur wenn dies der Fall ist, geht die Funktion weiter.
    if len(sequenz1) != len(sequenz2):
        print("Die Sequenzen müssen für die alignQuali-Funktion die gleiche "
              "Länge haben!")
    else:
        # In dieser for-Schleife wird die nucleotide_pairs Liste mit
        # Elementen befüllt, die in den Sequenzstrings jeweils an der Position
        # i stehen.
        for i in range(len(sequenz1)):
            nucleotide_pairs.append(sequenz1[i] + sequenz2[i])
        # Nun wird über die von befüllte nucleotide_pairs Liste iteriert und
        # gefragt, ob sich das Nukleotidpaar an der Stelle i in der Qualitäts-
        # liste q_list befindet.
        for i in range(len(nucleotide_pairs)):
            if nucleotide_pairs[i] in q_list:
                # Ist das Nukleotidpaar in der q_list enthalten, wird über-
                # prüft, an welchem Index das jweilige Paar in der q_list steht
                # und dadurch der "Match" des Paares bewertet.
                # Das jeweilige Ergebnis wird in Form eines Symbols in den zu
                # Beginn leeren Qualitätstring q_line konkateniert.
                if q_list.index(nucleotide_pairs[i]) <= 3:
                    q_line += "|"
                elif 4 <= q_list.index(nucleotide_pairs[i]) <= 7:
                    q_line += ":"
                elif 8 <= q_list.index(nucleotide_pairs[i]) <= 15:
                    q_line += "."
            # Ist eine Lücke in einer der Sequenzen enthalten, wird ein Leer-
            # zeichen im Qualitätstring an der jeweligen Stelle gesetzt.
            else:
                q_line += " "
        # Zu guter letzt wird das Ergebnis in der Form ausgegenen, dass in der
        # ersten Zeile die Sequenz 1 steht, direkt darunter der Qualitäts-
        # string und darunter wiederum die Sequenz 2.
        print(sequenz1)
        print(q_line)
        print(sequenz2)


if __name__ == "__main__":
    sequenz1 = ("GGTCAAAG_TA")
    sequenz2 = ("GGACTAGGGTA")

    print(sequenz1, sequenz2)
    alignQuali(sequenz1, sequenz2)

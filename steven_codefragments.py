
def accepted_characters(sequenz):
    if not type(sequenz) != type(""):
        sequenz = str(sequenz)
    #hier noch exception falls nicht als string castbar

    accepted_characters = ["A", "a", "C", "c", "G", "g", "T", "t", "_"]
    list_acc_bool = []
    index_unaccepted = []
    for i in range(len(sequenz)):
        if sequenz[i] in accepted_characters:
            list_acc_bool.append(True)
        else:
            list_acc_bool.append(False)
            index_unaccepted.append(i)

    if index_unaccepted:
        print(f"in {sequenz} nicht akzeptierte Characters an Index: {index_unaccepted}")
        #return False
    #else:
    #    return True

def quality_control(sequenz1, sequenz2):
    if accepted_characters(sequenz1) and accepted_characters(sequenz2):
        if len(sequenz1) == len(sequenz2):
            print ("quality check passed")
            return True
        else:
            print("quality check failed")
            #hier noch dialog?
            return False


if __name__ == "__main__":

    #testsequenzen
    #sequenz1 = ("g", "a", "c", "g")
    #sequenz2 = ("A", "a", "c", "A")
    sequenz1 = "ACTGGCTATTTCC___TAGCT"
    sequenz2 = "AATCGCTATTTCC_A_CAGCG"
    """"
    if accepted_characters(sequenz1):
        print("True")
    else:
        print("false")

    """
    #
    if quality_control(sequenz1, sequenz2):
        print("true")
    else:
        print("fail")

    #dictionary
    perfect_match = ["AA","GG","CC","TT"]
    good_match = ["CT","TC","AG","GA"]
    bad_match = ["CA","AC","CG","GC","TA","AT","TG","GT"]
    """
    von liste string erzeugen erforder join: from str import join
    alignment = []
    for i in range(len(sequenz1)):
        compare =sequenz1[i].upper() + sequenz2[i].upper()
        if compare in perfect_match:
            alignment.append("|")
        elif compare in good_match:
            alignment.append(":")
        elif compare in bad_match:
            alignment.append(".")
        else:
            alignment.append("_")
    """

    alignment_str = ""

    for i in range(len(sequenz1)):
        compare =sequenz1[i].upper() + sequenz2[i].upper()
        if compare in perfect_match:
            alignment_str +="|"
        elif compare in good_match:
            alignment_str += ":"
        elif compare in bad_match:
            alignment_str+="."
        else:
            alignment_str+="_"


    print(sequenz1)
    print(alignment_str)
    print(sequenz2)

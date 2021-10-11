#def check_input(sequenz1, sequenz2)
#    if type(sequenz1)


def accepted_characters(sequenz):
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
        print(f"nicht akzeptierte Characters an Index: {index_unaccepted}")
        return False
    else:
        return True

print(accepted_characters("AAAfgttt__rr"))

""""
def compare_base (Liste1, Liste2)
    #[„AA“,“GG“,“CC“,“TT“,“CT“,“TC“,“AG“,”GA”,”CA“,“AC“,“CG“,“GC“,“TA“,“AT“,”TG”,”GT”]
    # [„AA“,“GG“,“CC“,“TT“,“CT“,“TC“,“AG“,”GA”,”CA“,“AC“,“CG“,“GC“,“TA“,“AT“,”TG”,”GT”]
    accepted_characters = ("A", "a", "C", "c", "G", "g", "T", "t", "_")
    if character in accepted characters
    if nt_list1 ==0"_" or 
if __name__ == "__main__":
"""
sequenz1 =("g","d","f","g")

if type(sequenz1)!= type(""):
    print(type(sequenz1))
    sequenz1 = str(sequenz1)
    print(type(sequenz1))
    print("blub")
    print("blub2")
print("TEST")

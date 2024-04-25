# The dictionary for the transation (this dictionary will store the DAN-amino acids mapping)
aa_d = {}

# the FASTA file (this list will store the FASTA file)
DNA_d = []

# the correct translation (is given for cross-checking)
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

#INPUT name of amino acid file (make sure that you keep the amino_acids.txt under Assignment8 folder)
#RETURN a dictionary 
#Key is a tuple (c0, c1, ... , cn) where ci are codons
#Value is a pair [name, abbreviation] for the amino acid
#make sure to close the file after reading it
def get_amino_acids(name):
    f = open(name, "r")
    for i in f.readlines():
        codonTuple = ()
        aaList = []
        aaName = ''
        i = i.replace(',','')
        print(i)
        i = i.split()
        for j in i[::-1]:
            if len(j) == 3 and j.isupper() and j.isalpha():
                codonTuple += (j,)
            elif (len(j) == 1 and (j.isupper() and j.isalpha() or j == "-")):
                aaCode = j
            else:
                if j != aaCode:
                    aaName += j
        aaList.append(i[0])
        aaList.append(aaCode)
        aa_d[codonTuple] = aaList
    f.close()
    return aa_d
    

#INPUT file name of the DNA file (make sure that you keep the DNA.txt under Assignment8 folder)
#RETURN a list [header, DNA]
#header is first line in the file
#DNA is a string of letters from remainder of file
#no whitespace
#make sure to close the file
def get_DNA(name):
    f = open(name, "r")
    tmpStr = ''
    for i in f.readlines():
        if i[0] == ">": #header
            DNA_d.append(i.strip())
        else:
            tmpStr += i.strip()
    DNA_d.append(tmpStr)
    return DNA_d

#INPUT FAST file
#RETURN a string representing the protein (convert the DNA to amino acids)
#using the dictionary
def translate(DNA_d):
    aaStr = ''
    protein = DNA_d[1]
    for i in range(2,len(protein), 3):
        code = protein[i-2] + protein[i-1] + protein[i]
        for k in aa_d:
            if code in k:
                aaStr += aa_d[k][1]
    return aaStr


    
# ! Important !

# To test the code of Problem-1, You may not run it directly in VSC (due to File not found error), 
# please follow the instructions below.

# 1. Open a new Terminal in VSC. 

# Run the below command in the terminal i.e. after typing in the command, hit enter
# 2. cd Assignment8

# Now run the a8.py in the newly opened terminal i.e. type the below command and hit enter
# 3. python3 a8.py

# It should print output on the terminal based on how much of the problem have you completed. Using this way
# of running, you can easily monitor your progress on this problem.


if __name__ == "__main__":
    '''for your use'''
    
    # #PROBLEM 1
    # #do not change file names
    fn1,fn2 = "amino_acids.txt","DNA.txt"
    aa_d = get_amino_acids(fn1)
    DNA_d = get_DNA(fn2)
    protein = translate(DNA_d)

    print("Dictionary")
    print(aa_d)
    print("FASTA file")
    print(DNA_d)
    print("Translations match:", str(protein == actual))

    #should return "PLHS"    
    print(translate(["nothing", "CCACTGCACTCA"]))

    #should returns "D-"
    print(translate(["nothing", "GACTAA"]))
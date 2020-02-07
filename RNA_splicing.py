from textwrap import wrap


#create codon/Amino acid table for RNA and stop codons
RNA_table = {
    'UUU':'F','UUC':'F','UUA':'L',
    'UUG':'L','UCU':'S','UCC':'S',
    'UCA':'S','UCG':'S','UAU':'Y',
    'UGU':'C','UGC':'C','UGG':'W',
    'CUU':'L','CUC':'L','CUA':'L',
    'CUG':'L','CCU':'P','CCC':'P',
    'CCA':'P','CCG':'P','CAU':'H',
    'CAC':'H','CAA':'Q','CAG':'Q',
    'CGU':'R','CGC':'R','CGA':'R',
    'CGG':'R','AUU':'I','AUC':'I',
    'AUA':'I','AUG':'M','UAC':'Y',
    'ACU':'T','ACC':'T','ACA':'T',
    'ACG':'T','AAU':'N','AAC':'N',
    'AAA':'K','AAG':'K','AGU':'S',
    'AGC':'S','AGA':'R','AGG':'R',
    'GUU':'V','GUC':'V','GUA':'V',
    'GUG':'V','GCU':'A','GCC':'A',
    'GCA':'A','GCG':'A','GAU':'D',
    'GAC':'D','GAA':'E','GAG':'E',
    'GGU':'G','GGC':'G','GGA':'G',
    'GGG':'G'}

stop_codons = {
    'UAA':'Stop', 'UAG':'Stop', 'UGA':'Stop'}

#create empty strings/lists for sequence and introns
dna_seq = ''
dna_seq_new = ''

intron_list = []

#open fasta file and read it
i_f = open('rosalind_splc3.txt')
g = i_f.readlines()

#loop through and remove all "newline" characters from fasta file
for i in range(0, len(g)):
    g[i]=g[i].rstrip()

#start looping again through file line by line
for i in range(0, len(g)):
    
   #if line does not start with a header and is the first sequence, start another loop
   #the second loop goes thorugh the file again to append the first sequence together, (since they are split as new lines in the file)
   #once it reaches a line where the next line is a header, it breaks out of the loop and returns the first sequence which is the reference sequence 
    if not g[i].startswith('>') and i == 1:
        for m in range(1, len(g)):
            if not g[m].startswith('>') and not g[m+1].startswith('>'):
                dna_seq = dna_seq + g[m]
        
            if not g[m].startswith('>') and g[m+1].startswith('>'):
                dna_seq = dna_seq + g[m]
                break
#every other header after the first one indicates an intron sequence, so append the following introns to the intron list    
    if g[i].startswith('>') and i != 0:
        intron_list.append(g[i+1])
                
            
                    
dna_seq_new = dna_seq

#now search through the intron list and strip all the newlines (if any)
#search the intron list and replace any introns in the original dna sequence with a blankspace (effectively removing the intron)
for j in range(0, len(intron_list)):
    intron_list[j] = intron_list[j].rstrip()
    dna_seq_new = dna_seq_new.replace(intron_list[j], '')

#change the DNA strand to RNA
rna_seq = [dna_seq_new.replace('T', 'U')]

#break the RNA strand into 3 letter codons and create an empty protein string
RNA_codons = wrap(rna_seq[0], 3)
protein = ''

#refer to the RNA codon table and translate the RNA codons into an amino acid/protein string
for b in RNA_codons:
    if b in RNA_table:
        protein = protein + RNA_table[b]
    if b in stop_codons:
        break

#print the protein string    
print(protein)


        

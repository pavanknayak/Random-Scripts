#open file, and attach indexes to it

f = open('rosalind_gc1.txt')
g = enumerate(f)

#create lists and strings for later use
counter  = 0
counter_list = []
header_list = []
seq_string = ''
all_gc_content = []
seq_string_list = []

#start looping through file and adding indexes
for index, line in g:
    
    #create list of headers to pick highest from later
    if line.startswith('>'):
        counter += 1
        counter_list.append(counter)
        header_list.append(line)
    
    #identify header lines and add not index ==0 to avoid divide by zero error from GC calculation for first header
    if line.startswith('>') and not index == 0:
        
        #calculate GC content of previous previous sequence and add to list
        total_count = []
        GC_count =[]
        for i in seq_string:
            total_count.append(i)
            if i is 'C':
                GC_count.append(i)
            if i is 'G':
                GC_count.append(i)
        
        all_gc_content.append(len(GC_count)/len(total_count))
        seq_string_list.append(seq_string)
        seq_string = ''
    
    #add sequence to list and strip "new character" symbols
    if not line.startswith('>'):
        seq_string += line.rstrip()

#add last sequence to list of sequences
seq_string_list.append(seq_string)

#calculate GC content for last sequence
total_count = []
GC_count = []
for j in seq_string_list[-1]:
    total_count.append(j)
    if j is 'C':
        GC_count.append(j)
    if j is 'G':
        GC_count.append(j)


all_gc_content.append(len(GC_count)/len(total_count))

#calculate highest gc content value and find the index for that value in the header list, then print header and highest corresponding GC value
max_value = max(all_gc_content)
max_index = all_gc_content.index(max_value)

print(header_list[max_index][1:])
print('{}%'.format(max_value))
        
        
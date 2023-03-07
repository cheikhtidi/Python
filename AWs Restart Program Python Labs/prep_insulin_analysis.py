def prep(a):
    with open (a, 'r') as file:
        # Read the contents of the file
        contents = file.read()
        
        # Split the contents based on return carriages and output a list
        lines = contents.split('\n')
        # Remove any leading or trailing whitespace from the lines
        lines = [line.strip() for line in lines]
        # Keep the elements of the list except ORIGIN and //
        lines=lines[1:3]
        lines[0]=lines[0][2:]
        lines[1]=lines[1][3:]
        s=''.join(lines)
        #print(s)
        l=s.replace(" ","")
        #output the content of preproinsulin-seq-clean.txt 
    return l
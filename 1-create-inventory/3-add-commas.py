myCharacter = ','
outFilename = 'data\log-new-add-commas.txt'
inFilename = 'data\log-new-remove-empty-lines.txt'
with open(outFilename, 'w') as out_file:
    with open(inFilename, 'r') as in_file:
        for line in in_file:
            out_file.write(line.rstrip('\n') + myCharacter + '\n')



		
print ('process 3 complete')
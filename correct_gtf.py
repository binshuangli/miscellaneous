#Correct gtf file to make sure the CDS information is a multiply of 3 so that it will work with SNPGenie.
import  csv
with open("utg000001l_pilon10_corrected_0start.gtf","w") as f2:
	with open("utg000001l_pilon10.gtf") as f:
		for line in f:
			newline = line.rstrip('\n').split('\t')
			scaffold = newline[0]
			source = newline[1]
			type = newline[2]
			start = int(newline[3])
			end = int(newline[4])
			score = newline[5]
			strand = newline[6]
			if newline[7] == '.':
				phase = newline[7]
			else:
				phase = int(newline[7])
			attributes = newline[8]
			if strand == "+" and phase!='.':
				modular = (end - start + 1 - phase)%3
				start = start + phase
				end = end - modular
			elif strand == "-" and phase!='.':
				modular	= (end - start + 1 - phase)%3
				end = end - phase
				start = start +  modular
			phase = 0
			result = [scaffold,'\t',source,'\t',type,'\t', str(start),'\t',str(end),'\t',score,'\t',strand,'\t',str(phase),'\t',attributes]
			f2.writelines(result)
			f2.write('\n')

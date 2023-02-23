Phrase=str(input("Donner une phrase"))
sa=''
for i in range (len(Phrase)):
    if (Phrase[i])==' ' and (Phrase[i+1])==' ':
        continue
    else:
        sa=sa+Phrase[i]

print(sa)
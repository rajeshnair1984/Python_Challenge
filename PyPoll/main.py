import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'election_data.csv')

vote = 0
vote_Khan = 0
vote_Correy = 0
vote_Li = 0
vote_Tooley = 0
vote_percandi = []
candi = []
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    print(csv_header)
    for candidate in range(4):
        candidate = input("Name of the candidate?")
        candi.append(candidate)
    print(candi)

    for row in csv_reader:
        if len(row[0]) > 0:
            vote_count = vote + 1
            vote = vote_count
            if row[2] == "Khan":
                vote_count_Khan = vote_Khan + 1
                vote_Khan = vote_count_Khan
            if row[2] == "Correy":
                vote_count_Correy = vote_Correy + 1
                vote_Correy = vote_count_Correy
            if row[2] == "Li":
                vote_count_Li = vote_Li + 1
                vote_Li = vote_count_Li
            if row[2] == "O'Tooley":
                vote_count_Tooley = vote_Tooley + 1
                vote_Tooley = vote_count_Tooley
print(f'Total Vote: {vote}')
# print(vote_Khan)
# print(vote_Correy)
# print(vote_Li)
# print(vote_Tooley)

#CALCULATE PERCENTAGE OF VOTE FOR EACH CANDIDATE.

voteper_Khan = (vote_Khan/vote)*100
vote_percandi.append(voteper_Khan)
voteper_Correy = (vote_Correy/vote)*100
vote_percandi.append(voteper_Correy)
voteper_Li = (vote_Li/vote)*100
vote_percandi.append(voteper_Li)
voteper_Tooley = (vote_Tooley/vote)*100
vote_percandi.append(voteper_Tooley)

max = 0

for i in range(len(vote_percandi)):
    if vote_percandi[i] > max:
        max = vote_percandi[i]
    else:
        max = max

        # if vote_percandi[i] = max:
        #     print(index.vote_percandi) 

print(max)


print(f'Khan: {voteper_Khan:.3f}% ({vote_Khan})')
print(f'Correy: {voteper_Correy:.3f}% ({vote_Correy})')
print(f'Li: {voteper_Li:.3f}% ({vote_Li})')
print(f"O'Tooley: {voteper_Tooley:.3f}% ({vote_Tooley})")
print(vote_percandi)




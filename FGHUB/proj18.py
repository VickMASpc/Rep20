gryfPts = 0
huflPts = 0
rvncPts = 0
slthPts = 0

q1 = "Do you like Dawn or Dusk?"
q2 = "When I’m dead, I want people to remember me as:"
q3 = "Which kind of instrument most pleases your ear?"

print(f'{q1}\n1) Dawn\n2) Dusk')

q1ans = int(input(""))

if q1ans == 1:
    gryfPts += 1
    rvncPts += 1
elif q1ans == 2:
    huflPts += 1
    slthPts += 1
else:
    print("Please select one of the available inputs")

print(f'{q2}\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold')

q2ans = int(input(""))

if q2ans == 1:
    huflPts += 2
elif q2ans == 2:
    slthPts += 2
elif q2ans == 3:
    rvncPts += 2
elif q2ans == 4:
    gryfPts += 2
else:
    print("Please select one of the available inputs")

print(f'{q3}\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum')

q3ans = int(input(""))

if q3ans == 1:
    huflPts += 4
elif q3ans == 2:
    slthPts += 4
elif q3ans == 3:
    rvncPts += 4
elif q3ans == 4:
    gryfPts += 4
else:
    print("Please select one of the available inputs")

print(f'Slytherin: {slthPts} Hufflepuff: {huflPts}, Ravenclaw: {rvncPts} Gryffindor: {gryfPts}')

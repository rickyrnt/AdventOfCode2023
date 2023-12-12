with open('day1/input.txt', 'r') as file:
    lines = [x.rstrip('\n') for x in file.readlines()]

out = 0
tens = 0
ones = 0

#editor's note: in the future do line[ch:].startswith() and iterate thru an array of comparison strings for ease of coding

for line in lines:
    for ch in range(len(line)):
        if line[ch].isnumeric():
            tens = int(line[ch]) * 10
            break
        elif line[ch:ch + 3] == "one":
            tens = 10
            break
        elif line[ch:ch + 3] == "two":
            tens = 20
            break
        elif line[ch:ch + 5] == "three":
            tens = 30
            break
        elif line[ch:ch+3] == "six":
            tens = 60
            break
        elif line[ch:ch+4] == "four":
            tens = 40
            break
        elif line[ch:ch+4] == "five":
            tens = 50
            break
        elif line[ch:ch+5] == "seven":
            tens = 70
            break
        elif line[ch:ch+5] == "eight":
            tens = 80
            break
        elif line[ch:ch+4] == "nine":
            tens = 90
            break
        
    for ch in reversed(range(len(line))):
        if line[ch].isnumeric():
            ones = int(line[ch])
            break
        elif line[ch:ch + 3] == "one":
            ones = 1
            break
        elif line[ch:ch + 3] == "two":
            ones = 2
            break
        elif line[ch:ch + 5] == "three":
            ones = 3
            break
        elif line[ch:ch+3] == "six":
            ones = 6
            break
        elif line[ch:ch+4] == "four":
            ones = 4
            break
        elif line[ch:ch+4] == "five":
            ones = 5
            break
        elif line[ch:ch+5] == "seven":
            ones = 7
            break
        elif line[ch:ch+5] == "eight":
            ones = 8
            break
        elif line[ch:ch+4] == "nine":
            ones = 9
            break
    out += tens + ones
    
print(out)
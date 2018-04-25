def checkpass(p):
    check = 0;
    lower = [a.islower() for a in p]
    upper = [a.isupper() for a in p]
    digit = [a.isdigit() for a in p]

    for i in lower:
        if (i == True):
            check = check + 1;
            break

    for i in upper:
        if (i == True):
            check = check + 1;
            break

    for i in digit:
        if (i == True):
            check = check + 1;
            break

    if (check == 3):
        return True
    else:
        return False

print (checkpass("8fhwhFNSeri"))
print (checkpass("8fhwheri"))

def strength(p):
    strength = 1;
    lower = [a.islower() for a in p]
    upper = [a.isupper() for a in p]
    digit = [a.isdigit() for a in p]

    for i in lower:
        if (i == True):
            strength = strength * 1.1;

    for i in upper:
        if (i == True):
            strength = strength * 1.2;

    for i in digit:
        if (i == True):
            strength = strength * 1.3;

    if (strength > 10):
        return 10
    else:
        return strength

print strength("hudhfUNSEU4273488")
print strength("trnirnitrngirtin")
print strength("trtin")
print strength("rPP5n")

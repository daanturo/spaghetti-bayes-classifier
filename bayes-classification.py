decision = ""
while decision != "no" and decision != "yes":
    decision = input(
        'Do you want to use the assigned table of cars? (type "yes" or "no") \n'
    )


def readinput(inputfile):
    global attr, m, p, toclassify, col, row, no, listoffeat, featuremap, prioriestimate
    # attr: list of attributes (list of strings)
    # m: equivalent sample size (integer)
    # p: priori estimate (float)
    # toclassify: list of unclassified units and their featuremap (list of nested strings)
    # col: number of column, equal to the number of attr (integer)
    # row: number of known units (integer))
    # no: list of known units (list of nested strings)
    # listoffeat: list of featuremap under each attribute (list of strings)
    # featuremap: a map that show the corresponding attribute of each feature (map)
    # prioriestimate: if Priori Estimate is defined, use it instead of asking everytime (boolean)
    file = open(inputfile)
    no = [line.strip() for line in file]
    attr = no[0].split()  # Define attributes
    end = no.index("-")  # Determine the end of available data
    m = int(no[end + 1].split()[0])  # Get Equivalent sample size
    if len(no[end + 1].split()) == 2:
        p = float(no[end + 1].split()[1])  # Get Priori estimate if available
        prioriestimate = True
        if p > 1:
            p = 1
        elif p < 0:
            p = 0
    else:
        prioriestimate = False
    toclassify = [i.split() for i in no[end + 2 :]]
    col = len(attr)
    no = no[1:end]  # Remove other parts of input data, leaving only sold units' data
    row = len(no)
    for i in range(row):
        no[i] = no[i].split()
    featuremap = {}
    listoffeat = []
    for i in range(col):  # Get list of featuremap of each attribute and feature map
        listoffeat.append([])
        for j in range(row):
            featuremap[no[j][i]] = attr[i]
            if not (
                no[j][i] in listoffeat[i]
            ):  # Ensure that list of features does not contain duplicated items
                listoffeat[i].append(no[j][i])
    file.close()


print()
if decision == "yes":
    readinput("sample.txt")
else:
    readinput("new-input.txt")
# The following lines of code (until the end of "display" function) is only used to display a sorted table of data
maxlen = [len(str(row)) + 4]
for i in range(col):
    temp = [len(attr[i])]
    for j in range(row):
        temp.append(len(str(no[j][i])))
    maxlen.append(max(temp) + 3)


def spaces(strlen, colnum):
    if maxlen[colnum] - strlen > 0:
        return (maxlen[colnum] - strlen) * " "
    else:
        return ""


def display():
    print("No.", spaces(3, 0), end="")
    for i in range(col):
        print(attr[i], spaces(len(attr[i]), i + 1), end="")
    print()
    for i in range(0, row):
        print(i + 1, spaces(len(str(i + 1)), 0), end="")
        for j in range(col):
            print(no[i][j], spaces(len(no[i][j]), j + 1), end="")
        print()


def Probsingle(
    feature,
):  # Calculate a single unconditional Probability of a Feature under a Class
    count = 0
    for i in range(row):
        if no[i][attr.index(featuremap[feature])] == feature:
            count += 1
    return count / row


def Probcondition(
    feature1, feature2, p
):  # Calculate a conditional Probability of Feature that can happen AFTER a Feature of another Attribute is chosen
    count1, count2 = 0, 0
    for i in range(row):
        if no[i][attr.index(featuremap[feature2])] == feature2:
            count2 += 1
            if no[i][attr.index(featuremap[feature1])] == feature1:
                count1 += 1
    return (count1 + m * p) / (
        count2 + m
    )  # Apply Equivalen Sample Size and Priori Estimate


display()
print()
print('These are units which need to be classified, "-" indicates an unknown feature')
for i in toclassify:
    print(i)
print("\n")
if prioriestimate:
    print("Equivalent sample size: %d. Priori Estimate: %f" % (m, p))
else:
    print(
        "Equivalent sample size: %d. Your Priori Estimate must be between 0 and 1 (inclusive), it will become 1 if it is greater than 1 and 0 if smaller than 0."
        % m
    )
print("\n")
for target in toclassify:
    missingfeat = []
    knownfeat = []
    # these lists include integers and self-explanatory about the target which need to be classified
    for i in range(len(target)):
        if target[i] == "-":
            missingfeat.append(i)
        else:
            knownfeat.append(i)
    for i in missingfeat:  # iterate among missing attributes
        old = 0  # A variable used to store the old Probality of the previous Feature to determine the best class
        for j in listoffeat[
            i
        ]:  # Calculate and compare probability of each class under current attribute
            if not prioriestimate:
                pl = []  # list of Priori Estimates
                for k in knownfeat:
                    pl.append(
                        float(
                            input("Your Priori Estimate for P(%s|%s):" % (target[k], j))
                        )
                    )
                    if pl[k] < 0:
                        pl[k] = 0
                    elif pl[k] < 1:
                        pl[k] = 1
            print("Probability that %s is classified under %s:" % (target, j))
            print("(1/P(%s)) * P(%s)" % (target, j), end=" ")
            temp = Probsingle(
                j
            )  # Unconditional Probability of the feature being considered
            for k in knownfeat:  # Calculate the multiplacation of conditional Events
                print("* P(%s|%s)" % (target[k], j), end=" ")
                if not prioriestimate:
                    p = pl[k]
                temp = temp * Probcondition(target[k], j, p)
            print("\n = (1 / P(%s))  *  %f" % (target, temp))
            if (
                temp > old
            ):  # If the result is higher than the previous, the class if determined until better one appears
                old = temp
                resultingclass = j
            elif temp == old:
                resultingclass += " or " + j
            print()
        if old == 0:
            print(
                "Current data is not sufficient, please edit your data to provide more information, modify Equivalent Sample Size and/or Priori Estimate."
            )  # This happen when all Events of the missing features under current Attribute are impossible with current data
        else:
            print(
                "Therefore, the most suitable class for %s under %s is: %s"
                % (target, attr[i], resultingclass)
            )
        print("\n")

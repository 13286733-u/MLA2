import math
import os



# This is the same data as the picture above
# In the real program this would be loaded via csv

'''loaded_data = [ 
    [ 'Outlook', 'Temp', 'Humidity', 'Windy', 'Play' ],
    [ 'Wet', 'Hot', 'High', False, 'NO' ],
    [ 'Wet', 'Hot', 'High', True, 'NO' ],
    [ 'Sunny', 'Hot', 'High', False, 'YES' ],
    [ 'Cloudy', 'Mild', 'High', False, 'YES' ],
    [ 'Cloudy', 'Cool', 'Normal', False, 'YES' ],
    [ 'Cloudy', 'Cool', 'Normal', True, 'NO' ],
    [ 'Sunny', 'Cool', 'Normal', True, 'YES' ],
    [ 'Wet', 'Mild', 'High', False, 'NO' ],
    [ 'Wet', 'Cool', 'Normal', False, 'YES' ],
    [ 'Cloudy', 'Mild', 'Normal', False, 'YES' ],
    [ 'Wet', 'Mild', 'Normal', True, 'YES' ],
    [ 'Sunny', 'Mild', 'High', True, 'YES' ],
    [ 'Sunny', 'Hot', 'Normal', False, 'YES' ],
    [ 'Cloudy', 'Mild', 'High', True, 'NO' ] 
]'''

# THIS IS FOR EVALUATION PURPOSES ONLY COMMENT
# THIS OUT FOR OTHER USES
# USE '''
# IF YOU COMMENT THIS OUT YOU WILL NEED TO CHANGE 
# THE ATTRIBUTES AND TARGET AS WELL
loaded_data = [
[ 'sepal_length','sepal_width','petal_length','petal_width','species' ],
[ 5.1, 3.5, 1.4, 0.2, 'setosa' ],
[ 4.9, 3, 1.4, 0.2, 'setosa' ],
[ 4.7, 3.2, 1.3, 0.2, 'setosa' ],
[ 4.6, 3.1, 1.5, 0.2, 'setosa' ],
[ 5, 3.6, 1.4, 0.2, 'setosa' ],
[ 5.4, 3.9, 1.7, 0.4, 'setosa' ],
[ 4.6, 3.4, 1.4, 0.3, 'setosa' ],
[ 5, 3.4, 1.5, 0.2, 'setosa' ],
[ 4.4, 2.9, 1.4, 0.2, 'setosa' ],
[ 4.9, 3.1, 1.5, 0.1, 'setosa' ],
[ 5.4, 3.7, 1.5, 0.2, 'setosa' ],
[ 4.8, 3.4, 1.6, 0.2, 'setosa' ],
[ 4.8, 3, 1.4, 0.1, 'setosa' ],
[ 4.3, 3, 1.1, 0.1, 'setosa' ],
[ 5.8, 4, 1.2, 0.2, 'setosa' ],
[ 5.7, 4.4, 1.5, 0.4, 'setosa' ],
[ 5.4, 3.9, 1.3, 0.4, 'setosa' ],
[ 5.1, 3.5, 1.4, 0.3, 'setosa' ],
[ 5.7, 3.8, 1.7, 0.3, 'setosa' ],
[ 5.1, 3.8, 1.5, 0.3, 'setosa' ],
[ 5.4, 3.4, 1.7, 0.2, 'setosa' ],
[ 5.1, 3.7, 1.5, 0.4, 'setosa' ],
[ 4.6, 3.6, 1, 0.2, 'setosa' ],
[ 5.1, 3.3, 1.7, 0.5, 'setosa' ],
[ 4.8, 3.4, 1.9, 0.2, 'setosa' ],
[ 5, 3, 1.6, 0.2, 'setosa' ],
[ 5, 3.4, 1.6, 0.4, 'setosa' ],
[ 5.2, 3.5, 1.5, 0.2, 'setosa' ],
[ 5.2, 3.4, 1.4, 0.2, 'setosa' ],
[ 4.7, 3.2, 1.6, 0.2, 'setosa' ],
[ 4.8, 3.1, 1.6, 0.2, 'setosa' ],
[ 5.4, 3.4, 1.5, 0.4, 'setosa' ],
[ 5.2, 4.1, 1.5, 0.1, 'setosa' ],
[ 5.5, 4.2, 1.4, 0.2, 'setosa' ],
[ 4.9, 3.1, 1.5, 0.1, 'setosa' ],
[ 5, 3.2, 1.2, 0.2, 'setosa' ],
[ 5.5, 3.5, 1.3, 0.2, 'setosa' ],
[ 4.9, 3.1, 1.5, 0.1, 'setosa' ],
[ 4.4, 3, 1.3, 0.2, 'setosa' ],
[ 5.1, 3.4, 1.5, 0.2, 'setosa' ],
[ 5, 3.5, 1.3, 0.3, 'setosa' ],
[ 4.5, 2.3, 1.3, 0.3, 'setosa' ],
[ 4.4, 3.2, 1.3, 0.2, 'setosa' ],
[ 5, 3.5, 1.6, 0.6, 'setosa' ],
[ 5.1, 3.8, 1.9, 0.4, 'setosa' ],
[ 4.8, 3, 1.4, 0.3, 'setosa' ],
[ 5.1, 3.8, 1.6, 0.2, 'setosa' ],
# [ 4.6, 3.2, 1.4, 0.2, 'setosa' ],
[ 5.3, 3.7, 1.5, 0.2, 'setosa' ],
# [ 5, 3.3, 1.4, 0.2, 'setosa' ],
[ 7, 3.2, 4.7, 1.4, 'versicolor' ],
[ 6.4, 3.2, 4.5, 1.5, 'versicolor' ],
[ 6.9, 3.1, 4.9, 1.5, 'versicolor' ],
[ 5.5, 2.3, 4, 1.3, 'versicolor' ],
[ 6.5, 2.8, 4.6, 1.5, 'versicolor' ],
[ 5.7, 2.8, 4.5, 1.3, 'versicolor' ],
[ 6.3, 3.3, 4.7, 1.6, 'versicolor' ],
[ 4.9, 2.4, 3.3, 1, 'versicolor' ],
[ 6.6, 2.9, 4.6, 1.3, 'versicolor' ],
[ 5.2, 2.7, 3.9, 1.4, 'versicolor' ],
[ 5, 2, 3.5, 1, 'versicolor' ],
[ 5.9, 3, 4.2, 1.5, 'versicolor' ],
[ 6, 2.2, 4, 1, 'versicolor' ],
[ 6.1, 2.9, 4.7, 1.4, 'versicolor' ],
[ 5.6, 2.9, 3.6, 1.3, 'versicolor' ],
[ 6.7, 3.1, 4.4, 1.4, 'versicolor' ],
[ 5.6, 3, 4.5, 1.5, 'versicolor' ],
[ 5.8, 2.7, 4.1, 1, 'versicolor' ],
[ 6.2, 2.2, 4.5, 1.5, 'versicolor' ],
[ 5.6, 2.5, 3.9, 1.1, 'versicolor' ],
[ 5.9, 3.2, 4.8, 1.8, 'versicolor' ],
[ 6.1, 2.8, 4, 1.3, 'versicolor' ],
[ 6.3, 2.5, 4.9, 1.5, 'versicolor' ],
[ 6.1, 2.8, 4.7, 1.2, 'versicolor' ],
[ 6.4, 2.9, 4.3, 1.3, 'versicolor' ],
[ 6.6, 3, 4.4, 1.4, 'versicolor' ],
[ 6.8, 2.8, 4.8, 1.4, 'versicolor' ],
[ 6.7, 3, 5, 1.7, 'versicolor' ],
[ 6, 2.9, 4.5, 1.5, 'versicolor' ],
[ 5.7, 2.6, 3.5, 1, 'versicolor' ],
[ 5.5, 2.4, 3.8, 1.1, 'versicolor' ],
[ 5.5, 2.4, 3.7, 1, 'versicolor' ],
[ 5.8, 2.7, 3.9, 1.2, 'versicolor' ],
[ 6, 2.7, 5.1, 1.6, 'versicolor' ],
[ 5.4, 3, 4.5, 1.5, 'versicolor' ],
[ 6, 3.4, 4.5, 1.6, 'versicolor' ],
[ 6.7, 3.1, 4.7, 1.5, 'versicolor' ],
[ 6.3, 2.3, 4.4, 1.3, 'versicolor' ],
[ 5.6, 3, 4.1, 1.3, 'versicolor' ],
[ 5.5, 2.5, 4, 1.3, 'versicolor' ],
[ 5.5, 2.6, 4.4, 1.2, 'versicolor' ],
[ 6.1, 3, 4.6, 1.4, 'versicolor' ],
[ 5.8, 2.6, 4, 1.2, 'versicolor' ],
[ 5, 2.3, 3.3, 1, 'versicolor' ],
[ 5.6, 2.7, 4.2, 1.3, 'versicolor' ],
[ 5.7, 3, 4.2, 1.2, 'versicolor' ],
[ 5.7, 2.9, 4.2, 1.3, 'versicolor' ],
# [ 6.2, 2.9, 4.3, 1.3, 'versicolor' ],
[ 5.1, 2.5, 3, 1.1, 'versicolor' ],
# [ 5.7, 2.8, 4.1, 1.3, 'versicolor' ],
[ 6.3, 3.3, 6, 2.5, 'virginica' ],
[ 5.8, 2.7, 5.1, 1.9, 'virginica' ],
[ 7.1, 3, 5.9, 2.1, 'virginica' ],
[ 6.3, 2.9, 5.6, 1.8, 'virginica' ],
[ 6.5, 3, 5.8, 2.2, 'virginica' ],
[ 7.6, 3, 6.6, 2.1, 'virginica' ],
[ 4.9, 2.5, 4.5, 1.7, 'virginica' ],
[ 7.3, 2.9, 6.3, 1.8, 'virginica' ],
[ 6.7, 2.5, 5.8, 1.8, 'virginica' ],
[ 7.2, 3.6, 6.1, 2.5, 'virginica' ],
[ 6.5, 3.2, 5.1, 2, 'virginica' ],
[ 6.4, 2.7, 5.3, 1.9, 'virginica' ],
[ 6.8, 3, 5.5, 2.1, 'virginica' ],
[ 5.7, 2.5, 5, 2, 'virginica' ],
[ 5.8, 2.8, 5.1, 2.4, 'virginica' ],
[ 6.4, 3.2, 5.3, 2.3, 'virginica' ],
[ 6.5, 3, 5.5, 1.8, 'virginica' ],
[ 7.7, 3.8, 6.7, 2.2, 'virginica' ],
[ 7.7, 2.6, 6.9, 2.3, 'virginica' ],
[ 6, 2.2, 5, 1.5, 'virginica' ],
[ 6.9, 3.2, 5.7, 2.3, 'virginica' ],
[ 5.6, 2.8, 4.9, 2, 'virginica' ],
[ 7.7, 2.8, 6.7, 2, 'virginica' ],
[ 6.3, 2.7, 4.9, 1.8, 'virginica' ],
[ 6.7, 3.3, 5.7, 2.1, 'virginica' ],
[ 7.2, 3.2, 6, 1.8, 'virginica' ],
[ 6.2, 2.8, 4.8, 1.8, 'virginica' ],
[ 6.1, 3, 4.9, 1.8, 'virginica' ],
[ 6.4, 2.8, 5.6, 2.1, 'virginica' ],
[ 7.2, 3, 5.8, 1.6, 'virginica' ],
[ 7.4, 2.8, 6.1, 1.9, 'virginica' ],
[ 7.9, 3.8, 6.4, 2, 'virginica' ],
[ 6.4, 2.8, 5.6, 2.2, 'virginica' ],
[ 6.3, 2.8, 5.1, 1.5, 'virginica' ],
[ 6.1, 2.6, 5.6, 1.4, 'virginica' ],
[ 7.7, 3, 6.1, 2.3, 'virginica' ],
[ 6.3, 3.4, 5.6, 2.4, 'virginica' ],
[ 6.4, 3.1, 5.5, 1.8, 'virginica' ],
[ 6, 3, 4.8, 1.8, 'virginica' ],
[ 6.9, 3.1, 5.4, 2.1, 'virginica' ],
[ 6.7, 3.1, 5.6, 2.4, 'virginica' ],
[ 6.9, 3.1, 5.1, 2.3, 'virginica' ],
[ 5.8, 2.7, 5.1, 1.9, 'virginica' ],
[ 6.8, 3.2, 5.9, 2.3, 'virginica' ],
[ 6.7, 3.3, 5.7, 2.5, 'virginica' ],
[ 6.7, 3, 5.2, 2.3, 'virginica' ],
[ 6.3, 2.5, 5, 1.9, 'virginica' ],
# [ 6.5, 3, 5.2, 2, 'virginica' ],
[ 6.2, 3.4, 5.4, 2.3, 'virginica' ],
# [ 5.9, 3, 5.1, 1.8, 'virginica' ]
]
# Notify user of how many rows have been loaded
print("Successfully loaded {0} rows!".format(len(loaded_data)))

# Define the attributes to be used for testing (this provides
# extra freedom to the user instead of editing their dataset
# many times - and also if there are any IDs)

# In this scenario we want to use all our attributes
#attributes = [ 'Outlook', 'Temp', 'Humidity', 'Windy', 'Play' ]
attributes = ['sepal_length','sepal_width','petal_length','petal_width','species']

# We also need to define the class for the script to target
#target = "Play"
target = "species"

print ("There are {0} attributes to train on and we are targeting \"{1}\"".format(len(attributes), target))

# In our example dataset, the first row had no actual data
# instead it was used to title each column.  Lets separate
# them into two different objects for use later

header_row = loaded_data[0]
training_rows = loaded_data[1:]

# I come from a web developer background so using a json 
# object seems more familiar with me 
jsond_rows = []
for i in range(0, len(training_rows)):
    json_data = {}
    row = training_rows[i]
    for j in range(0, len(header_row)):
        json_data[header_row[j]] = row[j]

    jsond_rows.append(json_data)

# Now we need to remove any columns that won't be used by the
# algorithm when training, there's probably a really easy
# way to map this properly but I haven't gone through the 
# documentation thoroughly enough
for i in range(0, len(jsond_rows)):
    json_data = {}
    row = jsond_rows[i]
    for j in range(0, len(attributes)):
        json_data[attributes[j]] = row[attributes[j]]

    jsond_rows[i] = json_data

# Remove the target from the attributes so we don't get mixed up later
if target in attributes:
    attributes.remove(target)   

print ("We've filtered out any unused attributes!")

def getUniqueValues(data, attributeName):
    # Get all the possible values for our attribute
    attributeValues = []
    for row in data:
        val = row[attributeName]
        if val not in attributeValues:
            attributeValues.append(val)

    return attributeValues

# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm) 

# To calculate entropy we basically 
# need to calculate a value's occurence
# within it's own column/class
# the data object is still the whole set
# and the attribute name is the attribute
# for which we are calulcating entropy for

def calculateEntropy(data, attributeName):
    # Used to as a denominator in the fraction
    numberOfRows = len(data)

    # This small patch of code basically counts
    # the occurrences of a certain value within
    # that column
    occurrs = {}
    for row in data: 
        val = row[attributeName]

        if val not in occurrs:
            occurrs[val] = 0
    
        occurrs[val] += 1

    entropy = 0
    for val in occurrs:
        # Calculates proportino
        # Float is needed here otherwise it becomes 0
        p = occurrs[val] / float(numberOfRows)
        entropy += - p * math.log(p, 2)

    return entropy

# Pass the target Entropy, data and attribute name for which
# you want to calculate the information gain for
def calculateIGain(data, target, attributeName):
    # Used to as a denominator in the fraction
    numberOfRows = len(data)

    # We need the target's entropy to calculate info gain
    targetEntropy = calculateEntropy(data, target)

    # Get all the possible values for our attribute
    attributeValues = getUniqueValues(data, attributeName)

    # We want to group each attribute 
    # and then calculate their entropies
    sumOfEntropies = 0
    for attribute in attributeValues:
        # This function is used to group rows together based on the
        # value of an attribute
        def isGroup(row):
            if row[attributeName] == attribute:
                return True
            else:
                return False

        # Groups the rows
        matchedRows = list(filter(isGroup, data))

        entropy = len(matchedRows) / float(numberOfRows) * calculateEntropy(matchedRows, target)
        sumOfEntropies += entropy

    return targetEntropy - sumOfEntropies

# This function gets the attribute with the biggest information gain
def getBiggestInfoGain(infoGain):
    attributeName = None
    biggestGain = None

    for attribute in infoGain.keys():
        if biggestGain is None or biggestGain < infoGain[attribute]:
            biggestGain = infoGain[attribute]
            attributeName = attribute 

    return attributeName

def getInfoGains(data, target, attributes):
    # Let's find out how much information gain each attribute has
    informationGain = {}
    for attr in attributes:
        # Skip the target attr
        if attr == target:
            continue
        iGain = calculateIGain(data, target, attr)
        informationGain[attr] = iGain
    
    return informationGain

def createTree(data, target, attributes):
    # Create the tree object (this could also be a child)
    tree = {}

    # Get all the possible values for our target
    targetValues = getUniqueValues(data, target)

    # If there is only one possible value we can
    # end the tree
    if len(targetValues) == 1:
        tree['result'] = targetValues[0]
        return tree

    # If there are no attributes to train with
    # use the most common one
    if len(attributes) == 0:
        tree['result'] = most_frequent(targetValues)
        return tree

    # Calculate info gains for all the attributes
    infoGains = getInfoGains(data, target, attributes)
    # Get the biggest one 
    biggestInfoGain = getBiggestInfoGain(infoGains)

    # Set the attribute being tested at this stage
    tree['attributeName'] = biggestInfoGain
    tree['children'] = {}

    # Remove the attribute now
    #updatedAttributes = attributes.copy() # using copy doesn't change the attributes variable in the global
    updatedAttributes = attributes[:] # using copy doesn't change the attributes variable in the global
    updatedAttributes.remove(biggestInfoGain)

    # Get all the possible values of the biggest info attribute
    possibleValues = getUniqueValues(data, biggestInfoGain)

    # For every possible value we need to create a branch 
    # with a more filtered data set and the remaining attributes
    for value in possibleValues:
        filteredData = []
        for row in data:
            if row[biggestInfoGain] == value:
                filteredData.append(row)

        tree['children'][value] = createTree(filteredData, target, updatedAttributes)

    return tree

decisionTree = createTree(jsond_rows, target, attributes)

print (decisionTree)

def predict(data):
    tree = decisionTree
    while 'result' not in tree:
        child = data[tree['attributeName']]
        tree = tree['children'][child]

    return tree['result']

# This test data set will only work if you are using the iris dataset
# [ 'sepal_length','sepal_width','petal_length','petal_width','species' ],
test_data = [
    { 'sepal_length': 4.6, 'sepal_width': 3.2, 'petal_length': 1.4, 'petal_width': 0.2 }, # Setosa
    { 'sepal_length': 5, 'sepal_width': 3.3, 'petal_length': 1.4, 'petal_width': 0.2 }, # Setosa
    { 'sepal_length': 6.2, 'sepal_width': 2.9, 'petal_length': 4.3, 'petal_width': 1.3 }, # versicolor
    { 'sepal_length': 5.7, 'sepal_width': 2.8, 'petal_length': 4.1, 'petal_width': 1.3 }, # versicolor
    { 'sepal_length': 6.5, 'sepal_width': 3, 'petal_length': 5.2, 'petal_width': 2 }, # virginica
    { 'sepal_length': 5.9, 'sepal_width': 3, 'petal_length': 5.1, 'petal_width': 1.8 } # virginica
]

for row in test_data:
    prediction = predict(row)
    print (row, prediction)

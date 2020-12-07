import re


def listOfAllContainerBags(bagContainers, bagToBeContained):
    if bagToBeContained in bagContainers:
        containers = set(bagContainers[bagToBeContained])
        for bagContainer in bagContainers[bagToBeContained]:
            containers = set().union(containers, listOfAllContainerBags(bagContainers, bagContainer))
        return containers
    return set()


def countOfAllContainerBags(bagRules, bagToBeContained):
    bagContainers = {}
    for bagRule in bagRules:
        bags = list(filter(None, [x.strip() for x in re.split(r'bags contain|bags|bag contains|bag|0|1|2|3|4|5|6|7|8|9|,', bagRule)]))
        containerBag = bags[0]
        for bagContained in bags[1:]:
            if bagContained == "no other":
                break
            elif bagContained in bagContainers:
                bagContainers[bagContained].add(containerBag)
            else:
                bagContainers[bagContained] = set([containerBag])
    return len(listOfAllContainerBags(bagContainers, bagToBeContained))


def numberofBagCanBeContined(containedBags, containerBag):
    count = 1
    for containedBagWithCount in containedBags[containerBag]:
        bagCount = int(containedBagWithCount[:1])
        count = count+bagCount*numberofBagCanBeContined(containedBags, containedBagWithCount[2:])
    return count


def countTotalNumberOfBagCanBeContained(bagRules, shinyGoldBag):
    containedBags = {}
    for bagRule in bagRules:
        bags = list(filter(None, [x.strip() for x in re.split(r'bags contain|bags|bag contains|bag|,', bagRule)]))
        containerBag = bags[0]
        containedBags[containerBag] = set([])
        for innerBagWithCount in bags[1:]:
            if innerBagWithCount == "no other":
                break
            else:
                containedBags[containerBag].add(innerBagWithCount)
    return numberofBagCanBeContined(containedBags, shinyGoldBag)-1

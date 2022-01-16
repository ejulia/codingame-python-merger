import sys
import math


# Tree
class Tree:
    def __init__(self, cellIndex, size, isMine, isDormant):
        self.cellIndex = cellIndex
        self.size = size
        self.isMine = isMine
        self.isDormant = isDormant

    def getCell(self):
        return cells[self.cellIndex]

    def debug(self):
        debug("Tree: cellIndex=" + str(self.cellIndex) + " size=" + str(self.size) +
              " isMine=" + str(self.isMine) + " isDormant=" + str(self.isDormant))


# Cell
class Cell:
    def __init__(self, index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5):
        self.index = index
        self.richness = richness
        self.intNeighbours = [neigh_0, neigh_1,
                              neigh_2, neigh_3, neigh_4, neigh_5]
        self.neighbours = []

    def getTree(self):
        return allTrees.findByCell(self)

    def isAvailable(self):
        return self.richness > 0 and self.getTree() == None

    def getLevel2Neighbours(self, neighbourRichness=None):
        level2Neighbours = set()
        level2Neighbours.clear()
        for c_1 in self.neighbours:
            for c_2 in c_1.neighbours:
                if c_2 not in self.neighbours and c_2.index != self.index:
                    if neighbourRichness == None or c_2.richness == neighbourRichness:
                        level2Neighbours.add(c_2)
        return level2Neighbours

    def debug(self):
        debug("Cell: cellIndex=" + str(self.index))


# TreeList
class TreeList:
    def __init__(self, treeList=None):
        if treeList == None:
            self.trees = []
        else:
            self.trees = treeList

    def append(self, tree):
        self.trees.append(tree)

    def clear(self):
        self.trees.clear()

    def getStarterTree(self):
        return sorted(self.trees, key=lambda t: len(t.getCell().getLevel2Neighbours(3)), reverse=True)[0]

    def findByCell(self, cell):
        for t in self.trees:
            if t.cellIndex == cell.index:
                return t
        return None

    def getCountBySize(self, size):
        count = 0
        for t in self.trees:
            if t.size == size:
                count += 1
        return count


def getDayData():
    # Game general data
    day = int(input())  # the game lasts 24 days: 0-23
    # the base score you gain from the next COMPLETE action
    nutrients = int(input())
    # sun: your sun points, score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    # whether your opponent is asleep until the next day
    opp_is_waiting = inputs[2] != "0"
    return day, nutrients, sun, score, opp_sun, opp_score, opp_is_waiting


def getDayTrees():
    number_of_trees = int(input())  # the current amount of trees
    allTrees = TreeList()
    myTrees = TreeList()

    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        tree = Tree(cell_index, size, is_mine, is_dormant)
        allTrees.append(tree)
        if is_mine == 1:
            myTrees.append(tree)

    return allTrees, myTrees


def buildBoard():
    cells = []
    # Build the board @cells
    number_of_cells = int(input())  # 37
    cells = [None] * number_of_cells
    for i in range(number_of_cells):
        index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [
            int(j) for j in input().split()]
        cells[index] = Cell(index, richness, neigh_0, neigh_1,
                            neigh_2, neigh_3, neigh_4, neigh_5)

    # Once all cells are listed, populate the cell neighbours with the proper addresses
    for c in cells:
        for i in c.intNeighbours:
            if i != -1:
                c.neighbours.append(cells[i])

    return cells


def getDayActions():
    # Updating the list @actions
    stringActions = []
    number_of_possible_actions = int(input())  # all legal actions
    for i in range(number_of_possible_actions):
        stringActions.append(input())

    # Extract SEED actions
    stringSeedActions = [a for a in stringActions if a.__contains__("SEED")]
    seedActions = []
    for s in stringSeedActions:
        seedActions.append(SeedAction(s.split(' ')[1], s.split(' ')[2]))

    # Extract GROW actions
    stringGrowActions = [a for a in stringActions if a.__contains__("GROW")]
    growActions = []
    for s in stringGrowActions:
        growActions.append(GrowAction(s.split(' ')[1]))

    # Extract COMPLETE actions
    stringCompleteActions = [
        a for a in stringActions if a.__contains__("COMPLETE")]
    completeActions = []
    for s in stringCompleteActions:
        completeActions.append(CompleteAction(s.split(' ')[1]))

    return seedActions, growActions, completeActions


# Grow Action
class GrowAction:
    def __init__(self, cellIndex):
        self.cell = cells[int(cellIndex)]
        self.targetSize = cells[int(cellIndex)].getTree().size + 1

    def execute(self):
        print("GROW " + str(self.cell.index))

    def debug(self):
        debug("Action: GROW " + str(self.cell.index))


# Complete Action
class CompleteAction:
    def __init__(self, cellIndex):
        self.cell = cells[int(cellIndex)]

    def execute(self):
        print("COMPLETE " + str(self.cell.index))

    def debug(self):
        debug("Action: COMPLETE " + str(self.cell.index))


# Seed Action
class SeedAction:
    def __init__(self, sourceCellIndex, targetCellIndex):
        self.sourceCell = cells[int(sourceCellIndex)]
        self.targetCell = cells[int(targetCellIndex)]

    def execute(self):
        print("SEED " + str(self.sourceCell.index) +
              " " + str(self.targetCell.index))

    def debug(self):
        debug("Action: SEED " + str(self.sourceCell.index) +
              " " + str(self.targetCell.index))


def debug(message):
    print(str(message), file=sys.stderr, flush=True)


# Cells
cells = buildBoard()

# Tree lists
allTrees = TreeList()
myTrees = TreeList()

# Action lists
sortedActions = []

# Game markers
firstIteration = True
richCellRace = True

# game loop
while True:
    day, nutrients, sun, score, opp_sun, opp_score, opp_is_waiting = getDayData()

    allTrees, myTrees = getDayTrees()
    if firstIteration:
        starterTree = myTrees.getStarterTree()
        firstIteration = False

    seedActions, growActions, completeActions = getDayActions()

    # Test if the richCellRace is still on
    richestCells = cells[0:7]
    if richCellRace:
        richCellRace = False
        for c in richestCells:
            if c.isAvailable():
                richCellRace = True

    sortedActions.clear()

    if richCellRace:
        debug("Strategy: Rich-Cell Race")
        if starterTree.size == 1:
            sortedActions += filter(lambda a: a.cell ==
                                    starterTree.getCell(), growActions)
        sortedActions += filter(lambda a: a.targetCell.richness ==
                                3, seedActions)
        sortedActions += sorted(growActions,
                                key=lambda a: a.cell.richness, reverse=True)
        sortedActions += filter(lambda a: a.targetCell.richness ==
                                2, seedActions)

    elif day < 16:
        debug("Strategy: Seed on 3 - Grow")
        sortedActions += filter(lambda a: a.targetCell.richness ==
                                3, seedActions)
        # sortedActions += sorted(completeActions, key = lambda a: a.cell.richness, reverse=True)
        sortedActions += sorted(growActions,
                                key=lambda a: a.cell.richness, reverse=True)
        sortedActions += filter(lambda a: a.targetCell.richness ==
                                1, seedActions)

    else:
        debug("Strategy: Complete - Grow - Wait if grow available")
        sortedActions += sorted(completeActions,
                                key=lambda a: a.cell.richness, reverse=True)
        # If I have level-2 trees...
        if myTrees.getCountBySize(2) > 0:
            grow2Actions = sorted(filter(
                lambda a: a.targetSize == 3, growActions), key=lambda g: g.cell.richness, reverse=True)
            # ...I Grow them if I can...
            if len(grow2Actions) > 0:
                sortedActions += grow2Actions
            # ...otherwize I Wait until I have enough Sol points
            else:
                print("WAIT")
                continue
        # Else if I have level-1 trees...
        elif myTrees.getCountBySize(1) > 0:
            grow1Actions = sorted(filter(
                lambda a: a.targetSize == 2, growActions), key=lambda g: g.cell.richness, reverse=True)
            # ...I Grow them if I can...
            if len(grow1Actions) > 0:
                sortedActions += grow1Actions
            # ...otherwize I wait until I have enough Sol points
            else:
                print("WAIT")
                continue

    if len(sortedActions) > 0:
        sortedActions[0].execute()
    else:
        print("WAIT")

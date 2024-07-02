# search.py

# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """ Search the deepest search node in the tree first """
    "*** YOUR CODE HERE ***"
    print("Running Depth")
    # stack object to access stack class methods
    stack = util.Stack()
    # get state of starting node
    start_node = problem.getStartState()
    # set for keeping track of nodes that have been visited (set uses hash tables which increases performance)
    visited = set()
    # push the start node and empty list (for actions) to the stack
    stack.push((start_node, []))
    # while there's items in the stack
    while not stack.isEmpty():
        # pop the last node from stack and update actions,
        current_node, actions = stack.pop()
        #  If the current node is the goal state then return the list of actions to navigate maze
        if problem.isGoalState(current_node):
            return actions
        # Check to see if popped node has not been visited
        if current_node not in visited:
            # add the current node to the visited set
            visited.add(current_node)
            # iterate through the successor nodes to get the adjacent nodes, actions to get to each node and cost
            for adjacent_node, action, cost in problem.getSuccessors(current_node):
                # to ensure a previous visited adjacent node and a node that's already in the stack
                # doesn't get added to stack again
                if adjacent_node not in visited and adjacent_node not in stack.list:
                    # push the next node and concatenated list of actions with the next action to stack
                    stack.push((adjacent_node, actions + [action]))




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    print("Running Breadth")
    # queue object
    queue = util.Queue()
    # get starting node
    start_node = problem.getStartState()
    # set for keeping track of nodes that have been visited
    visited = set()
    # push the start node and empty list to the queue
    # queue inserts at 0 index
    queue.push((start_node, []))
    # while there's items in the queue
    while not queue.isEmpty():
        # pops the earliest pushed item from the queue and update actions
        current_node, actions = queue.pop()
        # if the current node is the goal state then return the actions to get there
        if problem.isGoalState(current_node):
            return actions
        # check to see if popped node has not been visited
        if current_node not in visited:
            # add the current node to the visited set
            visited.add(current_node)
            # iterate through successor nodes to get the adjacent nodes, action to get to each node and cost
            for adjacent_node, action, cost in problem.getSuccessors(current_node):
                # to ensure a previous visited adjacent node and a node that's already in the queue
                # doesn't get added to queue again
                if adjacent_node not in visited and adjacent_node not in queue.list:
                    # push the adjacent node and concatenated list of current actions with action required to get to the
                    # adjacent node to the queue
                    queue.push((adjacent_node, actions + [action]))


def uniformCostSearch(problem):
    print("running Uniform")
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # stack object to access stack methods
    priority_queue = util.PriorityQueue()
    # get starting node
    start_node = problem.getStartState()
    # set for keeping track of nodes that have been visited (set uses hash tables which increases performance)
    visited = set()
    # push the start node and empty list (for actions) and initial cost to priority queue
    priority_queue.push((start_node, []), 0)
    # while there's items in the priority queue
    while not priority_queue.isEmpty():
        # pops the node with least cost from priority queue and update actions
        current_node, actions = priority_queue.pop()
        # If the current node is the goal state then return the actions list
        if problem.isGoalState(current_node):
            return actions
        # check to see if node has not been visited
        if current_node not in visited:
            # add the current node to the visited set
            visited.add(current_node)
            # iterate through successor nodes to get the adjacent nodes, action to get to each node and cost
            for adjacent_node, action, cost in problem.getSuccessors(current_node):
                # to ensure a previous visited adjacent node and a node that's already in the priority queue
                # doesn't get added to priority queue again
                if adjacent_node not in visited and adjacent_node not in priority_queue.heap:
                    # actions list concatenated with the current actions and the action required to get to the
                    # adjacent node
                    next_actions = actions + [action]
                    # get the cost of the sequence of actions that are contained in the next_actions list
                    actions_cost = problem.getCostOfActions(next_actions)
                    # push the adjacent node, the concatenated list of current actions with action required to get
                    # to adjacent node and action cost to priority queue
                    priority_queue.push((adjacent_node, next_actions), actions_cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
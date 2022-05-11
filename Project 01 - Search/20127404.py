from lib2to3.pytree import Node
from typing import Deque
import numpy as np
import math
from queue import PriorityQueue
from collections import deque


def DFS(matrix, start, end):
    """
    DFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    
    # TODO:
    visited = {} # Include vertexs and their parents
    path = []
    matrix = np.array(matrix)

    frontier = deque()
    frontier.append(start) # Lưu dưới cấu trúc Stack
    visited[start] = None
    while frontier:
        node = frontier.pop() #Ví dụ đỉnh đang xét là đỉnh A
        if node == end:
            break
        for i in range(len(matrix[node])): # Những giá trị i là những đỉnh còn lại trong đồ thị, matrix[A][i] là những path-cost từ đỉnh A đến đỉnh i
            if matrix[node][i]!= 0 and i not in visited: #Nếu đỉnh kế tiếp của A chưa được visited // matrix[node][i] là path-cost từ đỉnh node tới đỉnh kế tiếp
                frontier.append(i) #Gắn đỉnh đó vào vào stack
                visited[i] = node #Lưu node cha (node) cùng với node (i) đã visit vào trong dictionary

    if end in visited: # Nếu goal đã được visit thì tiến hành vẽ path
        while end != start:
            path.append(end)    
            end = visited[end] #chuyển đỉnh Goal sang đỉnh Parent của nó
        path.append(start)
        path.reverse()
    return visited, path

def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    path=[]
    visited={}
    matrix = np.array(matrix)

    frontier = deque() #Kiểu cấu trúc Queue
    frontier.append(start)
    visited[start] = None
    while frontier:
        node = frontier.popleft()
        if node == end:
            break
        for i in range(len(matrix[node])):
            if matrix[node][i]!= 0 and i not in visited:
                frontier.append(i)
                visited[i] = node
    if end in visited:
        while end != start:
            path.append(end)    
            end = visited[end]
        path.append(start)
        path.reverse()
    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO:  
    path = []
    visited = {}
    visitedTemp = {} # Mảng này có tác dụng lưu trữ tạm thời các giá trị đang lấy trong frontier ra
    matrix  = np.array(matrix)
    #Mục tiêu kiếm đường đi với chi phí nhỏ nhất
    frontier = [] # Ta sẽ cài đặt list này như là một priority queue
    currentNodePathCost = 0
    frontier.append((start,0)) #Do yêu cầu của bài toán là lấy đường đi nhỏ nhất trong các đường đi nên chúng ta sẽ lấy path-cost là độ ưu tiên
    visited[start] = None
    visitedTemp[start] = start
    while frontier:
        # Xử lý để lấy được 2 giá trị path-cost và node
        tupleGet = frontier.pop() #Lấy đồng thời 2 giá trị node và path-cost
        (currentNode, currentNodePathCost) = tupleGet
        if currentNode == end:
            break
        for i in range(len(matrix[currentNode])):
            weight =  matrix[currentNode][i] + currentNodePathCost
            neighborNodePathCost = matrix[currentNode][i]
            if neighborNodePathCost != 0:
                if i in visited or i in frontier:# Nếu i đã được duyệt thì tiến hành kiểm tra và cập nhật đỉnh có giá trị nhỏ hơn
                    # Nếu path-cost nhỏ hơn path cost trước thì tiến hành cập nhật
                    if i in frontier and frontier[i][1] > weight:
                        visitedTemp[i] = currentNode
                    if i in visited:
                        visited[i] = currentNode
                        frontier[i][1] = weight
                else: #Còn không thì gắn vào mảnh tạm và tiếp tục duyệt
                    visitedTemp[i] = currentNode
                    frontier[i][1] = weight

    if end in visited:
        while end != start:
            path.append(end)
            end = visited[end]
        path.append(start)
        path.reverse()
    return visited, path

    

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    print(pos)
    return visited, path


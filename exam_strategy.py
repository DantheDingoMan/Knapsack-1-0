#!/usr/bin/env python3
# Solution by Aidan Schooling

from collections import namedtuple

Item = namedtuple("Item", ["value", "weight"])


def knapsack(capacity: int, items: list[Item]) -> list[int]:
    """
    General Knapsack solution.

    :param capacity: total knapsack capacity
    :param items: the list of items (named tuples) to consider
    :return: a list of chosen indices
    """
    indices = []
    nb = capacity
    try:
        nb = int(nb)
    except ValueError:
        nb = int(float(nb))
    nbofitems = len(items)
    matrix = [[0 for i in range(nb + 1)] for x in range(nbofitems + 1)]
    weights = []
    points = []
    for i in range(nbofitems):
        weights.append(int(items[i][1]))
        points.append(int(items[i][0]))
        

  
    for i in range(nbofitems + 1):
        
        
        for x in range(nb + 1):
            
            if i == 0 or x == 0:
                matrix[i][x] = 0
            elif weights[i-1] <= x:
                
                matrix[i][x] = max(points[i-1] + matrix[i-1][x-weights[i-1]], matrix[i-1][x])
            else:
                matrix[i][x] = matrix[i-1][x]

    maxval = matrix[nbofitems][nb]
    
    mv = maxval
    z = nb
    for i in range(nbofitems, 0, -1):

        if maxval <= 0:
            break
        if maxval == matrix[i-1][z]:
            continue
        else:
           
            indices.append(i-1)
 
            maxval = maxval - points[i - 1]
  
            z = z - weights[i - 1]
    indices.reverse()
    return (indices, mv)

    


def pick_questions_to_answer(filename: str) -> tuple[list[int], int]:
    """
    Main selection function

    :param filename: file to process
    :return: the list of chosen indices and total point value of all selected questions
    """
    
    total_points = 0
    items = []
    capacity = 0
    with open(filename, 'r') as file:
        for line in file:
            print(line)
            data = line.split()
            if capacity == 0:
                capacity = data[0]
                nbofqs = data[1]
            else:
                
                items.append(Item(data[0], data[1]))
    print(items)

    knapsackval = knapsack(capacity, items)
    print("Max value")
    print(knapsackval)
    
    for i in range(len(knapsackval)):
        total_points += int(items[i][1][0])


    return (knapsackval)
    



def main():
    """Entry point"""
    for i in range(1, 6):
        filename = f"data/projects/exam_strategy/questions{i}.in"
        selection = pick_questions_to_answer(filename)
        print(
            f"Case {i}: Items {sorted(selection[0])} sum up to {selection[1]}"
        )


if __name__ == "__main__":
    main()


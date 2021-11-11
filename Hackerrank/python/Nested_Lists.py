if __name__ == '__main__':
  # create list for nested list, and set to store second lowest score
    students = []
    scores = set()
    # loop input and store nested list, and set
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)
        
    # create a new variable that saves second lowest number
    second_lowest = sorted(scores)[1]
    
    # create list for final answer
    second_lowest_name = []
    
    # re-loop stored list and if each list's score is same as second lowest score, than append 
    for name, score in students:
        if score == second_lowest:
            second_lowest_name.append(name)
            
    # sort final answer list and print its values
    for name in sorted(second_lowest_name):
        print(name, end='\n')

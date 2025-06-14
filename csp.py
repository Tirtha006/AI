def is_consistent(variable,value,assignment,constraints):
    for neighbour in constraints[variable]:
        if neighbour in assignment and assignment[neighbour]==value:
            return False
        return True
    
def backtracking_search(variables,domains,constraints,assignment={}):
    if len(variables)==len(assignment):
        return assignment
    
    unassigned_vars=[v for v in variables if v not in assignment]
    first_var=unassigned_vars[0]

    for value in domains[first_var]:
        if is_consistent(first_var,value,assignment,constraints):
            assignment[first_var]=value

            result=backtracking_search(variables,domains,constraints,assignment)
            if result is not None:
                return result
            del_assignment[first_var]

    return None
variables=['A','B','C']
domains={
    'A':['Red','Blue','Green'],
    'B':['Red','Blue','Green'],
    'C':['Red','Blue','Green'],

}
constraints={
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B'],
}
solution=backtracking_search(variables,domains,constraints)
print(solution)

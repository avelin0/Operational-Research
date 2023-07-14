# SUDOKU - AMPL 
- Sudoku Implementation in AMPL

## Formulation
### Decision Variable
$$ x_{ijk} = 1\ if\ number\ k\ is\ in\ row\ i,\ column\ j;\ 0,\ on\ the\ contrary; $$ 

### RULE 1 - cell constraint 
$$ \sum_{k=1}^{9}x_{ijk} = 1\  for\ i\ = 1..9, j = 1..9 $$

### RULE 2 - row constraint
$$ \sum_{j=1}^{9}x_{ijk} = 1\  for\ i\ = 1..9, k = 1..9 $$

### RULE 3 - column constraint
$$ \sum_{i=1}^{9}x_{ijk} = 1\  for\ j\ = 1..9, k = 1..9 $$

### RULE 4 - submatrix constraint
$$ \sum_{3_{i0} - 2 }^{3_{i0}} \sum_{3_{j0} - 2}^{3_{j0}} x_{ijk} = 1\  for\ i_0 = 1..3, j_0 = 1..3 $$

## AMPL CODE (.mod)
![image](https://github.com/avelin0/Operational-Research/assets/12461215/6d701adf-56fa-4d48-adb3-03fb182c1280)
![image](https://github.com/avelin0/Operational-Research/assets/12461215/fc7da47a-3cdc-407f-b18d-bbba06311c4b)

[sudoku.mod](sudoku.mod)

## RESULT
![image](https://github.com/avelin0/Operational-Research/assets/12461215/b98e6adb-f3be-4ae3-8dd3-ce30580d43ab)

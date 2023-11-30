
# Digital Logic Circuit Optimization through Boolean Minimization using kmaps and Quine McCklusky

This project optimises digital logic circuits using Boolean minimisation techniques- K-map and Quine McCluskey. Max-terms or min-terms (values range 0-15) are given as input to generate an optimised 4-variable (a,b,c,d) boolean expression .



## Acknowledgements

 - https://github.com/vijaybharath99/Karnaugh-Map 



## Authors

- [@Tanvisusarla](https://github.com/Tanvisusarla)
- [@AnuragBoghra](https://github.com/AnuragBoghra)


## Requirement

Python (3.11)


    
## Install dependencies

```bash
  pip install tabulate
  pip install numpy
  pip install itertools
  pip install re
```




## Usage/Examples (Karnaugh Map)
The program takes min/maxterms as input and generates a minimised 4-variable(a,b,c,d) expression 

Run K_Map.py

Enter a number(for each minterm) seperated by a single space
the input prompt will be as follows

Enter terms within 0 to 15 : 0 2 4 6 8 9 14

Specify whether the given terms are minterms or maxterms according to the prompt

Enter 'min' for minterms and 'max' for maxterm :max 

The Output will be -

The Karnaugh-map is :

00    01    11    10
----  ----  ----  ----
   1     0     0     1
   1     0     0     1
   0     0     0     1
   1     1     0     0

Minimized boolean POS expression is: [A'+D']* [A+B'+C'] * [B+C+D']


## Usage/Examples (Quine McCluskey)

Run ImplicationTable.py

enter the number of minterms or maxterms you want to input. Example- 5

Enter number of minterms : 5

Enter the terms 0-15: 2 4 6 7 8

Enter number of dont cares : 3       

Enter the dont care terms 0-15: 10 11 14

Note- the value for each input prompt must range from 0 to 15.




## Screenshots

[ImplicationTable output Screenshot-implication.png](https://github.com/Tanvisusarla/DSD-Project/blob/main/Screenshot-implication.png)


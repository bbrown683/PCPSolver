'''
MIT License

Copyright (c) 2018 Ben Brown

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from solver import solve

def easy_test():
    alpha = 'a', 'ab', 'bba'
    beta = 'baa', 'aa', 'bb'

    solutions = solve(alpha, beta, 4)
    for solution in solutions:
        print(solution)

def moderate_test():
    alpha = '110','0011','0110'
    beta = '110110','00','110'

    solutions = solve(alpha, beta, 8)
    for solution in solutions:
        print(solution)

def difficult_test():
    alpha = 'abab','aaabbb','aab','ba','ab','aa'
    beta = 'ababaaa','bb','baab','baa','ba','a'

    solutions = solve(alpha, beta, 12)
    for solution in solutions:
        print(solution)

easy_test()
moderate_test()
difficult_test()
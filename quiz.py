#quiz code:

score=0
print("""(1)In python,what do you call a box to store data?
          a-text
          b-variable
          c-datatype """)
answer=input().lower()
if answer=='b':
   print("correct")
   score=score+1
else:
    print("wrong")
print("""(2)What are the arithmetic operators?
         a- *
         b- ^
         c- ?""")
answer=input().lower()
if answer=='a':
    print("correct")
    score=score+1
else:
    print("wrong")
print("""(3)What are the unordered collection of items called in python?
          a-key
          b-file
          c-dictionary""")
answer=input().lower()
if answer=='c':
    print("correct")
    score=score+1
else:
    print("wrong")
print("""(4) What is the output of the following code:
             import sys
             write=sys.stdout.write
             write('20')
             write('05\n')

             a-25
             b-2005
             c-205 """)
answer=input().lower()
if answer=='b':
 print("correct")
 score=score+1
else:
    print("wrong")
print("""(5) Interpret what kind of operation does it do: 'a+b'
             a-repetition
             b-concatenation
             c-slice""")
answer=input().lower()
if answer=='b':
    print("correct")
    score=score+1
else:
    print("wrong")
print("""(6) Which built-in string method merges the string representations of elements in sequence into a string,with seperator string?
          a-rstrip()
          b-join(seq)
          c-none """)
answer=input().lower()
if answer=='b':
    print("correct")
    score=score+1
else:
    print("wrong")
print("""(7)'2+4.5->2.0+4.5=6.5' the above conversion is:
         a-coercion
         b-conversion
         c-type conversion """)
answer=input().lower()
if answer=='a':
    print("correct")
    score=score+1
else:
    print("wrong")
print("""(8)Which function is defined without a name?
            a-recursive function
            b-lambda function
            c-string function""")
answer=input().lower()
if answer=='b':
    print("correct")
    score=score+1
else:
    print("wrong")
print("""(9)Which method is used to remove and return last object from the list?
         a-li.pop()
         b-li.remove()
         c-li.append() """)
answer=input().lower()
if answer=='a':
    print("correct")
    score=score+1
else:
    print("wrong")
print("""(10)Which statement in python is used when a statement is required syntactically but you do not want any command or code to execute?
          a- break
          b-continue
          c-pass """)
answer=input().lower()
if answer=='c':
    print("correct")
    score=score+1
else:
    print("wrong")
print("score: ",score)
print("Thank you for playing! :)")

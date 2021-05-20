# simple-py-parser
* Tool Used : PLY (Python Lex and Yacc)

* Language : ({EXPR, TERM, FACTOR}, {a, b, c, +, *, (, )}, R, EXPR)  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; EXPR> -> EXPR + TERM | TERM  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; TERM> -> TERM * FACTOR | FACTOR  
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; FACTOR -> (EXPR)|a|b|c  

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; For example, ((a + b) * a + c) * a + b * c should be evaluated to 12 when a=1, b=2, c=3.


## Install required package
```
pip3 install -r requirements.txt
```
## Strucure of fils
* plex.py (tokenize input string)
* pyacc.py (parse language syntax)
* parsetab.py (auto-generated, yacc reloads the table from parsetab.py when change is detected in the underlying grammar)
* parser.out (auto-generated, debugging file for yacc)
## Usage
```
python3 pyacc.py
```  
This will start the parser. You can input desired language and given values. The output should be a number. 

![Screenshot from 2021-05-20 23-44-18](https://user-images.githubusercontent.com/29471273/119009912-2af08100-b9c6-11eb-8d80-705068540ddb.png)

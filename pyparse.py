#file that will take a "song" list of tokens, and parse it

#Dflat Grammar!
# start -> stmtList rest
# stmtList -> stmt rest stmtList
# stmt -> varName assign expression
# stmt -> write varName
# stmt -> read varName
# stmt -> expression addOp expression
# expression -> multExp multOp multExp
# 


def parse(song):
    

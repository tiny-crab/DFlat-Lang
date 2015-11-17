According to Sebesta, a CFG representing a language must have a few traits:
  -Terminal Symbols
  -Nonterminal Symbols
  -Production Rules
  -Start Symbol!

Evan, if you want to change any of this, just do it! Really, the CFG won't matter too much right off the bat.
Just wanted to get started on the plex files :)

dflat -> lines
lines -> line | line . lines
line ->  var op numconst
var -> ??
op -> + | - | * | /

Basics for a Hello World Program:

something along the lines of:
  consoleout(Hello World!)

  This is my idea:
    consoleout = EeEeEBDC (fur elise)
    next measure is the start of input (don't know how we're going to differentiate strings/ints/etc, but whatever)
    How to do a string:
      A = 1
      B = 2
      C = 4
      D = 10
      E = 20
      F = 40
      G = 100
      Then just use octal ascii codes to input chars:
        Hello World! -> |110 145 154 154 157| 040 | 127 157 162 154 144 | 041 |
        -> | GD GFCA GFDC GFDC GFDCBA | F | GECBA GFDCBA GFEB GFDC GFC | FA

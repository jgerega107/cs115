# Demo of hmmm, the Harvey Mudd miniature machine
# D.N. Oct 2018

# When this file is loaded, it runs the program assigned
# to variable RunThis. Debug mode is controlled by 
# variable Mode. Read all the comments before trying it out.

import sys
import importlib
# Also requires hmmmAssembler.py and hmmmSimulator.py to
# be available in the same directory as this file.

"""
Jacob Gerega
10/31/19
I pledge my honor that I have abided by the Stevens Honor System.
"""


fibonacci = """
00 read r1 # read user input
01 setn r2 0 # set r2 register to zero
02 setn r3 1 # set r3 register to one
03 jeqzn r1 10 # begin conditional loop
04 write r2 # print register r2
05 add r4 r3 r2 # add registers together and store in r4 register
06 copy r2 r3 # copy register r3 to register r2
07 copy r3 r4 # copy register r4 to register r3
08 addn r1 -1 # subtract one from register r1 to decrement the loop counter
09 jumpn 3 # end of loop, go back to line three
10 halt # end of program
"""



# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = fibonacci

# Choose whether to use debug mode; uncomment one of the following lines.
#Mode = ['-n'] # not debug mode
Mode = ['-n'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b



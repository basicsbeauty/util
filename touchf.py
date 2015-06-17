#!/usr/bin/env python

##########################################################
# File  : ~/bin/touchp
# Usage : touchp <file_to_create>
##########################################################

import os
import sys

from os import path

###############################
# Constants: Begin
###############################
FAILURE = 1
SUCCESS = 0

ARG_VALID = 2

FILE_TYPE_CPP = 1
FILE_TYPE_HPP = 2
FILE_TYPE_SQL = 3
FILE_TYPE_PROTOBUF = 4
FILE_TYPE_BASH_SCRIPT = 5
FILE_TYPE_PYTHON_SCRIPT = 6

###############################
# Constants: End
###############################

project_name = None
file_to_create = None

###############################
# Function: processCommandLine()
###############################
def processCommandLine():
  
    if ARG_VALID != len(sys.argv):
        return False, None
  
    return True, sys.argv[1]

###############################
# Function: printHelp()
###############################
def printHelp():
    print __file__, ": Invalid usage"
    print __file__, " <file_to_create>"
    return FAILURE

###############################
# Function: createFile()
###############################
def createFile():

    global project_name
    global file_to_create

    file_type = None
    comment_character = "#"

    # Get file Extension
    file_extension = os.path.splitext(file_to_create)[1].strip()

    # Comment character
    if file_extension:

        if file_extension == '.cpp':
            file_type = FILE_TYPE_CPP
            comment_character = "//"
        elif file_extension == '.cpp':
            file_type = FILE_TYPE_HPP
            comment_character = "//"
        elif file_extension == '.sql':
            file_type = FILE_TYPE_SQL
            comment_character = "#"
        elif file_extension == '.proto':
            file_type = FILE_TYPE_PROTOBUF
            comment_character = "//"
        elif file_extension == '.sh':
            file_type = FILE_TYPE_BASH_SCRIPT
            comment_character = "#"
        elif file_extension == '.py':
            file_type = FILE_TYPE_PYTHON_SCRIPT
            comment_character = "#"
      
    #print "File: Extn: ", file_extension, " Cmnt: ", comment_character
  
    fp = open( file_to_create, 'w')
  
    if not fp:
      return False
  
    addStandardHeader( fp, file_type, comment_character)
    
    fp.write("\n")
    fp.close()
    return True

###############################
# Function: main()
###############################
def addStandardHeader( fp, file_type, comment_character):

    global file_to_create

    if fp is None:
        return False
    elif not isinstance( fp, file):
        return False

    if 1 == len(comment_character):
        comment_character_length = 64
    elif 2 == len(comment_character):
        comment_character_length = 32

    fp.write( comment_character * comment_character_length + "\n")
    fp.write( comment_character + " Filename: " + file_to_create + "\n")
    fp.write( comment_character + " Location: " + os.getcwd() + "\n")
    fp.write( comment_character + " Project : " + "\n")
    fp.write( comment_character + " Date    : " + os.popen( "date +%Y-%m-%d").read().strip() + "\n")
    fp.write( comment_character + " User    : " + os.getlogin().strip() + "\n")
    fp.write( comment_character + " Scope   : " + "\n")
    if file_type == FILE_TYPE_PROTOBUF:
      fp.write( comment_character + "   - Agent : \n")
      fp.write( comment_character + "   - Action: \n")
      fp.write( comment_character + "   - Object: \n")
    fp.write( comment_character * comment_character_length + "\n")


###############################
# Function: touchf()
###############################  
def touchf():

    global file_to_create

    status, file_to_create = processCommandLine() 
    if not status:
        return printHelp()
  
    if not createFile():
        print "File: Creation: Failed: "
        return FAILURE

    return SUCCESS

###############################
# Function: main()
###############################  
def main():    
    sys.exit( touchf())

if __name__ == "__main__":
    main()

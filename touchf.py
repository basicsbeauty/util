#!/usr/bin/env python

##########################################################
# File  : ~/bin/touchp
# Usage : touchp <file_to_create>
##########################################################

import os
import sys
import commands

###############################
# Constants: Begin
###############################
FAILURE = 1
SUCCESS = 0

ARG_VALID = 1 + 1

FILE_TYPE_CPP = 1
FILE_TYPE_HPP = 2
FILE_TYPE_SQL = 3
FILE_TYPE_PROTOBUF = 4
FILE_TYPE_BASH_SCRIPT = 5
FILE_TYPE_PYTHON_SCRIPT = 6
FILE_TYPE_PYTHON_UNKNOWN = 7

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

    # Get file Extension
    file_extension = os.path.splitext(file_to_create)[1].strip()

    comment_character = "#"
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
    else:
        file_type = FILE_TYPE_PYTHON_UNKNOWN
        comment_character = "#"
        

    #print "File: Extn: ", file_extension, " Cmnt: ", comment_character

    fp = open( file_to_create, 'w')

    if not fp:
      return False

    process_shebang( fp, file_type)
    addStandardHeader( fp, file_type, comment_character)
    process_body( fp, file_type)
    process_premissions( file_type)

    fp.write("\n")
    fp.close()
    return True

###############################
# Function: process_body
###############################
def process_body( fp, file_type):

    if fp is None:
        return False
    elif not isinstance( fp, file):
        return False

    if( file_type == FILE_TYPE_PYTHON_SCRIPT):
        process_body_python( fp)

###############################
# Function: process_body_python
###############################
def process_body_python( fp):

    if fp is None:
        return False
    elif not isinstance( fp, file):
        return False

    # File name without extension
    #  test.py -> test
    script_main_function_name = file_to_create.split('/')[-1].split('.')[0]

    import_stub = "\nimport os\nimport sys\n\n"
    fp.write( import_stub)

    # Constants
    fp.write("###############################\n")
    fp.write("# Constants\n")
    fp.write("###############################\n")
    fp.write("BASH_RCODE_FAILURE=1\n")
    fp.write("BASH_RCODE_SUCCESS=0\n")
    fp.write("FUNCTION_RCODE_FAILURE=0\n")
    fp.write("FUNCTION_RCODE_SUCCESS=1\n\n")

    # Function
    function_name_signature = script_main_function_name+"()"
    fp.write("###############################\n")
    fp.write("# Function: " + script_main_function_name + "\n")
    fp.write("###############################\n")
    fp.write("def " + function_name_signature + ":\n")
    fp.write("    pass\n\n")

    fp.write("###############################\n")
    fp.write("# Function: main \n")
    fp.write("###############################\n")
    fp.write("def main():\n")
    fp.write("    return " + function_name_signature + "\n\n")

    fp.write("if __name__ == \"__main__\":\n")
    fp.write("    sys.exit( main())\n\n")

###############################
# Function: process_premission
###############################
def process_premissions( file_type):

    global file_to_create

    if file_type is None:
        return False
    elif not isinstance( file_type, int):
        return False

    if( (file_type == FILE_TYPE_BASH_SCRIPT)
     or (file_type == FILE_TYPE_PYTHON_SCRIPT)):
        cmd = "chmod 744 " + file_to_create
        status, output = commands.getstatusoutput(cmd)
        return (status == 0)

###############################
# Function: process_shebang
###############################
def process_shebang( fp, file_type):

    if fp is None:
        return False
    elif not isinstance( fp, file):
        return False

    SHE_BANG_SUFFIX = "#!/usr/bin/env "
    if( file_type == FILE_TYPE_BASH_SCRIPT):
        fp.write( SHE_BANG_SUFFIX + "bash \n")
    elif ( file_type == FILE_TYPE_PYTHON_SCRIPT):
        fp.write( SHE_BANG_SUFFIX + "python \n")

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
    fp.write( comment_character + " Author  : " + os.getlogin().strip() + "\n")
    fp.write( comment_character + " Scope   : " + "\n")
    fp.write( comment_character + " Usage   : " + "\n")
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

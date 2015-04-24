#!/usr/bin/python

##############################################################
# Name:         adstf.py
# Description:  Add date stamp to file
# Type:         Tool
##############################################################


import os
import sys
import commands

ARG_VALID_COUNT = 2

##############################################################
# Script: Usage: Print
def printHelp():
  script_name = __file__
  print script_name, ": Invalid usage"
  print "Usage: ", script_name, " <target_file>"

##############################################################
# Command-Line: Arguments: Process
def cmdLineProcess():
  flag = False
  input_file_location = None
  
  # Argument count: Test
  if len(sys.argv) != ARG_VALID_COUNT:
    return flag, input_file_location
  
  # Argument count: Test
  if os.path.exists(sys.argv[1]):
    flag = True
    input_file_location = sys.argv[1]  
  
  return flag, input_file_location  

##############################################################
def addDateStamp( _input_file_location):
  
  fp = open( _input_file_location, 'a');
  if not fp:
    print "FATAL: Unable to access file for append: ", _input_file_locaiton
    return False
  
  # Delimiter
  date_delimiter = "###############################\n"
  
  # Date (MM-DD-YYYY, Day)
  cmd = "date +%m-%d-%Y\" \"%a"
  status, date_stamp = commands.getstatusoutput( cmd);
  if( status != 0):
    print "Cmd  : ", cmd
    print "FATAL: Unable to get date: Status: ", status
    return False
  date_stamp.strip()
  date_stamp += "\n"
  
  # Write to file
  fp.write( date_delimiter);  
  fp.write( date_stamp);
  fp.write( date_delimiter);
  
  fp.close()
  return True

##############################################################
def main():
  
  status, input_file_location = cmdLineProcess()
  #print 'Status: ', status, ' File: ', input_file_location
  if status == False:
    printHelp()
    sys.exit(1)
    
  status = addDateStamp(input_file_location)

main()

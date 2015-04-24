#!/usr/bin/env python

################################################################
# Filename: project_create.py
# Location: /home/ubuntu/Work
# Project : 
# Date    : 2013-08-24
# User    : ubuntu
# Scope   : 
#  - 
################################################################

import os
import sys
import commands

FAILURE = 1
SUCCESS = 0

ARG_VALID_COUNT = 2

project_name = None
file_to_create = None

###################################
# Function: processCommandLine()
###################################
def processCommandLine():
  
  if ARG_VALID_COUNT != len(sys.argv):
    return False, None
  
  return True, sys.argv[1]

###################################
# Function: printHelp()
###################################
def printHelp():
  print __file__, ": Invalid usage"
  print __file__, " <project_name_to_create>"
  return FAILURE

###################################
# Function: createProject
###################################
def createProject( _project_name):
  
  # Project Directory: <project_dir>
  # <project_dir>/aao_model
  # <project_dir>/aao_model/<project_name>.proto
  # <project_dir>/data_model
  # <project_dir>/data_model/db_setup.sql
  # <project_dir>/data_model/db_cleanup.sql
  # <project_dir>/data_model/table_setup.sql
  # <project_dir>/data_model/table_cleanup.sql
  # <project_dir>/auto_gen
  # <project_dir>/src
  # <project_dir>/web

  if not _project_name:
    print "FATAL: Incorrect project name: " . _project_name
    return False
  
  _project_name = str(_project_name)

  # Project: Directory: Create
  if not os.path.isdir( _project_name):
    cmd = "mkdir " + _project_name
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
      print "FATAL: Directory creation failed for project: " + _project_name
      return False
  else:
    print "INFO: Project directory already present:"
    
  # Project: aao_model: Directory: Create
  new_dirs = [ 'aao_model', 'data_model', 'auto_gen', 'src', 'web']
  for dir_name in new_dirs:
    new_dir = _project_name + "/" + dir_name
    cmd = "mkdir " + new_dir
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
      print "FATAL: Directory creation failed for project: " + new_dir
      return False
  
  # Files
  # Project: aao_model: proto: file: touch
  protobuf_file =  _project_name + "/aao_model/" + _project_name.lower() + ".proto"
  cmd = "touchf " + protobuf_file
  status, output = commands.getstatusoutput(cmd)
  if status != 0:
    print "FATAL: Protobuf file creation failed for project: " + protobuf_file
    return False

  # Project: aao_model: proto: file: touch
  sql_files =  [ 'db_setup.sql', 'db_cleanup.sql', 'table_setup.sql', 'table_cleanup.sql']
  for new_sql_file in sql_files:
    cmd = "touchf " + _project_name + "/data_model/" + new_sql_file
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
      print "FATAL: Protobuf file creation failed for project: " + new_sql_file
      return False
    
  return True

###################################
# Function: main()
###################################  
def main():

  status, file_to_create = processCommandLine() 
  if not status:
    return printHelp()
  
  if not createProject( file_to_create):
    print "File: Creation: Failed: "
    return FAILURE

  return SUCCESS

main()


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

BASH_FAILURE = 1
BASH_SUCCESS = 0

ARG_VALID_COUNT = 1 + 1

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
  return BASH_FAILURE

###################################
# Function: createProject
###################################
def createProject( _project_name):
  
  # Project Directory: <project_dir>
  # <project_dir>/src
  # <project_dir>/web
  # <project_dir>/auto_gen
  # <project_dir>/aao_model
  # <project_dir>/data_model
  # <project_dir>/data_model/db_setup.sql
  # <project_dir>/data_model/db_cleanup.sql
  # <project_dir>/data_model/table_setup.sql
  # <project_dir>/data_model/table_cleanup.sql
  # <project_dir>/aao_model/<project_name>.proto

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
    
  # Directories
  # - { src, web, aoo_model, auto_gen, data_model}
  DIR_SRC = 'src'
  DIR_WEB = 'web'
  DIR_AOO = 'aoo_model'
  DIR_AUTO = 'auto_gen'
  DIR_DATA = 'data_model'
  DIR_TESTS = 'tests'
  DIR_SRC_TEST = os.path.join( DIR_SRC, DIR_TESTS)
  new_dirs = [ DIR_SRC, DIR_WEB, DIR_AOO, DIR_AUTO, DIR_DATA, DIR_SRC_TEST]
  for dir_name in new_dirs:
    new_dir = os.path.join( _project_name, dir_name)
    cmd = "mkdir " + new_dir
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
      print "FATAL: Directory creation failed for project: " + new_dir
      return False
  
  # Files
  # { aoo_model/<project>.proto} 
  protobuf_file = os.path.join( _project_name, DIR_AOO, _project_name.lower() + ".proto")
  cmd = "touchf " + protobuf_file
  status, output = commands.getstatusoutput(cmd)
  if status != 0:
    print "FATAL: Protobuf file creation failed for project: " + protobuf_file
    return False

  # DB: { data_model/{db_setup.sql, db_cleanup.sql, table_setup.sql, table_cleanup.sql}}
  sql_files =  [ 'db_setup.sql', 'db_cleanup.sql', 'table_setup.sql', 'table_cleanup.sql', 'manage.py']
  for new_sql_file in sql_files:
    cmd = "touchf " + os.path.join( _project_name , DIR_DATA, new_sql_file)
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
      print "FATAL: Protobuf file creation failed for project: " + new_sql_file
      return False
    
  return True

###################################
# Function: create_project()
###################################  
def create_project():

  status, file_to_create = processCommandLine() 
  if not status:
    return printHelp()

  if not createProject( file_to_create):
    print "File: Creation: Failed: "
    return BASH_FAILURE

  return BASH_SUCCESS

###################################
# Function: main()
###################################  
def main():
    return create_project()

if __name__ == "__main__":
    sys.exit( main())

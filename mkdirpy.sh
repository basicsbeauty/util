#!/usr/bin/env bash

################################################################
# Filename: mkdirpy.sh
# Location: /home/ssatish/repos/util
# Project :
# Date    : 2015-07-22
# Author  : ssatish
# Usage   : mkdirpy <new_python_module_dir_name>
# Scope   :
#           - creates new directory
#           - creates new file <directory>/__init__.py
################################################################

# command line processing
if [ $# -ne 1 ]
then
  echo "usage: "$0" <new_python_module_dir_name>"
  exit
fi

new_target_dir=$1
echo "creating python module dir : "${new_target_dir}

# creating directory
cmd="mkdir "${new_target_dir}
eval $cmd 2> /dev/null
if [ $? -ne 0 ]
then
  echo "error: directory creation failed: "${new_target_dir}
  exit $?
else
  echo "directory creation succeded: "${new_target_dir}
fi

# creating module file
module_file=${new_target_dir}/"__int__.py"
cmd="touchf "${module_file}
eval $cmd 2> /dev/null
if [ $? -ne 0 ]
then
  echo "error: directory module file creation failed: "${new_target_dir}

  # undo: directory
  cmd="rmdir -rf "${new_target_dir}
  eval $cmd 2> /dev/null

  exit $?
fi

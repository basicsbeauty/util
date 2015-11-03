#!/bin/bash

# Command line arguments: Processing
if [ $# -ne 1 ]
then
    echo "Invalid usage: "
    echo "Usage: " $0 " <file_name>"
fi

# File presence check
if [ ! -f $1 ]
then
    echo "Error: File not present: " $1
fi

# File backup
cp $1 ~/backup/

if [ $? -ne 0 ]
then
    echo "Error: Backup failed: " $?
fi


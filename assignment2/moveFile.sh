#!/bin/bash

# function that takes two arguments destination and source. Moves .txt files from dst to src
function move {
  src=$1
  dst=$2
  if [ -d "$src" ]; then # checks if source folder is there
    if ! [ -d "$dst" ]; then # if destination folder is not found
      # makes folder
      echo "Destination folder hasn't been found. Making one..."
      mkdir ${dst}
    fi

    #YYYY-MM-DD-hh-mm
    now="$(date +'%F-%H-%M')"
    mkdir ${dst}/$now # New folder in destionation directory

    echo "Moving files..."
    for filename in "$src"/*.txt; do
      mv ${filename} ${dst}/$now # will move only txt files in "new folder
                                 # with date and time within destination folder"
    done


  else
    echo "Error: ${src} not found. Can not continue."
    exit 1
  fi
}

# call:
# $1 source, $2 destination
if [ "$#" == 2 ]; then # checks if there is enough arguments
  move $1 $2
else
  echo "Error: $# arguments are given. Need 2. Can not continue."
  exit 1
fi

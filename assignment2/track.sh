#!/bin/bash

label="" # holds value for label;
LOGFILE="/$(whoami)/.local/share/logfile.txt" # whoami finds name of the user

function track {
  if [ "$1" == "start" ]; then
    # checks if there is enough arguments
    if ! [ "$#" == 2 ]; then # need to have 2
      echo "Error: $# arguments are given. Need 2 (start [lable]). Can not continue."
    else
      # first we check if we have this file; if not, we make one
      if ! [ -f "$LOGFILE" ]; then
        touch "$LOGFILE"
      fi

      if [ -z "$label" ]; then # checks if label variable is empty
        label=$2 # label equal first argument
        echo "START $(date)" >> $LOGFILE
        echo "LABEL This is task ${label}" >> $LOGFILE
      else
        echo "There is already a task running"
      fi
    fi

  elif [ "$1" == "stop" ]; then
    if [ -z "$label" ]; then # checks if label variable is empty
      echo "There is no task that is running at the moment"
    else
      echo "END $(date)" >> $LOGFILE
      echo "" >> $LOGFILE
      label="" # to make lable avalable for next task
    fi

  elif [ "$1" == "status" ]; then
    if [ -z "$label" ]; then
      echo "There is no active task"
    else
      echo "Task ${label} is currently running"
    fi

  elif [ "$1" == "log" ]; then
    # TASK <lable>: HH:MM:SS
    input="$LOGFILE"
    startTime="" # holds value for start time
    lablename="" # holds value for label name
    endTime=""   # holds value for end time

    while IFS= read -r line
    do
      stLaEn="$(echo "$line" | cut -d " " -f1)"  # holds value for START LABEL END
      if [ "$stLaEn" == "START" ]; then
        startTime="$(echo "$line" | cut -d " " -f6)"
      elif [ "$stLaEn" == "LABEL" ]; then
        lablename="$(echo "$line" | cut -d " " -f5)"
      elif [ "$stLaEn" == "END" ]; then
        endTime="$(echo "$line" | cut -d " " -f6)"
      fi

      # makes sure that we print out only after we read three lines
      if ! [ -z "$startTime" ] && ! [ -z "$lablename" ] && ! [ -z "$endTime" ]; then
        # Finds out difference between start and end date; and prints it out
        printf "Task ${lablename}: " # so next print won't be on new line
        StartDate=$(date -u -d "$startTime" +"%s")
        FinalDate=$(date -u -d "$endTime" +"%s")
        date -u -d "0 $FinalDate sec - $StartDate sec" +"%H:%M:%S"

        # resets start, end time and lable (to make if work normaly)
        startTime=""
        lablename=""
        endTime=""
      fi

    done < "$input"
  else
    echo "'$1' is unknown function name"
    echo "Right way to use program is:
          track start [label]         To start tracker with givemn label
          track stop                  To stop tracker
          track status                To check status of the track
          track log                   To check log for tracker"
  fi
}


















# # Check if the function exists
# if declare -f "$1" > /dev/null
# then
#   "$@"  # call arguments
# else
#   # Print out error
#   echo "'$1' is unknown function name"
#   echo "Right way to use program is:
#         track start [label]         To start tracker with givemn label
#         track stop                  To stop tracker
#         track status                To check status of the track"
#   # exit 1
# fi

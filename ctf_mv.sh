#!/bin/bash

count=$(ls ~/Downloads/tmp | wc -w);
if [ ! "$count" -eq 0 ]
then
  if [ ! -d "$1" ]
  then
    mkdir "$1"
  fi
  name="flag"$(ls ~/Downloads/tmp/ | grep -oE "\.\S*")
  mv ~/Downloads/tmp/* "$1"/"$name";
  echo Done;
else
  echo There is nothing.
fi

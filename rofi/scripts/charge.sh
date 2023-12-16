#!/bin/bash

# Define the script's options
options="Full Charge"

# Display the options in rofi
selected=$(echo "$options" | rofi -dmenu -p "Battery Options:")

# Check if the user selected an option
if [ -n "$selected" ]; then
  case "$selected" in
    "Full Charge")
      # Run the command to charge the battery
      tlp chargeonce bat1
      ;;
  esac
fi

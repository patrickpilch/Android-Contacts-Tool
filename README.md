# Android Contacts Tool

This is a tool I quickly whipped up in a situation where my phone's screen was unusable, and my contacts were not backed up.
My tool takes the contacts database file from an android phone and spits out the phone numbers with their corresponding names.
It also has the option to put these names in a csv file.

## Usage

Simply provide the python script with the contacts database filename as an argument, and optionally include the '-csv' argument to create a .csv file. It will output a file in the same directory with the same filename as the contacts database.

## TODO

Add support for '.VCF' (vCard) contact files.
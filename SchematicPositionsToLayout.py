#!/usr/bin/env python

import sys
from array import array

print("\nThis simple script will take two files as parameters: a Kicad 5 schematic (.sch) and a PCB Layout (.kicad_pcb) file.")
print("The script lays out all the components in the PCB file on positions that mimic those in the Schematic.")
print("For the script to work, you'll need to finish your schematic and then import the schematic into a .kicad_pcb file.\n You can then use these two files as your input to this script.")
print("It then creates the file 'new.kicad_pcb' in your current folder that you can then use for laying out your board.")
print("\nNote that the script is provided 'as is' and I make no warranties whatsover, but it can shave hours of layout time.\n\n")
# check that parameters are valid
if len(sys.argv) < 2:
	sys.exit("Error: Please supply a Kicad .sch file as the first parameter")
if len(sys.argv) < 3:
	sys.exit("Error: Please supply a Kicad .kicad_pcb file as the second parameter")

# start by reading in the schematic
schematicItemNames = []
schematicItemPositions = []
pcbFileComplete = []
pcbComponentNames = []

with open(sys.argv[1], 'r') as my_file:
	for line in my_file:
		line = line.rstrip()
		if line.startswith("U "):
			schematicItemNames.append( line )
		if line.startswith("P "):
			schematicItemPositions.append( line )

# Read in the PCB file
with open(sys.argv[2], 'r') as my_file:
	for line in my_file:
		pcbFileComplete.append( line )
		if line.startswith("    (path /"):
			pcbComponentNames.append( line )

# Verify that the data is reasonably sound
i = 0
numNames = len(schematicItemNames)
numPositions = len(schematicItemPositions)
if numPositions == numNames:
	while i<numNames:
		"""
		print("--**********--")
		print(schematicItemNames[i])
		print(" : ")
		print(schematicItemPositions[i])
		"""
		i = i+1
	print("Number of components & positions found in schematic: ")
	print(numNames)
else:
	print("The number of names do not match the number of positions?")
	print(numNames)
	print(" vs ")
	print(numPositions)
	sys.exit("Error: Looks like there's an error in the input files?")

i = 0;
pcbFileLength = len(pcbFileComplete)
if pcbFileLength < 1:
	sys.exit("Error: Didn't find much data in your PCB file.")

# Start looping through the PCB file to find the current positions
while i<numNames:
	nameToLookFor = str( "    (path /"+schematicItemNames[i] )
	nameToLookFor = nameToLookFor.replace("U 1 1 ","")
	lineNumber = 0
	while lineNumber < pcbFileLength :
		if pcbFileComplete[lineNumber].find( nameToLookFor ) != -1:
			# the position may be up to three lines above the current
			positionOffset = 0;
			possiblePosition = str(pcbFileComplete[lineNumber-1])
			if possiblePosition.find("(at ") != -1:
				positionOffset = 1;
			possiblePosition = str(pcbFileComplete[lineNumber-2])
			if possiblePosition.find("(at ") != -1:
				positionOffset = 2;
			possiblePosition = str(pcbFileComplete[lineNumber-3])
			if possiblePosition.find("(at ") != -1:
				positionOffset = 3;
			possiblePosition = str(pcbFileComplete[lineNumber-4])
			if possiblePosition.find("(at ") != -1:
				positionOffset = 4;
			"""
			print("Found ")
			print(nameToLookFor)
			print(" on line ")
			print( lineNumber )
			print( " With position offset: ")
			print( positionOffset )
			"""

			# only update if we found the "at"
			if positionOffset > 0:
				currentPositionInPcb = str( pcbFileComplete[lineNumber-positionOffset] )
				currentPositionInSchematic = str( schematicItemPositions[i] ).split(" ")
				newX = float(currentPositionInSchematic[1])/100
				newY = float(currentPositionInSchematic[2])/100
				newPositionString = "    (at "+str(newX)+" "+str(newY)+")\n"
				"""
				print("Change position ")
				print( currentPositionInPcb )
				print(" to: ")
				print( newPositionString )
				print( "-*-\n")
				"""
				pcbFileComplete[lineNumber-positionOffset] = newPositionString
		lineNumber = lineNumber+1
	i = i+1

# save the result
f = open("new.kicad_pcb", "w")
for item in pcbFileComplete:
	f.write("{}".format(item))
f.close()

print("\n\nIf there's no errors above, we're all set! Look for the file 'new.kicad_pcb' in this folder :-)\n\n")


#python program that will scan an musicxml file, and at first, output the notes it finds :)

import xml.etree.ElementTree as ET

#need to clean this up, but needs to call other functions to lex, and then parse the xml files
def main():

    #should put a line in here to get the xml file from the shell

    #pass the file name in here to parse, hardcoded for now
    pplex()

def pplex():
    try:
        #creating a tree for the xml file
        tree = ET.parse('Testing/HelloWorld.xml')
    except IOError:
        print("Can't open that file, bucko.")

    #use this root to iterate through all of the children in the xml file
    root = tree.getroot()

    #giving a measure number for syntax
    measurenum = 0
    for measure in root.iter('measure'):
        measurenum += 1
        print("Measure " + str(measurenum) + " ")
        for note in root.iter('note'):
            pitch = note.find('pitch')
            step = pitch.find('step')
            if(step != 'NoneType'):
                steptext = step.text
                print(steptext)
        print("|\n")


main()

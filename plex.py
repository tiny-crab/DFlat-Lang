#file that tokenizes the measures inside the musicxml file

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

    #array whose elements are measures
    song = []




    #use this root to iterate through all of the children in the xml file
    root = tree.getroot()

    #for every measure in the song
    for measure in root.iter('measure'):
        
        #and for every note in the measure
        for note in measure.iter('note'):
            
            #get the pitch of the note (could also be a rest)
            pitch = note.find('pitch')
            
            #try to find a note name (will return "NoneType" if a rest)
            try:
                step = pitch.find('step')
                if(step != 'NoneType'):
                    try:
                        accidental = note.find('accidental')
                        print(get(accidental))
                    except:
                        steptext = step.text
                    print(steptext, end="")
            #if it's just a rest, skip back to the top of the note loop
            except:
                continue           
        print("|")

main()

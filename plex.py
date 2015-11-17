#file that tokenizes the measures inside the musicxml file

import xml.etree.ElementTree as ET

#need to clean this up, but needs to call other functions to lex
#and then parse the xml files
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

    #list whose elements are measures
    song = list()

    #use this root to iterate through all of the children in the xml file
    root = tree.getroot()

    #for every measure in the song
    for measure in root.iter('measure'):

        #array whose elements are notes: 'E' or 'e'
        notesInMeasure = []
        
        #and for every note in the measure
        for note in measure.iter('note'):
            
            #get the pitch of the note (could also be a rest)
            pitch = note.find('pitch')
            
            #try to find a note name and if it's flat
            try:
                steptext = pitch.find('step').text
            except:
                continue
            try:
                altertext = pitch.find('alter').text
            except:
                notesInMeasure.append(steptext)
                continue

            if(altertext == '-1'):
                notesInMeasure.append(steptext.lower())
            elif(altertext == '1'):
                print("What is this hashtag doing in mah music??")

        song.append(notesInMeasure)

    print(song)
main()

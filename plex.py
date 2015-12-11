#file that tokenizes the measures inside the musicxml file

import xml.etree.ElementTree as ET

#need to clean this up, but needs to call other functions to lex
#and then parse the xml files
def main():

    #should put a line in here to get the xml file from the shell
    try:
        pplex('Testing/HelloWorld.xml')
    except IOError:
        print("Can't open that file, bucko.")

def pplex(filename):
    #creating a tree for the xml file
    tree = ET.parse(filename)
        
    #list whose elements are measures
    song = list()

    #use this root to iterate through all of the children in the xml file
    root = tree.getroot()

    #for every measure in the song
    for measure in root.iter('measure'):

        #array whose elements are notes: 'E' or 'e'
        notesInMeasure = ""

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
                notesInMeasure += steptext
                continue

            if(altertext == '-1'):
                notesInMeasure += (steptext.lower())
            elif(altertext == '1'):
                print("What is this hashtag doing in my music?")

        song.append(notesInMeasure)

    print(song)
    return song
main()

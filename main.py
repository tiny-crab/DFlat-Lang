import plex

def main():

    #should put a line in here to get the xml file from the shell
    try:
        plex.pplex('Testing/HelloWorld.xml')
    except IOError:
        print("Can't open that file, bucko.")

main()

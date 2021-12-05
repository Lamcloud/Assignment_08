#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# SLam, 2021-Dec-04, added code to complete assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:
        
    properties:
        id: (int) with CD ID
        title: (string) with the title of the CD
        artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD class
    # -- Constructor --
    def __init__(self, id, title, artist):
        # -- Attributes --
        self.__id = id
        
        if title.strip() != '':
            self.__title = title
        else:
            raise Exception('CD title can\'t be empty!')
            
        if artist.strip() != '':
            self.__artist = artist
        else:
            raise Exception('Artist name can\'t be empty!')
            
    # -- Properties --
    @property  # Getter property
    def id(self):
        return self.__id
    
    @property  # Getter property
    def title(self):
        return self.__title
    
    @property  # Getter property
    def artist(self):
        return self.__artist
    
    # -- Methods --
    @staticmethod   
    def add_item(strID, strTitle, strArtist):
        """Add CD to list of dicts
        
        Args:
            strID (string): ID of the CD
            strTitle (string): Title of CD        
            strArtist (string): Artist of CD

        Returns
        -------
        lstOfCDObjects.

        """
        intID = int(strID)
        cd = CD(intID, strTitle, strArtist)
        lstOfCDObjects.append(cd)    
        return lstOfCDObjects
     
    @staticmethod
    def delete_item(lstOfCDObjects):
        """Delete CD from list of dicts
        
        Args:
            lstOfCDObjects: 2D data structure (list of objects) that holds the data during runtime
      
        Returns
        -------
        lstOfCDObjects: 2D data structure (list of objects) that holds the data during runtime

        """
        intRowNr = -1
        blnCDRemoved = False
        for cd in lstOfCDObjects:
            intRowNr += 1
            if cd.id == intIDDel:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return lstOfCDObjects
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        read_file(file_name, table): -> None
        write_file(file_name, lstOfCDObjects): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of CD objects): 2D data structure that holds the data during runtime

        Returns:
            None.
        """
                # Check if file exists
        try:          
            table.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                cd = CD(int(data[0]),data[1],data[2])
                table.append(cd)
                # adding for clarity
                print('table from read_file function:',table)
            objFile.close()
        # If file doesn't exist, tell user
        except FileNotFoundError as e:
            print('Text file does not exist!')
            print(e)

    # TODone Add code to process data to a file
    @staticmethod
    def write_file(file_name, table):
        # TODone Add code here
        """Function to save data to file
        
        Args:
            file_name (string): name of file used to write the data to
            table (list of CD objects): 2D data structure that holds the data during runtime
            
        Returns:
            None        
        """
        objFile = open(file_name, 'w')
        for cd in table:
            tplValues = (str(cd.id), cd.title, cd.artist)
            objFile.write(','.join(tplValues) + '\n')
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Class to process user input and display output"""

    
    """Handling Input / Output"""

    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            print('{}\t{} (by:{})'.format(cd.id, cd.title, cd.artist))
        print('======================================')

    # TODone add code to get CD data from user
    @staticmethod
    def ask_user():
        """Ask user to enter ID, Title, and Artist of CD
        
        Args:
            None        

        Returns
        -------
        strID (string): ID of the CD
        strTitle (string): Title of CD        
        strArtist (string): Artist of CD

        """
        try:
            strID = int(input('Enter an integer for ID: ').strip())          
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
            return strID, strTitle, strArtist
        except ValueError as e:
            print('ID has to be an integer!')
            print(e)
            
# -- Main Body of Script -- #
# TODone Add Code to the main body

# 1. When program starts, read in the currently saved Inventory
# Load data from file into a list of CD objects on script start
FileIO.read_file(strFileName, lstOfCDObjects)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice

    # Display menu to user
        # show user current inventory
        # let user add data to the inventory
        # let user save inventory to file
        # let user load inventory from file
        # let user exit program
            
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # Check if strings are empty from ask_user() function
        try:
            strID, strTitle, strArtist = IO.ask_user()
            lstOfCDObjects = CD.add_item(strID, strTitle, strArtist)
            IO.show_inventory(lstOfCDObjects)
        except Exception as e:
            print(e)
            print('Nothing to add.')       
            print()
        continue  # start loop back at top.
    
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstOfCDObjects)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIDDel = int(input('Enter an integer for the ID you would like to delete: ').strip())
            # 3.5.2 search thru table and delete CD
            lstOfCDObjects = CD.delete_item(lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        except ValueError as e:
            print('That is not an integer! <<< Customer Message')
            print(e)
            print()
        continue  # start loop back at top.
    
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODone move file processing code into function
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
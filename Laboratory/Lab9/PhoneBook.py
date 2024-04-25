from Contact import Contact

class PhoneBook:

    def __init__(self):
        """
        The phonebook keeps track of all contacts. This class is an example of 
        interacting with other classes a coder will make. 

        Instance variables provided for this constructor.
        """
        self.contactlist = []
        self.count = 0


    def addContact(self, c):
        if isinstance(c, Contact):
            self.contactlist.append(c)
        elif isinstance(c, dict):
            name = c["name"]
            pnum = c["number"]
            email = c["email"]
            birthday = c["birthday"]
            newContact = Contact(name,pnum,email,birthday)
            self.contactlist.append(newContact)

        self.count += 1
        """
        Given a contact, determine if you are given a dictionary or an instance of 
        a Contact class. Handle the adding to our phone book appropriately and update the counter.

        If you are given a dictionary, assume that a dictionary has the following keys 
        (and the values are in the correct format):
        - name
        - number
        - email
        - birthday

        NOTE: Why do we have to manually update the counter?
        """
    
    def getContactCount(self):
        return self.count
        """
        Returns the number of contacts stored in the 
        """
    
    def findContact(self, lName):
        tmp = []
        for i in self.contactlist:
            if lName == i.last:
                tmp.append(i)
        return tmp
        """
        Given a last name, find the contact(s) and return the contact information. 

        Will be a list. 
        """



    def groupChat(self, message):
        print(f"Sending message '{message}' to all contacts.")
        for i in self.contactlist:
            print(f"Sent to {i.getName()}")
        """
        Send a message to every contact in the phonebook
        """

    def __str__(self):
        return f'Phone Book: {self.count}'
        """
        Returns a string representation of the phonebook class. 

        The output will be
        > Phone Book: #

        Where # is the number of contacts in the phonebook. 
        """


class User:
    def __init__(self, username, password, email, phone):
        self.username = username
        # Encapsulation
        self.__password = password
        self.email = email
        self.phone = phone

    # def getPassword(self):
    #     return self.__password

    # def setPassword(self, password):
    #     self.__password = password

    def changePassword(self):

        print('*****Change Password*****')

        user = input('Enter Username:  ')
        currPass = input('Enter password:  ')

        if self.login(user, currPass):
            new1 = input('Enter New Password:  ')
            new2 = input('Confirm New Password:  ')
            if new1 == new2:
                self.__password = new1
                print('Password Changed!')
            else:
                print('New password not confirmed!')
        else:
            print('Invalid Cradentials')

    def printDetails(self):
        print(
            'Username', self.username, '\n'
            'Email', self.email, '\n'
            'Phone', self.phone
        )

    def login(self, username, password):
        if self.username == username and self.__password == password:
            return True
        else:
            return False


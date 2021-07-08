# This is a simple Python Program to convert Miles to Kilometre
def kilometre(mile):
    return(mile*1.609)# function for convert miles to kilometre.

mile = float(input("Enter the value in Mile\n"))#asking user to enter the value for convert.
kilometre = kilometre (mile)
print(mile,"Mile is = ",float(kilometre),"Kilometre")
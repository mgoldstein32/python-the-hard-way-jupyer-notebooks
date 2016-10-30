#importing arguments

#assigning variables to said arguments
print "Type the filename:"
#assigning a variable called "txt" as the file being opened
txt = raw_input("> ")
#printing out the file
print "Here's your file %r" %txt
filename = open(txt)
print filename.read()
#doing it again with a different variable
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

filename.close()
txt_again.close()

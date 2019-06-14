message = input("Hello Write something: ")
choosen_file = input("Choose file: 1) Kazahstan, 2) Paris. Input 1 or 2: ")
if choosen_file == 1:
	file_name = "google_kazakstan.txt"
else:
	file_name = "google_paris.txt"

file1 = open(file_name,"w") 
file1.write(message) 
file1.close()
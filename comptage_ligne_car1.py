file = open("df_all_no_spaces.txt","r") 
Counter = 0
  
Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1
          
print("This is the number of lines in the file") 
print(Counter) 

def counter(fname): 
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
  
    with open(fname, 'r') as f: 
        for line in f: 
            num_lines += 1
            word = 'Y'
            for letter in line: 
                if (letter != ' ' and word == 'Y'): 
                    num_words += 1
                    word = 'N'
                elif (letter == ' '): 
                    num_spaces += 1
                    word = 'Y'
                for i in letter: 
                    if(i !=" " and i !="\n"): 
                        num_charc += 1
    print("Number of words in text file: ", num_words) 
    print("Number of lines in text file: ", num_lines) 
    print('Number of characters in text file: ', num_charc) 
    print('Number of spaces in text file: ', num_spaces) 
    
def compte_car(fname, car):
    num_lines = 0
    num_charc = 0
      
    with open(fname, 'r') as f: 
        for line in f: 
            num_lines += 1
            for letter in line: 
                for i in letter: 
                    if(i == str(car)): 
                        num_charc += 1

    print("Nombre de ligne : ", num_lines)                        
    print(f"Nombre de {car} : ", num_charc) 
    
      
if __name__ == '__main__':  
    fname = 'df_all_no_spaces.txt'
    carac =";"
    try:  
        counter(fname)  
        print("\n")
        compte_car(fname,carac)
    except:  
        print('File not found') 
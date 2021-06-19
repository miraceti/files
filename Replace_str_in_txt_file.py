def replace_str_in_file(fichier, strfrom, strto):

    reading_file = open(fichier, "r")


    new_file_content = ""

    for line in reading_file:

        stripped_line = line.strip()

        # new_line = stripped_line.replace('<tr class="align-middle">', '<tr bgcolor = "grey" >')
        # stripped_line = new_line
        # new_line = stripped_line.replace('<tr class="align-middle bg-success ">', '<tr bgcolor = "green" >')
        # stripped_line = new_line
        # new_line = stripped_line.replace('<tr class="align-middle bg-danger">', '<tr bgcolor = "red" >')
        new_line = stripped_line.replace(strfrom, strto)
        stripped_line = new_line
        
        new_file_content += new_line +"\n"

    reading_file.close()


    writing_file = open(fichier, "w")

    writing_file.write(new_file_content)

    writing_file.close()

f =  "test1.html" 
#les ligne  neutre job desactivés
s1f = '<tr class="align-middle">'
s1t = '<tr bgcolor = "grey" >'
replace_str_in_file(f, s1f, s1t )

#les ligne  vert job succes
s1f = '<tr class="align-middle bg-success ">'
s1t =  '<tr bgcolor = "green" >'
replace_str_in_file(f, s1f, s1t )

#les ligne  rouge job en erreur
s1f = '<tr class="align-middle bg-danger">'
s1t = '<tr bgcolor = "red" >'
replace_str_in_file(f, s1f, s1t )
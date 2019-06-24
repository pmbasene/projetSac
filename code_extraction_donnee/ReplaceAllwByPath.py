#!/usr/bin/python
import os
import re

def change_directory(path):
    '''return the path where files are'''
    os.chdir(path)
    return os.getcwd()

def split_string(string, separator):
    '''this function take a string type in input and 
    the specific separator('=', '/', ':', etc. but not None)
    and return the right part of your string
    ! Note!:  separator is mandatory and do not None '''
    leftPartRep, rightpartRep = string.split(separator)
    # path_string = part2.strip()
    rightpartRep = rightpartRep.strip()
    leftPartRep = leftPartRep.strip()
    return leftPartRep, rightpartRep

def openFile_changeString(file, old_string, new_string):
    '''This function allows in first to open file with 
    writing mode and secondly to change an old string '''
    with open(file, 'w') as f:
        print('Changing {old_string} to + {new_string}+ in {file}'.format(**locals()))
        s = f.read()   # str type
        s = s.replace(old_string , new_string )
        return f.write(s)

#################### Main ########################
print(os.getcwd())
print('change directory ...')                          
PATH="/Users/ganasene/Desktop/doc/temp"      # Preciser le path d'acces au repertoire ou se trouve les fichiers à traiter   # penser a rendre le code interactif en demandant en ulisiteur de specifier le code repertoire   "try except ou simplement un I/O"
getdir = change_directory(PATH)                   #appel a la fonction change_directory() pour changer de repertoire
print(getdir)

print("=================================")
print('Lecture des fichiers........')
print("=================================")

compteurFichier = 0                        # permet de competer le nombre de fichier traitei
for file in os.listdir(getdir):            # parcourir les fichiers log du dossier precise en PATH
    # print(file)                          # lecture des fichiers , input :: file le nom du fichier, output :: fichier le contenu du fichier
  
    compteurFichier+=1
    with open(file, 'r') as f:       
        s = f.read()   # str type      
        varPath_patern = re.compile(r'\&\"\w*\"')                       # pattern pour les variables de chemin d'acces (&"variable-repetoire") exemple &"ParRepTmp"    
        matchVarPath = varPath_patern.findall(s)
        ParRep = re.compile(r'P[aA][rR].\w*.\w*\s=\s/export/home/.*|P[aA][rR].\w*.\w*\s=\s\w*_?\w*_?')     # pattern pour les repetoires d'acces chemin suivi de leur path(ou tout autre valeur) par ex: ParRepTmp=/to/the/path ou ParRepTmp= 00013034 
        # ParRep = re.compile(r'(P[aA][rR].\w*.\w*\s=)\s/export/home/.*|\s\w*_?\w*_?')                     # pattern pour les repetoires d'acces chemin uniquement  par ex: ParRepTmp=/to/the/path
        matchParRep = ParRep.findall(s)      # list type
        print('')
        print('Les repertoires sont au nombre de '+ str(len(matchParRep)) +' dans le fichier {file}'.format(**locals()))
        
        # Tester s'il existe des variables repertoire dans le fichier en cours  
        if not matchVarPath:
            print('Il y a de variables dans ce fichier')
        else:
            print(" - Les variables sont existantes sont {matchVarPath} ".format(**locals()))
            print('   Remplacement des variables par leur path-repertoire corresppond:')   

        for varOld in matchVarPath:
            var = varOld.lstrip('&').strip('"').strip()
            for item in matchParRep:                  # each item will be a string. so we can use the split_string function
                leftPartRep, rightpartRep = split_string(item,'=')
                # print(rightpartRep)            
                if leftPartRep == var:
                    with open(file, 'w') as f:
                        # s = f.read()   # str type
                        print("   > Changement de la variable [{varOld}] par son path '{rightpartRep}' dans le fichier {file} ".format(**locals()))
                        # print('Changing ['+ varOld +'] to ' + rightpartRep + ' in {file} '.format(**locals()))
                        s = s.replace(varOld, rightpartRep )
                        f.write(s)
print('')
print('***********************************************************************************************************************************************************************************************')
print('*****************************************************************Le nombre de fichiers traites {compteurFichier}***********************************************************'.format(**locals()))
print('***********************************************************************************************************************************************************************************************')
            

        
   

    



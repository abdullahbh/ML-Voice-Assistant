#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pydub')
get_ipython().system('pip install ffmpeg-python')


# In[2]:


import os
from zipfile import ZipFile
import patoolib
import shutil
from pydub import AudioSegment
from pydub.utils import which
import pydub


# In[3]:


with ZipFile('Assignment 7 part 1-20211129T152220Z-001.zip', 'r') as zipObj:
    zipObj.extractall()   # Extract all the contents of zip file in current directory
    names = zipObj.namelist()   
    


# In[28]:


cwd = os.getcwd()
#os.chdir('Assignment 7 part 1')
#os.chdir('../')

os.getcwd()


# # Extracting ZIP and RAR, Removing duplicates, Making subfolders

# In[5]:


#cwd = os.getcwd()
#print(cwd)
#os.chdir(r'\Assignment 07-B\Assignment 7 part 1')


my_list = os.listdir()
for i in my_list:
    if(i[-3:]=='zip'):
        with ZipFile(i, 'r') as zipObj:
                print('Extracting...zip ',i)
                #No subfolder files
                if i=='i202478.zip':
                    #filename=i
                    with ZipFile('i202478.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i202478')
                #duplicate        
                elif (i=='i200626(1).zip' or i=='i200626.zip'):
                    #filename=i
                    with ZipFile('i200626.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract')
                        
                #duplicate        
                elif (i=='i200697(2).zip' or i=='i200697(1).zip'or i=='i200697.zip' ):
                    #filename=i
                    with ZipFile('i200697.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i200697')
                        
                #duplicate        
                elif (i=='i202651(1).zip' or i=='i202651.zip'):
                    #filename=i
                    with ZipFile('i202651.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract')
                #duplicate
                elif (i=='i201787.zip' or i=='i201787(1).zip'):
                    #filename=i
                    with ZipFile('i201787.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract')
                        
                #duplicate
                elif (i=='i200844.zip' or i=='i200844(1).zip'):
                    #filename=i
                    with ZipFile('i200844.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract')
                        
                #duplicate?????????????????????hizaifa new folder
                elif (i=='i200693.zip' or i=='i200693(1).zip'):
                    #filename=i
                    with ZipFile('i200693.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract')
                #duplicate        
                elif (i=='i202416.zip' or i=='i202416(1).zip'):
                    #filename=i
                    with ZipFile('i202416.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract')
                        
                elif i=='i191706.zip':
                    #filename=i
                    with ZipFile('i191706.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i191706')   
                elif i=='i200667.zip':
                    #filename=i
                    with ZipFile('i200667.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i200667')
                elif i=='i200709.zip':
                    #filename=i
                    with ZipFile('i200709.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i200709')
                elif i=='i200894.zip':
                    #filename=i
                    with ZipFile('i200894.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i200894')
                elif i=='i201783.zip':
                    #filename=i
                    with ZipFile('i201783.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i201783')
                elif i=='i202652.zip':
                    #filename=i
                    with ZipFile('i202652.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i202652')
                elif i=='i202478.zip':
                    #filename=i
                    with ZipFile('i202478.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i202478')
                elif (i=='i200709(1).zip' or i=='i200709(2).zip' or i=='i200709.zip'):
                    #filename=i
                    with ZipFile('i200709.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i200709')
                elif i=='i200695.zip':
                    #filename=i
                    with ZipFile('i200695.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i200695')
                elif i=='i200676_dsn_ass7.zip':
                    #filename=i
                    with ZipFile('i200676_dsn_ass7.zip', 'r') as zippp:
                    #Extract all the contents of zip file in different directory
                        print('extracting Subfolder')
                        zippp.extractall('Extract/i200676')
                else:
                    zipObj.extractall('Extract')
                print('Done! with zip ',i)
                
    if (i[-3:] == 'RAR' or i[-3:] == 'rar'):
        print('Extracting...rar ',i)
        patoolib.extract_archive(i, outdir="Extract")
        print('Done! with rar ',i)

    
   


# # Renaming Files and ExtraSubfolder  

# In[36]:


#os.chdir('Extract')
#os.chdir('../')

cwd = os.getcwd()
print(cwd)
files = os.listdir(r'\Assignment 07-B\Assignment 7 part 1\Extract')
print(files)
for i in files:
    if os.path.isdir(f'Extract/{i}/{i}'):#general case
        os.rename(f'Extract/{i}/{i}', f'Extract/{i}/{i}i')
        shutil.move(f'Extract/{i}/{i}i', f'Extract/')
        shutil.rmtree(f'Extract/{i}')
        print(i,'....done')       
    if os.path.isdir(f'Extract/{i}/19I-1664'): #special case for the roll number
        shutil.move(f'Extract/{i}/19I-1664', f'Extract/')
        shutil.rmtree(f'Extract/{i}')
        print(i,'....done')
print(files)       


# In[19]:


#os.chdir('Extract')
for i in os.listdir():
    if i=='19I-1696':
        print('renaming...',i)
        os.rename(i,'i191696')
    elif i=='19I-166':
        print('renaming...',i)
        os.rename(i,'i190166')
    elif i=='New folder':
        print('renaming...',i)
        os.rename(i,'i200693')    
    else:
        print('renaming...',i)
        os.rename(i,i[:7])


# In[18]:


name_list=[]
for i in os.listdir():
    name_list.append(i)
print(name_list)


# # Converting to Wave 

# In[20]:


#os.chdir('../')
output_=i+'.wav'
for i in name_list:
    os.chdir(i)
    Audio_files=os.listdir()
    for j in Audio_files:
        sound = AudioSegment.from_file(j)
        sound.export(output_, format="wav")
        os.remove(j)
    os.chdir('../')
print('Done')


# # Spelling Correction

# In[38]:


#os.chdir('../')


for i in os.listdir():
    os.chdir(i)
    Audio_files = os.listdir()
    for i in Audio_files:
        new_name = i.lower()
        name_list = new_name.split()
        if 'ruha' in name_list:
            new_name=new_name.replace("ruha","")
        if 'ruha.' in name_list:
            new_name=new_name.replace("ruha.","")
        if 'voulme' in name_list:
            new_name=new_name.replace("voulme","volume")
        if 'humtv' in name_list:
            new_name=new_name.replace("humtv","hum tv")
        if 'bnd' in name_list:
            new_name=new_name.replace("bnd","band")
        if 'blub' in name_list:
            new_name=new_name.replace("blub","bulb")
        if 'jalaoo' in name_list:
            new_name=new_name.replace("jalaoo","jalao")
        if 'jlao' in name_list:
            new_name=new_name.replace("jlao","jalao")
        if 'zada' in name_list:
            new_name=new_name.replace("zada","ziada")
        if 'jao' in name_list:
            new_name=new_name.replace("jao","jeo")
        if 'tv' in name_list:
            new_name=new_name.replace("tv","t.v")
        if 't.v.' in name_list:
            new_name=new_name.replace("t.v.","t.v")
        if 't.vv' in name_list:
            new_name=new_name.replace("t.vv","t.v")
        if 'ac' in name_list:
            new_name=new_name.replace("ac","a.c")
        if 'awaaz' in name_list:
            new_name=new_name.replace("awaaz","awaz")
        if 'awz' in name_list:
            new_name=new_name.replace("awz","awaz")
        if 'lago' in name_list:
            new_name=new_name.replace("lago","lagao")
        if 'lagaao' in name_list:
            new_name=new_name.replace("lagaao","lagao")
        if 'lgao' in name_list:
            new_name=new_name.replace("lgao","lagao")
        if 'lagoa' in name_list:
            new_name=new_name.replace("lagoa","lagao")
        if 'chalaao' in name_list:
            new_name=new_name.replace("chalaao","chlao")
        if 'chalao' in name_list:
            new_name=new_name.replace("chalao","chlao")
        if 'chlaoo' in name_list:
            new_name=new_name.replace("chlaoo","chlao")
        if 'chalo' in name_list:
            new_name=new_name.replace("chalo","chlao")
        if 'kro' in name_list:
            new_name=new_name.replace("kro","karo")
        if 'keo' in name_list:
            new_name=new_name.replace("keo","karo")
        if 'karoo' in name_list:
            new_name=new_name.replace("karoo","karo")
        if 'loung' in name_list:
            new_name=new_name.replace("loung","lounge")
        if 'chanel' in name_list:
            new_name=new_name.replace("chanel","channel")
        if 'channal' in name_list:
            new_name=new_name.replace("channal","channel")
        if 'a.r.y' in name_list:
            new_name=new_name.replace("a.r.y","ary")
        if 'zyada' in name_list:
            new_name=new_name.replace("zyada","ziada")
        if 'zaida' in name_list:
            new_name=new_name.replace("zaida","ziada")
        if 'pay' in name_list:
            new_name=new_name.replace("pay","par")
        if 'pat' in name_list:
            new_name=new_name.replace("pat","par")
        if 'pr' in name_list:
            new_name=new_name.replace("pr","par")
        if 'per' in name_list:
            new_name=new_name.replace("per","par")
        if 'h.b.o' in name_list:
            new_name=new_name.replace("h.b.o","hbo")
        if 'gana' in name_list:
            new_name=new_name.replace("gana","gaana")
        if 'ganaa' in name_list:
            new_name=new_name.replace("ganaa","gaana")
        if 'ganay' in name_list:
            new_name=new_name.replace("ganay","gaaney")
        if 'gannay' in name_list:
            new_name=new_name.replace("gannay","gaaney")
        if 'ganna' in name_list:
            new_name=new_name.replace("ganna","gaaney")
        if 'ganay' in name_list:
            new_name=new_name.replace("gannay","gaaney")
        if 'ganne' in name_list:
            new_name=new_name.replace("ganne","gaaney")
        if 'pechla' in name_list:
            new_name=new_name.replace("pechla","pichla")
        if 'peechla' in name_list:
            new_name=new_name.replace("peechla","pichla")
        if 'phichla' in name_list:
            new_name=new_name.replace("phichla","pichla")
        if 'betaq' in name_list:
            new_name=new_name.replace("betaq","bethaq")
        if 'bethq' in name_list:
            new_name=new_name.replace("bethq","bethaq")         
        if 'bethak' in name_list:
            new_name=new_name.replace("bethak","bethaq")
        if 'behthak' in name_list:
            new_name=new_name.replace("behthak","bethaq")
        if 'betak' in name_list:
            new_name=new_name.replace("betak","bethaq")
        if 'alga' in name_list:
            new_name=new_name.replace("alga","agla")
        if 'betak' in name_list:
            new_name=new_name.replace("betak","bethaq")
        if 'teiz' in name_list:
            new_name=new_name.replace("teiz","tez")
        if 'taez' in name_list:
            new_name=new_name.replace("taez","tez")
        if 'teez' in name_list:
            new_name=new_name.replace("teez","tez")
        if 'lar' in name_list:
            new_name=new_name.replace("lar","par")
        if 'kum' in name_list:
            new_name=new_name.replace("kum","kam")
        if 'km' in name_list:
            new_name=new_name.replace("km","kam")
        if 'ky' in name_list:
            new_name=new_name.replace("ky","ki")
        if 'grage' in name_list:
            new_name=new_name.replace("grage","garage")
        if 'garrage' in name_list:
            new_name=new_name.replace("garrage","garage")
        if 'bythak' in name_list:
            new_name=new_name.replace("bythak","bethaq")
        if 'bethek' in name_list:
            new_name=new_name.replace("bethek","bethaq")
        if 'gany' in name_list:
            new_name=new_name.replace("gany","gaaney")
        if 'kr0' in name_list:
            new_name=new_name.replace("kr0","karo")
        if 'kari' in name_list:
            new_name=new_name.replace("kari","karo")
        if 'q.tv' in name_list:
            new_name=new_name.replace("q.tv","q-tv")
        if 'qt.v' in name_list:
            new_name=new_name.replace("qt.v","q-tv")
        if 'q-t.v' in name_list:
            new_name=new_name.replace("q-t.v","q-tv")
        if 'li' in name_list:
            new_name=new_name.replace("li","ki")
        if 'ka.' in name_list:
            new_name=new_name.replace("ka.","ka")
        if 'kight' in name_list:
            new_name=new_name.replace("kight","light")
        if 'sama' in name_list:
            new_name=new_name.replace("sama","samaa") 
        if 'wahroom' in name_list:
            new_name=new_name.replace("wahroom","washroom")
        if 'in' in name_list:
            new_name=new_name.replace("in","on")
        if 'geo' in name_list:
            new_name=new_name.replace("geo","jeo")
        if 'a.c.' in name_list:
            new_name=new_name.replace("a.c.","a.c")
        if '(1)' in name_list:
            new_name=new_name.replace("(1)","")
        if 'taiz' in name_list:
            new_name=new_name.replace("taiz","tez")
        if 'aahista' in name_list:
            new_name=new_name.replace("aahista","ahista")  
        if 'ok' in name_list:
            new_name=new_name.replace("ok","on")
        os.replace(i,new_name)
        print(i)
        print(files,'Done')


# In[ ]:


Final_list=[Ruha Bedroom ka Bulb jalao
Ruha Washroom ka Bulb jalao
Ruha Bathroom ka Bulb jalao
Ruha Kitchen ka Bulb jalao
Ruha Lounge ka Bulb jalao
Ruha Garage ka Bulb jalao
Ruha Bethaq ka Bulb jalao
Ruha Bedroom ki Light jalao
Ruha Washroom ki Light jalao
Ruha Bathroom ki Light jalao
Ruha Kitchen ki Light jalao
Ruha Lounge ki Light jalao
Ruha Garage ki Light jalao
Ruha Bethaq ki Light jalao
Ruha Bedroom ka Bulb on karo
Ruha Washroom ka Bulb on karo
Ruha Bathroom ka Bulb on karo
Ruha Kitchen ka Bulb on karo
Ruha Lounge ka Bulb on karo
Ruha Garage ka Bulb on karo
Ruha Bethaq ka Bulb on karo
Ruha Bedroom ki Light on karo
Ruha Washroom ki Light on karo
Ruha Bathroom ki Light on karo
Ruha Kitchen ki Light on karo
Ruha Lounge ki Light on karo

Ruha Garage ki Light on karo
Ruha Bethaq ki Light on karo
Ruha Bedroom ka Bulb band karo
Ruha Washroom ka Bulb band karo
Ruha Bathroom ka Bulb band karo
Ruha Kitchen ka Bulb band karo
Ruha Lounge ka Bulb band karo
Ruha Garage ka Bulb band karo
Ruha Bethaq ka Bulb band karo
Ruha Bedroom ki Light band karo
Ruha Washroom ki Light band karo
Ruha Bathroom ki Light band karo
Ruha Kitchen ki Light band karo
Ruha Lounge ki Light band karo
Ruha Garage ki Light band karo
Ruha Bethaq ki Light band karo
Ruha Bedroom ka Bulb off karo
Ruha Washroom ka Bulb off karo
Ruha Bathroom ka Bulb off karo
Ruha Kitchen ka Bulb off karo
Ruha Lounge ka Bulb off karo
Ruha Garage ka Bulb off karo
Ruha Bethaq ka Bulb off karo
Ruha Bedroom ki Light off karo
Ruha Washroom ki Light off karo
Ruha Bathroom ki Light off karo
Ruha Kitchen ki Light off karo
Ruha Lounge ki Light off karo
Ruha Garage ki Light off karo
Ruha Bethaq ki Light off karo
Ruha A.C chlao
Ruha A.C on karo
Ruha A.C band karo
Ruha A.C off karo
Ruha A.C ahista karo
Ruha A.C tez karo
Ruha A.C slow karo
Ruha A.C fast karo
Ruha T.V chlao
Ruha T.V on karo
Ruha T.V band karo
Ruha T.V off karo
Ruha T.V par jeo news lagao

Ruha T.V par samaa news lagao
Ruha T.V par ARY news lagao
Ruha T.V par cartoon network lagao
Ruha T.V par HBO lagao
Ruha T.V par HUM TV lagao
Ruha T.V par ARY Digital lagao
Ruha T.V par Q-TV lagao
Ruha T.V par discovery lagao
Ruha T.V par Masla TV lagao
Ruha Pichla channel lagao
Ruha Agla channel lagao
Ruha Previous channel lagao
Ruha Next channel lagao
Ruha T.V ki awaz ziada karo
Ruha T.V ki awaz slow karo
Ruha T.V ki awaz ahista karo
Ruha T.V ki awaz kum karo
Ruha T.V ki awaz tez karo
Ruha T.V ka volume slow karo
Ruha T.V ka volume ahista karo
Ruha T.V ka volume tez karo
Ruha T.V ka volume ziada karo
Ruha T.V ka volume kum karo
Ruha T.V mute karo
Ruha T.V unmute karo
Ruha Songs lagao
Ruha Gaaney lagao
Ruha Agla Gaana lagao
Ruha Pichla Gaana lagao
Ruha Agla Song lagao
Ruha Pichla Song lagao
Ruha Previous Song lagao
Ruha Next Song lagao
Ruha Previous Gaana lagao
Ruha Next Gaana lagao]


# In[ ]:


dirName=(r'C:\Users\DELL\OneDrive - FAST National University\3rd Semester\IDS\Assignment 07-B')

# create a list of file and sub directories 
# names in the given directory 
listOfFile = os.listdir(dirName)
allFiles = list()
# Iterate over all the entries
for entry in listOfFile:
    # Create full path
    fullPath = os.path.join(dirName, entry)
    # If entry is a directory then get the list of files in this directory 
    if os.path.isdir(fullPath):
        print(allFiles = allFiles + getListOfFiles(fullPath))
    else:
            allFiles.append(fullPath)
#print(allFiles)
print(listOfFile)


# In[ ]:


if (i[-3:] == 'RAR' or i[-3:] == 'rar'):
    print('Extracting...rar ',i)
    patoolib.extract_archive(i, outdir="Extracted")
    print('Done! with rar ',i)
    
    RAR ZIP
    
    
    
    
    # Get the current working directory
cwd = os.getcwd()
# Print the current working directory
print("Current working directory: {0}".format(cwd))
os.chdir(r'C:\Users\DELL\OneDrive - FAST National University\3rd Semester\IDS\Assignment 07-B\Assignment 7 part 1')
print("Current working directory: {0}".format(cwd))
os.mkdir('Extracted')

my_list = os.listdir(r'C:\Users\DELL\OneDrive - FAST National University\3rd Semester\IDS\Assignment 07-B\Assignment 7 part 1')

for i in my_list:
if(i[-3:]=='zip'):
    with ZipFile(i, 'r') as zipObj:
        if os.path.exists(i[:7]):
            print ('subfolder exists',i[:7])
            zipObj.extractall('Extracted')
            print('Done! with zip ',i)
            break
        else:
            print('making directory...',i)
            #os.mkdir(C:\Users\DELL\OneDrive - FAST National University\3rd Semester\IDS\Assignment 07-B\Assignment 7 part 1\Extracted\i[:7])
            os.chdir(r'C:\Users\DELL\OneDrive - FAST National University\3rd Semester\IDS\Assignment 07-B\Assignment 7 part 1\Extracted')
            os.mkdir(i[:7])
            print('Extracting...zip ',i)
            zipObj.extractall(i[:7])
            print('Done! with zip ',i)
            os.chdir("../Extracted")
        
   subfolder own

 if i=='i202478.zip':
                #filename=i
                with ZipFile('i202478.zip', 'r') as zippp:
                #Extract all the contents of zip file in different directory
                    print('extracting Subfolder')
                    zippp.extractall('Extract/i202478')
                    
                    
rename]
if i=='19I-1696':
    new_name='i191696'
    os.rename('19I-1696',new_name)
elif i=='New folder':
    os.rename(i,'i200693')    
else:
    os.rename(i,i[:7])


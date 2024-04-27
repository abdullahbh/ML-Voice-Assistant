#!/usr/bin/env python
# coding: utf-8

# # RUHA

# ## Importing Libraries

# In[1]:


from pathlib import Path
import pandas as pd 
import numpy as np
import os
import string
import librosa
import librosa as lr
import pickle
from zipfile import ZipFile
import shutil
from pydub import AudioSegment
from pydub.utils import which
import pydub
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report 
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.linear_model import PassiveAggressiveClassifier


# ## Feature Extraction of Audios (MFCC)

# In[2]:


mfccfeatures=[]
names=[]
labels=[]
MAX=5000
for i in os.listdir("D:/PROJECT/TestCase"):
    npath=os.path.join("D:/PROJECT/TestCase",i)
    print(npath)
    for j in os.listdir(npath):
        try:
            audio_path = os.path.join(npath,j)
            x , sr = librosa.load(audio_path)
            MFCC_Features = librosa.feature.mfcc(y=x, sr=sr)
            z=MFCC_Features.flatten()
            if(len(z)<=7000 and len(z)>= 2000):
                z=np.pad(z,(0,MAX-len(z)),'constant')
                mfccfeatures.append(z)
                print('try')
                labels.append(i)
        except:
            continue


# ## Removing NAN Values

# In[6]:


size=[]
for i in mfccfeatures:
    size.append(len(i))
n=max(size)
for i in mfccfeatures:
    while(len(i)<n):
        i.append(0)


# In[13]:


print(len(mfccfeatures))


# In[ ]:





# ## Sending MFCC to X for ML

# In[14]:


df=pd.DataFrame(mfccfeatures)
X=df
X


# ## Sending Labels to Y for ML 

# In[15]:


y=pd.DataFrame(labels)
y


# ## Combining DataFrames 

# In[16]:


result = [y,X]
result1=pd.concat(result,axis=1)
result1


# ## Prepare Train and Test 

# In[17]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=51)
print("shape of X_train = ",X_train.shape)
print("shape of X_test = ",X_test.shape)
print("shape of y_train = ",y_train.shape)
print("shape of y_test = ",y_test.shape)


# In[18]:


sc = StandardScaler()
sc.fit(X_train)
X_train_sc = sc.transform(X_train)
X_test_sc = sc.transform(X_test)


# ## 1-Decision Tree 

# In[19]:


Model1 = tree.DecisionTreeClassifier()
Model1 = Model1.fit(X_train, y_train)


# In[20]:


pred=Model1.predict(X_test)
Model1.score(X_test,y_test)


# In[21]:


print ("Accuracy : " , accuracy_score(y_test,pred)*100)  
print("Report : \n", classification_report(y_test, pred))
print("F1 Score : ",f1_score(y_test, pred, average='macro')*100)


# ## 2-KNN 

# In[22]:


Model2=KNeighborsClassifier()
Model2.fit(X_train, y_train)
pred=Model2.predict(X_test)
Model2.score(X_test,y_test)


# In[23]:


print ("Accuracy : " , accuracy_score(y_test,pred)*100)  
print("Report : \n", classification_report(y_test, pred))
print("F1 Score : ",f1_score(y_test, pred, average='macro')*100)


# In[ ]:





# ## 3-Passive Aggressive Classifier

# In[39]:


Model3 = PassiveAggressiveClassifier()
Model3.fit(X_train, y_train)

pred = Model3.predict(X_test)


# In[40]:


print ("Accuracy : " , accuracy_score(y_test,pred)*100)  
print("Report : \n", classification_report(y_test, pred))
print("F1 Score : ",f1_score(y_test, pred, average='macro')*100)


# ## 4-Logistic Regression

# In[26]:


Model4 = LogisticRegression()
Model4.fit(X_train, y_train)

pred = Model4.predict(X_test)


# In[27]:


print ("Accuracy : " , accuracy_score(y_test,pred)*100)  
print("Report : \n", classification_report(y_test, pred))
print("F1 Score : ",f1_score(y_test, pred, average='macro')*100)


# ## 5-Linear Support Vector Classification

# In[28]:


Model5 = LinearSVC()
Model5.fit(X_train, y_train)

pred = Model5.predict(X_test)


# In[29]:


print ("Accuracy : " , accuracy_score(y_test,pred)*100)  
print("Report : \n", classification_report(y_test, pred))
print("F1 Score : ",f1_score(y_test, pred, average='macro')*100)


# ## Making a folder to save Audio Recorded

# In[32]:


# os.mkdir('Save_Models')


# ## Saving All Used Models 

# In[33]:


pickle.dump(Model1, open("./Save_Models/DecisionTree", "wb"))
pickle.dump(Model2, open("./Save_Models/KNN", "wb"))
pickle.dump(Model3, open("./Save_Models/RandomForest", "wb"))
pickle.dump(Model4, open("./Save_Models/LogisticRegression", "wb"))
pickle.dump(Model5, open("./Save_Models/LinearSupportVectorClassification", "wb"))


# ## Loading All Used Models

# In[34]:


Model1 = pickle.load(open(".//Save_Models/DecisionTree", "rb"))
Model2 = pickle.load(open(".//Save_Models/KNN", "rb"))
Model3 = pickle.load(open(".//Save_Models/RandomForest", "rb"))
Model4 = pickle.load(open(".//Save_Models/LogisticRegression", "rb"))
Model5 = pickle.load(open(".//Save_Models/LinearSupportVectorClassification", "rb"))


# ## Getting Recorded Audio from WebPage and MFCC

# In[35]:


path='D:\PROJECT\Audios\Voice.wav'

mfccfeatures=[]
MAX=5000

x , sr = librosa.load(path)
MFCC_Features = librosa.feature.mfcc(y=x, sr=sr)
z=MFCC_Features.flatten()

if(len(z)<=5000 and len(z)>= 2000):
    z=np.pad(z,(0,MAX-len(z)),'constant')



# In[36]:


df2=pd.DataFrame(z)
df2
df2.set_axis(z, axis=0, inplace=False)
df2=df2.T
df2


# ## Label Predication Against our Audio Input

# In[37]:


MyAudio=[]

MyAudio.append(Model1.predict(df2))
MyAudio.append(Model2.predict(df2))
MyAudio.append(Model3.predict(df2))
MyAudio.append(Model4.predict(df2))
MyAudio.append(Model5.predict(df2))


# In[38]:


MyAudio


# In[ ]:





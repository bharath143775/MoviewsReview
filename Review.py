#load dataset and modules
import pandas as pd
import re
data=pd.read_csv('C:/Users/bharath.thothireddy/Desktop/indian movies.csv')
data.head()



#clean the data 
# data[(data['Timing(min)']=='-' & data['Rating(10)'=='-'])]
count=0
li_data=[]
li_genre=[]
for i in range(50601):
    if (data['Timing(min)'][i]=='-') & (data['Rating(10)'][i]=='-') & (data['Votes'][i]=='-'):
        pass
    else:
        #convert all timinings into integer data type
        data['Timing(min)'][i]=str(data['Timing(min)'][i])
        data['Timing(min)'][i]=''.join(re.findall('\d+',data['Timing(min)'][i]))
        if data['Timing(min)'][i]=='':
            data['Timing(min)'][i]=int(0)
        else:
            data['Timing(min)'][i]=int(data['Timing(min)'][i][:4])
        #convert all Ratings into float datatype
        if data['Rating(10)'][i]=='-':
            data['Rating(10)'][i]=float(0)
        else:
            data['Rating(10)'][i]=float(data['Rating(10)'][i])
        #convert votes to int type
        data['Votes'][i]=str(data['Votes'][i])
        if data['Votes'][i]=='-':
            data['Votes'][i]=0
        else:
            data['Votes'][i]=int(''.join(re.findall('\d+',data['Votes'][i])))
        li_data.append([data['ID'][i],data['Movie Name'][i],data['Year'][i],data['Timing(min)'][i],data['Rating(10)'][i],data['Votes'][i],data['Language'][i]])
        li_genre.append([data['ID'][i],data['Genre'][i]])
        
        
        
#create dataset for reviews
indianMoviesReview=pd.DataFrame(li_data)
indianMoviesReview.columns=['ID','Movie_name','Year','RunTime','Rating','Votes','Language']
indianMoviesReview.head()



#cheking genre data set
indianMoviesGenre=pd.DataFrame(li_genre)
indianMoviesGenre.head()



#get unique genres of movies
uni={'Comedy','Musical'}
for i in indianMoviesGenre[1]:
    li=[]
    if i=='-':
        pass
    else:
        li=i.split(',')
    for j in li:
        uni.add(j.strip())
uni=list(uni)
#print(len(indianMoviesGenre[1]))
uni.insert(0,'MovieId')
uni



#create dataset assigning relevant genre to movie
indianMoviesGenreUpdate=pd.DataFrame(columns=uni)



#store values in genre dataset
li=[0]*27
for i in range(len(indianMoviesGenre)):
    new=pd.DataFrame([li],columns=uni)
    new['MovieId']=indianMoviesGenre[0][i]
    if indianMoviesGenre[1][i]=='-':
        pass
    else:
        li1=indianMoviesGenre[1][i].split(',')
        for j in li1:
            #print(j)
            new[j.strip()]=1
    indianMoviesGenreUpdate=indianMoviesGenreUpdate.append(new)
indianMoviesGenreUpdate.head()



#shape of reviews dataset
indianMoviesReview.shape



#check info of data
indianMoviesReview.info()



#description of data
indianMoviesReview.describe()



#shape of genre dataset
indianMoviesGenreUpdate.shape
indianMoviesGenreUpdate.describe()
indianMoviesGenreUpdate.info()



#store the datasets in filesystem
#store reviews csv file
indianMoviesReview.to_csv('C:/Users/bharath.thothireddy/Desktop/Movie_reviews_update.csv')
#store genres file 
indianMoviesGenreUpdate.to_csv('C:/Users/bharath.thothireddy/Desktop/Movie_Genre_update.csv')


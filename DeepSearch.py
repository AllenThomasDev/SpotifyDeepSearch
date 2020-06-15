import spotipy
import spotipy.util as util
import pandas as pd
user_id = 'ENTER YOUR SPOTIFY USER ID HERE'
client_id='ENTER YOUR SPOTIFY API CLIENT ID HERE'
client_secret='ENTER YOUR SPOTIFY API SECRET ID HERE'
token = util.prompt_for_user_token(user_id,
                                   'user-follow-read',
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri='http://www.google.com/')

if token:
    sp = spotipy.Spotify(auth=token)

else:
    print("Can't get token for")


def getid():
    print("Enter an Artist's ID")
    artid= input()
    return(artid)

def addedge(artist_id,depth,width):
    global df
    global udf
    r=(sp.artist_related_artists(artist_id)['artists'][0:depth])
    a = sp.artist(artist_id)
    udf.append(a['uri'])
    if maindict.get(a['name'])!=1:
        for x in r:
            df=df.append({'source':a['name'],'target':x['name']},ignore_index=True)
            udf.append(x['uri'])
        maindict[a['name']]=1
        if width!=0:
            for x in r:
                addedge(x['uri'],depth,width-1)

def ChunksToDataframe(chunks):
    global edf
    for chunk in chunks:
        a = sp.artists(chunk)['artists']
        for x in a:
            x.update({'followers':x.get('followers').get('total')})
        rf=pd.DataFrame(a,columns=['name','followers','genres','popularity','uri'])
        edf=edf.append(rf)



edf=pd.DataFrame()
df=pd.DataFrame(columns=['source','target'])
udf=[]
maindict={}
artist_id=getid()
addedge(artist_id,5,1)
print(df)
udf=(list(set(udf)))
n=50
chunks = [udf[i * n:(i + 1) * n] for i in range((len(udf) + n - 1) // n )]  
ChunksToDataframe(chunks)
df=df.reset_index(drop=True)
edf=edf.reset_index(drop=True)
print(df,edf)
df.to_csv('edges.csv',columns=['source','target'],index=False)
edf.to_csv('nodes.csv',columns=['name','followers','genres','popularity','uri'],index=False)
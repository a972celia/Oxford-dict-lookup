import requests
import json
import pandas as pd
app_id='e5212d29'
app_key='bb9ea11df3f293227a4f9f1ea4888998'
language = 'en'

def wordlist():
    """
    create a wordlist file
    """
    df= pd.read_csv(r'/Users/Celia/Desktop/Book1.csv',index_col=0)
    wordlist=[]
    definlist=[]
    for i in range(len(df.index)):
        word_id=df.index[i]
        wordlist.append(word_id)
        needed_data=lookup(app_id,app_key,language,word_id)
        try:
            string=''.join(needed_data)
            definlist.append(string)
        except:
            definlist.append(needed_data)

    d={'Vocabulary':wordlist,'Definitions':definlist}
    new_df=pd.DataFrame(d)
    return new_df

def lookup(app_id,app_key,language,word_id):
    """
    use oxford api to lookup the definitions of Vocabulary
    """
    try:
        url="https://od-api.oxforddictionaries.com:443/api/v1/entries/{language}/{word_id}".format(
        language=language,
        word_id=word_id.lower())

        r=requests.get(url,headers={'app_id': app_id, 'app_key': app_key})
        response=json.loads(json.dumps(r.json()))
        definitions=response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]
        return definitions
   except:
       pass
new_df=wordlist()


Vocabulary_csv=new_df.to_csv(r'/Users/Celia/Desktop/Vocabulary.csv',index=None,header=True)

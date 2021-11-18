#Code sourced from Interface prompts provided by OpenBlender
#https://www.openblender.io/#/api_documentation

import OpenBlender
from io import StringIO
import pandas as pd
import json


action = 'API_getObservationsFromDataset'

# ANCHOR: 'Reuters Health News'

        
parameters = { 
    	'token':'619676319516294be8885e82KPdqPJVe5bTtrhLzXx1ghwpE9724yg',
	'id_user':'619676319516294be8885e82',
	'id_dataset':'5d5718ac9516293a12ad4f45' 
}
        

df = pd.read_json(StringIO(json.dumps(OpenBlender.call(action, parameters)['sample'])), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df.reset_index(drop=True, inplace=True)
df.to_csv("2ndNewDataset.csv", encoding='utf-8', index=False)

# ANCHOR: 'New York Times Health News'

        
parameters = { 
    	'token':'619676319516294be8885e82KPdqPJVe5bTtrhLzXx1ghwpE9724yg',
	'id_user':'619676319516294be8885e82',
	'id_dataset':'5d5aaf849516296e5749de67',
	'missing_values_treatment':{"treatment":"remove","exclude":[]} 
}
        

df = pd.read_json(StringIO(json.dumps(OpenBlender.call(action, parameters)['sample'])), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df.reset_index(drop=True, inplace=True)
df.to_csv("NewYorkTimesNewsDataset.csv", encoding='utf-8', index=False)

# ANCHOR: 'ABC News  International Health headlines'

        
parameters = { 
    	'token':'619676319516294be8885e82KPdqPJVe5bTtrhLzXx1ghwpE9724yg',
	'id_user':'619676319516294be8885e82',
	'id_dataset':'5d7f93389516294be568af4e',
	'missing_values_treatment':{"treatment":"remove","exclude":[]} 
}
        

df = pd.read_json(StringIO(json.dumps(OpenBlender.call(action, parameters)['sample'])), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df.reset_index(drop=True, inplace=True)
df.to_csv("ABCNewsDataset.csv", encoding='utf-8', index=False)


# ANCHOR: 'Fox News Health News'

        
parameters = { 
    	'token':'619676319516294be8885e82KPdqPJVe5bTtrhLzXx1ghwpE9724yg',
	'id_user':'619676319516294be8885e82',
	'id_dataset':'5d571fc09516293a13832042',
	'missing_values_treatment':{"treatment":"remove","exclude":[]} 
}
        

df = pd.read_json(StringIO(json.dumps(OpenBlender.call(action, parameters)['sample'])), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df.reset_index(drop=True, inplace=True)
df.to_csv("FoxNewsDataset.csv", encoding='utf-8', index=False)

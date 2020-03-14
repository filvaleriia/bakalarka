import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import numpy as np
from rdkit.Chem import Draw
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('/home/valeriia/bakalarka/filvaleriia/data.csv')


print(data.head())
data.info()

# copy raw data
data_new = data.copy()
print(data_new['smiles'].head())
print("--------------------------------------------------------")

data_new["Molecule"] = [Chem.MolFromSmiles(mol) for mol in data["smiles"]]

data_new.info()


#first colmun invert to binary systems

data_new['bin'] = [np.array(AllChem.GetMorganFingerprintAsBitVect(i,2, nBits=1024)) for i in data_new['Molecule']]
print(data_new['bin'].head())

data_new.info()

#maybe can make new table, wchich have 'chembl_id','Molecule', 'bin', 'potency', 'pec50', 'category'

# i don*t understand, as i can compare date
# i don*t understand, as i make regrasion model
# if i make clasifikation model i has to use Tanimote koeficient
#


#clasifikation model
#i use random forest, and i make to set 80:20


#RANDOM FOREST???
#regrese
train_br, test_br, train_pr, test_pr = train_test_split(data_new['bin'], data_new['pec50'],test_size = 0.25, random_state = 42)
#random_state?????

rf = RandomForestRegressor(n_estimators = 30, random_state = 42)
rf.fit(train_br, train_pr)

#classificatiom
train_bc, train_pc = make_classification(n_sestimators=100, max_depth= 4, random_state = 42)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(train_bc, train_pc)
print(clf.feature_impor
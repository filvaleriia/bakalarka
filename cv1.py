from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import numpy as np

m1 = Chem.MolFromSmiles('Cc1cc2c(cc1C(=C)c3ccc(cc3)C(=O)O)C(C)(C)CCC2(C)C')
bi={}
fp1 = [np.array(AllChem.GetMorganFingerprintAsBitVect(m1,radius=2, bitInfo = bi))]


print(fp1)
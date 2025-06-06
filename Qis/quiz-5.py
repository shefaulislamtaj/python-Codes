from rdkit import chem 
from rdkit.chem import Draw
from IPython.display import display
smiles = input("Enter a SMILES string: ")
mol = chem.MolFromSmikes(smiles)
if mol: 
     display(Draw.MolToImage(mol))
else:
    print("Invalid SMILES string!")
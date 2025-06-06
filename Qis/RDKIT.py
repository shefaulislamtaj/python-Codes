from rdkit import Chem
from rdkit.Chem import Draw
from IPython.display import display

smiles = input("Enter a SMILES string: ")
mol = Chem.MolFromSmiles(smiles)

if mol: 
    display(Draw.MolToImage(mol))
else:
    print("Invalid SMILES string")

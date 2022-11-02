import numpy as np
import pandas as pd
from urllib.request import urlopen
import pubchempy


root_path         = "~/Symmetry"
smiles_filepath    = f'{root_path}/Aromatic_Substituted_Output.csv'
is_practice       = False
output_filepath   = f'{root_path}/Aromatic_Substituted_Names.csv'

def readData(smiles_filepath):
  smiles_df   = pd.read_csv(smiles_filepath)
  return smiles_df

def convert_smile_To_Name(smile):
    compounds = pubchempy.get_compounds(smile, namespace='smiles')
    match = compounds[0]
    return match.iupac_name
  
def get_Name_from_SMILE():
    df=readData(smiles_filepath)
    pd.set_option('display.max_colwidth', None)
    total_rows = len(df.index)
    
    for row in range(0,total_rows):
            smile=df.loc[row,"SMILE"]
            df.loc[row,"NAME"]=convert_smile_To_Name(smile)
            
    df.to_csv(output_filepath, index=False)

    
if __name__ == "__main__":
  get_Name_from_SMILE()
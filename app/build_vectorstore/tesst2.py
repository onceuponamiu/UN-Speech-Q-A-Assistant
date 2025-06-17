import pandas as pd







import pandas as pd
from pathlib import Path

def load_debate_data():
    
    # Đọc file CSV
    df = pd.read_csv("./app/data/raw/un-general-debates.csv")

    return df

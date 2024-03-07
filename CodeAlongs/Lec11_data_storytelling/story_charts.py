import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

DATA_PATH= Path(__file__).parents[2]/ "Data"

class StoryCharts:
    def __init__(self) -> None:
        pass
        
        
    def _plot(self, x, y, colors= "#1400F4", ** label_kwargs):
        self.fig, self.ax= plt.subplots()
        
    def Line(self, x, y):
        pass
#Check to run script as a stand-alone, main is the file name
if __name__ == "__main__":
    print("\n\n")
    print(DATA_PATH)
    #print(__name__)
    
    df = pd.read_csv(DATA_PATH/ "co2_annmean_mlo.csv", skiprows= 43)
    print(df.head())
    
    sc= StoryCharts()
    sc._plot(2, 3)
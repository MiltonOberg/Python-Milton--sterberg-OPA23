class Pikachu:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    @property
    def height(self):
        return self._height
    @property
    def width(self):
        return self._width

class Pichu:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    @property
    def height(self):
        return self._height
    @property
    def width(self):
        return self._width



class Userinterface:
    def userinterface():
        import numpy as np
        unidentified_width = float(input("Enter width of entity: "))
        unidentified_height = float(input("Enter height of entity: "))


        unidentified_distance_pikachu = np.sqrt((width_mean_pikachu - unidentified_width)**2 + (height_mean_pikachu - unidentified_height)**2) 
        unidentified_distance_pichu = np.sqrt((width_mean_pichu - unidentified_width)**2 + (height_mean_pichu - unidentified_height)**2)

        if unidentified_distance_pikachu < unidentified_distance_pichu:             #If Pikachu distance is smaler then Pichu's
            print(f"You most likly found a Pikachu!")
        elif unidentified_distance_pichu < unidentified_distance_pikachu:           #If Pichu distance is smaler then Pikachu's
            print(f"You most likly found a Pichu!")
        else:
            print(F"I am unshore if you found a Pikachu or Pichu...")               #If the distance are the same
    

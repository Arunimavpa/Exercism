class SpaceAge:
    planet_years ={
        'earth':1.0,
        'mercury':0.2408467,
        'venus':0.61519726,
        'mars':1.8808158,
        'jupiter':11.862615,
        'saturn':29.447498,
        'uranus':84.016846,
        'neptune':164.79132
    }
    def __init__(self, seconds):
        self.seconds=seconds

    def age(self,planet):
        earth_seconds=31557600
        return round((self.seconds / earth_seconds) / self.planet_years[planet], 2)
        
    def on_earth(self):
        return self.age('earth')

    def on_mercury(self):
        return self.age('mercury')
    
    def on_venus(self):
        return self.age('venus')
    
    def on_mars(self):
        return self.age('mars')
    
    def on_jupiter(self):
        return self.age('jupiter')
    
    def on_saturn(self):
        return self.age('saturn')
    
    def on_uranus(self):
        return self.age('uranus')
    
    def on_neptune(self):
        return self.age('neptune')






import random
import pickle
import csv

class House:
    def __init__(self):
        self.bedrooms = random.randrange(1, 7)
        self.bathrooms = random.randrange(1, 10)
        self.ensuit = random.randrange(0, self.bedrooms+1)
        self.distanceToCity = random.randrange(100, 100000)
        self.area = random.choice([2, 4, 6, 10])
        self.garden = random.randrange(0, 10)
        self.price = int(round(((100 * self.bedrooms) + (75*self.bathrooms)+(100*self.ensuit)+(10000000*(1/self.distanceToCity))+(1000*(self.area*self.area))+(500*(self.garden*self.garden)))))*20

    def returnNetVals(self):
        return [self.bedrooms, self.bathrooms, self.ensuit, self.distanceToCity, self.area, self.garden, self.price]

houseCount = 2000

if __name__ == "__main__":
    houses = [House() for x in range(houseCount)]
    data = [x.returnNetVals() for x in houses]
    print(data)
    with open("TrainingData.csv", 'w') as f:
        csv_writer = csv.writer(f)
        for row in data:
            csv_writer.writerow(row)
        f.close()
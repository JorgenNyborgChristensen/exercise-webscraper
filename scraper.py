from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv

driver = webdriver.Firefox()

exercises = []
muscleGroups = []
equipmentTypes = []

urls = ['https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/1/muscle/chest', 'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/6/muscle/neck',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/11/muscle/traps',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/12/muscle/shoulders',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/15/muscle/biceps',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/2/muscle/forearms',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/13/muscle/abdominals',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/7/muscle/quadriceps',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/9/muscle/calves',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/10/muscle/triceps',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/3/muscle/lats',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/4/muscle/middle-back',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/5/muscle/lower-back',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/14/muscle/glutes']


f = csv.writer(open('exercises.csv', 'w'))
f.writerow(['Muscle Group', 'Exercise', 'Equipment'])

for url in urls:
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('div', attrs={'class':'ExResult-cell ExResult-cell--nameEtc'}):
        #print(a)
        exercise = a.find('h3', attrs={'class':'ExHeading ExResult-resultsHeading'}).a
        muscle = a.find('div', attrs={'class':'ExResult-details ExResult-muscleTargeted'}).a
        equipment = a.find('div', attrs={'class' : 'ExResult-details ExResult-equipmentType'}).a
        f.writerow([muscle.get_text(strip=True), exercise.get_text(strip=True), equipment.get_text(strip=True)])
        
driver.close()



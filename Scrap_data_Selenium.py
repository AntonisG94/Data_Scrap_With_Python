# Import βιβλιοθηκων που χρειαζονται για το προγραμμα μας
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re


#Δηλωση του PATH που βρισκεται ο chrome driver μας για ανοίξει ο webdriver της βιβλιοθηκης Selenium
PATH="C:\Program Files (x86)\chromedriver.exe"
#Δηλωση της ιστοσελίδας που θα κάνουμε scrap τα δεδομένα μας
url = 'https://www.youtube.com/channel/UCzSeVpD8AKKyWRz1HtW0kkw/videos'
#Δηλωση του browser που ανοιγουμε και του PATH ως webdriver
driver = webdriver.Chrome(PATH)
#Ανακατεύθυνση στο URL της ιστοσελιδας μας
driver.get(url)
#Ζητάμε με συναρτηση της βιβλιοθηκης Selenium να μας τραβηξει ολα τα elements με συγκεκριμενο class name
videos = driver.find_elements(By.CLASS_NAME,'style-scope ytd-grid-video-renderer')
#Δηλωση κενών λιστών που θα χρησιμοποιησουμε αργότερα για την εισαγωγη των δεδομενων μας ως text
mylist1 = []
mylist2 = []
#Επαναληψη για ολα τα δεδομενα που εχουμε στο videos ετσι ωστε να ξεχωρισουμε το καθε ενα σαν πληροφορια που χρειαζομαστε
for video in videos:
    #Ζητάμε με συναρτηση της βιβλιοθηκης Selenium να μας τραβηξει ολα τα elements με xPATH ΊΔΙΟ και που αναφέρεται στον τιτλο των βιντεο
    title = video.find_element(By.XPATH,'.//*[@id="video-title"]').text
    #Ζητάμε με συναρτηση της βιβλιοθηκης Selenium να μας τραβηξει ολα τα elements με xPATH ΊΔΙΟ και που αναφέρεται στις προβολες των βιντεο
    views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    #Κρατάμε μόνο τον αριθμό των views για να μπορουμε να χρησιμοποιησουμε την στηλη για το scatterplot
    numeric_filter = filter(str.isdigit, views)
    numeric_string = "".join(numeric_filter)
    #Ζητάμε με συναρτηση της βιβλιοθηκης Selenium να μας τραβηξει ολα τα elements με xPATH ΊΔΙΟ και που αναφέρεται στην αναρτηση των βιντεο
    upload_time = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
    #Ζητάμε με συναρτηση της βιβλιοθηκης Selenium να μας τραβηξει ολα τα elements με xPATH ΊΔΙΟ και που αναφέρεται στο URL των βιντεο
    thumbnails = video.find_elements(By.XPATH,'//*[@id="thumbnail"]')
    #Δημιουργία στηλων και γραμμων με πληροφορία
    item1 = {
    'University of the Aegean Videos Title' : title,
    'Views Until Now' : numeric_string,
    'Uploaded' : upload_time,
    }
    #Δημιουργία λιστας με ολες τις πληροφορίες που χρειαζομαστε για το dataframe
    mylist1.append(item1)
#Επαναληψη για ολα τα δεδομενα που εχουμε thumbnails
#Αφου τα Links για καθε βιντεο δινονται σαν attribute μεσα σε ετικετες με id thumbnail
#Πρεπει να γίνει αντληση δεδομένων σε δευτερο επίπεδο
for href in thumbnails:
    #Ζηταμε ολα τα στοιχεα απο το thumbnails με attribute href
    hrefs = href.get_attribute('href')
    # hrefs.pop(key, None)
    #Αποκλειουμε πιθανον σφαλμα στα δεδομενα μας οχι πιθανον Null τιμες αλλα None
    if (hrefs is not None) :
    #Δημιουργία στηλων και γραμμων με πληροφορία
        item2 = {
            'Links' : hrefs
        }
        #Δημιουργία λιστας με ολες τις πληροφορίες που χρειαζομαστε για το dataframe
        mylist2.append(item2)
driver.close()
#Κατασκευη DataFrame από την λιστα μας.
df1 = pd.DataFrame(mylist1)
#Αποκλειουμε πιθανον σφαλμα και ΝaN τιμη στο dataframe μας
new_df1 = df1.dropna(axis=0)
#Κατασκευη DataFrame από την λιστα μας.
df2 = pd.DataFrame(mylist2)
#Αποκλειουμε πιθανον σφαλμα και ΝaN τιμη στο dataframe μας
new_df2 = df2.dropna(axis=0)
#Ενωση των dataframe μας για την ωραιοτερη εγγραφη τους σε Excel αρχειο
result = new_df1.join(new_df2, how="outer")
#Δημιουργία Excel αρχειου και εγγραφη των dataframe μας
filepath = Path('data.xlsx')
filepath.parent.mkdir(parents=True, exist_ok=True)
result.to_excel(filepath, encoding = "ISO-8859-7")

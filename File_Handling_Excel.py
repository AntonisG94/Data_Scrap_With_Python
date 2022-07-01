# Import βιβλιοθηκων που χρειαζονται για το προγραμμα μας
import pandas as pd
import csv
from win32com.client import Dispatch
import easygui
from matplotlib import pyplot as plt
import numpy as np

#ΔΗΜΙΟΥΡΓΙΑ ΣΥΝΑΡΤΗΣΗΣ ΓΙΑ MESSAGE BOX ΩΣΤΕ ΝΑ ΕΜΦΑΝΙΣΟΥΜΕ ΤΑ ΠΟΣΟΣΤΑ NULL ΤΙΜΩΝ
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#ΕΝΑΡΞΗ ΕΦΑΡΜΟΓΗΣ EXCEL ΚΑΙ ΤΗΝ ΕΜΦΑΝΙΖΟΥΜΕ ΜΠΡΟΣΤΑ ΓΙΝΕΤΑΙ VISIBLE
xl = Dispatch("Excel.Application")
xl.Visible = True
#ΑΝΟΙΓΟΥΜΕ ΤΟ ΑΡΧΕΙΟ EXCEL ΜΑΣ ΠΟΥ ΑΠΟΘΗΚΕΥΣΑΜΕ ΑΠΟ ΤΟ SCRAP
wb = xl.Workbooks.Open(r'F:\Giannhs\Tasks\data.xlsx')
#ΔΗΜΙΟΥΡΓΙΑ DATAFRAME ΜΕΣΩ ΤΟΥ EXCEL ΜΑΣ
df = pd.read_excel('data.xlsx',0)
#ΔΗΜΙΟΥΡΓΙΑ ΓΙΑ ΚΑΘΕ ΣΤΗΛΗ ΠΟΣΟΣΤΟΥ ΜΗΔΕΝΙΚΩΝ ΤΙΜΩΝ
percent_missing = df. isnull(). sum() * 100 / len(df)
#ΔΗΜΙΟΥΡΓΙΑ ΤΟΥ MESSAGE BOX ΓΙΑ ΤΗΝ ΕΜΦΑΝΙΣΗ ΤΟΥΣ
easygui.msgbox(str(percent_missing),title="PERCENT OF VALUES THAT ARE NULL" )
#ΔΗΜΙΟΥΡΓΙΑ LOOP ΓΙΑ ΤΟΝ ΕΛΕΓΧΟ ΚΑΘΕ ΣΤΗΛΗΣ ΓΙΑ LOOP ΤΙΜΕΣ
for y in df.columns:
    #ΕΛΕΓΧΟΣ ΑΝ Η ΣΤΗΛΗ ΜΕ ΜΗΔΕΝΙΚΕΣ ΤΙΜΕΣ ΑΠΟΤΕΛΕΙ ΣΤΗΛΗ ΜΕ ΑΡΙΘΜΗΤΙΚΑ ΔΕΔΟΜΕΝΑ
    if(df[y].dtype == np.float64 or df[y].dtype == np.int64):
      #ΕΛΕΓΧΟΣ ΑΝ Η ΣΤΗΛΗ ΕΧΕΙ ΜΗΔΕΝΙΚΕΣ ΤΙΜΕΣ
      if df.isnull().values.any() is True:
          #ΓΕΜΙΣΜΑ ΜΗΔΕΝΙΚΩΝ ΤΙΜΩΝ ΜΕ ΤΟΝ ΜΕΣΟ ΟΡΟ ΤΗΣ ΣΤΗΛΗΣ
          df.fillna(df.mean())
#ΔΙΑΛΕΓΟΥΜΕ ΤΙΣ ΣΤΗΛΕΣ ΠΟΥ ΘΑ ΔΗΜΙΟΥΡΓΗΣΟΥΜΕ ΤΟ ΔΙΑΓΡΑΜΜΑ ΔΙΑΣΠΟΡΑΣ
x = df.loc[:,'Unnamed: 0']
y = df.loc[:,'Views Until Now']
#ΒΑΖΟΥΜΕ ΤΙΤΛΟ ΣΤΟ ΔΙΑΓΡΑΜΜΑ
plt.title("ΔΙΑΓΡΑΜΜΑ ΔΙΑΣΠΟΡΑΣ ΤΩΝ VIEWS ΜΕ ΤΟΝ ΑΥΞΟΝΤΑ ΑΡΙΘΜΟ ΤΟΥΣ")
#ΒΑΖΟΥΜΕ ΤΙΤΛΟ ΣΤΟΝ ΑΞΟΝΑ Χ
plt.xlabel("ΑΥΞΟΝΤΑΣ ΑΡΙΘΜΟΣ")
#ΒΑΖΟΥΜΕ ΤΙΤΛΟ ΣΤΟΝ ΑΞΟΝΑ Υ
plt.ylabel("Views Until Now")
#ΔΗΛΩΝΟΥΜΕ ΤΙΣ ΣΤΗΛΕΣ ΠΟΥ ΘΑ ΔΗΜΙΟΥΡΓΗΣΟΥΜΕ ΤΟ ΔΙΑΓΡΑΜΜΑ ΔΙΑΣΠΟΡΑΣ
plt.scatter(x,y)
#ΑΝΟΙΓΟΥΜΕ ΤΟ ΔΙΑΓΡΑΜΜΑ ΜΕ matplotlib
plt.show()

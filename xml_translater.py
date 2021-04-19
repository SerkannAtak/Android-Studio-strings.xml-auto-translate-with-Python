# Serkan Atak
import re
import numpy as np
from googletrans import Translator

translator = Translator()
content = open("strings.xml").read() #open your file
remove_trans, values, translated_texts, translated_all = [], [], [], []

all_strings = re.findall('<string name="(.*)">(.*)</string>', content) #Get ID and values
strings_with_transFalse = re.findall('<string name="(.*)" translatable="false">(.*)</string>', content) #Get ID and values

for i in range(all_strings.__len__()): # finding the translatable="false" strings
    for k in range(strings_with_transFalse.__len__()):
        if all_strings[i][1] == strings_with_transFalse[k][1]:
            remove_trans.append(all_strings[i]) #The translatable="false" strings

for i in range(remove_trans.__len__()): # Removing the translatable="false" strings
    all_strings.remove(remove_trans[i])

for i in range(all_strings.__len__()):
    values.append(all_strings[i][1]) # Get just values

for k in range(values.__len__()):
    translation = translator.translate(str(values[k]), src='en', dest='tr') # Translate the value dest = "language code you want to translate"
    translated_texts.append(translation.text) # Put translated value in array

for m in range(all_strings.__len__()):
            temp = "<string name=\"" + all_strings[m][0] + "\">" +  translated_texts[m] + "</string>" # Recrate the string value with ID
            translated_all.append(temp) # Put the string value in array

with open("string.xml", "w", encoding="utf-8") as txt_file: #Name your file
    txt_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?> \n")
    txt_file.write("<resources>\n")
    for line in translated_all:
        temp = line.replace("\ n", "\\" + "n") #
        temp = temp.replace("\ N", "\\" + "n") # \n and \' fixing
        temp = temp.replace("'", "\\" + "'")   #
        txt_file.write("\t" + temp + "\n")
    txt_file.write("</resources>")

# -*- coding: utf-8 -*-
"""
Spyder Editor

Rather hastily coded, had to create a new virtual environment for spider as there was a bug with 5.1.5 regarding user input
at least on Ubuntu.
"""
#morse-code command line, rather than backing the morse in I load a pandas DF

import pandas as pd

to_be_coded = input("Hey User enter your text!\n").upper()


morse_code = pd.read_csv("morse.txt", names=["AlphNum", "Morse"])
morse_dict = morse_code.set_index("AlphNum").to_dict()
encoded = ""
for i in to_be_coded:
    if morse_dict["Morse"].get(i):
        encoded += morse_dict["Morse"][i]
    else:
        encoded += i
        
        
        
        
        
        
    

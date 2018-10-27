# inconsistent use of tabs and spaces in indentation

# With the IDLE editor you can use this:

# Menu Edit → Select All
# Menu Format → Untabify Region
# Assuming your editor has replaced 8 spaces with a tab, enter 8 into the input box.
# Hit select, and it fixes the entire document.

import urllib.request

def html(txt):
        x = ""
        x = x + "<!DOCTYPE HTML>" + "\n"
        x = x + "<html>" + "\n"
        x = x + '<meta charset="utf-8">' + "\n"
        x = x + txt
        x = x + "</html>" + "\n"
        return x

def head(func):
        def inner(url):
                txt = ""
                txt = txt + "<head>" + "\n"
                txt = txt + "<title>" + func(url) + "</title>" + "\n" 
                txt = txt + func(url) + "\n"
                txt = txt + "</head>" + "\n"
                return txt
        return inner
        
def body(func):
        def inner(url, imageurl, alttxt):
                txt = ""
                txt = txt + "<body>" + "\n"
                txt = txt + "<i>" + "\n"
                txt = txt + "<pre>" + "\n"
                txt = txt + func(url) + "\n"
                txt = txt + "</pre>" + "\n"
                txt = txt + "</i" + "\n"
##                txt = txt + "<p><img src='http://dfedorov.spb.ru/python/files/tutchev.jpg' alt='Портрет ﻿Федора Тютчева'></p>" + "\n"
                txt = txt + "<p><img src='" + imageurl + "' alt='" + alttxt + "'></p>" + "\n"
                txt = txt + "</body>" + "\n"
                
                return txt
        return inner
            
def readfirstline(url):
        try:
                with urllib.request.urlopen(url) as webpage:
                        for line in webpage:
                                line = line.strip()
                                line = line.decode('utf-8')
                                break
                return line
        except:
                print ("Error opening file:" + url)
                return ""

def readlinesexcept1st(url):
        i=0
        txt = ""
        try:
                with urllib.request.urlopen(url) as webpage:
                        for line in webpage:
                                if i==0:
                                        i=i+1
                                else:
                                        line = line.strip()
                                        if len(line)>0:
                                                line = line.decode('utf-8') + "\n"
                                                txt = txt  + line
                return txt
        except:
                print ("Error opening file: " + url)
                return ""
                
def writetofile(txt):
        with open("xx.html", 'w', encoding='utf-8') as output_file:
                output_file.write(txt)

                
def buildhtml(url, imageurl, alttxt):
        new_headertitle = head(readfirstline)
        new_bodytxt = body(readlinesexcept1st)
        txt = new_headertitle(url) + new_bodytxt(url, imageurl, alttxt)

        # print (html(txt))

        writetofile(html(txt))
        

buildhtml("http://dfedorov.spb.ru/python/files/tutchev.txt", "http://dfedorov.spb.ru/python/files/tutchev.jpg", "Портрет ﻿Федора Тютчева")

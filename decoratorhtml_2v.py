# inconsistent use of tabs and spaces in indentation

# With the IDLE editor you can use this:

# Menu Edit → Select All
# Menu Format → Untabify Region
# Assuming your editor has replaced 8 spaces with a tab, enter 8 into the input box.
# Hit select, and it fixes the entire document.

import urllib.request
import copy
import sys
import traceback

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
        def inner(lines, imageurl, alttxt):
                txt = ""
                txt = txt + "<body>" + "\n"
                txt = txt + "<i>" + "\n"
                txt = txt + "<pre>" + "\n"
                txt = txt + func(lines) + "\n"
                txt = txt + "</pre>" + "\n"
                txt = txt + "</i" + "\n"
                txt = txt + "<p><img src='" + imageurl + "' alt='" + alttxt + "'></p>" + "\n"
                txt = txt + "</body>" + "\n"
                
                return txt
        return inner
            
def readfirstline(lists):
        return lists[0]

def readlinesexcept1st(lines):
        txt = ""
        newlines = lines.copy()
        del newlines[0]
        for line in newlines:
                txt = txt + line + "\n"
        return txt

def readlines(url):
        i=0
        declines = []
        try:
                with urllib.request.urlopen(url) as webpage:
                        lines = webpage.readlines()
                        #.decode('utf-8-sig')
                        #print (webpage.headers.getheader('Content-Type'))
                        #print (webpage.info().get_content_charset())
                for line in lines:
                        line = line.decode('utf-8-sig')
                        lines[i] = line.strip()
                        i = i + 1
   
                return lines
        except:
                print ("Error opening file: " + url)
                return []
def readurl(url):
        i=0
        declines = []
        try:
                
                with urllib.request.urlopen(url) as webpage:
                        txt = webpage.read().decode('utf-8-sig')
                lines = txt.replace("\n", "").split("\r")
                return lines
        except Exception as e:
                # Get current system exception
                ex_type, ex_value, ex_traceback = sys.exc_info()

                # Extract unformatter stack traces as tuples
                trace_back = traceback.extract_tb(ex_traceback)
##                print (trace_back)
                # Format stacktrace
                stack_trace = list()
                
##                print ("---------->")
##                for trace in trace_back:
##                        print (trace)
##                        print (trace[0])
##                        print (trace[1])
##                        print (trace[2])
##                        print (trace[3])
##                print ("<----------")
                
                for trace in trace_back:
                        stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
                        break
                
                print("Exception type : %s " % ex_type.__name__)
                print("Exception message : %s" %ex_value)
                print("Stack trace : %s" %stack_trace)
                return []

        
def writetofile(txt):
        with open("xx1.html", 'w', encoding='utf-8') as output_file:
                output_file.write(txt)

                
def buildhtml(url, imageurl, alttxt):
        #lines = readlines(url)
        lines = readurl(url)
        new_headertitle = head(readfirstline)
        new_bodytxt = body(readlinesexcept1st)
        txt = new_headertitle(lines) + new_bodytxt(lines, imageurl, alttxt)

##        print (html(txt))

        writetofile(html(txt))


##errlst = ["<FrameSummary file D:\SG\PythonSamples\decoratorhtml_2v.py, line 83 in readurl>", "<FrameSummary file D:\APPS\Python37\lib\\urlib\request.py, line 222 in urlopen>"]
##for x in errlst:
##        print (x[0])
##          ##"<FrameSummary file D:\APPS\Python37\lib\urllib\request.py, line 222 in urlopen>","<FrameSummary file D:\APPS\Python37\lib\urllib\request.py,line 531 in open>","<FrameSummary file D:\APPS\Python37\lib\urllib\request.py, line 641 in http_response>","<FrameSummary file D:\APPS\Python37\lib\urllib\request.py, line 569 in error>","<FrameSummary file D:\APPS\Python37\lib\urllib\request.py, line 503 in _call_chain>","<FrameSummary file D:\APPS\Python37\lib\urllib\request.py, line 649 in http_error_default>"]        
##print (errlst)
url = "http://dfedorov.spb.ru/python/files/tutchev.txt"
##readurl(url)
buildhtml(url, "http://dfedorov.spb.ru/python/files/tutchev.jpg", "Портрет ﻿Федора Тютчева")

import urllib.request
import copy
import sys
import traceback

def f1():
    try:
        f2()
    except:
        #traceback.print_exc(file=sys.stdout, limit=1)
        traceback.print_exc(file=sys.stdout) 
def f2():
    f3()

def f3():
    x = 1/0
       

    
def exceprtionexample():
    try:
        x = 1/0
    except:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()
        
        traceback.print_exc(file=sys.stdout)
        print("1.==================")
        traceback.print_exception(ex_type, ex_value, ex_traceback, limit=2, file=sys.stdout)
        print("2.==================")

        print (ex_traceback)
        
        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)  # FrameSummary Objects
        print (trace_back)
        
        print ("---------->")
        for trace in trace_back:        # trace is a FrameSummary object
                print (trace)
                print (trace.filename)  # trace[0]
                print (trace.lineno)    # trace[1]
                print (trace.name)      # trace[2]
                print (trace.line)      # trace[3]
        print ("<----------")
        # Format stacktrace
        stack_trace = list()        
        for trace in trace_back:
                stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
                break
        
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#f1()
exceprtionexample()
    

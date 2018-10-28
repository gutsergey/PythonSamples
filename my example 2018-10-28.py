Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> abs(-9)
9
>>> abs(-1,2)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    abs(-1,2)
TypeError: abs() takes exactly one argument (2 given)
>>> abs(1.2)
1.2
>>> j1
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    j1
NameError: name 'j1' is not defined
>>> 1j
1j
>>> abs(1j)
1.0
>>> help pow
SyntaxError: invalid syntax
>>> help pow()
SyntaxError: invalid syntax
>>> help(pow)
Help on built-in function pow in module builtins:

pow(x, y, z=None, /)
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> i=3
>>> j=3
>>> k=4-1
>>> id(i)
8791146812512
>>> id(j)
8791146812512
>>> id(k)
8791146812512
>>> n=5000000
>>> m=5000000
>>> id(n)
50822448
>>> id(m)
50822512
>>> def convert_to_cels(fahren):
	return (fahren-32) * 5/9

>>> id(convert_to_cels)
50987080
>>> convert_to_cels(80.8)
27.11111111111111
>>> def f(x):
	print(id(x))
	x = 2 * x
	return x

>>> x = 1
>>> id(x)
8791146812448
>>> x = f(x + 1) + f(x + 2)
8791146812480
8791146812512
>>> 
========== RESTART: D:/SG/PythonSamples/test_func_and_their_ids.py ==========
8791146812448
Traceback (most recent call last):
  File "D:/SG/PythonSamples/test_func_and_their_ids.py", line 11, in <module>
    x = f(x + 1) + f(x + 2)
  File "D:/SG/PythonSamples/test_func_and_their_ids.py", line 2, in f
    print("1.x=" + x)
TypeError: can only concatenate str (not "int") to str
>>> 
========== RESTART: D:/SG/PythonSamples/test_func_and_their_ids.py ==========
8791146812448
1.x=2
8791146812480
8791146812544
2.x=4
1.x=3
8791146812512
8791146812608
2.x=6
8791146812736
>>> 53//10
5
>>> -53//10
-6
>>> -6*10
-60
>>> 53%10
3
>>> -53%10
7
>>> -(53//10)
-5
>>> -53/10
-5.3
>>> _
-5.3
>>> 0 and 8
0
>>> 8 and 0
0
>>> 6 and 8
8
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> q="123456"
>>> q
'123456'
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> q.isnumeric()
True
>>> lst1=[4,5,5,6,7,8]
>>> lst2=[5,6]
>>> if lst2 in lst1:
	print("ok")

	
>>> if 5 in lst1:
	print("ok")

	
ok
>>> lst1[1]
5
>>> lst1[1:2]
[5]
>>> lst3=lst1[:]
>>> lst3
[4, 5, 5, 6, 7, 8]
>>> lst[1]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    lst[1]
NameError: name 'lst' is not defined
>>> lst1
[4, 5, 5, 6, 7, 8]
>>> lst3[2]=8
>>> lst3
[4, 5, 8, 6, 7, 8]
>>> lst1
[4, 5, 5, 6, 7, 8]
>>> s=range(0,10)
>>> s
range(0, 10)
>>> or n in range(0,10)
SyntaxError: invalid syntax
>>> for n in range(0,10):
	print(n)

	
0
1
2
3
4
5
6
7
8
9
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1,11,2))
[1, 3, 5, 7, 9]
>>> list(range(11,1,-2))
[11, 9, 7, 5, 3]
>>> list(range(11,1))
[]
>>> list(range(11,1,-1))
[11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> total=0
>>> for i in range(1,101):
	total+=1

	
>>> total
100
>>> total
100
>>> total
100
>>> total=0
>>> for i in range(1,101):
	total = total + 1

	
>>> total
100
>>> total=0
>>> or i in range(1,101):
	total+=i
	
SyntaxError: invalid syntax
>>> or i in range(1,101):
	total+=i
	
SyntaxError: invalid syntax
>>> for i in range(1,101):
	total+=i

	
>>> total
5050
>>> sum(list(range(1,101)))
5050
>>> v=[4,10,5,7.5,-5.9]
>>> for i in range(len(v)):
	print("v[", i, "]", "=", v[i])

	
v[ 0 ] = 4
v[ 1 ] = 10
v[ 2 ] = 5
v[ 3 ] = 7.5
v[ 4 ] = -5.9
>>> 
>>> 
>>> def hisogram(s):
	d = disct()
	for c in s:
		if c not in d:
			d[c] = 1
			else:
				
SyntaxError: invalid syntax
>>> def hisogram(s):
	d = disct()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[s] += 1
	return d

>>> histogram("qwertyqwertyqwerty12345")
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    histogram("qwertyqwertyqwerty12345")
NameError: name 'histogram' is not defined
>>> def histogram(s):
	d = disct()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[s] += 1
	return d

>>> histogram("qwertyqwertyqwerty12345")
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    histogram("qwertyqwertyqwerty12345")
  File "<pyshell#113>", line 2, in histogram
    d = disct()
NameError: name 'disct' is not defined
>>>  def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[s] += 1
	return d
SyntaxError: unexpected indent
>>> 
>>> def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[s] += 1
	return d

>>> histogram("qwertyqwertyqwerty12345")
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    histogram("qwertyqwertyqwerty12345")
  File "<pyshell#118>", line 7, in histogram
    d[s] += 1
KeyError: 'qwertyqwertyqwerty12345'
>>> def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

>>> histogram("qwertyqwertyqwerty12345")
{'q': 3, 'w': 3, 'e': 3, 'r': 3, 't': 3, 'y': 3, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1}
>>> 
================= RESTART: D:/SG/PythonSamples/histogram.py =================
{'q': 3, 'w': 3, 'e': 3, 'r': 3, 't': 3, 'y': 3, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1}
>>> import dis
>>> dis.dis("a=7")
  1           0 LOAD_CONST               0 (7)
              2 STORE_NAME               0 (a)
              4 LOAD_CONST               1 (None)
              6 RETURN_VALUE
>>> s=36
>>> import sys
>>> sys.getrefcount(s)
15
>>> s12=3
>>> sys.getrefcount(s12)
140
>>> 

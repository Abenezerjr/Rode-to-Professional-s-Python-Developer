import re

"""
Regular Expressions

In computing, a regular expression, also referred to as "regex" or "regexp", provides a concise and flexible means
for matching strings of text, such as particular characters, words, or patterns of characters. A regular expression
is written in a formal language that can be interpreted by a regular expression processor
   ^ Matches the beginning of the a line
   $ Matches the end of the a line
   .  Matches any character
   \s  Matches whitespace 
    \S Matches any non-whitespace character
   * Repeats a character zero or more times 
   *? Repeats a character zero or more times (non-greedy) 
   + Repeats a character one or more times. 
   +? Repeats a character one or more times (non-greedy) 
   [aeiou] Matches a single character in the listed set 
   [^XYZ] Matches a single character not in the listed set 
   [ a-z0-9] The set of characters can include a range 
   ( Indicates where string extraction is to start
   ) Indicates where string extraction is to end


"""

text = 'The rain in Spain'
x = re.search("^The.*Spain$", text)
print(x)

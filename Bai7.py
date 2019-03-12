def  remove_dollar_sign (s):
     new_string = s.replace("$","")
     return new_string

user_input = input ("Enter string with $: ")
print ( remove_dollar_sign (user_input))
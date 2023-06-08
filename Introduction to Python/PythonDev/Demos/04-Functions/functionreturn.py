def display_message(msg):
  print(msg)

def generate_hyperlink(href, text):
  return "<a href={0}>{1}</a>".format(href, text)

def get_number_in_range(msg, lower, upper):
  while True:
    num = int(input(msg))
    if num >= lower and num < upper:
      return num


# Usage (i.e. client code)
result1 = display_message("Hello world")
print("result1 is %s" % result1)

result2 = generate_hyperlink("http://www.bbc.co.uk", "BBC")
print("result2 is %s" % result2)

result3 = get_number_in_range("Favourite month? ", 1, 13)
print("result3 is %s" % result3)

#define functions for operations
def add():
  print("This is addition function");
  no1 = int(input('First Number:'));
  no2 = int(input('Second Number:'));
  return no1+no2;

def substract():
  print("This is substract function");
  no1 = int(input('First Number:'));
  no2 = int(input('Second Number:'));
  return no1-no2;

def multiply():
  print("This is multiply function");
  no1 = int(input('First Number:'));
  no2 = int(input('Second Number:'));
  return no1*no2;

def division():
  print("This is division function");
  no1 = int(input('First Number:'));
  no2 = int(input('Second Number:'));
  return no1/no2;

def square():
  print("This is square function");
  no = int(input('Number:'));
  return no**2;

print ("Welcome to Manasyu's calculator");
for x in range(3):
  op = input("What calculation you want to perform? ");
  if op == "add":
    print ("Answer:",add());
  elif op == "substract":
    print ("Answer:",substract());
  elif op == "division":
    print ("Answer:",division());
  elif op == "square":
    print ("Answer:",square());
  elif op == "exit":
    break
  else :
    print ("Unsupported operation, keep tuned for updates");
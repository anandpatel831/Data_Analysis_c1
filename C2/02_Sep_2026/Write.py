# with open("python.txt","r+") as f:
#      print("the file content:")
#      print(f.read())
#      f.seek(5)
#      f.write("\n this is seek() of python file handling.")
#      with open("python.txt","r") as f:
#        print(f.read())

lines=[
    "Till now we have covered data types,operator,function using.\n",
    "We are learning for 2 sessions for 5-days a week as a hands-on.\n",
    "This partical session will help students for theirfinal project building."
]
with open("python.txt","w") as f:

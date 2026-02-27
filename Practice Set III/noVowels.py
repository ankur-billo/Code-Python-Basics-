sentence = "Hello I am new to python and am learning to find vowels in it"
sum =0 
vowels =['a','e','i','o','u']
for char in sentence.lower():  #coz it doesn't check capitalize letter
    if(char in vowels):
        sum+=1
print(f"There are {sum} vowels in it")
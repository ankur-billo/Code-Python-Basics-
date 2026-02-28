def marks(**kwargs):
    #kwargs is a dictioary which store key value pairs for all the values passed to marks
    for item in kwargs.keys():
        print (f"The marks of {item} is {kwargs[item]}")
marks(Subham=55,Riya=98,Hiya=9)

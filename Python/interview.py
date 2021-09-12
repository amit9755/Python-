#List = [3,4,7,10,45,32,21,12,34]

def finding_Nnumber(List):
    for i in range(len(List)):
        for j in range(len(List)):
            if List[i] > List[j]:
                List[i], List[j] = List[j], List[i]
    print("Bigest Number in List :{}".format(List[len(List)-1]))
    print("Smallest Number in List :{}".format(List[0]))


#string = "Hello world!! Good evening"
def counting_char_string(string):
    chr_List = []
    numberOfChar_List = []

    for chr in string:
        if chr is not chr_List:
            chr_List.append(chr)
    print(chr_List)


print()

def main():
    #List = [3, 4, 7, 10, 45, 32, 21, 12, 34]
    string = "Hello world!! Good evening"
    counting_char_string(string)
    #finding_Nnumber(List)

if __name__ =="__main__":
    main()



class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class student(Person):
    def __int__(self, id):
        self.id = id
        Person.__init__()


obj_student = student




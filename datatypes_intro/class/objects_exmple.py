# class human:
#     color="white"
#     height=5.11
#     def run(self):
#         print("running.....")
#     def walk(self):
#         print("walking.....")
# sundeep=human()
# print(sundeep.color,sundeep.height)
# sundeep.run()
# sundeep.walk()

# class human:                        #class
#     def __init__(self,c,h):         #constructor
#         self.color=c
#         self.height=h
#         def run(self):
#             print("RUNNING.....")
#             def walk(self):
#                 print("WALKING.....")
# sundeep=human("white",5.11)              #object
# print(sundeep.color,sundeep.height)
# saradhi=human("black",5.6)
# print(saradhi.color,saradhi.height)
# suresh=human("fair",6.2)
# print(suresh.color,suresh.height)
# class human:
#
#     def __init__(self):
#         print("constructor")
#     def run(self):
#         print("running.....")
#     def walk(self):
#         print("walking.....")
# sundeep=human()
# saradhi=human()
# class human:
#     def __init__(self,c,h):
#         self.color=c
#         self.height=h
#         def run(self,n):
#             print(n+" "+"running.....")
#         def walk(self):
#             print("walking.....")
# sundeep=human("white",5.11)
# print(sundeep.color,sundeep.height)
# saradhi=human("black",6.2)
# print(saradhi.color,saradhi.height)
# sundeep.run("sundeep")
# # saradhi.run("saradhi")
# class baseclass:           #inheritence
#     a=10
#     b=100
#     def display(self):
#         print("base class")
# class derivedclass:
#     c=50
#     d=200
#     def show(self):
#         print("derived class")
# bobject=baseclass()
# print(bobject.a,bobject.b)
# bobject.display()
# dobject=derivedclass()
# print(dobject.c,dobject.d)
# dobject.show()
# class baseclass:                          #parent class
#     a=10
#     b=100
#     def display(self):
#         print("base class")
# class derivedclass(baseclass):            #child class
#     c=20
#     d=200
#     def show(self):
#         print("derived class")
# dobject=derivedclass()
# print(dobject.c,dobject.d)
# dobject.show()
# print(dobject.a,dobject.b)
# dobject.display()
# class grandparent:
#     def gpdisplay(self):
#         print("grandparent method")
# class parent(grandparent):
#     def pdisplay(self):
#         print("parent method")
# class child(parent):
#     def cdisplay(self):
#         print("child display")
"""c=child()
c.cdisplay()
c.pdisplay()
c.gpdisplay()
p=parent()
p.pdisplay()
p.gpdisplay()"""
# gp=grandparent()
# gp.gpdisplay()
# class parent:
#     def pdisplay(self):
#         print("parent class")
# class son(parent):
#     def sdisplay(self):
#         print("son class")
# class daughter(parent):
#     def ddisplay(self):
#         print("daughter class")
# s=son()
# s.sdisplay()
# s.pdisplay()
# d=daughter()
# d.ddisplay()
# d=pdisplay()
# p=parent()
# p.pdisplay()
# class father:
#     def fdisplay(self):
#         print("father class")
# class mother:
#     def mdisplay(self):
#         print("mother class")
# class child(father,mother):
#     def cdisplay(self):
#         print("child class")
# c=child()
# c.cdisplay()
# c.fdisplay()
# c.mdisplay()
class demo:
    def add(self,a=100,b=500,c=100):
      print(a+b+c)
obj=demo()
obj.add(200)
obj.add(100,200)
obj.add(100,200,300)
class parent:
    def transport(self):
        print("cycle")
class child(parent):
    def transport(self):
        print("bike")
c=child()
c.ptransport()
# p=parent()
# p.transport()



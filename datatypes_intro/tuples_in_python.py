# t=('foo','bar','baz','qux','quux','corge')
# t=(1,2,3)
# print(type(t))
# t=(1,'abc',True,1.234)
# print(t)
# t=('foo','bar','baz','qux','quux','corge')
# t[0]='madhu'
# print(t)
# t=('foo','bar','baz','qux','quux','corge',[1,2,3,4])
# t[-1][0]="madhu"
# print(t)
# print(t[0])
# print(t[-1])
#
# print(t[1:4])
# print(t[::-1])
# t=()
# print(type(t))
# l=[]
# print(type(l))
# t=1,'abc',3.14,True
# print(type(t))
# t=(5)
# print(type(t))
# t=("madhu",)
# print(type(t))
# t=tuple([1,2,3])
# print(type(t))
# t=("abc")
# print(tuple(t))
# a=b=c=100
# print(a,b,c)
# a,b,c=100,200,300
# print(a,b,c)
# t=('foo','bar','baz','qux')
# s1,s2,s3,s4=t
# print(s1,s4)
# print(s1)
# t=('foo','bar','baz','qux')
# s1,*s2,s4=t
# print(s1,s4)
# print(s2)

# t=('foo','bar','baz','qux','madhu')
# s1,*s2,s4=t
# print(s1,s2,s4)
#

# name="madhu"
# for i in range(5):
#    print(name*3)
# a=10
# b=20
# # print(a,b)
# a,b=b,a
# print(a,b)
# email_adress="msraju2009@gamil.com"
# print(email_adress.split("@"))
# username,domain_name=email_adress.split("@")
# print(domain_name)
# print(username)

# t=('foo','bar','baz''qux','madhu')
# print(sorted(t))
contacts=[('madhu','+91-9845168660'),('python','+ 1-4343239223928')]
print(contacts[0][1].split("-")[-1])
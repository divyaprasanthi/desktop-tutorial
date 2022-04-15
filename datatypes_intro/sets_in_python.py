# s={}
# print(type(s))
# s=set()
# print(type(s))
# s=set()
# s={'red','green','blue','red'}
# print(s)
# s={1,'abc','1.23',3.14,5+6j,True}
# print(s)
# s={False,'abc','1.23',3.14,5+6j,0}
# print(s)
# print(bool(1))
# print(bool(0))
# s='quux'
# print(set(s))
# s={0,'abc','1.23',3.14,5+6j,1,False}
# print(s)
# s.add('yellow')
# print(s)
# s.update(['purple','black'])
# print(s)
# s={'red','yellow','blue'}
# s.remove('blue')
# print(s)
# s.discard('yellow')
# print(s)
# s.pop()
# print(s)
# x=s.pop()
# print(x)
# clear method
# x1={'foo','ba','baz'}
# x1.clear()
# print(x1)
# print(len(x1))
# x1={'foo','bar','baz'}
# x2={'baz','qux','quux'}
# print(x1.union(x2))
# print(x1/x2)
# a={1,2,3,4}
# b={2,3,4,5}
# c={3,4,5,6}
# d={4,5,6,7}
# print(a.union(b,c,d))
# print(a|b|c|d)
x1={'foo','bar','baz'}
x2={'baz','qux','quux'}
print(x1.intersection(x2))
print(x1&x2)
a={1,2,3,4}
b={2,3,4,5}
c={3,4,5,6}
d={4,5,6,7}
print(a.intersection(b,c,d))
print(a&b&c&d)
a={1,2,3,30,300}
b={10,20,30,40}
c={100,200,300,400}
print(a.difference(b,c))
print(a-b-c)
l1=[11,16,21,26,31,36,41]
l2=[26,41,36]
# print(l1-l2)
print(set(l1)-set(l2))
# print(l1.inrsection(l2))
x1={'foo','bar','baz'}
x2={'baz','qux','quux'}
# print(x1^x2)
# print(x1)
# x1.intersection_update(x2)
# print(x1)
# print(x1.isdisjoint(x2))
superset={'foo','bar','baz','qux','quux'}
# print(x1.issubset(superset))
# print(x3>x1)
# print(x1<x3)
# print(x1==x3)

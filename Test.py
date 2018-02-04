from Lines import Line
from Vector import Vector

"""
myVector = Vector([1,2,3])
print(myVector)
myVector1 = Vector([-1,-2,-3])
myVector2 = Vector([0,0,0])
print(myVector == myVector1)
print(myVector.__eq__(myVector1))
print(myVector.times_scalar(4))
print(myVector.plus(myVector1))

a = Vector([8.218,-9.341])
b = Vector([-1.129,2.111])

c = Vector([7.119,8.215])
d = Vector([-8.223,0.878])

e = Vector([1.671,-1.012,-0.318])
f = 7.41

print(a.plus(b))
print(c.minus(d))
print(e.times_scalar(f))
print(myVector.magnitude())
print(myVector.normalized())
print(myVector.dot(myVector1))

a1 = Vector([-0.221,7.437])
b1 = Vector([8.813,-1.331,-6.247])

print(a1.magnitude())
print(b1.magnitude())

print(Vector([5.581,-2.136]).normalized())
print(Vector([1.996,3.108,-4.554]).normalized())
print(c.angle(d,True))

#example 8
v1 = Vector([7.887,4.138])
w1 = Vector([-8.802,6.776])

v2 = Vector([-5.955,-4.904,-1.874])
w2 = Vector([-4.496,-8.755,7.103])

print(v1.dot(w1))
print(v2.dot(w2))

v3 = Vector([3.183,-7.627])
w3 = Vector([-2.668,5.319])

v4 = Vector([7.35,0.221,5.188])
w4 = Vector([2.751,8.259,3.985])
print(v3.angle(w3))
print(v4.angle(w4,True))
print(myVector.angle(myVector1,True))
#example 9
print('Example #9')
v91 = Vector([-7.579,-7.88])
w91 = Vector([22.737,23.64])

print(v91.angle(w91))
print(pi)
print(v91.parallelism(w91))
print(v91.orthogonal(w91))

v92 = Vector([-2.029,9.97,4.172])
w92 = Vector([-9.231,-6.639,-7.245])

print(v92.parallelism(w92))
print(v92.orthogonal(w92))

v93 = Vector([-2.328,-7.284,-1.214])
w93 = Vector([-1.821,1.072,-2.94])

print(v93.parallelism(w93))
print(v93.orthogonal(w93))

v94 = Vector([2.118,4.827])
w94 = Vector([0,0])

print(v94.parallelism(w94))
print(v94.orthogonal(w94))

#example 10
print('Example #10')

v101 = Vector([3.039,1.879])
w101 = Vector([0.825,2.036])

print(v101.projection_to(w101))

v102 = Vector([-9.88,-3.264,-8.159])
w102 = Vector([-2.155,-9.353,-9.473])
print(v102.orthogonal_to(w102))

v103 = Vector([3.009,-6.172,3.692,-2.51])
w103 = Vector([6.404,-9.144,2.759,8.718])

print(v103.projection_to(w103))
print(v103.orthogonal_to(w103))

#example 11
print('Example #11')

v111 = Vector([8.462,7.893,-8.187])
w111 = Vector([6.984,-5.975,4.778])
print(v111.cross(w111))

v112 = Vector([-8.987,-9.838,5.031])
w112 = Vector([-4.268,-1.861,-8.866])
print(v112.paralleogram_area(w112))

v113 = Vector([1.5,9.547,3.691])
w113 = Vector([-6.007,0.124,5.772])
print(v113.triangle_area(w113))

v114 = Vector([8.462,7.893,-8.187])
w114 = Vector([0,0,0])
print(v114.cross(w114))
"""


line1 = Line(normal_vector=Vector(['4.046','2.836']),constant_term='1.21')
line2 = Line(normal_vector=Vector(['10.115','7.09']),constant_term='3.025')
print("Intersection Test #1")
print(line1.intersection(line2))

line3 = Line(normal_vector=Vector(['7.204','3.182']),constant_term='8.68')
line4 = Line(normal_vector=Vector(['8.172','4.114']),constant_term='9.883')
print("Intersection Test #2")
print(line3.intersection(line4))

line5 = Line(normal_vector=Vector(['1.182','5.562']),constant_term='6.744')
line6 = Line(normal_vector=Vector(['1.773','8.343']),constant_term='9.525')
print("Intersection Test #3")
print(line5.intersection(line6))
print(line5 == line6)

v93 = Vector(['1.182','5.562'])
w93 = Vector(['1.773','8.343'])
print(v93.is_parallel(w93))
class A:pass
class B:pass
class C(A,B):pass
print(C.__mro__)
class D(B,A):pass
class E(D,B):pass
class F(E, A):pass
print(E.__mro__)
print(F.__mro__)


#多态
class A:
    def run(self):
        print('sss')

class B(A):
    def run(self):
        print('cat')

class B(A):  #先查找子类方法,如果没找到，就去父类中找
    pass

class C(A):
    def run(self):
        print('dog')
   

cat1 = B()
dog1 = C()
cat1.run()
dog1.run()

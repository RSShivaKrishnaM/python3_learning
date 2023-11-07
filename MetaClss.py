class MetaCls(type):
    def __new__(cls, name, bases, attrs):
        if attrs.pop('abstract', False):
            print('Abstract Class', name)
            return super(MetaCls, cls).__new__(cls, name, bases, attrs)
        if 'foo' in attrs and 'bar' in attrs:
            # raise TypeError('Class %s cannot contain both foo and bar'%name)
            print('Normal Class2:',name)
        if 'foo' not in attrs and 'bar' not in attrs:
            raise TypeError('Class %s must provide either a foo attribute or a bar attribute' %name)
        print('Normal Class:',name)
        return super(MetaCls, cls).__new__(cls, name, bases, attrs)
    
class AbsCls(metaclass = MetaCls):
    abstract = True
    
class NormCls(metaclass = MetaCls):
    foo = 42
    bar = 10
    
        
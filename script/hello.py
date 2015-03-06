__metaclass__ = type

import sys; 
if not ".\\" in sys.path:
    sys.path.append(".\\") 
if not 'args' in sys.modules:
    b = __import__('args')
else:
    eval('import args')
    b = eval('reload(args)')


aegs1 = b.modelset();
print aegs1.test1("bfc");

class login():
        def loginName(self, name, password):
            self.name = name
            self.password = password
            if name == 'test' and password == '123456':
                return "SUCCESS"
            else:
                return "FAILED"
        def loginAccess(self):
            return 'SUCCESS'

def ageAdd(x, y):
    return x + y

print ageAdd(5,5);

x = login();
print x.loginName('test', 'test');
print x.loginAccess();
    
name = raw_input('Enter you name:');
print x.loginName('test','1234561');
print name;

lists=[1,2,1];
lists1=[2,3];
lists.extend(lists1);
print lists

string1="bfc"
string2="ss"
print string1 + string2;
print lists1.append(5);

lists.remove(1);
print lists;

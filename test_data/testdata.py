from project.project import Project
import random
import string




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +" "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

Testdata =Project(name=random_string("name",5), discription=random_string("header",5))
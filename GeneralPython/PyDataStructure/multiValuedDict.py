#http://code.activestate.com/recipes/52219-associating-multiple-values-with-each-key-in-a-dic/
#https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s06.html

def repeatedValue():
    # this method allows duplicate values for the same key
    d = dict()
    # To add a key->value pair, do this:
    #d.setdefault(key, []).append(value)

    d.setdefault('a',[]).append('apple')
    d.setdefault('b',[]).append('ball')
    d.setdefault('c',[]).append('cat')
    d.setdefault('a',[]).append('aeroplane')
    d.setdefault('a',[]).append('anar')
    d.setdefault('b',[]).append('balloon')

    #aval = d['a']
    print(d)

    d['a'].remove('apple')

    print(d)

def nonRepeatedValue():
    example = {}
    example.setdefault('a', set()).add('apple')
    example.setdefault('b', set()).add('ball')
    example.setdefault('a', set()).add('ant')
    #example.setdefault('a', set()).add('apple')
    #example.setdefault('c', {})['cat']=1
    #example.setdefault('a', {})['ant']=1
    #example.setdefault('a', {})['apple']=1

    print(example)

    d = example['a']
    print(d)

if __name__ == '__main__':
    #repeatedValue()
    nonRepeatedValue()


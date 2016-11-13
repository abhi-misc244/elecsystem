from elecengpy import elementfile as ef
c = ef.cableclass()
print c
print c.resistance
print c.length
c.printdata()
print '------'
c.changelength('1.0')
#c.changesize(2.5)
print c
print c.resistance
print c.length
c.printdata()

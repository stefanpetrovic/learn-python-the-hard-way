class Parent(object):

	def override(self): 
		print 'Parent override'

class Child(Parent):
	pass


class ChildAltered2(Parent):

	def override(self):
		print 'Child override'
		super(ChildAltered2, self).override()
		print 'Child override after parent'



p = Parent()

c = Child()

c2 = ChildAltered2()

#p.override()

#c.override()

c2.override()

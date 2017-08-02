lines = open("enade.txt").readlines()
NCOL = 23
COD_COL = 1
NAME_COL = 2
SIGLA_COL = 3
GRADE_COL = NCOL - 1

class University:
	def __init__(self, name, sigla):
		self.name = name
		self.grades = []
		if sigla and sigla != "-":
			self.sigla = sigla
		else:
			self.sigla = ""

	def add_grade(self, grade):
		self.grades.append(grade)

	def average_grade(self):
		return sum(self.grades) / self.grades.len()

	def dropdown_name(self):
		return self.name

	def __str__(self):
		return "University(%s, %s)" % (self.name, self.sigla)

unis = {}
for l in lines:
	toks = l.split("\t")
	for i in range(0, len(toks) - 1, NCOL):
		key = toks[i + COD_COL]
		u = unis.get(key, University(toks[i + NAME_COL], toks[i + SIGLA_COL]))
		u.add_grade(toks[i + GRADE_COL])
		unis[key] = u

name_set = {}
for u in unis.values():
	name_set[u.dropdown_name()] = True

out = open("universidades.txt", "w")
for n in sorted(name_set):
	print n
	out.write(str(n) + "\n")



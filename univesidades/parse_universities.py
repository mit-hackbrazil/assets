#!/usr/bin/python
# -*- coding: utf-8 -*-
lines = open("igc.txt").readlines()
NCOL = 16
COD_COL = 1
NAME_COL = 2
SIGLA_COL = 3
GRADE_COL = NCOL - 2

class University:
	def __init__(self, name, sigla):
		self.name = name
		self.grades = []
		if sigla and len(sigla) > 1:
			self.sigla = sigla
		else:
			self.sigla = ""

	def add_grade(self, grade):
		try:
			grade = float(grade)
		except ValueError:
			grade = 0

		self.grades.append(grade)

	def average_grade(self):
		if self.grades:
			return sum(self.grades) / len(self.grades)

		return 0

	def dropdown_name(self):
		if self.sigla:
			return "%s - %s" % (self.sigla, self.name)

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

# add USP

usp = University("UNIVERSIDADE DE SÃO PAULO", "USP");
usp.add_grade(5)
unis[0] = usp

name_set = {}
out = open("universidades.txt", "w")
for u in sorted(unis.values(), key=lambda u: u.dropdown_name()):
	out.write(u.dropdown_name() + "\n")



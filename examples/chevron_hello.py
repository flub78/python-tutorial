#!/usr/bin/python

import chevron

print(chevron.render('Hello, {{ mustache }}!', {'mustache': 'World'}))
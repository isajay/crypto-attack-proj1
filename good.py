#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            `L��eU�����d�Xbl�6��(y6y�wP ,B��NM�v�i̹�a_�?>T2M_��N�6G\0�g�~��$�~4{&��~����ЍF����*e��u�,�%�p��Z�ϗm"""
from hashlib import sha256
hash = sha256(blob).hexdigest()
base = "9458f160adad1fb19e9cbb5ffa4018e903fa09ad28bfa06856e50cc26d053643"
if hash != base:
	print "I mean no harm."
else:
	print "You are doomed!"

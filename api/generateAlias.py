#!/usr/bin/python
#******************************************************************************
# Filename: generateAlias.py
# Purpose:  this code holds the function and library that enable a new alias to
#				be generated for a channel
# Authors:  Abbie Fred
#******************************************************************************
import petname

def create_alias():
	'''
		This function will generate an alias for a user upon the creation of a
		channel.
		The user will be allowed to change their assigned alias by clicking the
		"Generate Alias" button.
		The number input in the Generate method determines how many words are
		included in the alias. This can be changed later if needed.
		Note: Login is required for this function to work.
		
	'''
	user_alias = petname.Generate(2)
	return user_alias

# Diamondback

Diamondback is a Python library that can be used to supplement Amazon Web Service's (AWS) Step Functions.

## Problem
AWS Step Functions are defined with JSON based "Amazon States Language." JSON sucks, it's super verbose, allows no options for variables and, it's totally unreadable with complex state machines. So this package seeks to obfuscate JSON into a much more readable Python library. 

## Solution

Use simple Python code to define your state machine and export it to JSON.


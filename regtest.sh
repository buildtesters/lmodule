#!/bin/bash 
coverage run -m pytest -vra tests/
coverage report -m

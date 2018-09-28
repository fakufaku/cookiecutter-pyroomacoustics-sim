#!/bin/bash

if [ -f "../{{ cookiecutter.script_name }}.py" ]; then
  echo "A file with the same name already exists"
  exit 1
else
  mv {{cookiecutter.script_name }}.py ..
  cd ..
  rmdir {{ cookiecutter.script_name }}
  exit 0
fi

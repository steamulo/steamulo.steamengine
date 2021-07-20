#!/bin/bash

PYTHON_REQUIREMENTS_FILE=requirements.txt

download_galaxy () {
  ansible-galaxy install -r ${CUR_MOL_VENV_DIR}/roles/requirements.yml -p ${CUR_MOL_VENV_DIR}/roles/ --force
}

setup_env () {
  dir=$(basename ${CUR_MOL_VENV_DIR})
  if [[ -d "${CUR_MOL_VENV_DIR}/.virtualenv" ]]
  then
    source ${CUR_MOL_VENV_DIR}/.virtualenv/${dir}/bin/activate
  else
    virtualenv -p `which python3` ${CUR_MOL_VENV_DIR}/.virtualenv/${dir} && source ${CUR_MOL_VENV_DIR}/.virtualenv/${dir}/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r ${CUR_MOL_VENV_DIR}/$PYTHON_REQUIREMENTS_FILE
  fi
}

update_requirements () {
  pip freeze > ${CUR_MOL_VENV_DIR}/$PYTHON_REQUIREMENTS_FILE
}

rebuild_env () {
  deactivate
  rm -rf ${CUR_MOL_VENV_DIR}/.virtualenv
  setup_env
}

if [[ ! -f "venv.sh" ]]; then
  echo "Sourcing must be done in the base directory"
  return 1
fi

CUR_MOL_VENV_DIR=`pwd`
setup_env

echo "############################################################"
echo "Type 'deactivate' to quit venv"
echo "Type 'download_galaxy' to download ansible roles"
echo "Type 'rebuild_env' to update your virtualenv"
echo "############################################################"

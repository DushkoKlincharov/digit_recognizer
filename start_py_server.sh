pip3 install virtualenv
virtualenv env
source env/bin/activate
pip install tensorflow flask pillow scipy
export FLASK_APP=server.py
flask run

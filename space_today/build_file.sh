echo "BUILD START"

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install --force-reinstall -U setuptools
pip install -r requirements.txt

npm i rimraf
npm i --save-dev cross-env

python3 manage.py tailwind build
python3 manage.py collectstatic --noinput

echo "BUILD END"
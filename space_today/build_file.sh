echo "BUILD START"

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install --force-reinstall -U setuptools
pip install -r requirements.txt

npm install rimraf

python3 manage.py tailwind build
python3 manage.py collectstatic --noinput

echo "BUILD END"
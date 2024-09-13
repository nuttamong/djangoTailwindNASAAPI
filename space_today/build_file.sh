echo "BUILD START"

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install --force-reinstall -U setuptools
pip install -r requirements.txt

npm i rimraf
npm i --save-dev cross-env
npm i tailwindcss
npm i --save-dev postcss-import

python3 manage.py tailwind build
python3 manage.py collectstatic --noinput

echo "BUILD END"
echo "Build Start"
sudo apt install python3.9-pip
python3.9 -m pip install psycopg2-binary
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic
echo "Build End"

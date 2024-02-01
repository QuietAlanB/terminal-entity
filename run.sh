which python3.10
if [ $? -eq 0 ]
then
	python3.10 src/main.py
	exit 0
fi

which python3
if [ $? -eq 0 ]
then
	python3 src/main.py
	exit 0
fi

which python
if [ $? -eq 0 ]
then
	python src/main.py
	exit 0
fi

echo "cannot find python on the system (searched for python3.10, python3, python)"
exit 1

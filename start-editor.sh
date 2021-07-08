#! /bin/bash

export FLASK_APP=editor/app.py
export PYTHONPATH=.
export SKF_FLASK_DEBUG='True'
export JWT_ENABLED='False'

python3 editor/app.py 

while :
do
	case "$(ps x |grep -v grep |grep -c "Python skf")" in

	0)  echo "Restarting skf editor:"
	    python3 editor/app.py 
	    ;;
	2)  echo "SKF editor already running"
	    ;;
	esac
done
DOIT_CONFIG = {'default_tasks':['babel', 'doc', 'wheel']}

def task_babel():
	return {
		"actions": ["pybabel update -D gui -i habittracker/po/gui.pot -d habittracker/po -l ru",
					"pybabel compile -D gui -d habittracker/po -l ru"],
		"file_dep": ["habittracker/gui.py"],
		"targets": ["habittracker/po/gui.pot", 
					"habittracker/po/ru/LC_MESSAGES/gui.po",
					"habittracker/po/ru/LC_MESSAGES/gui.mo"]
	}

def task_doc():
	return {
		"actions": ["sphinx-build -M html docs/source docs/build"]
	}


def task_wheel():
	return {
		"actions": ["python3 -m build"]
	}


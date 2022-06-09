DOIT_CONFIG = {'default_tasks': ['babel', 'doc']}


def task_babel():
    return {
            "actions": ["pybabel update -D gui -i habittracker/po/gui.pot -d habittracker/po -l ru",
                        "pybabel compile -D gui -d habittracker/po -l ru"],
            "file_dep": ["habittracker/gui.py"],
            "targets": ["habittracker/po/ru/LC_MESSAGES/gui.po",
                        "habittracker/po/ru/LC_MESSAGES/gui.mo"]
    }


def task_doc():
    return {
            "actions": ["sphinx-build -M html docs/source docs/build"]
    }


def task_sdist():
    # with open('MANIFEST.in', 'r+') as f:
    #     lines = f.readlines()
    #     lines[0] = 'include habittracker/po/ru/LC_MESSAGES/gui.po\n'
    #     f.seek(0)
    #     f.writelines(lines)
    return {
            "actions": ["python3 -m build -s"]
    }


def task_wheel():
    # with open('MANIFEST.in', 'r+') as f:
    #     lines = f.readlines()
    #     lines[0] = 'include habittracker/po/ru/LC_MESSAGES/gui.mo\n'
    #     f.seek(0)
    #     f.writelines(lines)
    return {
            "actions": ["python3 -m build -w"]
    }

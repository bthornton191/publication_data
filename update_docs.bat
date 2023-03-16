cd rst
call make html
cd ..
robocopy rst\build\html docs /e /mir

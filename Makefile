.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: build
build:	
	python -m PyInstaller --onefile --windowed --icon=./Pr/logo.ico --add-data "Pr:Pr" --distpath ./dist --name "coloring cube" --noconfirm main.py

.PHONY: run
run:	
	python main.py
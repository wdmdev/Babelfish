base_setup:
	if [ ! -d "env" ]; then \
		python3 -m venv env; \
		python3 -m pip install --no-cache-dir -r requirements.txt; \
	fi; \
	source env/bin/activate; \
	python3 base_setup.py; \
	deactivate

train:
	source env/bin/activate; \
	python3 train.py --config_path Configs/config.yml; \
	deactivate

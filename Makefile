base_setup:
	python3 -m venv env; \
	source env/bin/activate; \
	python3 -m pip install --no-cache-dir -r requirements.txt; \
	python3 base_setup.py; \
	deactivate

train:
	source env/bin/activate; \
	python3 train.py --config_path Configs/config.yml; \
	deactivate

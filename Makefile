base_setup:
	python -m venv env; \
	source env/bin/activate; \
	pip install -r requirements.txt; \
	python base_setup.py; \
	deactivate

train:
	source env/bin/activate; \
	python train.py --config_path Configs/config.yml; \
	deactivate
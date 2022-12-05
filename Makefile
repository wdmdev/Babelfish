# VCTK setup using the same format as the StarGANv2-VC paper
base_env:
	python3 -m pip install --upgrade pip; \
	python3 -m venv env; \
	source env/bin/activate; \
	python3 -m pip install --no-cache-dir -r requirements.txt; \
	deactivate

base_data:
	source env/bin/activate; \
	python3 base_setup.py; \
	deactivate

babel_split_train:
	source env/bin/activate; \
	python3 train.py --config_path Configs/babelfish_split_config.yml; \
	deactivate

babel_split_multi_train:
	source env/bin/activate; \
	python3 train.py --config_path Configs/babelfish_split_multi_config.yml; \
	deactivate
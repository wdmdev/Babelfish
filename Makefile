# VCTK setup using the same format as the StarGANv2-VC paper
base_setup:
	python3 -m pip install --upgrade pip; \
	python3 -m venv env; \
	source env/bin/activate; \
	python3 -m pip install --no-cache-dir -r requirements.txt; \
	python3 base_setup.py; \
	deactivate

#Emotional speech data setup for English speakers only
english_esd_setup:
	python3 -m pip install --upgrade pip; \
	python3 -m venv env; \
	source env/bin/activate; \
	python3 -m pip install --no-cache-dir -r requirements.txt; \
	python3 english_esd_setup.py; \
	python3 Data/make_esd_data_lists.py; \
	deactivate


#Training as in the StarGANv2-VC paper
base_train:
	source env/bin/activate; \
	python3 train.py --config_path Configs/config.yml; \
	deactivate

#Emotional speech training
esd_train:
	source env/bin/activate; \
	python3 train.py --config_path Configs/esd_config.yml; \
	deactivate

# VCTK setup using the same format as the StarGANv2-VC paper
base_setup:
	if [ ! -d "env" ]; then \
		python3 -m venv env; \
		python3 -m pip install --no-cache-dir -r requirements.txt; \
	fi; \
	source env/bin/activate; \
	python3 base_setup.py; \
	deactivate

#Emotional speech data setup for English speakers only
english_esd_setup:
	if [ ! -d "env" ]; then \
		python3 -m venv env; \
		python3 -m pip install --no-cache-dir -r requirements.txt; \
	fi; \
	source env/bin/activate; \
	python3 esd_setup.py; \
	python3 Data/make_esd_data_lists.py
	deactivate


#Training as in the StarGANv2-VC paper
base_train:
	source env/bin/activate; \
	python3 train.py --config_path Configs/config.yml; \
	deactivate

#Emotional speech training
base_train:
	source env/bin/activate; \
	python3 esd_train.py --config_path Configs/esd_config.yml; \
	deactivate

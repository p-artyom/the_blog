WORKDIR = blog
TEMPLATES-DIR = $(WORKDIR)/templates
MANAGE = python $(WORKDIR)/manage.py

run:
	$(MANAGE) runserver

style:
	black -S -l 79 $(WORKDIR)
	djlint $(TEMPLATES-DIR) --reformat
	isort $(WORKDIR)
	flake8 $(WORKDIR)

super:
	$(MANAGE) createsuperuser

makemig:
	$(MANAGE) makemigrations

mig:
	$(MANAGE) migrate

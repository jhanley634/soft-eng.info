
OUT = blog/asset/pandoc.min.css

SHELL := bash

# Eventually a penultimate entry will be in need of a pair of prev/next links.
CACHE_INVALIDATE = grep -L '^    next' blog/out/20*.html

SERVER_DIR = /var/www/soft-eng.info

all: $(OUT)
	rm -f $(shell $(CACHE_INVALIDATE))
	blog/bin/gen.py
	rsync -av blog/{asset,out/*.html} speedy2.sector6.net:$(SERVER_DIR)/blog/
	rsync -av robots.txt speedy2.sector6.net:$(SERVER_DIR)/

%.min.css: %.css
	minify $<  > $@

TEST_OPT = --tb=native --capture=tee-sys

test:
	pytest $(TEST_OPT)

coverage:
	coverage erase
	coverage run -m pytest $(TEST_OPT)
	coverage html
	coverage report

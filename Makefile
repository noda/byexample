# TOC_DIR := toc
# TOC_SOURCES := $(shell find toc -name '*.md')
# TOC_OBJS := $(sort $(TOC_SOURCES:%.md=%.html))

EXAMPLES_SOURCES := $(shell find toc -name '*.md')

all: index energyview selfhost

index: docs/index.html

energyview: docs/energyview

selfhost: docs/selfhost

docs/index.html: toc/index.md
	pandoc -o $@ $^ \
		--template=templates/index \
		--metadata title="NODA by Example"

docs/energyview: toc/energyview.md
	pandoc -o $@ $^ \
		-t html \
		--template=templates/overview \
		--metadata title="EnergyView API by Example"

docs/selfhost: toc/selfhost.md
	pandoc -o $@ $^ \
		-t html \
		--template=templates/overview \
		--metadata title="EnergyView API by Example"

clean:
	rm toc/*.html

.PHONY: docs/index.html docs/energyview docs/selfhost

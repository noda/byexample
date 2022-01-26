# TOC_DIR := toc
# TOC_SOURCES := $(shell find toc -name '*.md')
# TOC_OBJS := $(sort $(TOC_SOURCES:%.md=%.html))

MD := mkdir

EXAMPLE_SOURCES := $(shell find examples -name '*.md')
EXAMPLE_OBJS := $(subst examples/,docs/,$(EXAMPLE_SOURCES:.md=.html))
EXAMPLE_DIRS = $(subst /,/,$(sort $(dir $(EXAMPLE_OBJS))))

all: docs index energyview selfhost examples

docs:
	$(MD) -p $(EXAMPLE_DIRS)

index: docs/index.html

energyview: docs/energyview.html

selfhost: docs/selfhost.html

examples: $(EXAMPLE_SOURCES)
	pandoc -o $(subst examples/,docs/,$(^:.md=.html)) $^ \
		--metadata-file=$(shell dirname $^)/metadata.yaml \
		--template=templates/example

docs/index.html: toc/index.md
	pandoc -o $@ $^ \
		--template=templates/index \
		--metadata title="NODA by Example"

docs/energyview.html: toc/energyview.md
	pandoc -o $@ $^ \
		--template=templates/overview \
		--metadata title="EnergyView API by Example"

docs/selfhost.html: toc/selfhost.md
	pandoc -o $@ $^ \
		--template=templates/overview \
		--metadata title="EnergyView API by Example"

clean:
	rm toc/*.html

.PHONY: docs docs/index.html docs/energyview.html docs/selfhost.html $(EXAMPLE_SOURCES)

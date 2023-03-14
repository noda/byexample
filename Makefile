MD := mkdir

EXAMPLE_SOURCES := $(shell find examples -name '*.md')
EXAMPLE_OBJS := $(subst examples/,docs/,$(EXAMPLE_SOURCES:.md=.html))
EXAMPLE_DIRS = $(subst /,/,$(sort $(dir $(EXAMPLE_OBJS))))
EXAMPLE_TARGETS := $(patsubst examples/%.md,docs/%.html,$(EXAMPLE_SOURCES))

all: docs index examples

docs:
	$(MD) -p $(EXAMPLE_DIRS)

examples: $(EXAMPLE_TARGETS)

# "loop" all examples and run byexample-page.py on each
docs/%.html: examples/%.md
	python byexample-page.py $^ $@

docs/index.html: $(EXAMPLE_SOURCES)
	python byexample-index.py examples > $@

# examples: $(EXAMPLE_SOURCES)
# 	python byexample-page.py $^ $(subst examples/,docs/,$(^:.md=.html))

# docs/index.html: toc/index.md
# 	pandoc -o $@ $^ \
# 		--template=templates/index \
# 		--metadata title="NODA by Example"

clean:
	rm toc/*.html

.PHONY: docs docs/index.html docs/energyview.html docs/selfhost.html $(EXAMPLE_SOURCES)

EXAMPLE_SOURCES := $(shell find examples -name '*.md')
EXAMPLE_OBJS := $(subst examples/,docs/,$(EXAMPLE_SOURCES:.md=.html))
EXAMPLE_DIRS := $(sort $(dir $(EXAMPLE_OBJS)))
EXAMPLE_TARGETS := $(patsubst examples/%.md,docs/%.html,$(EXAMPLE_SOURCES))
EXAMPLE_JS := $(shell find js -name '*.js')
EXAMPLE_JS_TARGETS := $(patsubst js/%.js,docs/js/%.js,$(EXAMPLE_JS))
EXAMPLE_CSS := $(shell find css -name '*.css')
EXAMPLE_CSS_TARGETS := $(patsubst css/%.css,docs/css/%.css,$(EXAMPLE_CSS))
EXAMPLE_IMAGES := $(shell find images -name '*.png')
EXAMPLE_IMAGES_TARGETS := $(patsubst images/%.png,docs/images/%.png,$(EXAMPLE_IMAGES))
TEMPLATE_INDEX := $(shell find templates -name 'index.html')
TEMPLATE_EXAMPLE := $(shell find templates -name 'example.html')

all: docs examples index

docs: $(EXAMPLE_DIRS) docs/css docs/js docs/images docs/CNAME $(EXAMPLE_JS_TARGETS) $(EXAMPLE_CSS_TARGETS) $(EXAMPLE_IMAGES_TARGETS)

$(EXAMPLE_DIRS):
	mkdir -p $@

docs/CNAME:
	echo -n byexample.noda.se > $@

docs/css:
	mkdir -p $@

docs/js:
	mkdir -p $@

docs/images:
	mkdir -p $@

docs/css/%.css: css/%.css
	cp $^ $@

docs/js/%.js: js/%.js
	cp $^ $@

docs/images/%.png: images/%.png
	cp $^ $@

examples: $(EXAMPLE_TARGETS)

index: docs/index.html

# "loop" all examples and run byexample-page.py on each
docs/%.html: examples/%.md $(TEMPLATE_EXAMPLE) | docs
	python byexample-page.py $< $@

docs/index.html: $(EXAMPLE_SOURCES) $(TEMPLATE_INDEX) | docs
	python byexample-index.py examples > $@

clean:
	rm -rf docs/*.html
	rm -rf docs/js
	rm -rf docs/css
	rm -rf docs/CNAME
	rm -rf $(EXAMPLE_TARGETS)

.PHONY: all clean docs/CNAME docs/css docs/js docs/images docs/index.html

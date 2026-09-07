.PHONY: all clean

RAW_FILES := $(wildcard *.raw)
PROCESSED := $(RAW_FILES:.raw=.up)

all: $(PROCESSED)

%.up: %.raw
	tr '[:lower:]' '[:upper:]' < $< > $@

clean:
	rm -f *.up

SRC = src
OUT := enron.css
SASSC := sass --stop-on-error

all: build

build: $(OUT)

$(OUT): $(SRC)/enron/*.scss
	$(SASSC) $(SRC)/enron/_index.scss $@

clean:
	rm -f $(OUT) $(OUT).map

.PHONY: all build clean

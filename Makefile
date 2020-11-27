SRC = src
SASSC := sass --stop-on-error

all: enron.css test/style.css

enron.css: $(SRC)/enron/*.scss
	$(SASSC) $(SRC)/enron/_index.scss $@

test/style.css: $(SRC)/enron/*.scss test/*.scss
	$(SASSC) test/style.scss $@ -I $(SRC)

clean:
	rm -f enron.css enron.css.map
	rm -f test/style.css

.PHONY: all build clean

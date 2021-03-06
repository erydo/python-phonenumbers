alldata: metadata geodata locale

# Dump the JRE's Locale information
DumpLocale.class: DumpLocale.java
	javac $<

phonenumbers/geodata/locale.py: DumpLocale.class
	java DumpLocale > $@

locale: phonenumbers/geodata/locale.py

phonenumbers/geodata/__init__.py: buildgeocodingdata.py ../resources/geocoding
	python buildgeocodingdata.py ../resources/geocoding $@

tests/testgeodata/__init__.py: buildgeocodingdata.py ../resources/test/geocoding
	python buildgeocodingdata.py ../resources/test/geocoding $@

geodata: phonenumbers/geodata/__init__.py tests/testgeodata/__init__.py

phonenumbers/data/__init__.py: ../resources/PhoneNumberMetaData.xml buildmetadatafromxml.py
	python buildmetadatafromxml.py ../resources/PhoneNumberMetaData.xml phonenumbers/data

metadata: phonenumbers/data/__init__.py tests/testdata/__init__.py geodata

tests/testdata/__init__.py:  ../resources/PhoneNumberMetaDataForTesting.xml buildmetadatafromxml.py
	python buildmetadatafromxml.py ../resources/PhoneNumberMetaDataForTesting.xml tests/testdata

test: alldata tests/testdata/__init__.py
	python phonenumbers/__init__.py
	python phonenumbers/re_util.py
	python phonenumbers/unicode_util.py
	python phonenumbers/geocoder.py
	python tests/__init__.py

# Coverage; requires coverage module
COVERAGE=$(shell hash python-coverage 2>&- && echo python-coverage || echo coverage)
COVERAGE_FILES=phonenumbers/*.py
coverage: coverage_clean coverage_generate coverage_report
coverage_clean:
	$(COVERAGE) -e
coverage_generate:
	$(COVERAGE) -x phonenumbers/re_util.py
	$(COVERAGE) -x phonenumbers/unicode_util.py
	$(COVERAGE) -x tests/__init__.py
coverage_report:
	$(COVERAGE) -m -r $(COVERAGE_FILES)
coverage_annotate:
	$(COVERAGE) annotate $(COVERAGE_FILES)

VERSION=$(shell grep __version__ phonenumbers/__init__.py | sed 's/__version__ = "\(.*\)"/\1/')
TARBALL=dist/phonenumbers-$(VERSION).tar.gz
# Build setuptools packaged tarball $(TARBALL)
sdist: alldata
	python setup.py sdist
$(TARBALL): sdist

install: alldata
	python setup.py build
	sudo python setup.py install

clean:
	rm -f MANIFEST *.pyc phonenumbers/*.pyc phonenumbers/data/*.pyc phonenumbers/geodata/*.pyc
	rm -f tests/*.pyc tests/data/*.pyc tests/geodata/*.pyc
	rm -rf build deb_dist dist

distclean: clean
	rm -rf phonenumbers/data tests/testdata
	rm -rf phonenumbers.egg-info
	rm -rf build
	rm -f DumpLocale.class

# Create Debian package.  Requires py2dsc, included in the python-stdeb package.
DEB_VERSION=$(VERSION)-1_all
deb: deb_dist/python-phonenumbers_$(DEB_VERSION).deb

deb_dist/python-phonenumbers_$(VERSION)-1_all.deb: $(TARBALL)
	py2dsc $(TARBALL)
	cd deb_dist/phonenumbers-$(VERSION) && dpkg-buildpackage -us -uc -nc

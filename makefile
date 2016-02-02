#SHELL := /bin/bash
BUILD_DEST=build

CODE_DEST="${BUILD_DEST}/code"
VER_BRANCH=build-release
VER_FILE=VERSION

LITERATE_TOOLS="https://github.com/vlead/literate-tools.git"
LITERATE_DIR=literate-tools
ELISP_DIR=elisp
ORG_DIR=org-templates
STYLE_DIR=style
CODE_DIR=build/code
PWD=$(shell pwd)
LINT_FILE=${PWD}/${CODE_DIR}/lint_output
EXIT_FILE=${PWD}/exit.txt
STATUS=0

all:  build-with-lint

clean-literate:
	rm -rf ${ELISP_DIR}
	rm -rf ${ORG_DIR}
	rm -rf ${STYLE_DIR}
	rm -rf src/${ORG_DIR}
	rm -rf src/${STYLE_DIR}

pull-literate-tools:
	@echo "pulling literate support code"
	echo ${PWD}
ifeq ($(wildcard elisp),)
	@echo "proxy is..."
	echo $$http_proxy
	git clone ${LITERATE_TOOLS}
	mv ${LITERATE_DIR}/${ELISP_DIR} .
	mv ${LITERATE_DIR}/${ORG_DIR} .
	mv ${LITERATE_DIR}/${STYLE_DIR} .
	ln -s ${PWD}/${ORG_DIR}/ ${PWD}/src/${ORG_DIR}
	ln -s ${PWD}/${STYLE_DIR}/ ${PWD}/src/${STYLE_DIR}
	rm -rf ${LITERATE_DIR}
else
	@echo "Literate support code already present"
endif

init: pull-literate-tools
	rm -rf ${BUILD_DEST}
	mkdir -p ${BUILD_DEST} ${CODE_DEST}

build: init write-version
	emacs  --script elisp/publish.el
	rm -f ${BUILD_DEST}/docs/*.html~
	cp -R src/static/ ${BUILD_DEST}/code/src/
	cp -R src/templates/ ${BUILD_DEST}/code/src/

# get the latest commit hash and its subject line
# and write that to the VERSION file
write-version:
	echo -n "Built from commit: " > ${CODE_DEST}/${VER_FILE}
	echo `git rev-parse HEAD` >> ${CODE_DEST}/${VER_FILE}
	echo `git log --pretty=format:'%s' -n 1` >> ${CODE_DEST}/${VER_FILE}

lint:
	pep8 --ignore=E302 ${PWD}/${CODE_DIR} > ${LINT_FILE};

build-with-lint: build lint

clean:  clean-literate
	rm -rf ${BUILD_DEST}


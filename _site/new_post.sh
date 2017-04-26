#!/bin/bash

POSTNAME=$(echo "$@" | sed 's/ /-/g' )
DATE=$(date +%Y-%m-%d)
FILE="_drafts/${DATE}-${POSTNAME}.md"

echo ${FILE}

if [ ! -f "${FILE}" ]
then
    echo "writing template to ${FILE}"
    # write the entry template to a new post
    cat >${FILE} << EOM
---
layout: post
title: $1
tags: []
---
  
  FILL IN POST HERE
EOM
fi

${EDITOR} ${FILE}

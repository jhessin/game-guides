#!/usr/bin/env bash

git reset --hard
git fetch origin
git checkout origin/master
git branch -d master
git checkout -b master origin/master

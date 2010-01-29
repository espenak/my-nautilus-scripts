#!/bin/bash


D=~/.gnome2/nautilus-scripts/Git/
mkdir -p $D
install -t $D \
	Edit\ history \
	Browse\ history \
	Commit\ \(Save\) \
	Create\ repository

install -m 644 -t $D shared.py

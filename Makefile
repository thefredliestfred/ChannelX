# This makefile is meant to clean out pycache files that clutter the ChannelX project

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

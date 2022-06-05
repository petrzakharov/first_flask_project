#!/usr/bin/env bash
flask db migrate
flask db upgrade
flask add_mockup
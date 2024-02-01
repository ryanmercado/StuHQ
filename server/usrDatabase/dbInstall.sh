#!/bin/sh

sudo apt update

sudo apt install sqlite3

# to use db CLI, run 'sqlite3 usrDB.db'
# ask GPT how to interact with SQLite3 CLI if you are lost. (.tables will show all our tables, PRAGMA table_info(tableName) will show all columns in a table, etc.)
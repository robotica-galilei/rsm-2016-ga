#!/bin/sh

pm2 start server/nameserver.py --interpreter="python"
pm2 start server/server.py --interpreter="python"


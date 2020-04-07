#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    web骨架
"""
import logging;logging.basicConfig(level=logging.INFO)
from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
def index(request):
    return web.Response(body=b'<h1>My Web App</h1>', content_type='text/html')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    logging.info('server started at http://127.0.0.1:9257...')
    web.run_app(app, host='127.0.0.1', port=9527)


init()

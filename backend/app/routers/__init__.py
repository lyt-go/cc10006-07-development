"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import streaming as router_streaming
from app.routers import lakeformat as router_lakeformat
from app.routers import compaction as router_compaction
from app.routers import catalog as router_catalog
from app.routers import snapshotmgr as router_snapshotmgr
from app.routers import icebergopt as router_icebergopt
from app.routers import schemareg as router_schemareg
from app.routers import increment as router_increment
from app.routers import filelayout as router_filelayout
from app.routers import coldstore as router_coldstore
from app.routers import databranch as router_databranch
from app.routers import checkpoint as router_checkpoint
from app.routers import watershed as router_watershed
from app.routers import gcpolicy as router_gcpolicy
from app.routers import indexing as router_indexing
from app.routers import tagassign as router_tagassign
from app.routers import accesslog as router_accesslog
from app.routers import failover as router_failover

ROUTERS = [router_streaming, router_lakeformat, router_compaction, router_catalog, router_snapshotmgr, router_icebergopt, router_schemareg, router_increment, router_filelayout, router_coldstore, router_databranch, router_checkpoint, router_watershed, router_gcpolicy, router_indexing, router_tagassign, router_accesslog, router_failover]

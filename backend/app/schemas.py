"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class StreamingEntry(BaseModel):
    """接入流明细结构。"""

    field_0: str | None = None  # 流编号
    field_1: str | None = None  # 数据源类型
    field_2: str | None = None  # 消费组名称
    field_3: str | None = None  # 初始位点
    field_4: str | None = None  # 分区数量
    field_5: str | None = None  # 序列化格式
    field_6: str | None = None  # 水位提交间隔
    field_7: str | None = None  # 异常重启策略

class LakeformatEntry(BaseModel):
    """表格式明细结构。"""

    field_0: str | None = None  # 格式编号
    field_1: str | None = None  # 表名称
    field_2: str | None = None  # 湖格式类型
    field_3: str | None = None  # 主键字段
    field_4: str | None = None  # 分区字段
    field_5: str | None = None  # 排序字段
    field_6: str | None = None  # 文件大小阈值
    field_7: str | None = None  # 压缩算法

class CompactionEntry(BaseModel):
    """合并策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 触发文件数
    field_3: str | None = None  # 触发时间窗口
    field_4: str | None = None  # 合并算法
    field_5: str | None = None  # 并行度
    field_6: str | None = None  # 排序键
    field_7: str | None = None  # 文件保留数

class CatalogEntry(BaseModel):
    """目录条目明细结构。"""

    field_0: str | None = None  # 条目编号
    field_1: str | None = None  # 目录层级
    field_2: str | None = None  # 表名
    field_3: str | None = None  # 列名
    field_4: str | None = None  # 列类型
    field_5: str | None = None  # 分区键
    field_6: str | None = None  # 数据格式
    field_7: str | None = None  # 最近更新

class SnapshotmgrEntry(BaseModel):
    """表快照明细结构。"""

    field_0: str | None = None  # 快照编号
    field_1: str | None = None  # 所属表名
    field_2: str | None = None  # 快照ID
    field_3: str | None = None  # 快照时间
    field_4: str | None = None  # 文件总数
    field_5: str | None = None  # 总记录数
    field_6: str | None = None  # 总大小MB
    field_7: str | None = None  # 过期标记

class IcebergoptEntry(BaseModel):
    """优化计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 优化类型
    field_3: str | None = None  # 目标文件大小
    field_4: str | None = None  # 文件分组策略
    field_5: str | None = None  # 并行度
    field_6: str | None = None  # 优化窗口
    field_7: str | None = None  # 重写策略

class SchemaregEntry(BaseModel):
    """Schema版本明细结构。"""

    field_0: str | None = None  # 版本编号
    field_1: str | None = None  # 主题名称
    field_2: str | None = None  # Schema类型
    field_3: str | None = None  # 兼容策略
    field_4: str | None = None  # Schema定义
    field_5: str | None = None  # 版本号
    field_6: str | None = None  # 注册时间
    field_7: str | None = None  # 废弃时间

class IncrementEntry(BaseModel):
    """增量视图明细结构。"""

    field_0: str | None = None  # 视图编号
    field_1: str | None = None  # 基表名称
    field_2: str | None = None  # 增量字段
    field_3: str | None = None  # 起始快照
    field_4: str | None = None  # 截止快照
    field_5: str | None = None  # 变更类型过滤
    field_6: str | None = None  # 输出列映射
    field_7: str | None = None  # 查询缓存秒

class FilelayoutEntry(BaseModel):
    """布局策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 表名
    field_2: str | None = None  # 分区路径模式
    field_3: str | None = None  # 文件名模板
    field_4: str | None = None  # 文件组大小
    field_5: str | None = None  # 目录层级深度
    field_6: str | None = None  # 隐藏分区键
    field_7: str | None = None  # 过期路径清理

class ColdstoreEntry(BaseModel):
    """分层策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 表名
    field_2: str | None = None  # 热数据天
    field_3: str | None = None  # 温数据天
    field_4: str | None = None  # 冷存储类型
    field_5: str | None = None  # 迁移触发条件
    field_6: str | None = None  # 迁移并行度
    field_7: str | None = None  # 回迁策略

class DatabranchEntry(BaseModel):
    """分支定义明细结构。"""

    field_0: str | None = None  # 分支编号
    field_1: str | None = None  # 分支名称
    field_2: str | None = None  # 源分支名
    field_3: str | None = None  # 分支类型
    field_4: str | None = None  # 创建时间
    field_5: str | None = None  # 创建人
    field_6: str | None = None  # 合并状态
    field_7: str | None = None  # 过期时间

class CheckpointEntry(BaseModel):
    """检查点明细结构。"""

    field_0: str | None = None  # 检查点编号
    field_1: str | None = None  # 关联流编号
    field_2: str | None = None  # 检查点时间
    field_3: str | None = None  # 已处理偏移量
    field_4: str | None = None  # 状态大小KB
    field_5: str | None = None  # 持久化位置
    field_6: str | None = None  # 保留天数
    field_7: str | None = None  # 失败原因

class WatershedEntry(BaseModel):
    """水位标记明细结构。"""

    field_0: str | None = None  # 标记编号
    field_1: str | None = None  # 表名
    field_2: str | None = None  # 分区键值
    field_3: str | None = None  # 数据写入时间
    field_4: str | None = None  # 数据可见时间
    field_5: str | None = None  # 数据延迟秒
    field_6: str | None = None  # 缺失分区数
    field_7: str | None = None  # 补齐状态

class GcpolicyEntry(BaseModel):
    """清理策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 表名
    field_2: str | None = None  # 快照保留数
    field_3: str | None = None  # 数据保留天
    field_4: str | None = None  # 孤立文件清理
    field_5: str | None = None  # 过期分区清理
    field_6: str | None = None  # 清理执行时间
    field_7: str | None = None  # 清理状态

class IndexingEntry(BaseModel):
    """索引定义明细结构。"""

    field_0: str | None = None  # 索引编号
    field_1: str | None = None  # 表名
    field_2: str | None = None  # 索引列
    field_3: str | None = None  # 索引类型
    field_4: str | None = None  # 分桶数量
    field_5: str | None = None  # 数据跳过策略
    field_6: str | None = None  # 布隆过滤列
    field_7: str | None = None  # 统计信息更新时间

class TagassignEntry(BaseModel):
    """表标签明细结构。"""

    field_0: str | None = None  # 标签编号
    field_1: str | None = None  # 表名
    field_2: str | None = None  # 标签名
    field_3: str | None = None  # 标签值
    field_4: str | None = None  # 业务分类
    field_5: str | None = None  # 敏感等级
    field_6: str | None = None  # 数据owner
    field_7: str | None = None  # 创建日期

class AccesslogEntry(BaseModel):
    """访问记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 表名
    field_2: str | None = None  # 查询类型
    field_3: str | None = None  # 查询用户
    field_4: str | None = None  # 查询时间
    field_5: str | None = None  # 扫描文件数
    field_6: str | None = None  # 扫描数据量MB
    field_7: str | None = None  # 查询耗时毫秒

class FailoverEntry(BaseModel):
    """恢复方案明细结构。"""

    field_0: str | None = None  # 方案编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 故障类型
    field_3: str | None = None  # 恢复起点
    field_4: str | None = None  # 最大重试
    field_5: str | None = None  # 降级策略
    field_6: str | None = None  # 通知渠道
    field_7: str | None = None  # 恢复超时分钟

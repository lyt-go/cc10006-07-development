<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">实时数据湖仓一体化平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向实时数据入湖、流批一体处理、湖仓分层存储、元数据统一管理、数据合并优化与增量查询服务的实时数据湖仓工程平台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "实时入湖", path: "/streaming" }, { label: "湖格式管理", path: "/lakeformat" }, { label: "数据合并", path: "/compaction" }, { label: "统一元数据", path: "/catalog" }, { label: "快照管理", path: "/snapshotmgr" }, { label: "表优化", path: "/icebergopt" }, { label: "Schema注册", path: "/schemareg" }, { label: "增量查询", path: "/increment" }, { label: "文件布局", path: "/filelayout" }, { label: "冷热分层", path: "/coldstore" }, { label: "数据分支", path: "/databranch" }, { label: "检查点管理", path: "/checkpoint" }, { label: "分区水位", path: "/watershed" }, { label: "过期清理", path: "/gcpolicy" }, { label: "索引加速", path: "/indexing" }, { label: "标签标记", path: "/tagassign" }, { label: "访问日志", path: "/accesslog" }, { label: "故障恢复", path: "/failover" }]
</script>

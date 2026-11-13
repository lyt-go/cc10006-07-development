import { createRouter, createWebHistory } from 'vue-router'

import Overview from '@/views/Overview.vue'
const Streaming = () => import('@/views/streaming/index.vue')
const Lakeformat = () => import('@/views/lakeformat/index.vue')
const Compaction = () => import('@/views/compaction/index.vue')
const Catalog = () => import('@/views/catalog/index.vue')
const Snapshotmgr = () => import('@/views/snapshotmgr/index.vue')
const Icebergopt = () => import('@/views/icebergopt/index.vue')
const Schemareg = () => import('@/views/schemareg/index.vue')
const Increment = () => import('@/views/increment/index.vue')
const Filelayout = () => import('@/views/filelayout/index.vue')
const Coldstore = () => import('@/views/coldstore/index.vue')
const Databranch = () => import('@/views/databranch/index.vue')
const Checkpoint = () => import('@/views/checkpoint/index.vue')
const Watershed = () => import('@/views/watershed/index.vue')
const Gcpolicy = () => import('@/views/gcpolicy/index.vue')
const Indexing = () => import('@/views/indexing/index.vue')
const Tagassign = () => import('@/views/tagassign/index.vue')
const Accesslog = () => import('@/views/accesslog/index.vue')
const Failover = () => import('@/views/failover/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'overview', component: Overview },
    { path: '/streaming', name: 'streaming', component: Streaming },
    { path: '/lakeformat', name: 'lakeformat', component: Lakeformat },
    { path: '/compaction', name: 'compaction', component: Compaction },
    { path: '/catalog', name: 'catalog', component: Catalog },
    { path: '/snapshotmgr', name: 'snapshotmgr', component: Snapshotmgr },
    { path: '/icebergopt', name: 'icebergopt', component: Icebergopt },
    { path: '/schemareg', name: 'schemareg', component: Schemareg },
    { path: '/increment', name: 'increment', component: Increment },
    { path: '/filelayout', name: 'filelayout', component: Filelayout },
    { path: '/coldstore', name: 'coldstore', component: Coldstore },
    { path: '/databranch', name: 'databranch', component: Databranch },
    { path: '/checkpoint', name: 'checkpoint', component: Checkpoint },
    { path: '/watershed', name: 'watershed', component: Watershed },
    { path: '/gcpolicy', name: 'gcpolicy', component: Gcpolicy },
    { path: '/indexing', name: 'indexing', component: Indexing },
    { path: '/tagassign', name: 'tagassign', component: Tagassign },
    { path: '/accesslog', name: 'accesslog', component: Accesslog },
    { path: '/failover', name: 'failover', component: Failover },
  ],
})

export default router

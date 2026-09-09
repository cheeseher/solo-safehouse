# SOLO · 个人安全屋

一个移动端优先的独居住宅参考设计网站。以生活需求为线索，展示设计理念、空间概念效果图、柜体分层、抽屉内部净尺寸、生活动线与机器人清扫连接。

## Cloudflare Pages 部署

在 Cloudflare **Workers & Pages → Create application → Pages → Connect to Git** 中选择这个仓库：

| 配置 | 填写 |
| --- | --- |
| 项目名称 | `solo-safehouse`（若名称占用，使用可用名称） |
| 生产分支 | `main` |
| Framework preset / 框架 | `None` |
| Build command / 构建命令 | `exit 0` |
| Build output directory / 输出目录 | `dist` |
| Root directory / 根目录 | 留空（仓库根目录） |
| 环境变量 | 无需设置 |

`dist` 已包含完整静态产物，无需 npm、数据库或后端。选择 **Pages 的 Git 集成**，不是要求部署命令的 Workers 创建流程。连接后提交到 `main` 会触发自动部署；以 Cloudflare 最终返回的域名为准。可在 Pages 项目的 Custom domains 中绑定已有域名的子域名，例如 `solo.你的域名`。

首次部署后，建议在微信中实测打开首页、大图查看与柜体展开。当前网站设置了标题和描述，未接入微信公众号 JS-SDK；不承诺微信分享卡片显示形式或大陆网络表现。

## 内容与交互

- 理念与六个主要空间：客厅、工作室、轻厨房、卧室、卫浴、家政。
- 玄关、露台、独立网络/NAS 设备区补充展示。
- 11 组柜体正立面，可展开查看分层与物品清单；3 组抽屉俯视净尺寸图。
- 全屋布局、生活动线、机器人清扫三种可切换图层。
- 吹风机 H01 修订：干区独立挂放，机身与线缆整体归位，避免塞入 150mm 镜柜。
- 原生 dialog 大图查看、放大细节、原图入口；键盘操作、系统深色模式与减少动效支持。
- 无外部字体、脚本、追踪或运行时 API 请求；图片为本地响应式 WebP。

关闭 JavaScript 仍能阅读正文、展开柜体，并通过普通链接打开原图与另外两种动线图。

## 文件与修改

- `dist/index.html`：完整正文。
- `dist/style.css`：响应式布局、深色模式、打印样式。
- `dist/app.js`：图层切换、大图查看、柜体锚点。
- `dist/assets`：本地 WebP 与可独立打开的 SVG 图纸。
- `scripts/design-data.json`：统一柜体、抽屉和平面尺寸数据。
- `scripts/build.py`：使用 Python 3 标准库重建 HTML/SVG；无需安装依赖。

修改文案或尺寸时优先修改 `scripts/build.py` / `scripts/design-data.json`，再执行 `python3 scripts/build.py` 并提交对应 `dist` 文件。CSS 与 JS 直接修改。WebP 是保留的图片源，生成器不改写图片。部署直接使用已提交的 `dist`，无需在 CF 安装 Python。

## 设计边界

这是概念参考，不是实测户型或施工下料图。约 98.3㎡ 为概念室内净地面（含柜体占地，露台另计），不等同于建筑面积。写实图片由 AI 生成，尺寸和结构以图纸为准；柜体名义分区仍需扣除板材、五金与管线占位。设备选型、结构、防水、电气、维护净空与当地要求需在施工前由专业人员复核。

网站不公开原始私人聊天链接或个人经历，也不包含账号凭证。

## 实用主义修订 / 2026.09

- 客厅：中央脚踏改为可靠近的硬质可移动餐桌，保留硬质边几；生活/清扫平面同步更新。
- 书桌：两块屏幕统一朝向，加入 MacBook 立式位、Mac mini、苹果键鼠与桌垫，新增 D10 桌面俯视布置。
- `scripts/practical_details.py` 保存桌面占位数据、图纸生成与说明。
- 新效果图使用内置图像生成编辑工具制作，版本化保存在 `dist/assets/study-v2.webp` 与 `living-v2.webp`，并提供小屏版本；原始旧图保留以便回溯。
- 编辑提示词记录在 `scripts/image-prompts-v2.md`。图片表现材质与氛围，实际机型、接口、承重与净空需复核。

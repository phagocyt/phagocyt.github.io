# publishconf.py
from pelicanconf import *   # 继承你的基础配置

# 关键：输出到仓库根目录（即 main root）
OUTPUT_PATH = '.'

# 上线通常关闭相对链接；如果你本地用相对链接，也可保留
RELATIVE_URLS = False

# 如果哪天用了“删除输出目录”选项，保留这些关键文件/目录（双保险）
OUTPUT_RETENTION = [
    '.git', '.github', '.nojekyll', '.venv',
    'content', 'pelicanconf.py', 'publishconf.py',
    'theme', 'themes', 'README.md'
]

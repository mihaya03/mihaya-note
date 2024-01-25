---
title: "Hugo 自作の関数"
date: 2024-02-07T16:09:53+09:00
draft: false
tags: ["hugo"]
---

### 概要

* Hugoで複数の記事を作成または更新した際に、執筆完了したファイルのみを`git add`、`commit`、`push`する関数を作成した
* 対象は引数に指定したディレクトリ下のMarkdownファイルとする

### コード例

```python
from pathlib import Path
import re
import subprocess

def search_markdown_files(directory):
    draft_files = []
    base_path = Path(directory).resolve()
    for file_path in base_path.rglob('*.md'):  
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if re.search(r'^draft: false$', content, re.MULTILINE):
                draft_files.append(file_path.resolve())  
    return draft_files

def git_add_push_changed_files(directory):
    draft_files = search_markdown_files(directory)
    draft_files_set = set(draft_files)  

    status_output = subprocess.check_output(['git', 'status', '--porcelain'], encoding='utf-8')
    base_path = Path(directory).resolve()
    files_to_add = []
    for line in status_output.split('\n'):
        if line.startswith(' M ') or line.startswith('?? '):
            file_path = Path(line[3:]).resolve()
            if file_path in draft_files_set:  
                files_to_add.append(file_path)

    if files_to_add:
        subprocess.run(['git', 'add'] + [str(file) for file in files_to_add])
        subprocess.run(['git', 'commit', '-m', 'Automatically added changed or new markdown files'])
        subprocess.run(['git', 'push', 'origin', 'main'])
        print("Changed or new files have been committed and pushed.")
    else:
        print("No changed or new markdown files to commit and push.")
```

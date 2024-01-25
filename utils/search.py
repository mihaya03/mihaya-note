from pathlib import Path
import re
import subprocess

def search_markdown_files(directory):
    draft_files = []
    base_path = Path(directory).resolve()
    for file_path in base_path.rglob('*.md'):  # マークダウンファイルを再帰的に検索
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if re.search(r'^draft: false$', content, re.MULTILINE):
                draft_files.append(file_path.resolve())  # 絶対パスをリストに追加
    return draft_files

def git_add_push_changed_files(directory):
    draft_files = search_markdown_files(directory)
    draft_files_set = set(draft_files)  # 効率的な検索のためにセットに変換

    status_output = subprocess.check_output(['git', 'status', '--porcelain'], encoding='utf-8')
    base_path = Path(directory).resolve()
    files_to_add = []
    for line in status_output.split('\n'):
        if line.startswith(' M ') or line.startswith('?? '):
            # 相対パスから絶対パスに変換
            file_path = Path(line[3:]).resolve()
            if file_path in draft_files_set:  # 絶対パスでの比較
                files_to_add.append(file_path)

    if files_to_add:
        subprocess.run(['git', 'add'] + [str(file) for file in files_to_add])
        subprocess.run(['git', 'commit', '-m', 'Automatically added changed or new markdown files'])
        subprocess.run(['git', 'push', 'origin', 'main'])
        print("Changed or new files have been committed and pushed.")
    else:
        print("No changed or new markdown files to commit and push.")
        
git_add_push_changed_files('./content/posts/')
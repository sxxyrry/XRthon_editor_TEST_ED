import ghapi.all as ghapi
from folders import folder
from typing import Any
import fastcore.net
import ssl
import base64
import os


class _installer():
    def __init__(self):
        self.isinstall = False

    def get_github_file_with_ghapi(self, token, owner, repo, path, ref='main'):
        """
        使用`ghapi`库获取GitHub项目中的指定文件内容。

        参数:
            token (str): GitHub个人访问令牌。
            owner (str): 仓库所有者用户名或组织名。
            repo (str): 仓库名称。
            path (str): 文件在仓库中的相对路径。
            ref (str, optional): 分支或提交SHA，默认为'main'分支。
        返回:
            str: 文件内容。
        """
        api = ghapi.GhApi(token=token)
    
        repos = api.repos

        response = repos.get_content(owner=owner, repo=repo, path=path, ref=ref) # type: ignore
        encoded_content = response.content
        decoded_content = base64.b64decode(encoded_content).decode('utf-8')
        return decoded_content

    def install(self, name, state: str = 'module'):
        try:
            ssl._create_default_https_context = ssl._create_unverified_context

            token = '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'

            owner = 'sxxyrry'  # 仓库所有者用户名或组织名
            repo = f'XRthon_{state}'    # 仓库名称
            path: str = name
            file_path: str = f'{path}/{path}.XRn'  # 文件在仓库中的相对路径

            if state == 'package':
                if os.path.exists(os.path.join(folder, f'./package/{path}.XRn')): # type: ignore
                    self.isinstall = True
            
            if state == 'module':
                if os.path.exists(os.path.join(folder, f'./module/{path}.XRn')): # type: ignore
                    self.isinstall = True

            file_contents: str = self.get_github_file_with_ghapi(token, owner, repo, file_path)

            if state == 'package':
                if self.isinstall == True:
                    if os.path.exists(os.path.join(folder, f'./package/{path}.XRn')): # type: ignore
                        with open(os.path.join(folder, f'./package/{path}.XRn'), 'r') as f: # type: ignore
                            if f.read() == file_contents:
                                print(' > Package already installed')
                                return
                            elif f.read() != file_contents:
                                inputs: str = input(f' > Have you downloaded a package called \'{name}\'?(Y or N) >>>')
                                if inputs == 'Y':
                                    pass
                                elif inputs == 'N':
                                    return
                                else:
                                    print(f' > No command for {inputs}')
                self.isinstall = True
            
            if state == 'module':
                if self.isinstall == True:
                    if os.path.exists(os.path.join(folder, f'./module/{path}.XRn')): # type: ignore
                        with open(os.path.join(folder, f'./module/{path}.XRn'), 'r') as f: # type: ignore
                            if f.read() == file_contents:
                                print(' > Module already installed')
                                return
                            elif f.read() != file_contents:
                                inputs: str = input(f' > Have you downloaded a module called \'{name}\'?(Y or N) >>>')
                                if inputs == 'Y':
                                    pass
                                elif inputs == 'N':
                                    return
                                else:
                                    print(f' > No command for {inputs}')
                self.isinstall = False

            with open(os.path.join(folder, f'./module/{path}.XRn'), 'w') as f:
                f.write(file_contents)
        except fastcore.net.HTTP404NotFoundError: # type: ignore
                print(' > An error may have occurred because of a network error or the file does not exist')

installer = _installer()

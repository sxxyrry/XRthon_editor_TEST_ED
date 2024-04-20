import os
import random
import string
from typing import Any, Literal

from folders import folder


var: dict[Any, Any] = {'var' : 'var'}
func_name = None # type: ignore
list_1_s : list[str] = []
AllVariablesDelete = False
ErrorNotStop = False
import_list: list[list[str]] = []

def generate_random_string(length = 10, allowed_chars=None) -> str:
    """
    Generates a random string of specified length.

    Parameter:
        length (int): The length of a random string.
        allowed_chars (str, optional): The allowed character set, defaulting to all ASCII letters (uppercase and lowercase) and numbers.

    Return:
        str: A random string of specified length.
    """
    if allowed_chars is None:
        allowed_chars = string.ascii_letters + string.digits

    return ''.join(random.choice(allowed_chars) for _ in range(length))

del generate_random_string, random, string

for filename in os.listdir(os.path.join(folder, './module')):
    if filename.endswith('.XRn'):
        imports: str = filename.split('.XRn')[0]
        import_list.append(['module', imports]) # type: ignore

for foldername in os.listdir(os.path.join(folder, './package')):
    imports: str = foldername
    import_list.append(['package', imports]) # type: ignore

class XR_quit(BaseException):
    def __init__(self, *args : object) -> None:
        self.args = args
        super().__init__(*self.args)

class _XR_bool_types(type):
    """XR_bool_types"""
    
    def __return_self_super_init__(self) -> dict[str, Any]:
        self.super_init_True: tuple[Literal['True'],
                                    Literal['1'],
                                    Literal[1],
                                    Literal[True]] = ('True', '1', 1, True)
        self.super_init_False: tuple[Literal['False'],
                                     Literal['0'],
                                     Literal[0],
                                     Literal[False]] = ('False', '0', 0, False)
        self.super_init_: Tuple[self.super_init_True, # type: ignore
                                self.super_init_False] = self.super_init_True + self.super_init_False # type: ignore
        return {'super_init_' : self.super_init_,
                'super_init_False' : self.super_init_False,
                'super_init_True' : self.super_init_True}

def _XR_bool(text, var : dict) -> bool | None:
    super_init_ = _XR_bool_types.__return_self_super_init__(_XR_bool_types)['super_init_'] # type: ignore
    super_init_True = _XR_bool_types.__return_self_super_init__(_XR_bool_types)['super_init_True'] # type: ignore
    super_init_False = _XR_bool_types.__return_self_super_init__(_XR_bool_types)['super_init_False'] # type: ignore
    if text in var:
        if var[text][1] in super_init_:
            if var[text][1] in super_init_True:
                return True
            elif var[text] in super_init_False:
                return False
            else:
                return False
        else:
            return False
    elif text in super_init_:
        if text in super_init_True:
            return True
        elif text in super_init_False:
            return False
        else:
            return False
    else:
        return False

def XR_type_(text : str, var : dict) -> Any | None:
    if text in var:
        return var[text][0]
    else:
        return None

class XRthon_main():
    def __init__(self) -> None:
        global func_name
        self.import_module_list: list[str] = []
        self.always_debug_after_execution = False
        self.var: dict[str, list[Any]] = {'breakpoints': []}  # 初始化 breakpoints 为空列表

    def raises(self, text : str):
        raise XR_quit(text)

    def inits(self, path, list_, var):
        paths_: str = ''.join(path)
        path_: list[str] = paths_.split(('\\'))
        list_p: list[str] = []
        for text in path_:
            for text__ in text.split('/'):
                list_p.append(text__)
        path_len_: int = len(list_p) - 1
        pathss_: list[str] = list_p[path_len_].split('.')
        pathss_len_: int = len(pathss_) - 1
        var.update({'__name__' : ['str.__name__', pathss_[pathss_len_ -1]],
                    '__path__' : ['str.__path__', path],
                    '__init__' : ['str.__init__', list_[1]],
                    '__file__' : ['str.__file__', list_p[path_len_]],
                    '__package__' : ['str.__package__', list_p[path_len_ - 1]],
                    'True' : ['True', True],
                    'False' : ['False', False],
                    'None' : ['None', None],})

    def raisess(self, text: str, types: str, code: str, file_: str, line= 0, code_=1):
        Error_table: set[str] = {
                       'VariableError',
                       'InitError',
                       'CodeError',
                       'ErrortypeError',
                       'NameError',
                       'EmptyFunctionError',
                       'LogicError',
                       'ConditionError',
                       'TextError',
                       'EmptyIterableError',
                       'NotSupportError',
                       'CanNotDeleteError',
                       'PrintError',
                       'CanNotSetError',
                       'LoopImportError',
                      }
        if types in Error_table:
            file_s: str = os.path.join(file_)
            print('Backtrack (last call):')
            print(f'  File "{file_s}", line {line}')
            print(f'    {code}')
            print(f'    {types}: Error: {text}, Status code: {code_}\n')
            if ErrorNotStop == True:
                return 'ENS'
            else:
                return 0
        else:
            returns: Literal['ENS', 0] | None = self.raisess(f'name {types} is not defined', 'NameError', code, file_)
            if returns == 0:
                return 0
    
    def Logic(self, var : dict, text : str, file_now_line : int, path : str, file_line : int, file_text : str,list_1_s : list[str],
              init_ : bool = True):
        global func_name, AllVariablesDelete, ErrorNotStop
        list_1_s = [text_4 if file_text != '' else ''  for text_4 in file_text.split('\n')]
        if file_now_line == 1:
            if init_ == True:
                if 'init' in text:
                    list_: list[str] = text.split(':')
                    if '#' in list_[0]:
                        self.raisess('init undefined', 'InitError', text, path, file_now_line)
                        return
                    self.inits(path, list_, var)
                    return
                else:
                    returns: Literal['ENS', 0] | None = self.raisess('init undefined', 'InitError', text, path, file_now_line)
                    if returns == 0:
                        return 0
            else:
                pass
        if '    ' in text:
            return
        elif '#' in text:
            return
        elif text == '':
            return
        elif '=' in text:
            list_ = text.split('=')
            v_name_: str = list_[0]
            v: str = list_[1]
            if '.' in v_name_:
                list_1_: list[str] = v_name_.split('.')
                names: str = list_1_[0]
                d_: str = list_1_[1]
                if names == 'del':
                    if d_ == 'AllVariablesDelete':
                        if _XR_bool(v, var) == True | False: # type: ignore
                            print('WARNING: ')
                            print('When set to \'True\', all variables are deleted, as well as special variables.')
                            print('Therefore, an error will be reported when printing special variables.')
                            AllVariablesDelete = _XR_bool(v, var) # type: ignore
                        else:
                            returns = self.raisess('Can not set AllVariablesDelete', 'CanNotSetError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                    else:
                        returns = self.raisess('Can not set AllVariablesDelete', 'CanNotSetError', text, path, file_now_line)
                        if returns == 0:
                            return 0
                elif names == 'SYS':
                    if d_ == 'ErrorNotStop':
                        if _XR_bool(v, var) == True | False: # type: ignore
                            ErrorNotStop = _XR_bool(v, var) # type: ignore
                        else:
                            returns = self.raisess('Can not set ErrorNotStop', 'CanNotSetError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                else:
                    returns = self.raisess('Can not set', 'CanNotSetError', text, path, file_now_line)
                    if returns == 0:
                        return 0
            elif 'input' in v:
                #breakpoint()
                v_list_: list[str] = v.split(':')
                print('', end='')
                is_ = 0
                for text_1 in v_list_:
                    is_ += 1
                    if is_ == 1:
                        continue
                    elif (text_1 == '__name__' or
                    text_1 == '__path__' or
                    text_1 == '__init__' or
                    text_1 == '__file__' or
                    text_1 == '__package__' or
                    text_1 == 'True' or
                    text_1 == 'False' or
                    text_1 == 'None'):
                        if not text_1 in var:
                            returns = self.raisess('special variable cannot be printed', 'PrintError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                        else:
                            if len(v_list_) >= 3:
                                More: str = v_list_[1]
                                if More == 'type':
                                    print(str(XR_type_(v_list_[2], var)), end='')
                                else:
                                    print(str(var[text_1][1]), end='')
                            else:
                                print(str(var[text_1][1]), end='')
                    elif text_1 in var:
                        if len(v_list_) >= 3:
                            More = v_list_[1]
                            if More == 'type':
                                print(str(XR_type_(v_list_[2], var)), end='')
                            else:
                                print(str(var[text_1][1]), end='')
                        else:
                            print(str(var[text_1][1]), end='')
                    else:
                        if not text_1 == '':
                            if len(v_list_) >= 3:
                                More = v_list_[1]
                                if More == 'type':
                                    print(str(XR_type_(v_list_[2], var)), end='')
                                else:
                                    print(text_1, end='')
                            else:
                                print(text_1, end='')
                    v = input('')
            elif '{' in v and '}' in v:
                vs = set( )
                v_list_ = v.split('{')[1].split('}')
                for vars in v_list_:
                    if vars == '':
                        continue
                    vars_list_: list[str] = vars.split(',')
                    i = 0
                    for vars_ in vars_list_:
                        i += 1
                        vs.update({vars_})
                    var.update({v_name_ : ['set', vs, i]})
                return
            elif '.' in v:
                v_list_ = v.split('.')
                for v_ in v_list_:
                    if v_.isnumeric():
                        var.update({v_name_ : ['float', float(v), len(v)]})
                        return
                v_names_: str = v_list_[0]
                v_d_: str = v_list_[1]
                if v_names_ in var:
                    if v_d_ in var[v_names_]:
                        if var[v_names_][v_d_].isnumeric():
                            var.update({v_name_ : ['int', var[v_names_][v_d_], len(var[v_names_][v_d_])]})
                        else:
                            var.update({v_name_ : ['str', var[v_names_][v_d_], len(var[v_names_][v_d_])]})
                    else:
                        returns = self.raisess('variable undefined', 'VariableError', text, path, file_now_line)
                        if returns == 0:
                            return 0
                else:
                    returns= self.raisess('variable undefined', 'VariableError', text, path, file_now_line)
                    if returns == 0:
                        return 0
                return
            elif v in import_list and v in var:
                var.update({v_name_ : var[v]})
                return
            elif v.isnumeric():
                var.update({v_name_ : ['int', int(v), len(v)]})
                return
            var.update({v_name_ : ['str', v, len(v)]})
        elif ':' in text:
            list_ = text.split(':')
            f: str = list_[0]
            if f == 'print':
                text_2: list[str] = list_[1].split('\'')
                print('', end='')
                for text_1 in text_2:
                    if (text_1 == '__name__' or
                    text_1 == '__path__' or
                    text_1 == '__init__' or
                    text_1 == '__file__' or
                    text_1 == '__package__' or
                    text_1 == 'True' or
                    text_1 == 'False' or
                    text_1 == 'None'):
                        if not text_1 in var:
                            returns = self.raisess('special variable cannot be printed', 'PrintError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                        else:
                            if len(list_) >= 3:
                                More = list_[1]
                                if More == 'type':
                                    print(str(XR_type_(list_[2], var)), end='')
                                else:
                                    print(str(var[text_1][1]), end='')
                            else:
                                print(str(var[text_1][1]), end='')
                    elif text_1 in var:
                        if len(list_) >= 3:
                            More = list_[1]
                            if More == 'type':
                                print(str(XR_type_(list_[2], var)), end='')
                            else:
                                print(str(var[text_1][1]), end='')
                        else:
                            print(str(var[text_1][1]), end='')
                    else:
                        if not text_1 == '':
                            if len(list_) >= 3:
                                More = list_[1]
                                if More == 'type':
                                    print(str(XR_type_(list_[2], var)), end='')
                                else:
                                    print(text_1, end='')
                            else:
                                print(text_1, end='')
                print()
            elif f == 'init':
                pass
            elif f == 'input':
                text_2 = list_[1].split('\'')
                print('', end='')
                for text_1 in text_2:
                    if (text_1 == '__name__' or
                    text_1 == '__path__' or
                    text_1 == '__init__' or
                    text_1 == '__file__' or
                    text_1 == '__package__' or
                    text_1 == 'True' or
                    text_1 == 'False' or
                    text_1 == 'None'):
                        if not text_1 in var:
                            returns = self.raisess('special variable cannot be printed', 'PrintError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                        else:
                            if len(list_) >= 3:
                                More = list_[1]
                                if More == 'type':
                                    print(str(XR_type_(list_[2], var)), end='')
                                else:
                                    print(str(var[text_1][1]), end='')
                            else:
                                print(str(var[text_1][1]), end='')
                    elif text_1 in var:
                        if len(list_) >= 3:
                            More = list_[1]
                            if More == 'type':
                                print(str(XR_type_(list_[2], var)), end='')
                            else:
                                print(str(var[text_1][1]), end='')
                        else:
                            print(str(var[text_1][1]), end='')
                    else:
                        if not text_1 == '':
                            if len(list_) >= 3:
                                More = list_[1]
                                if More == 'type':
                                    print(str(XR_type_(list_[2], var)), end='')
                                else:
                                    print(text_1, end='')
                            else:
                                print(text_1, end='')
                    v = input('')
            elif f == 'return':
                print('The program has exited\n')
                return 0
            elif f == 'raise':
                text_2 = list_[1].split(',')
                if len(text_2) == 2:
                    returns = self.raisess(text_2[0], text_2[1], text, path, file_now_line)
                    if returns == 0:
                        return 0
                elif len(text_2) == 3:
                    try:
                        returns = self.raisess(text_2[0], text_2[1], text, path, file_now_line, int(text_2[2]))
                        if returns == 0:
                            return 0
                    except SystemExit:
                        pass
                    except:
                        returns = self.raisess(f'code {text} is ERROR', 'CodeError', text, path, file_now_line)
                        if returns == 0:
                            return 0
                else:
                    returns = self.raisess(f'code {text} is ERROR', 'CodeError', text, path, file_now_line)
                    if returns == 0:
                        return 0
            elif f == 'def':
                func_name = list_[1]
                args_str: str = ''.join(list_[2:-1]).strip('(').strip(')')
                args_list: list[str] = [arg.strip() for arg in args_str.split(',') if arg.strip()]
                
                var[func_name] = ['function',  {'args': args_list, 'body': []}]
                
                next_file_line: int = file_now_line + 1
                
                try:
                    while not 'end' in list_1_s[next_file_line - 1] or list_1_s[next_file_line - 1].split(':')[0] != 'end':
                        list___: list[str] = list_1_s[next_file_line - 1].split('    ')
                        text___: Literal[''] = ''
                        is_ = 0
                        for text__ in list___:
                            is_ += 1
                            if is_ == 1:
                                continue
                            else:
                                if text__ == '':
                                    text___ += '    ' # type: ignore
                                else:
                                    text___ += text__ # type: ignore
                        var[func_name][1]['body'].append(text___)
                        next_file_line += 1
                except IndexError:
                    returns = self.raisess(f'Function "{func_name}" is empty','EmptyFunctionError', text, path, file_now_line)
                    if returns == 0:
                        return 0
                        
                if not var[func_name][1]['body'] or var[func_name][1]['body'] == ['']:
                    returns = self.raisess(f'Function "{func_name}" is empty', 'EmptyFunctionError', text, path, file_now_line)
                    if returns == 0:
                        return 0
                return
            elif f == 'if':
                condition: str = text.split(':')[1].split(' ')[0]
                next_file_line = file_now_line + 1
                i = 0

                def test_1(i) -> Literal[0] | None:
                    nonlocal next_file_line, condition
                    returns: bool | None = self.evaluate_expression(var, condition)
                    if returns == True:
                        if i == 1:
                            i += 1
                            returns = test_1(i) # type: ignore
                            if returns == 0:
                                return 0
                            return
                        elif i >= 2:
                            DontnownameVar1: list[str] = list_1_s[file_now_line - 1].split(':')
                            DontnownameVar2: Literal[''] = ''
                            is_ = 0
                            for _ in DontnownameVar1:
                                is_ += 1
                                if _ == 'end':
                                    continue
                                else:
                                    if is_ == len(DontnownameVar1) - 1:
                                        DontnownameVar2 += _ + ':' # type: ignore # type: ignore
                                    else:
                                        DontnownameVar2 += _ # type: ignore
                            while (not 'end' in list_1_s[next_file_line - 1] or
                                list_1_s[next_file_line - 1].split(':')[0] != 'end' and
                                DontnownameVar2 == text):
                                
                                texts_: Literal[''] = ''
                                for _is in range(len(list_1_s[next_file_line - 1].split('    '))):
                                    if _is == 0:
                                        continue
                                    else:
                                        texts_ += list_1_s[next_file_line - 1].split('    ')[_is] # type: ignore

                                returns = self.Logic(var, texts_, file_now_line, path, file_line, file_text, list_1_s,
                                                     False) # type: ignore
                                if returns == 0:
                                    return 0
                                next_file_line += 1
                            
                    elif returns == False:
                        return
                    elif returns != False and returns == 0:
                        return 0
                    
                returns = test_1(1)
                if returns == 0:
                    return 0

            elif f in var:
                if var[f][0] == 'function':
                    function_info: Any = var[f][1]
                    
                    local_vars: dict[str, Any] = {arg: None for arg in function_info['args']}
                    
                    local_vars.update(var)

                    def test_2(i) -> Literal[0] | None:
                        if i == 1:
                            i += 1
                            returns: Literal[0] | None = test_2(i)
                            if returns == 0:
                                return 0
                            return
                        elif i >= 2:
                            for texts in function_info['body']:
                                returns = self.Logic(local_vars, texts, file_now_line, path, file_line, file_text, list_1_s, False)
                                if returns == 0:
                                    return 0
                    
                    returns = test_2(1)
                    if returns == 0:
                        return 0

                    var[func_name][1]['return_value'] = None
                else:
                    returns = self.raisess(f'name {text} is not defined', 'NameError', text, path, file_now_line)
                    if returns == 0:
                        return 0
                
            elif f == 'for':
                next_file_line = file_now_line + 1
                v_name_ = list_[1]
                v = list_[1]

                def test_3(i) -> Literal[0] | None:
                    nonlocal next_file_line, v
                    text_l: list[Any] = []
                    if i == 1:
                        i += 1
                        returns: Literal[0] | None = test_3(i)
                        if returns == 0:
                            return 0
                        return
                    elif i >= 2:
                        DontnownameVar1: list[str] = list_1_s[file_now_line - 1].split(':')
                        DontnownameVar2: Literal[''] = ''
                        is_ = 0
                        for _ in DontnownameVar1:
                            is_ += 1
                            if _ == 'end':
                                continue
                            else:
                                if is_ == len(DontnownameVar1) - 1:
                                    DontnownameVar2 += _ + ':' # type: ignore
                                else:
                                    DontnownameVar2 += _ # type: ignore
                        while (not 'end' in list_1_s[next_file_line - 1] or
                               list_1_s[next_file_line - 1].split(':')[0] != 'end' and
                               DontnownameVar2 == text):
                            texts_: Literal[''] = ''
                            for _is in range(len(list_1_s[next_file_line - 1].split('    '))):
                                if _is == 0:
                                    continue
                                else:
                                    texts_ += list_1_s[next_file_line - 1].split('    ')[_is] # type: ignore

                            text_l.append(texts_)
                            next_file_line += 1
                        ns = int(v)
                        _line_ = 0
                        for i in range(ns):
                            _line_ = 0
                            for texts__ in text_l:
                                _line_ += 1
                                var.update({'ln' : ['int', ns]})
                                var.update({'i' : ['int', i + 1]})
                                returns = self.Logic(var, texts__, _line_, path, file_line, file_text, text_l, False)
                                if returns == 0:
                                    return 0
                    
                returns = test_3(1)
                if returns == 0:
                    return 0
                
            elif f == 'while':
                next_file_line = file_now_line + 1
                v_name_ = list_[1]
                v = list_[1]

                def test_4(i) -> Literal[0] | None:
                    nonlocal next_file_line, v
                    text_l: list[Any] = []
                    if i == 1:
                        i += 1
                        returns: Literal[0] | None = test_4(i)
                        if returns == 0:
                            return 0
                        return
                    elif i >= 2:
                        DontnownameVar1: list[str] = list_1_s[file_now_line - 1].split(':')
                        DontnownameVar2: Literal[''] = ''
                        is_ = 0
                        for _ in DontnownameVar1:
                            is_ += 1
                            if _ == 'end':
                                continue
                            else:
                                if is_ == len(DontnownameVar1) - 1:
                                    DontnownameVar2 += _ + ':' # type: ignore
                                else:
                                    DontnownameVar2 += _ # type: ignore
                        while (not 'end' in list_1_s[next_file_line - 1] or
                            list_1_s[next_file_line - 1].split(':')[0] != 'end' and
                            DontnownameVar2 == text):
                            texts_: Literal[''] = ''
                            for _is in range(len(list_1_s[next_file_line - 1].split('    '))):
                                if _is == 0:
                                    continue
                                else:
                                    texts_list = list_1_s[next_file_line - 1].split('    ')
                                    is___ = 0
                                    for text_ss in texts_list:
                                        is___ += 1
                                        if is___ == 1:
                                            continue
                                        elif text_ss == '':
                                            texts_ += '    ' # type: ignore
                                        else:
                                            texts_ += text_ss # type: ignore 

                            text_l.append(texts_)
                            next_file_line += 1
                        iss = 0
                        if '\'' in list_[1]:
                            list_s = list_[1].split('\'')
                            for isss in list_s:
                                if isss == '':
                                    continue
                                while _XR_bool(isss, var):
                                    iss += 1
                                    file_next_line = file_now_line + 1
                                    returns = self.Logic(var, text_l[iss - 1], file_next_line, path, file_line, file_text, text_l, False)
                                    if returns == 0:
                                        return 0

                returns = test_4(1)
                if returns == 0:
                    return 0
            
            elif f == 'import':
                v = list_[1]

                if v == 'SYS.var':
                    self.inits(path, list_, var)
                elif ['module', v] in import_list:
                    path__: str = os.path.join(folder, '\\module\\', f'{v}.XRn')
                    varsss: dict[str, Any] = var
                    with open(path__, 'r', encoding='UTF-8') as fs:
                        varss: dict = {}
                        if v in self.import_module_list:
                            pass
                        else:
                            self.import_module_list.append(v)
                        try:
                            varss_: dict[str, Any] | Literal[0] = self.XRthon_file(fs, path__, 'import', varss) # type: ignore
                            if varss_ == 0:
                                return 0
                        except XR_quit:
                            texts____: Literal[''] = ''
                            i = 0
                            for text_ in self.import_module_list:
                                i += 1
                                if i == len(self.import_module_list):
                                    texts____ += text_ # type: ignore
                                else:
                                    texts____ += text_ + ', ' # type: ignore
                            returns = self.raisess(f'{texts____} Round-robin import between modules', 'LoopImportError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                        else:
                            varss_: dict[str, Any] | Literal[0] = self.XRthon_file(fs, path__, 'import', varss) # type: ignore
                            varsss.update({v: ['object', varss_]}) # type: ignore
                            # print(varsss)
                            var.update(varsss)
                    '''
                elif ['package', v] in import_list:
                    path__: str = os.path.join(folder, '.\\package\\', f'{v}.XRn')
                    varsss: dict[str, Any] = var
                    with open(path__, 'r', encoding='UTF-8') as fs:
                        varss: dict = {}
                        if v in self.import_module_list:
                            pass
                        else:
                            self.import_module_list.append(v)
                        try:
                            varss_: dict[str, Any] | Literal[0] = self.XRthon_file(fs, path__, 'import', varss) # type: ignore
                            if varss_ == 0:
                                return 0
                        except XR_quit:
                            texts____: Literal[''] = ''
                            i = 0
                            for text_ in self.import_module_list:
                                i += 1
                                if i == len(self.import_module_list):
                                    texts____ += text_ # type: ignore
                                else:
                                    texts____ += text_ + ', ' # type: ignore
                            returns = self.raisess(f'{texts____} Round-robin import between modules', 'LoopImportError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                        else:
                            varss_: dict[str, Any] | Literal[0] = self.XRthon_file(fs, path__, 'import', varss) # type: ignore
                            varsss.update({v: ['object', varss_]}) # type: ignore
                            # print(varsss)
                            var.update(varsss)
                '''
                else:
                    returns = self.raisess(f'name {v} is not import file', 'NotImportFileError', text, path, file_now_line)
                    if returns == 0:
                        return 0
            elif f == 'del':
                if AllVariablesDelete == True:
                    if ',' in list_[1]:
                        list_s_: list[str] = list_[1].split(',')
                        for i in list_s_:
                            if i in var:
                                var.pop(i)
                            else:
                                returns = self.raisess(f'can not delete {i}', 'CanNotDeleteError', text, path, file_now_line)
                                if returns == 0:
                                    return 0
                    else:
                        v = list_[1]
                        if v in var:
                            var.pop(v)
                elif AllVariablesDelete == False:
                    if ',' in list_[1]:
                        list_s_ = list_[1].split(',')
                        for i in list_s_:
                            if i in var:
                                if (i == '__name__' or
                                    i == '__path__' or
                                    i == '__init__' or
                                    i == '__file__' or
                                    i == '__package__' or
                                    i == 'True' or
                                    i == 'False' or
                                    i == 'None'):
                                    returns = self.raisess(f'can not delete {i}', 'CanNotDeleteError', text, path, file_now_line)
                                    if returns == 0:
                                        return 0
                                else:
                                    var.pop(i)
                            else:
                                returns = self.raisess(f'can not delete {i}', 'CanNotDeleteError', text, path, file_now_line)
                                if returns == 0:
                                    return 0
                    else:
                        v = list_[1]
                        if v in var:
                            if (v == '__name__' or
                                v == '__path__' or
                                v == '__init__' or
                                v == '__file__' or
                                v == '__package__' or
                                v == 'True' or
                                v == 'False' or
                                v == 'None'):
                                returns = self.raisess(f'can not delete {v}', 'CanNotDeleteError', text, path, file_now_line)
                                if returns == 0:
                                    return 0
                            else:
                                var.pop(v)
                        else:
                            returns = self.raisess(f'can not delete {v}', 'CanNotDeleteError', text, path, file_now_line)
                            if returns == 0:
                                return 0
                    
            elif f == 'end':
                return
            
            else:
                returns = self.raisess(f'name {f} is not defined', 'NameError', text, path, file_now_line)
                if returns == 0:
                    return 0
        else:
            returns = self.raisess(f'name {text} is not defined', 'NameError', text, path, file_now_line)
            if returns == 0:
                return 0

    def eval_condition(self, var, condition, body_lines, start_line, path, file_line, file_text) -> Literal[0] | None:
        evaluated_condition: bool | None = self.evaluate_expression(var, condition)
        if evaluated_condition:
            for line_num, line_text in enumerate(body_lines, start=start_line):
                file_now_line: int = line_num
                returns: Literal[0] | None = self.Logic(var, line_text, file_now_line, path, file_line, file_text, list_1_s)
                if returns == 0:
                    return 0

    def evaluate_expression(self, var, expression) -> bool | None:
        return _XR_bool(expression, var)

    def debug_mode(self, text, var, path, file_now_line, file_line, file_text, list_1_s) -> Literal[0] | None:
        if '#' in text:
            return
        print(f'Executing line {file_now_line}, code: {text}')
        try:
            user_input: str = input('Enter \'s\' in step debug mode, \'p\' to print the variable, \'quit\' to quit:')
        except KeyboardInterrupt:
            return
        if user_input == 's':
            retruns: Literal[0] | None = self.Logic(var, text, file_now_line, path, file_line, file_text, list_1_s)
            if retruns == 0:
                return 0
        elif 'p' in user_input:
            text_S_: list[str] = user_input.split(' ')
            if text_S_[0] == 'p':
                text_S__: list[str] = text_S_[1].split('\'')
            else:
                return
            if text_S__[1] in var:
                print('', var[text_S__[1]])
            else:
                returns: Literal['ENS', 0] | None = self.raisess(f'name {text_S_[1]} is not defined', 'NameError', text, path,
                                                                 file_now_line)
                if returns == 0:
                    return 0
            self.debug_mode(text, var, path, file_now_line, file_line, file_text, list_1_s)
        elif user_input == 'quit':
            self.always_debug_after_execution = False
            retruns = self.Logic(var, text, file_now_line, path, file_line, file_text, list_1_s)
            if retruns == 0:
                return 0
            return
        else:
            self.debug_mode(text, var, path, file_now_line, file_line, file_text, list_1_s)
            return

    def XRthon_file(self, file, path=os.path.join(folder, './TEST/TEST.XRn'), code__ = 'file',
                    var = var, mo='') -> None | dict[str, Any]:
        if var == ['var']:
            pass
        global list_1_s
        texts: str = ''.join(file.read())
        file_line: int = len(file.read().split('\n'))
        file_text: str = texts
        file_now_line = 0
        list_1: list[str] = texts.split('\n')
        list_1_s = [text_4 if file_text != '' else ''  for text_4 in file_text.split('\n')]
        for text in list_1:
            if code__ == 'import':
                if not '    ' in text:
                    if ('input:' in text or
                        'print:' in text or
                        'raise:' in text or
                        'retrun:' in text or
                        'if:' in text or
                        'elif:' in text or
                        'else:' in text or
                        'for:' in text or
                        'while:' in text):
                        continue
            file_now_line += 1
            if file_now_line in self.var['breakpoints']:
                self.always_debug_after_execution = True
                retruns: Literal[0] | None = self.debug_mode(text, self.var, path, file_now_line, file_line, file_text, list_1_s)
                if retruns == 0:
                    return
            else:
                if self.always_debug_after_execution:
                    retruns: Literal[0] | None = self.debug_mode(text, self.var, path, file_now_line, file_line, file_text, list_1_s)
                    if retruns == 0:
                        return
                else:
                    self.always_debug_after_execution = False
                    if code__ == 'import' and var != {'var' : 'var'}:
                        try:
                            retruns: Literal[0] | None = self.Logic(var, text, file_now_line, path, file_line, file_text,
                                                                    list_1_s, False)
                            if retruns == 0:
                                return 0 # type: ignore
                        except RecursionError:
                            raise XR_quit()
                    else:
                        retruns: Literal[0] | None = self.Logic(self.var, text, file_now_line, path, file_line, file_text, list_1_s)
                        if retruns == 0:
                            return

            if not (file_now_line in self.var['breakpoints'] or self.always_debug_after_execution):
                continue
        if code__ == 'import':
            return var

_XRthon_main_ = XRthon_main()

if __name__ == '__main__':
    with open(os.path.join(folder, './TEST/', 'TEST.XRn'), 'r', encoding='UTF-8') as file:
        _XRthon_main_.XRthon_file(file, str(folder) + '\\TEST\\' + 'TEST.XRn')

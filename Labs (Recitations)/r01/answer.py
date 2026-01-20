import time
import sys
import random
from typing import (
    Iterable, List, Optional,
    Callable, Tuple, Dict
)


def selection_sort(X:Iterable[int]) -> List[int]:
    """
    Selection sort.
    
    Args:
        X (list): A list of integers.
    
    Returns:
        list: The sorted list.
    """
    for i in range(len(X)):
        min_idx = i
        for j in range(i + 1, len(X)):
            if X[j] < X[min_idx]:
                min_idx = j
        X[i], X[min_idx] = X[min_idx], X[i]
    return X

def insertion_sort(X:Iterable[int]) -> List[int]:
    """
    Insertion sort.
    
    Args:
        X (list): A list of integers.
    
    Returns:
        list: The sorted list.
    """
    for i in range(1, len(X)):
        key = X[i]
        j = i - 1
        while j >= 0 and X[j] > key:
            X[j + 1] = X[j]
            j -= 1
        X[j + 1] = key
    return X


def merge_sort(X:Iterable[int]) -> List[int]:
    """
    Merge sort.
    
    Args:
        X (list): A list of integers.
    
    Returns:
        list: The sorted list.
    """
    if len(X) <= 1:
        return X

    mid = len(X) // 2
    left = merge_sort(X[:mid])
    right = merge_sort(X[mid:])

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            X[k] = left[i]
            i += 1
        else:
            X[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        X[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        X[k] = right[j]
        j += 1
        k += 1

    return X

def quick_sort(X:Iterable[int]) -> List[int]:
    """
    Quicksort.
    
    Args:
        X (list): A list of integers.
    
    Returns:
        list: The sorted list.
    """
    def _partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(arr, low, high):
        if low < high:
            pi = _partition(arr, low, high)
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)

    _quicksort(X, 0, len(X) - 1)
    return X


class SortCompetitor(object):
    
    def __init__(
        self,
        sort_funcs:Dict[str, Callable] = {},
        n_nums:List[int] = [1e3, 1e4, 1e5, 1e6],
        silence:bool=False
    ) -> None:
        EnvChecker(
            python_major = 3, 
            python_minor = 10,
            n_max_iter = 1e7,
            matplotlib = None,
            tabulate = None
        )
        self._sort_funcs:Dict[str, Callable] = sort_funcs
        self._n_nums:List[int] = sorted(n_nums)
        self._silence:bool = silence
        
    def _is_sorted(self, lst:List[int]):
        if len(lst) <= 1: return True
        ascending = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
        descending = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
        return ascending or descending
        
    def test_sort_func(
        self,
        func:Callable,
        n_num:int=1e3
    ) -> Tuple[str,float]:
        _lst = list(range(int(n_num)))
        random.shuffle(_lst)
        _status = 'incorrect'
        _t_start = time.perf_counter()
        _sort_lst = None
        try:
            _sort_lst = func(_lst)
        except NotImplementedError:
            _status = 'not_implement'
        _t_end = time.perf_counter()
        if _sort_lst is not None and isinstance(_sort_lst, list):
            if self._is_sorted(_sort_lst):
                _status = 'pass'
        return _status, (_t_end-_t_start)
    
    def test(self):
        _pass, _time = {}, {}
        for _name, _func in self._sort_funcs.items():
            _pass.setdefault(_name, [])
            _time.setdefault(_name, [])
            if not self._silence:
                print(f'Running {_name} to sort list size: [', end='', flush=True)
            for _n_num in self._n_nums:
                if not self._silence:
                    print(f'{_n_num}, ', end='', flush=True)
                _s, _t = self.test_sort_func(_func, n_num=_n_num)
                _pass[_name].append(_s)
                _time[_name].append(_t)
            if not self._silence:
                print(f']')
        return _pass, _time
    
    def table(self, pass_dict, time_dict):
        from tabulate import tabulate
        _status_emoji = {
            'pass': '✅',
            'incorrect': '❌',
            'not_implement': '⚠️'
        }
        table = []
        for sort_name, statuses in pass_dict.items():
            row = [sort_name] + [_status_emoji.get(s, s) for s in statuses]
            table.append(row)
        print(
            tabulate(
                table,
                headers=["Status"] + [f'{n:.0e}' for n in self._n_nums],
                tablefmt="grid"
            ),
            end='\n\n'
        )
        table = []
        for sort_name, sort_time in time_dict.items():
            row = [sort_name] + sort_time
            table.append(row)
        print(
            tabulate(
                table,
                headers=["Time (s)"] + [f'{n:.0e}' for n in self._n_nums],
                tablefmt="grid",
                floatfmt='.3f'
            )
        )
        
    def plot_time(self, time_dict):
        """
        Plot a line chart for sort times.
        
        Args:
            time_dict (dict): {sort_name: [time,...]}
        """
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 5))

        # Plot each sort
        for sort_name, sort_time in time_dict.items():
            plt.plot(self._n_nums, sort_time, marker='o', label=sort_name)

        # Set log-scale for input sizes
        plt.xscale('log')
        plt.xlabel("Input size (n)")
        plt.ylabel("Time (s)")
        plt.title("Sort Time vs Input Size")
        plt.grid(True, which="both", linestyle='--', alpha=0.5)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    def __call__(self):
        _pass, _time = self.test()
        self.table(_pass, _time)
        self.plot_time(_time)
        return _pass, _time
    
    
class EnvChecker(object):
    
    @classmethod
    def _check_package(
        cls,
        name_:str,
        install_instruct:Optional[str]=None
    ) -> None:
        from importlib.util import find_spec
        if find_spec(name_) is None:
            if install_instruct is None:
                install_instruct = f'`pip install {name_}`\nor\n`pip3 install {name_}`'
            _err_info = \
            'Package Does Not Exist.\n' + \
            '------------------------------------\n' + \
            'Please install following:\n' + \
            f'{install_instruct}\n' + \
            '------------------------------------\n'
            raise ImportError(_err_info)
    
    @classmethod    
    def _check_python(
        cls,
        major:int = 3,
        minor:Optional[int] = None,
    ) -> None:
        _target_v = str(major)
        if minor is not None:
            _target_v += f'.{minor}'
        _err_info = \
        'Python needs upgrade.\n' + \
        '------------------------------------\n' + \
        'Please install following:\n' + \
        f'If you are using conda: conda install python={_target_v}\n' + \
        'Or download from: https://www.python.org/downloads/\n' + \
        '------------------------------------\n'
        _v_info = sys.version_info
        _v_major = _v_info.major
        _v_minor = _v_info.minor
        if _v_major < major:
            raise RuntimeError(_err_info)
        if minor is not None and _v_minor < minor:
            raise RuntimeError(_err_info)
        
    @classmethod
    def _check_max_iters(
        cls,
        iter_limit:int = 1e7
    ) -> None:
        if sys.getrecursionlimit() < iter_limit:
            sys.setrecursionlimit(int(iter_limit))
    
    @classmethod       
    def check_env(
        cls,
        python_major:int=3,
        python_minor:Optional[int]=14,
        n_max_iter:int=1e7,
        **kwargs
    ) -> None:
        cls._check_python(major=python_major, minor=python_minor)
        for pkg_name, install_inst in kwargs.items():
            cls._check_package(name_ = pkg_name, install_instruct=install_inst)
        cls._check_max_iters(n_max_iter)
    
    def __init__(self, *args, **kwargs):
        self.check_env(*args, **kwargs)
        
        
if __name__ == '__main__':
    SortCompetitor(
        sort_funcs={
            'Tim Sort': sorted,
            'Quick Sort': quick_sort,
            'Merge Sort': merge_sort,
            'Selection Sort': selection_sort,
            'Insertion Sort': insertion_sort,
        },
        n_nums=[1e2, 1e3, 1e4, 2e4, 5e4],
        silence=False
    )()
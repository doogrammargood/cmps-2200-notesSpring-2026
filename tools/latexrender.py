from typing import (
    List, Iterable, Union, Optional,
    Callable, Tuple, IO
)

class RenderLine(object):
    
    def _render_plain(
        self,
        X:Union[List[str], str],
    ) -> List[str]:
        if isinstance(X, str):
            X = [fr'\text{{{X}}}']
        X = [fr'{x}' for x in X]
        return X
    
    def _render_effect(
        self,
        X:List[str],
        selects:Union[bool, List[bool]],
        effect:Callable[[List[str]], List[str]],
    ) -> List[str]:
        if isinstance(selects, bool) or selects is None:
            selects = [selects] * len(X)
        return [
            effect(text)
            if select else text
            for text, select
            in zip(X, selects)
        ]
        
    def _render_color(
        self,
        X:List[str],
        color:Optional[Union[List[str], str]]=None,
    ) -> List[str]:
        if isinstance(color, str) or color is None:
            color = [color] * len(X)
        for _unique_color in set(color):
            _color_selects = [
                c_ is not None and c_==_unique_color
                for c_ in color
            ]
            X = self._render_effect(
                X=X,
                selects=_color_selects,
                effect=lambda x:fr'\textcolor{{{_unique_color}}}{{{x}}}'
            )
        return X

    def _render_bold(self, X:List[str], selects:List[bool]) -> List[str]:
        return self._render_effect(
            X=X,
            selects=selects,
            effect=lambda x:fr'\textbf{{{x}}}'
        )
    
    def _render_italic(self, X:List[str], selects:List[bool]) -> List[str]:
        return self._render_effect(
            X=X,
            selects=selects,
            effect=lambda x:fr'\textit{{{x}}}'
        )
    
    def _render_underline(self, X:List[str], selects:List[bool]) -> List[str]:
        return self._render_effect(
            X=X,
            selects=selects,
            effect=lambda x:fr'\underline{{{x}}}'
        )
    
    def _render_deleteline(self, X:List[str], selects:List[bool]) -> List[str]:
        return self._render_effect(
            X=X,
            selects=selects,
            effect=lambda x:fr'\sout{{{x}}}'
        )
    
    def render(
        self,
        X:Union[List[str], str],
        color:Optional[Union[List[str], str]]=None,
        bold:Optional[Union[List[bool], bool]]=None,
        italic:Optional[Union[List[bool], bool]]=None,
        underline:Optional[Union[List[bool], bool]]=None,
        deleteline:Optional[Union[List[bool], bool]]=None,
    ) -> List[str]:
        X = self._render_plain(X=X)
        X = self._render_bold(X=X, selects=bold)
        X = self._render_italic(X=X, selects=italic)
        X = self._render_underline(X=X, selects=underline)
        X = self._render_deleteline(X=X, selects=deleteline)
        X = self._render_color(X=X, color=color)
        return X
    
    
    def __init__(
        self,
        X:Iterable[Union[float, int]],
        color:Optional[Union[List[str], str]]=None,
        bold:Optional[Union[List[bool], bool]]=None,
        italic:Optional[Union[List[bool], bool]]=None,
        underline:Optional[Union[List[bool], bool]]=None,
        deleteline:Optional[Union[List[bool], bool]]=None,
    ):
        self.X:Union[Iterable[Union[float, int]], str]=X
        self.color:Optional[Union[List[str], str]]=color
        self.bold:Optional[Union[List[bool], bool]]=bold
        self.italic:Optional[Union[List[bool], bool]]=italic
        self.underline:Optional[Union[List[bool], bool]]=underline
        self.deleteline:Optional[Union[List[bool], bool]]=deleteline
    
    @property
    def rich_x(self) -> List[str]:
        return self.render(
            X=self.X,
            color=self.color,
            bold=self.bold,
            italic=self.italic,
            underline=self.underline,
            deleteline=self.deleteline
        )
    @property    
    def latex(self) -> str:
        if isinstance(self.X, str):
            return fr'{self.rich_x[0]}'
        else:
            return '&'.join(self.rich_x)
    
    def __repr__(self) -> str:
        return '\n'.join(self.rich_x)
    
    def _repr_html_(self) -> str:
        from IPython.display import display, Latex
        display(Latex(
            fr'$${self.latex}$$'
        ))
        return ''
        
        
class RenderArrayLine(RenderLine):
    
    def __init__(
        self,
        X:Iterable[Union[float, int]],
        format:str='d',
        array_bracket:Tuple[str, str]=('[', ']'),
        color:Optional[Union[List[str], str]]=None,
        bold:Optional[Union[List[bool], bool]]=None,
        italic:Optional[Union[List[bool], bool]]=None,
        underline:Optional[Union[List[bool], bool]]=None,
        deleteline:Optional[Union[List[bool], bool]]=None,
    ):
        super().__init__(
            X=X, color=color, bold=bold,
            italic=italic, underline=underline,
            deleteline=deleteline
        )
        self.X = [
            array_bracket[0],
            *[f'{x:{format}},' for x in self.X[:-1]],
            f'{self.X[-1]:{format}},',
            array_bracket[1],
        ]
        self.color = self._extend_effect(color)
        self.bold = self._extend_effect(bold)
        self.italic = self._extend_effect(italic)
        self.underline = self._extend_effect(underline)
        self.deleteline = self._extend_effect(deleteline)

    def _extend_effect(self, effect:Optional[List]):
        if isinstance(effect, list):
            return [None, *effect, None]
        return effect

    @property
    def latex(self) -> str:
        _f_cols = 'l' * len(self.X)
        _out = fr'\[\begin{{array}}{{{_f_cols}}} {super().latex} \end{{array}}\]'
        return _out
    
class RenderTextLine(RenderLine):
    def __init__(
        self,
        X:str,
        color:Optional[str]=None,
        bold:Optional[bool]=None,
        italic:Optional[bool]=None,
        underline:Optional[bool]=None,
        deleteline:Optional[bool]=None,
    ):
        super().__init__(
            X=X, color=color, bold=bold,
            italic=italic, underline=underline,
            deleteline=deleteline
        )
        

class LatexRender(object):
    
    def __init__(self, *args:List[RenderLine]) -> None:
        self._lines:List[RenderLine] = list(args)
        
    def __repr__(self) -> str:
        return f'< Render Block (n={len(self._lines)}) >'
    
    def _repr_html_(self) -> str:
        from IPython.display import display, Latex
        display(Latex(f'$$\n{self.latex}\n$$'))
        return ''
    
    @property    
    def latex(self):
        _latex_output = '\n'.join(
            [_line.latex+r'\\' for _line in self._lines]
        )
        return f'{_latex_output}'
        
    def render_array(
        self,
        X:Iterable[Union[float, int]],
        format:str='d',
        array_bracket:Tuple[str, str]=('[', ']'),
        color:Optional[Union[List[str], str]]=None,
        bold:Optional[Union[List[bool], bool]]=None,
        italic:Optional[Union[List[bool], bool]]=None,
        underline:Optional[Union[List[bool], bool]]=None,
        deleteline:Optional[Union[List[bool], bool]]=None,
    ):
        self._lines.append(
            RenderArrayLine(
                X=X, format=format, array_bracket=array_bracket,
                color=color, bold=bold, italic=italic,
                underline=underline, deleteline=deleteline,
            )
        )
        return self
    
    def render_text(
        self,
        X:str,
        color:Optional[str]=None,
        bold:Optional[bool]=None,
        italic:Optional[bool]=None,
        underline:Optional[bool]=None,
        deleteline:Optional[bool]=None,
    ):
        self._lines.append(
            RenderTextLine(
                X=X, color=color, bold=bold, italic=italic,
                underline=underline, deleteline=deleteline,
            )
        )
        return self
    
    def render(
        self,
        X:Union[Iterable[Union[float, int]], str],
        *args, **kwargs
    ):
        if isinstance(X, str):
            return self.render_text(X, *args, **kwargs)
        else:
            return self.render_array(X, *args, **kwargs)
        
    def to_latex(self, path_or_writable:Optional[Union[IO, str]]):
        if path_or_writable is None:
            return self.latex
        elif isinstance(path_or_writable, str):
            with open(path_or_writable, 'w') as f_handle:
                f_handle.write(self.latex)
        elif isinstance(path_or_writable, IO):
            path_or_writable.write(self.latex)
        else:
            raise TypeError('Path of IO Buffer is not supported.')
            
        
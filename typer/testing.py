from typing import IO, Any, Iterable, Mapping, Optional, Text, Union

from click.testing import CliRunner as ClickCliRunner  # noqa
from click.testing import Result
from typer.main import Typer
from typer.main import get_command as _get_command


class CliRunner(ClickCliRunner):
    def invoke(  # type: ignore
        self,
        app: Typer,
        args: Optional[Union[str, Iterable[str]]] = None,
        input: Optional[Union[bytes, Text, IO[Any]]] = None,
        env: Optional[Mapping[str, str]] = None,
        catch_exceptions: bool = True,
        color: bool = False,
        **extra: Any,
    ) -> Result:
        use_cli = _get_command(app)
        # FIXME: type ignore?
        return super().invoke(
            use_cli,
            args=args,  # type: ignore
            input=input,
            env=env,
            catch_exceptions=catch_exceptions,
            color=color,
            **extra,
        )

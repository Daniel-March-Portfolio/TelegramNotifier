from dataclasses import dataclass


@dataclass(frozen=True)
class TemplateWidgets:
    progress_bar = "{{PROGRESS_BAR}}"

    ALL = {progress_bar}

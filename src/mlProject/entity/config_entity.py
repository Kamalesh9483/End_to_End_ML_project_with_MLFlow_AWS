from dataclasses import dataclass
from pathlib import Path

# Instead of using self. using dataclase decorator we can define the return type like below

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
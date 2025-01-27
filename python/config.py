from dataclasses import dataclass, field
from typing import Literal


@dataclass
class ModelConfig:
    signal_length: int = 300
    signal_channels: int = 1
    classes: int = 5
    embed_size: int = 16
    encoder_layers_num: int = 2
    encoder_heads: int = 4
    dropout: float = 0.1


@dataclass
class Config:
    device: Literal["cpu", "cuda", "mps"] = "mps"
    train_proportion: float = 0.8
    dl_batch_size: int = 256
    dl_num_workers: int = 6
    lr: float = 5e-4
    weight_decay: float = 1e-4
    epochs: int = 100
    validation_interval: int = 5
    save_interval: int = 5
    model: ModelConfig = field(default_factory=lambda: ModelConfig())

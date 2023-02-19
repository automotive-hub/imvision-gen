from typing import List
from typing import Any
from dataclasses import dataclass
import json

from dataclasses import dataclass
from typing import List


@dataclass
class DealershipInfo:
    name: str
    location: str
    public_imgs: List[str]
    local_imgs: List[str]


@dataclass
class VehicleInfo:
    vehicle_name: str
    vin: str
    price: int
    dealership_info: DealershipInfo
    vehicle_public_url_imgs: List[str]
    vehicle_local_imgs: List[str]


@dataclass
class MediaInfo:
    vehicle_name: str
    vin: str
    price: int
    dealership_info: DealershipInfo
    vehicle_public_url_imgs: List[str]
    vehicle_local_imgs: List[str]


@dataclass
class AdsMedia:
    desktop_video_ref: str
    mobile_video_ref: str
    banner_ref: str
    gif_ref: str


@dataclass
class Status:

    image: int = 0
    image_total: int = 0
    # status
    # ["idle", "processing", "done"]
    download: str = "idle"
    video: str = "idle"
    classification: str = "idle"

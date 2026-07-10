from typing import Dict

from semantics.adapters.apache import ApacheMetadataAdapter
from semantics.adapters.base import VendorAdapter
from semantics.adapters.bigquery import BigQueryAdapter
from semantics.adapters.databricks import DatabricksAdapter
from semantics.adapters.fabric import FabricAdapter
from semantics.adapters.openmetadata import OpenMetadataAdapter
from semantics.adapters.snowflake import SnowflakeAdapter

ADAPTERS: Dict[str, VendorAdapter] = {
    adapter.name: adapter
    for adapter in (
        DatabricksAdapter(),
        SnowflakeAdapter(),
        FabricAdapter(),
        BigQueryAdapter(),
        OpenMetadataAdapter(),
        ApacheMetadataAdapter(),
    )
}

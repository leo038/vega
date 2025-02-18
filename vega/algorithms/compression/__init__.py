# -*- coding:utf-8 -*-

# Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.
# This program is free software; you can redistribute it and/or modify
# it under the terms of the MIT License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# MIT License for more details.

"""Lazy import compression algorithms."""

from vega.common.class_factory import ClassFactory

ClassFactory.lazy_register("vega.algorithms.compression", {
    "prune_ea": ["PruneCodec", "PruneEA", "PruneSearchSpace", "PruneTrainerCallback"],
    "prune_ea_mobilenet": ["PruneMobilenetCodec", "PruneMobilenetTrainerCallback"],
    "quant_ea": ["QuantCodec", "QuantEA", "QuantTrainerCallback"],
    "prune_dag": ["PruneDAGSearchSpace", "AdaptiveBatchNormalizationCallback", "SCOPDAGSearchSpace",
                  "KnockoffFeaturesCallback"],
})

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln.Inputs
{

    public sealed class VolumeSetAutoscalingArgs : global::Pulumi.ResourceArgs
    {
        [Input("maxCapacity", required: true)]
        public Input<int> MaxCapacity { get; set; } = null!;

        [Input("minFreePercentage", required: true)]
        public Input<int> MinFreePercentage { get; set; } = null!;

        [Input("scalingFactor", required: true)]
        public Input<double> ScalingFactor { get; set; } = null!;

        public VolumeSetAutoscalingArgs()
        {
        }
        public static new VolumeSetAutoscalingArgs Empty => new VolumeSetAutoscalingArgs();
    }
}

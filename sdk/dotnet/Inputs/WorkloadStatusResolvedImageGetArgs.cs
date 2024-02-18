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

    public sealed class WorkloadStatusResolvedImageGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("images")]
        private InputList<Inputs.WorkloadStatusResolvedImageImageGetArgs>? _images;
        public InputList<Inputs.WorkloadStatusResolvedImageImageGetArgs> Images
        {
            get => _images ?? (_images = new InputList<Inputs.WorkloadStatusResolvedImageImageGetArgs>());
            set => _images = value;
        }

        [Input("resolvedAt")]
        public Input<string>? ResolvedAt { get; set; }

        [Input("resolvedForVersion")]
        public Input<int>? ResolvedForVersion { get; set; }

        public WorkloadStatusResolvedImageGetArgs()
        {
        }
        public static new WorkloadStatusResolvedImageGetArgs Empty => new WorkloadStatusResolvedImageGetArgs();
    }
}

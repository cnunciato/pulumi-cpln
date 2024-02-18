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

    public sealed class VolumeSetStatusGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("bindingId")]
        public Input<string>? BindingId { get; set; }

        [Input("locations")]
        private InputList<string>? _locations;
        public InputList<string> Locations
        {
            get => _locations ?? (_locations = new InputList<string>());
            set => _locations = value;
        }

        [Input("parentId")]
        public Input<string>? ParentId { get; set; }

        [Input("usedByWorkload")]
        public Input<string>? UsedByWorkload { get; set; }

        public VolumeSetStatusGetArgs()
        {
        }
        public static new VolumeSetStatusGetArgs Empty => new VolumeSetStatusGetArgs();
    }
}

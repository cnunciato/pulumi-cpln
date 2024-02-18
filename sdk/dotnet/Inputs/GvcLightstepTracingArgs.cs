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

    public sealed class GvcLightstepTracingArgs : global::Pulumi.ResourceArgs
    {
        [Input("credentials")]
        public Input<string>? Credentials { get; set; }

        [Input("customTags")]
        private InputMap<string>? _customTags;
        public InputMap<string> CustomTags
        {
            get => _customTags ?? (_customTags = new InputMap<string>());
            set => _customTags = value;
        }

        [Input("endpoint", required: true)]
        public Input<string> Endpoint { get; set; } = null!;

        [Input("sampling", required: true)]
        public Input<int> Sampling { get; set; } = null!;

        public GvcLightstepTracingArgs()
        {
        }
        public static new GvcLightstepTracingArgs Empty => new GvcLightstepTracingArgs();
    }
}

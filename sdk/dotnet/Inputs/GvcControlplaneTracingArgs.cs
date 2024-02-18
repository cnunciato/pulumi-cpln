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

    public sealed class GvcControlplaneTracingArgs : global::Pulumi.ResourceArgs
    {
        [Input("customTags")]
        private InputMap<string>? _customTags;
        public InputMap<string> CustomTags
        {
            get => _customTags ?? (_customTags = new InputMap<string>());
            set => _customTags = value;
        }

        [Input("sampling", required: true)]
        public Input<int> Sampling { get; set; } = null!;

        public GvcControlplaneTracingArgs()
        {
        }
        public static new GvcControlplaneTracingArgs Empty => new GvcControlplaneTracingArgs();
    }
}
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

    public sealed class PolicyTargetQuerySpecTermArgs : global::Pulumi.ResourceArgs
    {
        [Input("op")]
        public Input<string>? Op { get; set; }

        [Input("property")]
        public Input<string>? Property { get; set; }

        [Input("tag")]
        public Input<string>? Tag { get; set; }

        [Input("value")]
        public Input<string>? Value { get; set; }

        public PolicyTargetQuerySpecTermArgs()
        {
        }
        public static new PolicyTargetQuerySpecTermArgs Empty => new PolicyTargetQuerySpecTermArgs();
    }
}

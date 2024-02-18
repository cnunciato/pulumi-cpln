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

    public sealed class PolicyTargetQuerySpecGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("match")]
        public Input<string>? Match { get; set; }

        [Input("terms")]
        private InputList<Inputs.PolicyTargetQuerySpecTermGetArgs>? _terms;
        public InputList<Inputs.PolicyTargetQuerySpecTermGetArgs> Terms
        {
            get => _terms ?? (_terms = new InputList<Inputs.PolicyTargetQuerySpecTermGetArgs>());
            set => _terms = value;
        }

        public PolicyTargetQuerySpecGetArgs()
        {
        }
        public static new PolicyTargetQuerySpecGetArgs Empty => new PolicyTargetQuerySpecGetArgs();
    }
}

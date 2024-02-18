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

    public sealed class IdentityAwsAccessPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("cloudAccountLink", required: true)]
        public Input<string> CloudAccountLink { get; set; } = null!;

        [Input("policyRefs")]
        private InputList<string>? _policyRefs;
        public InputList<string> PolicyRefs
        {
            get => _policyRefs ?? (_policyRefs = new InputList<string>());
            set => _policyRefs = value;
        }

        [Input("roleName")]
        public Input<string>? RoleName { get; set; }

        public IdentityAwsAccessPolicyArgs()
        {
        }
        public static new IdentityAwsAccessPolicyArgs Empty => new IdentityAwsAccessPolicyArgs();
    }
}

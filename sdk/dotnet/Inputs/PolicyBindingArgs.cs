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

    public sealed class PolicyBindingArgs : global::Pulumi.ResourceArgs
    {
        [Input("permissions", required: true)]
        private InputList<string>? _permissions;
        public InputList<string> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<string>());
            set => _permissions = value;
        }

        [Input("principalLinks", required: true)]
        private InputList<string>? _principalLinks;
        public InputList<string> PrincipalLinks
        {
            get => _principalLinks ?? (_principalLinks = new InputList<string>());
            set => _principalLinks = value;
        }

        public PolicyBindingArgs()
        {
        }
        public static new PolicyBindingArgs Empty => new PolicyBindingArgs();
    }
}